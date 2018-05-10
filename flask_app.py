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

from flask import Flask, request, send_from_directory, redirect
from Config import Config
import requests
app = Flask(__name__)


@app.route('/getMostRecent')
def getMostRecent():
    #Get serves most recent file
    r = requests.get(Config.getMostRecentUrl)
    url = r.text

    return redirect(url)

@app.route('/files')
def serveFile():
    filename = request.args.get('filename')
    if (filename.lower().endswith('.mp3')): # the requested file is mp3
        return send_from_directory('public_files/', filename, mimetype="audio/mp3")    # Serve the requested mp3
    elif (filename.lower().endswith('.png')):# the requested file is png
        return send_from_directory('public_files/', filename, mimetype="image/png")# Serve the requested png


@app.route('/rss')
def serveRss():
    # Return the podcast RSS generated
    return send_from_directory('public_files/', 'podcast.xml', mimetype="text/xml")
