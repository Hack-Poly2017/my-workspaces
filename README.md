# My Workspaces
## Team
* [cnguyen](https://github.com/ChauTNguyen)
* [feliciahou27](https://github.com/feliciahou27)
* [jkannn](https://github.com/jkannn)
* [nguyenDjoseph](https://github.com/nguyenDjoseph)
* [vehansayvazi](https://github.com/vehansayvazi)

## About
[Devpost](https://devpost.com/software/my-workspaces)

## Table of Contents
* [Setting up the dev environment](#setting-up-the-dev-environment)
    * [Mac](#mac)
    * [Linux](#linux)
* [Running the web application](#running-the-web-application)
* [Premade accounts](#premade-accounts)

## Setting up the dev environment
You will need ```node v0.9.12, v7.4.0, and python 2.7```.
To take care of the different node versions, use a node version manager such as [nvm](https://github.com/creationix/nvm). This is what I'll use in both sections.

### Mac
If you have [brew](https://brew.sh/), you'll have a much better time.

```
## Terminal

### Sets up brew, nvm, and the project directory!
~/anywhere $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
~/anywhere $ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
~/anywhere $ export NVM_DIR="$HOME/.nvm"
~/anywhere $ [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm
~/anywhere $ brew install redis
~/path/to-contain-project $ git clone <giturl>
~/path/to-contain-project $ cd <foldername>

### Setup python stuffs!
~/path/to/my-workspaces $ virtualenv env (anything works, of course)
~/path/to/my-workspaces $ env/bin/pip install -r requirements.txt

### Setup node stuffs!
(nvm install node installs the latest version of node which
 we need to install dependencies)
~/path/to/my-workspaces $ cd chat
~/path/to/my-workspaces/chat $ nvm install node && nvm install 0.9
~/path/to/my-workspaces/chat $ nvm use node && npm install (or yarn)
```


### Linux
Same as above except you don't have pip installed with Python by default, you don't have brew, and the ```redis``` package we need is called ```redis-server``` in ```apt```. Just run the three following commands, and then start from the top of the [Mac](#mac).

```
## Terminal
sudo apt-get upgrade && sudo apt-get update
sudo apt-get install python-pip
sudo apt-get install redis-server
```

## Running the web application
Running is the same on both OS X and Linux. The syntax used here assumes that you followed the above instructions. Make sure you start ```redis-server``` before you run ```chat_server.js```.

```
## Terminal 1 - Django instance
~/path/to/my-workspaces $ source env/bin/activate
~/path/to/my-workspaces $ python app/manage.py runserver 3000
```

```
## Terminal 2 - Redis instance
~/anywhere $ redis-server
```

```
## Terminal 3 - Node server instance
~/path/to/my-workspaces/chat $ nvm use 0.9
~/path/to/my-workspaces/chat $ node chat_server.js
```

## Premade accounts
| username | password |
|:--------:|----------|
| cnguyen  | temp1234 |
| bobby    | test1234 |
| jeremy   | temp1234 |