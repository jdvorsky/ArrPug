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
from Config import Config

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

wav = '/home/pi/' + date + '.wav'
mp3 = '/home/pi/' + date + '.mp3'
os.system('ffmpeg -i ' + wav + ' -vn -ar 16000 -ac 1 -ab 96k -f mp3 ' + mp3)
#Upload the file
os.system("cd")

cmd = "sudo ./gdrive-linux-rpi upload --parent " + Config.folderId + "  --share /home/pi/*.mp3"
link = os.system(cmd)
