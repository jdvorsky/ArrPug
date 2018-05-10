# ArrPug - Automated RaspberryPi recorder and podcast upload generator.

### Summary
------
ArrPug utilizes a Raspberry Pi, Python, Google Drive, gdrive, Google App scripts, and pythonanywhere. After some initial setup and two presses of a button, one can automatically record, upload, and generate a podcast. A raspberry pi records, names, and uploads files to google drive. A Google App script in conjunction with python scripts hosted on Pythonanywhere then generate the podcasts on a user-defined schedule. All services used are free and are sufficient for most podcasters.

ArrPug was initially created for a small local church. The intention was to make an affordable process that could be fully automated. With a few tweaks and/or changes in the config file this can easily be generalized to serve other podcasters.

The additional Google App script, serveMostRecent.gs, is used to serve users who do not subscribe to the podcast the most recent recording and its deployed link can be provided in conjuction with a link to view your podcast directory on Google Drive.  

### Basic Setup
------
The included wiring diagram and listenButton.py are used to start/stop recordings and upload the file as well as safely shutdown the Pi. Be sure it is run on startup by updating crontab:
> sudo crontab -e

> reboot sudo sleep 30 && sudo  /usr/bin/python3 /home/pi/listenButton.py

In addition, record.py has a commented out upload section. The original design was to schedule recordings in crontab for a set length of time and upload them once completed. The code can easily be reverted back to this state and used for other recording purposes.

Currently, the podcast is hosted from Google Drive. There are commented out sections in myFeedgen.py and getNFiles.py that allow the hosting to be done on a server running the python scripts. There are few other small tweaks that should be evident in myFeedgen.py.

ArrPug is using a pi sound card from Amazon so that recordings could be done via AUX to RCA. It can be purchased [here](https://www.amazon.com/gp/product/B01HCC0210/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01HCC0210&linkCode=as2&tag=jdvorsky-20&linkId=b0efbd4ea7f1f13e924a4766ef1a2f03) with its relevant GitHub located [here](
https://github.com/Audio-Injector/stereo-and-zero).

gdrive, specifically gdrive-linux-rpi, was set up on the pi as described under the Linux section of [this](http://olivermarshall.net/how-to-upload-a-file-to-google-drive-from-the-command-line/) webpage. You may need to run the first upload manually via a bash terminal so that you can authorize your specific drive folder.

A virtual environment was used to execute poscastBuilder.py on pythonanywhere.com. With an account setup open a bash terminal and enter the following:
>mkvirtualenv myvirtualenv --python=/usr/bin/python3.6 --system-site-packages

It can then be turned on and tested:
>workon myvirtualenv

To schedule podcasterBuilder.py on pythonanywhere, navigate to Tasks and schedule with the following command (all one line):
>/home/YOU_USERNAME_HERE/.virtualenvs/myvirtualenv/bin/python3 /home/YOUR_USERNAME_HERE/YOUR_PARENT_DIR/podcastBuilder.py



#### The following files must be on your pi:
> Config.py

> listenButton.py

> record.py

> upload.py

#### The following files are deployed as Google web apps:
> getNfiles.gs

> serveMostRecent.gs (optional, see summary)

#### The following files must be in your website folder on pythonanywhere or personal host:
> Config.py

> flask_app.py

> myFeedgen.py

> podcastBuilder.py

------
###### If this saved you some time and/or you feel like donating:
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/JCDvorsky)
