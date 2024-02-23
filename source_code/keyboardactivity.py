import ctypes
from ctypes import wintypes
import time
import random

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# List of all codes for keys:
#https://learn.microsoft.com/ru-ru/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
Y_KEY = 0x59
U_KEY = 0x55
I_KEY = 0x49
O_KEY = 0x4F
P_KEY = 0x50
H_KEY = 0x48
J_KEY = 0x4A
K_KEY = 0x4B
L_KEY = 0x4C
SEMICOLON_KEY = 0xBA
N_KEY = 0x4E
M_KEY = 0x4D
COMMA_KEY = 0xBC
DOT_KEY = 0xBE
SLASH_KEY = 0xBF

 
# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

# testing
def keys_test():
    PressKey(Y_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(U_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(I_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(O_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(P_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(H_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(J_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(K_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(L_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(SEMICOLON_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(N_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(M_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(COMMA_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(DOT_KEY)
    time.sleep(1)
    clean_keys()
    PressKey(SLASH_KEY)
    time.sleep(1)
    clean_keys()

def play_note(note_name):
    match note_name:
        case "1Key0":
            PressKey(Y_KEY)
        case "1undefinedKey0":
            PressKey(Y_KEY)
        case "1Key1":
            PressKey(U_KEY)
        case "1undefinedKey1":
            PressKey(U_KEY)
        case "1Key2":
            PressKey(I_KEY)
        case "1undefinedKey2":
            PressKey(I_KEY)
        case "1Key3":
            PressKey(O_KEY)
        case "1undefinedKey3":
            PressKey(O_KEY)
        case "1Key4":
            PressKey(P_KEY)
        case "1undefinedKey4":
            PressKey(P_KEY)
        case "1Key5":
            PressKey(H_KEY)
        case "1undefinedKey5":
            PressKey(H_KEY)
        case "1Key6":
            PressKey(J_KEY)
        case "1undefinedKey6":
            PressKey(J_KEY)
        case "1Key7":
            PressKey(K_KEY)
        case "1undefinedKey7":
            PressKey(K_KEY)
        case "1Key8":
            PressKey(L_KEY)
        case "1undefinedKey8":
            PressKey(L_KEY)
        case "1Key9":
            PressKey(SEMICOLON_KEY)
        case "1undefinedKey9":
            PressKey(SEMICOLON_KEY)
        case "1Key10":
            PressKey(N_KEY)
        case "1undefinedKey10":
            PressKey(N_KEY)
        case "1Key11":
            PressKey(M_KEY)
        case "1undefinedKey11":
            PressKey(M_KEY)
        case "1Key12":
            PressKey(COMMA_KEY)
        case "1undefinedKey12":
            PressKey(COMMA_KEY)
        case "1Key13":
            PressKey(DOT_KEY)
        case "1undefinedKey13":
            PressKey(DOT_KEY)
        case "1Key14":
            PressKey(SLASH_KEY)
        case "1undefinedKey14":
            PressKey(SLASH_KEY)
    time.sleep(0.005)
            
def clean_keys():
    ReleaseKey(Y_KEY)
    ReleaseKey(U_KEY)
    ReleaseKey(I_KEY)
    ReleaseKey(O_KEY)
    ReleaseKey(P_KEY)
    ReleaseKey(H_KEY)
    ReleaseKey(J_KEY)
    ReleaseKey(K_KEY)
    ReleaseKey(L_KEY)
    ReleaseKey(SEMICOLON_KEY)
    ReleaseKey(N_KEY)
    ReleaseKey(M_KEY)
    ReleaseKey(COMMA_KEY)
    ReleaseKey(DOT_KEY)
    ReleaseKey(SLASH_KEY)

def add_little_error():
    if (random.randint(0, 9) == 0):
        time.sleep(0.01)

if __name__ == "__main__":
    time.sleep(2)
    winsound.Beep(500, 1000)

    keys_test()
