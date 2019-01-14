import threading
import colorsys
import time
import datetime as dt
import logging
import noise
import psutil
from . import msirgb

LOGGER = logging.getLogger(__name__)


class Task(threading.Thread):

    def __init__(self):
        super().__init__()
        self.setDaemon(False)
        self.running = True
        self.stopped = False

    def stop(self):
        self.running = False
        while not self.stopped:
            time.sleep(0.01)


class StaticTask(Task):

    def __init__(self, cmd: str):
        super().__init__()
        self.cmd = cmd

    def run(self):
        msirgb.set_cmd(self.cmd)
        self.stopped = True


class StaticColorTask(StaticTask):

    def __init__(self, r: int, g: int, b: int, pulse=False):
        args = []
        if pulse:
            args.append("-p")
        super().__init__(msirgb.get_cmd_color(r, g, b, " ".join(args)))


class HueWheelTask(Task):

    def __init__(self, speed=20.0):
        super().__init__()
        self.speed = float(speed)
        self.state = 0

    def run(self):

        # to ensure task stop on exception
        try:

            # get current time
            t1 = dt.datetime.now()

            # main loop
            while self.running:
                args = []

                r, g, b = colorsys.hsv_to_rgb((self.state % 96.0) / 96.0, 0.9, 1)
                args.append("{:01X}".format(int(r * 15.999)) * 8)
                args.append("{:01X}".format(int(g * 15.999)) * 8)
                args.append("{:01X}".format(int(b * 15.999)) * 8)

                # options
                args += ["-d511"]
                args += ["--fade-in", "r", "g", "b"]

                # execute
                msirgb.set_cmd(" ".join(args))

                # determine progress
                t2 = dt.datetime.now()
                self.state += (t2 - t1).total_seconds() * self.speed
                t1 = t2

                # slow down
                time.sleep(min(1.0 / self.speed, 0.1))

        except Exception as e:
            logging.exception(e)

        # set stop
        self.stopped = True


class PerlinTask(Task):

    def __init__(self, speed=1, red=0, green=0, blue=0):
        super().__init__()
        self.speed = speed
        self.colors = []
        if red:
            self.colors.append((0, red))
        if green:
            self.colors.append((1, green))
        if blue:
            self.colors.append((2, blue))

    def run(self):

        # to ensure task stop on exception
        try:

            # get current time
            t_start = dt.datetime.now()

            # main loop
            while self.running:

                # get pos
                t_now = dt.datetime.now()
                t_diff = t_now - t_start
                pos = t_diff.total_seconds() * self.speed / 100.0

                # build values
                args = [0, 0, 0, "-d0"]
                for color in self.colors:
                    offset = color[0] * 1024 // 3
                    val = noise.pnoise1(pos + offset, octaves=1, persistence=0.5, lacunarity=2, base=0, repeat=1024)
                    val = ((val + 1.0) / 2.0) * 0.9 + 0.1
                    args[color[0]] = val * color[1]

                # set colors
                msirgb.set_cmd(msirgb.get_cmd_color(*args))

                # slow down
                time.sleep(min(1.0 / self.speed, 0.1))

        except Exception as e:
            logging.exception(e)

        # set stop
        self.stopped = True


class CPULoadTask(Task):

    def __init__(self, red=255, green=255, blue=255, color_min=0, color_max=1.0):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue
        self.color_min = color_min
        self.color_max = color_max
        self.last_val = 0.0
        self.frame_time = 1.0 / 20

    def run(self):

        # to ensure task stop on exception
        try:

            # main loop
            while self.running:

                # get cpu load
                cur_load = psutil.cpu_percent() / 100.0

                # smooth load
                diff = cur_load - self.last_val
                load = self.last_val + diff * min(1.0, self.frame_time * 10)

                # get color multiplier
                val = self.color_min + load * (self.color_max - self.color_min)

                # set color
                msirgb.set_cmd(msirgb.get_cmd_color(
                    self.red * val,
                    self.green * val,
                    self.blue * val,
                    "-d0"
                ))

                # slow down
                time.sleep(self.frame_time)

        except Exception as e:
            logging.exception(e)

        # set stop
        self.stopped = True
