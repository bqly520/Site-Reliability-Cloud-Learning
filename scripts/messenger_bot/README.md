# Messenger Bot

This is a messenger bot that provides a few functionalities! From spamming a friend with messages, stickers, or simply to just smash that **Like** button. Please refer to the sections below to understand how each function works and how they are used.

### Concepts Learned
- OOP
  - [Class](#class)
  - [Object](#object)
  - [Methods](#methods)
  - [Encapsulation](#encapsulation)
- [Selenium Webdriver](#selenium-webdriver)
  - [XPath](#xpath)
  - [ActionChains](#actionchains)
- Python
  - [virtualenv](#virtualenv)
  - [pycache](#pycache)
  - [try/except](#tryexcept)
  - [\_\_main\_\_](#__main__)

### Setup and Execute

Unfortunately, you will have to clone all of the materials in this repository or you can simply copy/pasta the files you need! Additionally, there is an option to use SVN to only clone a specific folder but we won't be using that here.
1. Clone the repository to your local system
```bash
git clone https://github.com/bqly520/Site-Reliability-Cloud-Learning.git
```
###### virtualenv
2. Create and activate your virtual environment, only use `deactivate` to close your virtual environment session. *virtualenv* creates a folder which contains all the necessary executables to use the packages(“site-packages”) that a Python project would need.
```bash
# created a python virtual environment named 'venv'
virtualenv venv

# activates your virtual environment so you can switch to this scope
source venv/bin/activate

# close and exit out of your virtual environment
deactivate
```
###### Selenium Webdriver
3. Install the following packages 
```bash
# installs Selenium framework, drives the interactions on the required web page and rerun them without any manual input
pip3 install selenium

# installs virtual environment for Python
pip3 install virtualenv
```
4. Create a `secrets.py` file with your username and password for Messenger.com
```python
username = 'username_here'
password = 'password_here'
```
###### pycache
5. To ensure your secrets aren't getting cached, we will create an environment variable to suppress `__pycache__` to be created. *\_\_pycache\_\_* are bytecode-compiled and optimized bytecode-compiled versions of your program's files(secrets in this case) that enables your program to start a little faster.
```bash
# open up your bash profile, this file gets executed at terminal start-up
vi ~/.bash_profile

# create an environment variable with any string passed as the argument
export PYTHONDONTWRITEBYTECODE="bobo"

 # Restart your terminal
```
6. **Note:** Please ensure you review `if __name__ == '__main__':` below to make updates on what methods you'd like your bot to use.
7. Finally, you can run the code with using the following command
```bash
# non-interactive session
python messenger_bot.py

# interactive session
python -i messenger_bot.py
```

### Functionalities

###### Class
```python
# A class is a blueprint for the object. The class MessngerBot contains all of the details(attributes) about the bot.
class MessengerBot():

    # init method that includes an incognito flag with a private attribute called 'name'
    # there is a setter function below to make changes to the name attribute if needed
    # if you'd like to start an incognito session, 'enable incognito = True'
    def __init__(self, name, incognito):
    
    # this method will enable you to login to Messenger
    def login(self):
```

###### XPath
```python
# This method has an INFINITE while loop to spam the person of your choice with
# the message passed into the function. To exit out of the infinite loop,
# use the following key combo <CTRL>+C
# XPath can be used to navigate through elements and attributes in an XML document.
def spam(self, person, message):

# This method will ensure your window is messaging the correct person after login
def messagePerson(self, person):
```

###### Methods
```python
# This method will send an emoji or it just smashes that like button
# Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.
def emoji(self):
```

###### try/except
###### ActionChains
```python  
# This method will loop through the dictionary of key words and will choose a randomized sticker
# The try block lets you test a block of code for errors.
# The except block lets you handle the error. This is needed because if we chose a key word that didn't match any stickers,
# we will simply clear out the sticker and try again.
# ActionChains, ActionChains are a way to automate low level interactions such as mouse movements, mouse button actions, key press, and context menu interactions. This is useful for doing more complex actions like hover over and drag and drop.
def sticker(self, person):
```

###### Encapsulation
```python
# This method will allow you to set the name of the sender, and can only be set by using this method, this the the private attribute
# Encapsulation describes the idea of wrapping data and the methods that work on data within one unit.
def setName(self, name):
```

###### Object
###### \_\_main\_\_
```python
# __main__ , If python runs program with main, this will execute everything including main in-order from top to bottom. If python runs a program and imports the program with a main function, the new program will run everything besides the stuff in main!
# An object is also called an instance of a class and the process of creating this object is called instantiation.
# Object is simply a collection of data (variables) and methods (functions) that act on those data. 
if __name__ == '__main__':
```