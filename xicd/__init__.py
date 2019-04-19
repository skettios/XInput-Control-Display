import sys
sys.path.append("xicd")

import tkinter as tk
import time
from xicdcfg import Config

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self._canvas = None
        self._config = Config("config.json")
        self._config.setup()
        self._running = True
        self._init_window()
        self._init_overlay()

    def _exit_window(self):
        self._running = False

    def _init_window(self):
        self.master.title("Xicd")
        self.master.resizable(False, False)
        self.master.protocol("WM_DELETE_WINDOW", self._exit_window)
        self.pack(fill=tk.BOTH, expand=True)

    def _init_overlay(self):
        overlay = self._config._config["overlay"]
        overlay_script = self._config._config["overlays"][overlay]["file"].replace('.py', '').replace('/', '.')
        print(f"Script: {overlay_script}")
        self._overlay = __import__(overlay_script, fromlist=["__overlay_init__", "__overlay_update__"])
        self._overlay.__overlay_init__(self._config._config["overlays"][overlay]["options"], self)

    def loop(self):
        while self._running:
            self._overlay.__overlay_update__()
            self.update()
            time.sleep(0.01)
