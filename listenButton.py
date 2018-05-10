# Copyright (C) 2018 John Connor Dvorsky
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import RPi.GPIO as GPIO
import time
import os
import subprocess, signal

GPIO.setmode(GPIO.BCM)
#even if they were there...we would ignore them!
GPIO.setwarnings(False)




GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) #shutdown button
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #record button
GPIO.setup(22, GPIO.OUT) #upload light
GPIO.setup(27, GPIO.OUT) #recording light

recording = False


while True:
    input_state = GPIO.input(17)
    shutdown = GPIO.input(4)

    #start recording
    if ((not input_state) and ( not recording)):
        print('Button Pressed')
        cmd = [ 'python3', '/home/pi/record.py']
        proc = subprocess.Popen(cmd)
        recording = True
        GPIO.output(27,GPIO.HIGH)
        time.sleep(1)

    input_state = GPIO.input(17)

    #end recording and upload file
    if ((not input_state) and (recording)):
        os.system('sudo killall -SIGKILL arecord')
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(27,GPIO.LOW)
        os.system('python3 /home/pi/upload.py')
        recording = False
        time.sleep(1)
        GPIO.output(22,GPIO.LOW)

    #Shut the pi down so that it can be disconnected from power
    if((not shutdown) and (not recording)):
        subprocess.call(['shutdown', 'now'], shell=False)
