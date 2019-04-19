import json
from pathlib import Path

class Config:
    def __init__(self, path):
        self._path = path
        self._config = {}

    def _set_defaults(self):
        self._config = {
            "overlay": "guitar",
            "overlays": {
                "guitar": {
                    "file": "overlays/guitar.py",
                    "options": {
                        "background_color": "cyan",
                        "button": {
                            "width": 100,
                            "height": 150,
                            "green": [0, 0],
                            "red": [110, 0],
                            "yellow": [220, 0],
                            "blue": [330, 0],
                            "orange": [440, 0]
                        },
                        "strum_bar": {
                            "position": [575, 50],
                            "width": 150,
                            "height": 50
                        }
                    }
                }
            }
        }

    def setup(self):
        self._set_defaults()
        if Path(self._path).is_file():
            self.load()
        else:
            self.save()

    def load(self):
        with open(self._path, "r") as input_file:
            self._config = json.load(input_file)

    def save(self):
        with open(self._path, "w") as output_file:
            json.dump(self._config, output_file, indent=4)
