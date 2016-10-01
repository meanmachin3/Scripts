from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
import requests
import json
#### Thanks, https://gist.github.com/BoppreH/4000505 ####
class WindowsBalloonTip:
    def __init__(self, title, msg):
        message_map = {
                win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow( classAtom, "Taskbar", style, \
                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                0, 0, hinst, None)
        UpdateWindow(self.hwnd)
        #iconPathName = os.path.abspath(os.path.join( sys.path[0], "balloontip.ico" ))
        iconPathName = "C:\Users\meanmachine\Downloads\Sunny.ico"
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
           hicon = LoadImage(hinst, iconPathName, \
                    win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
          hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, \
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER+20,\
                          hicon, "Balloon  tooltip",msg,200,title))
        # self.show_balloon(title, msg)
        time.sleep(10)
        DestroyWindow(self.hwnd)
    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0) # Terminate the app.

def balloon_tip(title, msg):
    w=WindowsBalloonTip(title, msg)

if __name__ == '__main__':
    getIPResponse = requests.get('http://ip.42.pl/raw')
    my_ip = getIPResponse.text
    url = 'http://freegeoip.net/json/' + my_ip
    response = requests.get(url)
    j = json.loads(response.text)
    city = j['city']
    openWeatherURL = 'http://api.openweathermap.org/data/2.5/weather?q=' + city +'&APPID=83e2622fd44fbc000e40d8aa8e5f3d94'
    weather_response = requests.get(openWeatherURL)
    weather_json = json.loads(weather_response.text)
    message = 'Temp: ' + str(weather_json['main']['temp'] - 273 ) + ' C'
    balloon_tip("Today's Weather", message)
