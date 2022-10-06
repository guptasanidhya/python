from pygame import mixer
from time import time
from datetime import datetime

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user=input()
        if input_of_user==stopper:
            mixer.music.stop()
            break

def logs(msg):
    with open("mylogs.txt",'a') as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__=='__main__':
    water_time=time()
    eyes_time=time()
    physical_time=time()
    water_sec=40*60
    eyes_sec=50*60
    physical_sec=60*60

    while True:
        if time()-water_time>water_sec:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3','drank')
            water_time=time()
            logs("Drank water at")
        if time()-eyes_time>eyes_sec:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3','eyesdone')
            eyes_time=time()
            logs("Eyes Relaxed at")
        if time()-physical_time>physical_sec:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3','donephy')
            physical_time=time()
            logs("Physical Activity done at")


