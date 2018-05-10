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

class Config:
    ################# For flask_app.py ###############################
    #get most recent web app url
    getMostRecentUrl = 'https://script.google.com/macros/s/AKfycbyH4saN06nZe37PINlimqasCMKCNELemEvnYJBiX4GKOOeC5X4/exec'



    ################# For getNFiles.py ###############################
    #getNthFile web app url used in getNFiles.py
    getNthFileUrl = 'https://script.google.com/macros/s/AKfycby3WUU0qqTmJwMpNQDul6j-uxG5O6erYZUCSOo282pHo50mkjn1/exec?num='

    #feel free to add more parametes here for building your own podcast
    summary = ""
    author = "North Tiverton Baptist Church"


    ################# For myFeedgen.py ###############################
    baseUrl = 'http://pisermons.pythonanywhere.com' #also for podcastBuilder.py
    podcastTitle = 'NTBC Sermons'
    podcastDescription = "Five Most Recent Sermons"
    ownerName = ' '
    ownerEmail = "piSermons@gmail.com"
    mainImage = "ChurchName.png"

    ################# For podcastBuilder.py ###############################
    fileDirectory = '/home/pisermons/mysite/public_files/'
    numberOfFiles = 50


    ################# For upload.py ###############################
    folderId = '1Hw1DRxu1S1iv1Wu_0u0LS4xjqUBcvxSh'
