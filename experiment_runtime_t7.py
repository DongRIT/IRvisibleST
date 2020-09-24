import threading
from datetime import datetime
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO
import os
from picamera import PiCamera


GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
# pin 7 is for IRED and pin 13 is for white LED
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)



global Show_Time

# Show_Time = 1

Screen_Height = 1920
Screen_Width = 1200

#on and off time of light blinking
# on_time = 0.051
on_time = 0.068
off_time = 0.010

frame_number = 32
time_between_targets = 0

usr = input("Please input user name or ID:")
usr = str(usr)

# lock = threading.Lock()

camera = PiCamera()
camera.resolution = (800,600)
camera.framerate = 30


########### turn off camera auto gain and awb###########
camera.iso=400
# Wait for the automatic gain control to settle
# sleep(2)
for i in range (20):
    GPIO.output(7, GPIO.HIGH)  # Turn on
    GPIO.output(13, GPIO.LOW)
    time.sleep(0.068)
    #0.041
    GPIO.output(7, GPIO.LOW)  # Turn on
    GPIO.output(13, GPIO.LOW)
    time.sleep(0.010)
    GPIO.output(7, GPIO.LOW)  # Turn off
    GPIO.output(13, GPIO.HIGH)
    time.sleep(0.068)
    GPIO.output(7, GPIO.LOW)  # Turn on
    GPIO.output(13, GPIO.LOW)
    time.sleep(0.010)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

#######################################################

def Target_onset():
    GPIO.output(7, GPIO.HIGH)  # Turn on
    GPIO.output(13, GPIO.LOW)
    time.sleep(0.068)
    GPIO.output(7, GPIO.LOW)  # Turn on
    GPIO.output(13, GPIO.LOW)
    time.sleep(0.010)
    GPIO.output(7, GPIO.LOW)  # Turn off
    GPIO.output(13, GPIO.HIGH)
    time.sleep(0.068)
    GPIO.output(7, GPIO.LOW)  # Turn on
    GPIO.output(13, GPIO.LOW)
    time.sleep(0.010)
    GPIO.output(7, GPIO.HIGH)  # Turn on
    GPIO.output(13, GPIO.LOW)
    time.sleep(0.068)
    GPIO.output(7, GPIO.LOW)  # Turn on
    GPIO.output(13, GPIO.LOW)
    time.sleep(0.010)

#######################################################


