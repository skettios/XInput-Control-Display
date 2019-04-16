import ctypes.wintypes

XINPUT_GAMEPAD_DPAD_UP = 0x0001
XINPUT_GAMEPAD_DPAD_DOWN = 0x0002
XINPUT_GAMEPAD_DPAD_LEFT = 0x0004
XINPUT_GAMEPAD_DPAD_RIGHT = 0x0008
XINPUT_GAMEPAD_START = 0x0010
XINPUT_GAMEPAD_BACK = 0x0020
XINPUT_GAMEPAD_LEFT_THUMB = 0x0040
XINPUT_GAMEPAD_RIGHT_THUMB = 0x0080
XINPUT_GAMEPAD_LEFT_SHOULDER = 0x0100
XINPUT_GAMEPAD_RIGHT_SHOULDER = 0x0200
XINPUT_GAMEPAD_A = 0x1000
XINPUT_GAMEPAD_B = 0x2000
XINPUT_GAMEPAD_X = 0x4000
XINPUT_GAMEPAD_Y = 0x8000


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
xinput_get_state.argtypes = [
    ctypes.wintypes.DWORD, ctypes.POINTER(XINPUT_STATE)]
xinput_get_state.restype = ctypes.wintypes.DWORD

