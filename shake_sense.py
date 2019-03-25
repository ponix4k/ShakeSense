#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

red = 2
green = 3
blue = 4

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(red,GPIO.OUT)
    GPIO.setup(green,GPIO.OUT)
    GPIO.setup(blue,GPIO.OUT)
    
    GPIO.output(red, GPIO.LOW)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue, GPIO.LOW)

def blink(colour, length):
    GPIO.output(colour,GPIO.HIGH)
    time.sleep(length)
    GPIO.output(colour, GPIO.LOW)

setup()
blink(red,1)
blink(blue,2)
blink(green,3)