out_win = 'MG'
cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(
    out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.moveWindow('MG',1920,0)

#######################################################################
Background_Img = cv2.imread('background/background_0.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)

Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)
# camera = PiCamera()
# camera.resolution = (800,600)
# camera.framerate = 30

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result0/')
    camera.capture_sequence((usr+'/result0/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

#################################################################################################
Background_Img = cv2.imread('background/background_1.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)

Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result1/')
    camera.capture_sequence((usr+'/result1/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

#######################################################################################3
Background_Img = cv2.imread('background/background_2.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)

# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result2/')
    camera.capture_sequence((usr+'/result2/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

################################################################################
Background_Img = cv2.imread('background/background_3.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)


# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result3/')
    camera.capture_sequence((usr+'/result3/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

#####################################################################################
Background_Img = cv2.imread('background/background_4.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)


# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result4/')
    camera.capture_sequence((usr+'/result4/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

################################################################################################
Background_Img = cv2.imread('background/background_5.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)


# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result5/')
    camera.capture_sequence((usr+'/result5/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

##################################################################################################
Background_Img = cv2.imread('background/background_6.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset


def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)

# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result6/')
    camera.capture_sequence((usr+'/result6/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

###############################################################################################
Background_Img = cv2.imread('background/background_7.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)


# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result7/')
    camera.capture_sequence((usr+'/result7/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

###########################################################################################
Background_Img = cv2.imread('background/background_8.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)


# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result8')
    camera.capture_sequence((usr+'/result8/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

#############################################################################################
Background_Img = cv2.imread('background/background_9.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset


def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)


# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result9')
    camera.capture_sequence((usr+'/result9/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

###################################################################################
Background_Img = cv2.imread('background/background_10.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)


# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result10')
    camera.capture_sequence((usr+'/result10/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

#################################################################################
Background_Img = cv2.imread('background/background_11.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)


# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result11')
    camera.capture_sequence((usr+'/result11/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

################################################################################
Background_Img = cv2.imread('background/background_12.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)


# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result12')
    camera.capture_sequence((usr+'/result12/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)


##################################################################################
Background_Img = cv2.imread('background/background_13.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)


# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result13')
    camera.capture_sequence((usr+'/result13/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

####################################################################################
Background_Img = cv2.imread('background/background_14.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result14/')
    camera.capture_sequence((usr+'/result14/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

#############################################################################
Background_Img = cv2.imread('background/background_15.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result15/')
    camera.capture_sequence((usr+'/result15/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)


############################################################################
Background_Img = cv2.imread('background/background_16.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result16/')
    camera.capture_sequence((usr+'/result16/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

########################################################################################
Background_Img = cv2.imread('background/background_17.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result17/')
    camera.capture_sequence((usr+'/result17/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

#####################################################################################
Background_Img = cv2.imread('background/background_18.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result18/')
    camera.capture_sequence((usr+'/result18/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)


###########################################################################################
Background_Img = cv2.imread('background/background_19.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result19/')
    camera.capture_sequence((usr+'/result19/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

##################################################################################
Background_Img = cv2.imread('background/background_20.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset


def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result20/')
    camera.capture_sequence((usr+'/result20/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

####################################################################################
Background_Img = cv2.imread('background/background_21.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result21/')
    camera.capture_sequence((usr+'/result21/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

###########################################################################################
Background_Img = cv2.imread('background/background_22.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset
def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result22/')
    camera.capture_sequence((usr+'/result22/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)


############################################################################
Background_Img = cv2.imread('background/background_23.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result23/')
    camera.capture_sequence((usr+'/result23/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)


#################################################################################
Background_Img = cv2.imread('background/background_24.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset


def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result24/')
    camera.capture_sequence((usr+'/result24/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

##############################################################################
Background_Img = cv2.imread('background/background_25.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result25/')
    camera.capture_sequence((usr+'/result25/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

####################################################################################
Background_Img = cv2.imread('background/background_26.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result26/')
    camera.capture_sequence((usr+'/result26/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)


################################################################################
Background_Img = cv2.imread('background/background_27.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result27/')
    camera.capture_sequence((usr+'/result27/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

########################################################################
Background_Img = cv2.imread('background/background_28.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)



def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result28/')
    camera.capture_sequence((usr+'/result28/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

###################################################################################
Background_Img = cv2.imread('background/background_29.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)

def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result29/')
    camera.capture_sequence((usr+'/result29/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

####################################################################################
Background_Img = cv2.imread('background/background_30.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result30/')
    camera.capture_sequence((usr+'/result30/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

#################################################################################
Background_Img = cv2.imread('background/background_31.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)



def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result31/')
    camera.capture_sequence((usr+'/result31/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)


#################################################################################
Background_Img = cv2.imread('background/background_32.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result32/')
    camera.capture_sequence((usr+'/result32/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

####################################################################################
Background_Img = cv2.imread('background/background_33.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result33/')
    camera.capture_sequence((usr+'/result33/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

#################################################################################
Background_Img = cv2.imread('background/background_34.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result34/')
    camera.capture_sequence((usr+'/result34/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
time.sleep(time_between_targets)

################################################################################
Background_Img = cv2.imread('background/background_35.png')
cv2.imshow(out_win, Background_Img)

cv2.waitKey(1)
Target_onset

def Led_Light():
    event.set()
    global Start_Point
    global end
    end = 0
    Start_Point = 0
    while end == 0:
        GPIO.output(7, GPIO.HIGH)  # Turn on
        GPIO.output(13, GPIO.LOW)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)
        GPIO.output(7, GPIO.LOW)  # Turn off
        GPIO.output(13, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(7, GPIO.LOW)  
        GPIO.output(13, GPIO.LOW)
        time.sleep(off_time)



# Show_Points(Point_X, Point_Y, Show_Time)

# cap = cv2.VideoCapture(0)


def Rapid_Capture():
    event.wait()

    global now_Point_X
    global now_Point_Y
    global end
    global Start_Point

    end = 0


    frames = frame_number
    Start_Point = 0
    j=0

    time.sleep(0.1)
    start = time.time()
    os.makedirs(usr+'/result35/')
    camera.capture_sequence((usr+'/result35/%02d.jpg' % i for i in range(j,j+frames)), use_video_port=True)
    finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    end = 1

t1 = threading.Thread(target=Rapid_Capture)
t2 = threading.Thread(target=Led_Light)
event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
event.wait()
for t in (t1, t2):
    t.join()

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)

cv2.destroyAllWindows()

