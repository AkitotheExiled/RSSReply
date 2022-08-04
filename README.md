
# RSSReply

### Description
A script that takes information from a RSS Feed and submits it onto your subreddit of choice!
- - - -

Recent Changes
| Date | Description | Link |
| --- | --- | --- |
| 8/4/22 | POST_DESC flag added | [NEW](#post-desc) |
| 8/4/22 | COMMENT_DESC flag added | [NEW](#comment-desc) |
| 6/14/22 | PREFER_IMAGES flag added | [NEW](#prefer-images) |
| 6/14/22 | DEVMODE flag added | [NEW](#devmode) |
| 6/14/22 | Feed_type will be **removed** next update | [NEW](#feed-type) |
| 6/14/22 | Support added for submitting single images and gallerys from RSS Feeds | [NEW](#prefer-images) |
| 6/14/22 | Reworked fetch/post logic.  Recommended updates to delay as follows | [NEW](#delay) |


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
        * [run_once](#run-once)
        * [[*CHANGED*]feed_type](#feed-type)
        * [flairids](#flair-ids)
        * [[NEW]devmode](#devmode)
        * [[NEW]prefer_images](#prefer-images)
        * [[**NEW**]comment-desc](#comment-desc)
        * [[**NEW**]post-desc](#post-desc)
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
* During installation - Select the checkbox Add Python to Path or [manually adding to Path](https://datatofish.com/add-python-to-windows-path/)
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

### Delay
* The time in seconds before fetching the RSS feed again.
* **This does not have an effect when RUN_ONCE=true**
```
DELAY=300
```

### Subreddit
* The subreddit you will be running the program in!
```
mysubredditexample
```

### Rss feed
* The RSS FEED the program will query for information. **Now you can use multiple feeds/subreddits**
* [How to find an rss feed's url](https://rss.com/blog/find-rss-feed/)
* **NEW** Added ability to have more than one rss feed for your subreddit
```
https://n4g.com/rss/news?channel=next-gen&sort=latest
```

**NEW MULTIPLE FEEDS**
* Separate each rss url with a comma
```
yoursubreddit : https://n4g.com/rss/news?channel=next-gen&sort=latest, https://n4g.com/rss/news?channel=ps5&sort=latest
```

### Run once
* When true, the script will run one time and then exit. **DELAY DOES NOT AFFECT WHEN TRUE**
* When false, the script will loop many times waiting DELAY seconds between runs.
```
RUN_ONCE=false
```

### Feed type
**LEAVE ON DEFAULT SETTING.  WILL BE REMOVED IN 1.11**
```
FEED_TYPE=latest
```

### Devmode
* Leave on default

```
DEVMODE=false
```

### Prefer-images
* RSS Urls that contain direct links to images will now upload the image directly when this setting is on.

```
PREFER_IMAGES=true
```

### Comment-desc
* Set to true to allow the bot to comment the item description in the comments

```
COMMENT_DESC=false
```

### Post-desc
* Set to true to change the bots behavior to post the description as a text post.
* ONLY ENABLE IF YOUR RSS FEED AS TEXT IN THE DESCRIPTION!!

```
POST_DESC=false
```

### Flair ids
* Flair ids are not required.  Script will issue a warning if no flair ids are mentioned.
* Grab the flair id for post flairs from your subreddit
* *Flair count must match subreddit count(2 subreddits, 2 flair-template ids needed).*
```
jf82hh3-328dh328-dfj2384r2h,2390423-jfsdf832-fsjsfj28
```

- - - -
### Putting it together
* On your desktop, navigate to the extracted folder, RSSReply-master and open it. 
* Open the config.ini file
* Enter in your information that we've been gathering and save it!

**It should now look like this!**

```
[main]
USER =user123
PASSWORD=myultrasecretpassword
CLIENT_ID=ddMaksjJsuyeb
SECRET=daklfanlfkanl392r29neorfjs
DELAY=300
RUN_ONCE=false
FEED_TYPE=latest
DEVMODE=false
PREFER_IMAGES=true
COMMENT_DESC=false
POST_DESC=false

[suburl]
mysubredditexample : https://n4g.com/rss/news?channel=next-gen&sort=latest
mysecondsubreddit : https://n4g.com/rss/news?channel=ps3&sort=latest

[flairs]
FLAIR_IDS=jf82hh3-328dh328-dfj2384r2h,2390423-jfsdf832-fsjsfj28
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


### To-do List
- [x] Adding support for multiple subreddits/feeds COMPLETED 9/11/20
- [x] Added support for flair-template ids for multiple subreddits COMPLETED 9/13/20



