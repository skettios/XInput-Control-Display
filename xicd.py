import tkinter as tk
import xinput
import ctypes
import time

class GuitarStrumBar:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.strum_up = canvas.create_rectangle(x, y, x + 150, y + 25, fill="white", outline="gray")
        self.strum_down = canvas.create_rectangle(x, y + 25, x + 150, y + 50, fill="white", outline="gray")

    def update(self, button_state):
        if button_state & xinput.XINPUT_GAMEPAD_DPAD_UP:
            self.canvas.itemconfig(self.strum_up, fill="gray")
        else:
            self.canvas.itemconfig(self.strum_up, fill="white")

        if button_state & xinput.XINPUT_GAMEPAD_DPAD_DOWN:
            self.canvas.itemconfig(self.strum_down, fill="gray")
        else:
            self.canvas.itemconfig(self.strum_down, fill="white")


class GuitarButton:
    def __init__(self, canvas, x1, y1, x2, y2, color, button_value):
        self.canvas = canvas
        self.color = color
        self.button_value = button_value
        self.rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def update(self, button_state):
        if button_state & self.button_value:
            self.canvas.itemconfig(self.rectangle, fill="white")
        else:
            self.canvas.itemconfig(self.rectangle, fill=self.color)


class Xicd(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.running = True
        self.init_window()

    def exit_window(self):
        self.running = False

    def init_window(self):
        self.master.title("Xicd")
        self.master.resizable(False, False)
        self.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self, width=900, height=300,
                                highlightbackground="cyan", background="cyan")
        self.green_button = GuitarButton(
            self.canvas, 0, 0, 100, 150, "green", xinput.XINPUT_GAMEPAD_A)
        self.red_button = GuitarButton(
            self.canvas, 110, 0, 210, 150, "red", xinput.XINPUT_GAMEPAD_B)
        self.yellow_button = GuitarButton(
            self.canvas, 220, 0, 320, 150, "yellow", xinput.XINPUT_GAMEPAD_Y)
        self.blue_button = GuitarButton(
            self.canvas, 330, 0, 430, 150, "blue", xinput.XINPUT_GAMEPAD_X)
        self.orange_button = GuitarButton(self.canvas, 440, 0, 540, 150,
                                          "orange",
                                          xinput.XINPUT_GAMEPAD_LEFT_SHOULDER)
        self.strum_bar = GuitarStrumBar(self.canvas, 575, 50)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.master.protocol("WM_DELETE_WINDOW", self.exit_window)

    def update_buttons(self):
        controller_state = xinput.XINPUT_STATE()
        while self.running:
            xinput.xinput_get_state(0, ctypes.byref(controller_state))
            button_state = controller_state.Gamepad.wButtons
            self.green_button.update(button_state)
            self.red_button.update(button_state)
            self.yellow_button.update(button_state)
            self.blue_button.update(button_state)
            self.orange_button.update(button_state)
            self.strum_bar.update(button_state)
            self.update()
            time.sleep(0.01)


def main():
    root = tk.Tk()
    app = Xicd(master=root)
    app.update_buttons()


if __name__ == "__main__":
    main()
