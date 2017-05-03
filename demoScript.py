import os
import threading


def videos():
    os.system("TASKKILL /F /IM mplayer.exe 2>NUL | find /I /N \"mplayer.exe\" >NUL")
    threading.Timer(43200.0, videos).start()
    os.system("start /min .\mplayer.exe -playlist \".\Videos\Intrusion Detection\playlist.txt\" -vo direct3d -geometry 1920x1080-1920+0 -loop 0 -noborder -aspect 16:9")
    os.system("start /min .\mplayer.exe -playlist \".\Videos\People and vehicle Tracking\playlist.txt\" -vo direct3d -geometry 1920x1080+0+0 -loop 0 -noborder -aspect 16:9")
    os.system("start /min .\mplayer.exe -playlist \".\Videos\Perimeter Protection\playlist.txt\" -vo direct3d -geometry 1920x1080+1920+0 -loop 0 -noborder -aspect 16:9")
    os.system("start /min .\mplayer.exe -playlist \".\Videos\Traffic Management\playlist.txt\" -vo direct3d -geometry 1920x1080+3840+0 -loop 0 -noborder -aspect 16:9")

videos()
