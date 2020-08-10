
# RSSReply

### Description
A script that takes information from a RSS Feed and submits it onto your subreddit of choice!
- - - -

* [Getting started](#installing-script)
    * [Installing Python](#installing-python)
    * [Installing requirements](#installing-requirements)
    * [Setting your config](#setting-your-config)
        * [username and password](#username-and-password)
        * [secret and client_id](#secret-and-client_id)
        * [delay](#delay)
        * [subreddit](#subreddit)
        * [rssurl](#rss-feed)
        * [Putting it all together](#putting-it-together)
* [Running your script](#running-your-script)
* [Bug tracking](#contributing)
* [Contact me](#contact)
- - - -
# Installing Script
* Download the zip file for this repo.
* Extract the contents to your desktop.
- - - -

## Installing Python
* Download [Python 3.7](https://www.python.org/downloads/release/python-370/)
* Add Python to Path by selecting box during installation or [manually adding to Path](https://datatofish.com/add-python-to-windows-path/)
* Open up Command Prompt and type "python", it should tell you the version if its installed correctly.
```
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
- - - -
## Installing requirements
* Open up the command prompt.  You may type cmd or command prompt in the windows search bar.  Your command prompt should look like below
```
Microsoft Windows [Version 10.0.18362.959]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\AkitotheExiled>

```
* Now lets navigate to our directory where we downloaded the script.  In the command prompt, type, **cd desktop/RSSReply-master** Now your command prompt should look like
```
C:\Users\AkitotheExiled\Desktop\RSSReply-master>
```

* Installing requirements.txt so our script can be ran.  In the command prompt, type **python pip install requirements.txt**.  Press enter and wait for the command to finish.  
```
C:\Users\AkitotheExiled\Desktop\RSSReply-master>python pip install requirements.txt
```
- - - -
## Setting your config
### username and password
* Enter your username and password for the account you will be using for the program
```
USER= user123
PASSWORD= myultrasecretpassword
```
### Secret and Client_ID
* Go to reddit.com and login to your account. Now select your account name in the top right and select user settings
* Select Privacy & Security
* At the very bottom, select Manage third-party app authorization
* At the very bottom again, select create another app..
* In the name, type "ParseNReply by ScoopJr"
* Select the radio button: script
* In description, type "RSS Parse and Reply"
* For about url, type "http://localhost"
* For redirect url, type "http://localhost"
* Select create app

**Secret**
* look next to the text, "Secret", and copy this text down somewhere

```
SECRET= daklfanlfkanl392r29neorfjs
```

**Client_ID**
* Look at ParseNReply by ScoopJr, and right under Personal Use Script, is our client_id
* Copy the text and save it somewhere

```
CLIENT_ID= ddMaksjJsuyeb
```


### Subreddit
* The subreddit you will be running the program in!
```
mysubredditexample
```

### Rss feed
* The RSS feed the bot pulls from.
* [How to find an rss feed's url](https://rss.com/blog/find-rss-feed/)
```
RSSURL = https://n4g.com/rss/news?channel=next-gen&sort=latest
```

### Delay
* The time in seconds before fetching the RSS feed again.
```
DELAY=300
```


- - - -
### Putting it together
* On your desktop, navigate to the extracted folder, RSSReply-master and open it. 
* Open config.ini and it should look something like this.
* Enter in your information from before and select save!

**It should now look like this!**

```
[main]
USER =user123
PASSWORD=myultrasecretpassword
CLIENT_ID=ddMaksjJsuyeb
SECRET=daklfanlfkanl392r29neorfjs
SUBREDDIT=mysubredditexample
RSSURL=https://n4g.com/rss/news?channel=next-gen&sort=latest
DELAY=300

```
- - - -

## Running your script
* **Make sure your account is a moderator in the subreddit you will be running in!!**
* Time to run your script!  In the command prompt, type, **python parsereplybot.py**.  Your command prompt should match the below text

```
C:\Users\AkitotheExiled\Desktop\RSSReply-master>python parsereplybot.py
```
* Press the enter key on your keyboard.  The script should be running now :)


### Contributing
Issue Tracker: https://github.com/AkitotheExiled/RSSReply/issues

### Contact
https://www.reddit.com/user/ScoopJr




