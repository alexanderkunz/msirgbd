import subprocess
import threading
import logging

LOGGER = logging.getLogger(__name__)
CMD_LOCK = threading.Semaphore(value=0)
CMD_THREAD = None
CMD_THREAD_STOP = False
CMD_LIST = []
CMD_LIST_LOCK = threading.Lock()


def set_cmd_thread_start():

    # worker function for thread
    def worker():

        # we need those
        global CMD_LOCK
        global CMD_LIST

        # main loop
        while True:

            # wait for lock
            CMD_LOCK.acquire()

            # check for stop
            if CMD_THREAD_STOP:
                break

            cmd = None
            with CMD_LIST_LOCK:
                if len(CMD_LIST):
                    cmd = CMD_LIST[-1]
                    CMD_LIST.clear()
            if cmd:
                proc = subprocess.Popen(["msi-rgb", *cmd.strip().split(" ")])
                proc.wait()

    # start worker, limit to one instance
    global CMD_THREAD
    if CMD_THREAD is None:
        CMD_THREAD = threading.Thread(target=worker)
        CMD_THREAD.setDaemon(True)
        CMD_THREAD.start()


def set_cmd_thread_stop():
    global CMD_THREAD_STOP
    CMD_THREAD_STOP = True
    if CMD_THREAD:
        CMD_LOCK.release()
        CMD_THREAD.join()


def set_cmd(cmd: str):
    global CMD_LIST
    global CMD_LIST_LOCK
    with CMD_LIST_LOCK:
        if not len(CMD_LIST) or CMD_LIST[-1] != cmd:
            CMD_LIST.append(cmd)
            CMD_LOCK.release()


def get_cmd_fmt(r1, r2, r3, r4, g1, g2, g3, g4, b1, b2, b3, b4, args=""):
    return "{:02X}{:02X}{:02X}{:02X} {:02X}{:02X}{:02X}{:02X} {:02X}{:02X}{:02X}{:02X} {}".format(
        r1, r2, r3, r4,
        g1, g2, g3, g4,
        b1, b2, b3, b4,
        args
    )


def get_cmd_color(r: int, g: int, b: int, args=""):
    args = (
        "{:01X}".format(int(r / 255 * 15.999)) * 8,
        "{:01X}".format(int(g / 255 * 15.999)) * 8,
        "{:01X}".format(int(b / 255 * 15.999)) * 8,
        args
    )
    return " ".join(args)
