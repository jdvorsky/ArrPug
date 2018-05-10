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

import os, datetime, subprocess
from pydub import AudioSegment

#delete last sermon
os.system("rm -rf /home/pi/*.wav")
os.system("rm -rf /home/pi/*.mp3")

#format the file name with the service and its date
date = datetime.datetime.now()
options = {0 : 'Monday',
           1 : 'Tuesday',
           2 : 'Wednesday',
           3 : 'Thursday',
           4 : 'Friday',
           5 : 'Saturday',
           6 : 'Sunday'
}

weekDay = options[datetime.datetime.today().weekday()]
hour = (date.hour )
if(hour > 17):
    service = "Evening"
else:
    service = 'Morning'
month = str(date.month)
day = str(date.day)
year = str(date.year)
date = str( year + '-' + month + '-' + day + '-' + weekDay + '-' + service)

#record the sermon
RecordCMD = 'sudo XDG_RUNTIME_DIR=/run/user/1000  /usr/bin/arecord -D plughw:0 -r 16000  --duration=5400 -f S16_LE -vv /home/pi/' + date + '.wav'
os.system(RecordCMD)

#Uncomment these lines if scheduling. This one script will record and upload.
# wav = '/home/pi/' + date + '.wav'
# mp3 = '/home/pi/' + date + '.mp3'
# #AudioSegment.from_wav(wav).export(mp3, format="mp3")
# os.system('ffmpeg -i ' + wav + ' -vn -ar 44100 -ac 2 -ab 192k -f mp3 ' + mp3)
# #Upload the file
# os.system("cd")
# link = os.system("sudo ./gdrive-linux-rpi upload --parent 1Hw1DRxu1S1iv1Wu_0u0LS4xjqUBcvxSh --share /home/pi/*.mp3")
