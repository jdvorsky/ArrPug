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

import os, requests, urllib

from Config import Config

#Download num files of name and store them in dirPath as name
def getNFiles(num, dirPath):

    fileList = []
    #if you need local copies of the files, uncomment these lines and change fetch
    # directory in myFeedgen

    # cmd = "rm " + dirPath + "*.mp3"
    # os.system(cmd)

    #This assums you have num files to serve. If not, you will get repeats of
    # the last. These may or may not display in the podcast depending on your podcast app.
    while (num > 0):
        webAppUrl =  Config.getNthFileUrl + str(num-1)
        r = requests.get(webAppUrl)
        response = r.text
        response = response.split()
        fileId = response[0]
        name = response[1]
        size = response[2]
        downloadUrl = 'http://drive.google.com/uc?export=download&id='+ fileId
        #if you need local copies of the files, uncomment these lines and change fetch
        # directory in myFeedgen

        # savePath = dirPath + name
        # urllib.request.urlretrieve(downloadUrl, savePath)
        num = int(num) - 1


        fileList.append({'abstract': Config.summary, 'authors': Config.author,'title': name, 'url': downloadUrl, 'size': size})

    return fileList
