import bottle
import logging
import pickle
import sys, threading
from .log import setup_logging
from . import msirgb, tasks, res

LOGGER = logging.getLogger(__name__)


class MSIRGBDaemon(bottle.Bottle):

    def __init__(self):
        super().__init__()

        # state
        self.task = None

        # load old task state
        try:
            with open("task.bin", "rb") as f:
                task = pickle.load(f)
                self.set_task(task)
        except (FileNotFoundError, TypeError, EOFError) as e:
            LOGGER.debug("Failed to load task: {}".format(e))

        # logging
        setup_logging()

        # start thread
        msirgb.set_cmd_thread_start()

        # default task
        if self.task is None:
            self.set_task(tasks.StaticColorTask(
                r=255,
                g=0,
                b=0,
                pulse=True
            ))

        @self.route("/")
        @self.route("/index")
        @self.route("/index.html")
        @self.route("/index.php")
        def index():
            return res.INDEX

        @self.route("/color/<r:int>/<g:int>/<b:int>/<pulse:int>")
        def color(r: int, g: int, b: int, pulse: int):
            self.set_task(tasks.StaticColorTask(
                r=r,
                g=g,
                b=b,
                pulse=pulse > 0
            ))
            return index()

        @self.route("/hue/<speed:int>")
        def hue(speed: int):
            speed = max(speed, 1)
            self.set_task(tasks.HueWheelTask(speed=speed))
            return index()

        @self.route("/heartbeat")
        def heartbeat():
            self.set_task(tasks.StaticTask(
                cmd="206487a9 206487a9 10325476 -ir -ig -ib -d 5")
            )
            return index()

        @self.route("/police")
        def police():
            self.set_task(tasks.StaticTask(
                cmd="FF00FF00 0 00FF00FF -d15"
            ))
            return index()

        @self.route("/easter")
        def easter():
            self.set_task(tasks.StaticTask(
                cmd="58e01c0d 504fdcb9 e4aa75eb --blink 2 -d 32"
            ))
            return index()

        @self.route("/perlin/<speed:int>/<r:int>/<g:int>/<b:int>")
        def perlin(speed, r, g, b):
            self.set_task(tasks.PerlinTask(
                speed=speed,
                red=r,
                green=g,
                blue=b
            ))
            return index()

    def __del__(self):

        # stop thread
        msirgb.set_cmd_thread_stop()

    def stop_task(self):
        if self.task is not None:
            self.task.stop()
            self.task = None

    def set_task(self, task):

        # end old task
        self.stop_task()

        # dump task to file
        self.task = task
        self.task._started = None
        self.task._stderr = None
        try:
            with open("task.bin", "wb") as f:
                pickle.dump(self.task, f, -1)
        except (PermissionError, ValueError) as e:
            LOGGER.warning("Failed to save task: {}".format(e))
        self.task._started = threading.Event()
        self.task._stderr = sys.stderr

        # start task
        self.task.start()


def main():
    daemon = MSIRGBDaemon()
    daemon.run(host="localhost", port=40000)
    del daemon
