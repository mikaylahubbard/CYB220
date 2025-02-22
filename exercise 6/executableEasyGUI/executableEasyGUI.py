from easygui import *

import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

msgbox("Hello!!!! This is an executable easyGUI program!", "hello there")

msgbox("Watson says hello!", "watson", "Say Hi", image=resource_path('watson.png'))

msgbox("Thank you for your time :)", "bye", "Goodbye")
