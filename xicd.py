import ctypes
import ctypes.wintypes

class XINPUT_GAMEPAD(ctypes.Structure):
    _fields_ = [("wButtons", ctypes.wintypes.WORD),
                ("bLeftTrigger", ctypes.wintypes.BYTE),
                ("bRightTrigger", ctypes.wintypes.BYTE),
                ("sThumbLX", ctypes.wintypes.SHORT),
                ("sThumbLY", ctypes.wintypes.SHORT),
                ("sThumbRX", ctypes.wintypes.SHORT),
                ("sThumbRY", ctypes.wintypes.SHORT)]

class XINPUT_STATE(ctypes.Structure):
    _fields_ = [("dwPacketNumber", ctypes.wintypes.DWORD),
                ("Gamepad", XINPUT_GAMEPAD)]

xinput = ctypes.windll.xinput1_3

xinput_get_state = xinput.XInputGetState
xinput_get_state.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(XINPUT_STATE)]
xinput_get_state.restype = ctypes.wintypes.DWORD

state = XINPUT_STATE()
controller_state = xinput_get_state(0, ctypes.byref(state))
if controller_state > 0:
    print("No controller connected.")

while 1:
    xinput_get_state(0, ctypes.byref(state))
    if state.Gamepad.wButtons > 0:
        print(f"Buttons: {state.Gamepad.wButtons}")
