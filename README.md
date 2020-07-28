
# RSSReply

### Description
A script that takes information from a RSS Feed and submits it onto your subreddit of choice!

### Preqs - requirements.txt
```
beautifulsoup4==4.9.1
bs4==0.0.1
certifi==2020.6.20
chardet==3.0.4
idna==2.10
lxml==4.5.2
praw==7.1.0
prawcore==1.4.0
requests==2.24.0
six==1.15.0
soupsieve==2.0.1
SQLAlchemy==1.3.18
update-checker==0.17
urllib3==1.25.10
websocket-client==0.57.0
```



### Secret and Client_ID
* Go to reddit.com and select user settings
* Select Privacy & Security
* At the very bottom, select Manage third-party app authorization
* At the very bottom again, select create another app..
* In the name, type "ParseNReply by ScoopJr"
* Select the bubble: script
* In description, type "Bot that reflairs posts based on command"
* For about url, type "http://localhost"
* For redirect url, type "http://localhost"
* Select create app

**Secret**
* look next to the text, "Secret", and copy this text down somewhere

*mysecret*
```
daklfanlfkanl392r29neorfjs
```

**Client_ID**
* Look at ParseNReply by ScoopJr, and right under Personal Use Script, is our client_id
* Copy the text and save it somewhere

*myclient_id*
```
ddMaksjJsuyeb
```

**RSSURL**
* Get your favorite RSS Feed
* In my case I will be using N4G's RSS Feed.

*RSSURL*
```
https://n4g.com/rss/news?channel=next-gen&sort=latest
```

### Installing Python
* Download Python 3.7: https://www.python.org/downloads/release/python-370/
* Add Python to Path by selecting box during installation or manually adding to Path(https://datatofish.com/add-python-to-windows-path/)
* Open up Command Prompt and type "python", it should tell you the version if its installed correctly.

### Installation for Home PC
* Open up your Command Prompt again, type 
```
pip install requirements.txt
```
* Download the ZIP file and extract the contents to your desktop
* Open the config.ini file and place your information inside and save the file

```
[main]
USER =example
PASSWORD=ex_password
CLIENT_ID=ddMaksjJsuyeb
SECRET=daklfanlfkanl392r29neorfjs
RSSURL=https://n4g.com/rss/news?channel=next-gen&sort=latest
SUBREDDIT=mysubredditexample
DELAY=300
```
### DELAY
* Amount of time in seconds to wait before refetching the RSS Feed information.


### NOTE BEFORE RUNNING
* The account that you are running the script on must be a moderator in the subreddit you are running!

*I.E. ScoopJr is a moderator of Kgamers, where I test all my scripts.*

### Running the bot
* Open up your command prompt
* Navigate to the directory your bot is in
```
cd desktop/RSSReply
```
* Type the following
```
python parsereplybot.py
```
* Press the enter key

*The bot is now running!*

### Contributing
Issue Tracker: https://github.com/AkitotheExiled/RSSReply/issues

### Contact
https://www.reddit.com/user/ScoopJr

