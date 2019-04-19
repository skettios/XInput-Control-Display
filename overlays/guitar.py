import tkinter as tk
import xinput
import ctypes


class GuitarStrumBar:
    def __init__(self, canvas, width, height, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.strum_up = canvas.create_rectangle(x, y, x + width, y + (height / 2), fill="white", outline="gray")
        self.strum_down = canvas.create_rectangle(x, y + (height / 2), x + width, y + height, fill="white", outline="gray")

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
    def __init__(self, canvas, width, height, x, y, color, button_value):
        self.canvas = canvas
        self.color = color
        self.button_value = button_value
        self.rectangle = canvas.create_rectangle(x, y, x + width, y + height, fill=color)

    def update(self, button_state):
        if button_state & self.button_value:
            self.canvas.itemconfig(self.rectangle, fill="white")
        else:
            self.canvas.itemconfig(self.rectangle, fill=self.color)



def __overlay_init__(options, frame):
    global controller_state
    global green_button
    global red_button
    global yellow_button
    global blue_button
    global orange_button
    global strum_bar

    controller_state = xinput.XINPUT_STATE()
    background_color = options["background_color"]
    canvas = tk.Canvas(frame, width=900, height=300, highlightbackground=background_color, background=background_color)
    button_width = options["button"]["width"]
    button_height = options["button"]["height"]
    button_position = options["button"]["green"]
    green_button = GuitarButton(canvas, button_width, button_height, button_position[0], button_position[1], "green", xinput.XINPUT_GAMEPAD_A)
    button_position = options["button"]["red"]
    red_button = GuitarButton(canvas, button_width, button_height, button_position[0], button_position[1], "red", xinput.XINPUT_GAMEPAD_B)
    button_position = options["button"]["yellow"]
    yellow_button = GuitarButton(canvas, button_width, button_height, button_position[0], button_position[1], "yellow", xinput.XINPUT_GAMEPAD_Y)
    button_position = options["button"]["blue"]
    blue_button = GuitarButton(canvas, button_width, button_height, button_position[0], button_position[1], "blue", xinput.XINPUT_GAMEPAD_X)
    button_position = options["button"]["orange"]
    orange_button = GuitarButton(canvas, button_width, button_height, button_position[0], button_position[1], "orange", xinput.XINPUT_GAMEPAD_LEFT_SHOULDER)
    strum_bar_width = options["strum_bar"]["width"]
    strum_bar_height = options["strum_bar"]["height"]
    strum_bar_position = options["strum_bar"]["position"]
    strum_bar = GuitarStrumBar(canvas, strum_bar_width, strum_bar_height, strum_bar_position[0], strum_bar_position[1])
    canvas.pack(fill=tk.BOTH, expand=True)

def __overlay_update__():
    xinput.xinput_get_state(0, ctypes.byref(controller_state))
    button_state = controller_state.Gamepad.wButtons
    green_button.update(button_state)
    red_button.update(button_state)
    yellow_button.update(button_state)
    blue_button.update(button_state)
    orange_button.update(button_state)
    strum_bar.update(button_state)
