
# RSSReply

### Description
A script that takes information from a RSS Feed and submits it onto your subreddit of choice!

### Installing Python
* Download Python 3.7: https://www.python.org/downloads/release/python-370/
* Add Python to Path by selecting box during installation or manually adding to Path(https://datatofish.com/add-python-to-windows-path/)
* Open up Command Prompt and type "python", it should tell you the version if its installed correctly.

### Setting up config.ini
* Download the zip file for this repo.
* Extract the contents to your desktop.
* Move on to Secret and Client_ID section.

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

#### Lets put our gathered information into our config.ini file.
* On your desktop, navigate to the extracted folder, RSSReply-master and open it. 
* Open config.ini and it should look something like this.

**Default config.ini**

```
[main]
USER=username
PASSWORD=password
CLIENT_ID=clientid
SECRET=secret
SUBREDDIT=subreddit
RSSURL=rssfeedurl
DELAY=300
```

* Now lets enter in our gathered information.  Once you've added all the required information, USER, PASSWORD, CLIENT_ID, SECRET, SUBREDDIT, RSSURL.  Select file in notepad, and select save.  Now your file should look like this below.

```
[main]
USER =user123
PASSWORD=myultrasecretpassword
CLIENT_ID=ddMaksjJsuyeb
SECRET=daklfanlfkanl392r29neorfjs
RSSURL=https://n4g.com/rss/news?channel=next-gen&sort=latest
SUBREDDIT=mysubredditexample
DELAY=300
```
* Now lets move on to the Running your script section.

### NOTE BEFORE RUNNING
* The account that you are running the script on must be a moderator in the subreddit you are running!

*I.E. ScoopJr is a moderator of Kgamers, where I test all my scripts.*

### Running your script
1. Open up the command prompt.  You may type cmd or command prompt in the windows search bar.  Your command prompt should look like below
```
Microsoft Windows [Version 10.0.18362.959]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\AkitotheExiled>

```
2. Now lets navigate to our directory where we downloaded the script.  In the command prompt, type, **cd desktop/RSSReply-master** Now your command prompt should look like
```
C:\Users\AkitotheExiled\Desktop\RSSReply-master>
```

3. Time to run our script!  In the command prompt, type, **python parsereplybot.py**.  Your command prompt should match the below text

```
C:\Users\AkitotheExiled\Desktop\RSSReply-master>python parsereplybot.py
```
4. Press the enter key on your keyboard.  The script should run now.


### Contributing
Issue Tracker: https://github.com/AkitotheExiled/RSSReply/issues

### Contact
https://www.reddit.com/user/ScoopJr

