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

import os
from feedgen.feed import FeedGenerator
from Config import Config

def generateRss(fileList,directoryPath,baseUrl):

  fg = FeedGenerator()

  fg.load_extension('podcast')

  #Setup Feed
  fg.title(Config.podcastTitle)
  baseUrl = Config.baseUrl
  feed = baseUrl + '/rss'
  fg.link(href=feed)
  fg.description(Config.podcastDescription)
  fg.language('en')
  mainImage = baseUrl + '/files?filename='  + Config.mainImage
  fg.image(mainImage)
  #using Technology as other tags like Christianity wont validate
  fg.podcast.itunes_category('Technology', 'Podcasting')
  fg.podcast.itunes_owner(name=Config.ownerName, email = Config.ownerEmail)

  #Setup episodes
  for i in fileList:
      fe = fg.add_entry()
      mp3 = directoryPath + i['title']

      # for local files
      # stat = os.stat(mp3)
      # size = os.path.getsize(mp3)
      # mp3File = baseUrl + '/files?filename=' + i['title']
      # fe.enclosure(mp3File, str(size) , 'audio/mp3')

      fe.enclosure(i['url'], str(i['size']) , 'audio/mp3')
      fe.title(i['title'])
      descriptionText = 'Authors: ' +  i['authors']
      fe.description(descriptionText)
      link = baseUrl + '/files?filename=' + i['title']
      fg.link(href=i['url'])
      fe.podcast.itunes_explicit('no')
      image = baseUrl + '/files?filename=' + Config.mainImage
      fe.podcast.itunes_image(image)

  #Save Rss
  fg.rss_str(pretty=True)
  saveLocation = directoryPath + 'podcast.xml'
  fg.rss_file(saveLocation)
