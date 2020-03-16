# Messenger Bot

This is a messenger bot that provides a few functionalities! From spamming a friend with messages, stickers, or simply to just smash that **Like** button. Please refer to the sections below to understand how each function works and how they are used.

### Concepts Learned
- OOP
  - [Class](#class)
  - Object
  - Methods
  - Encapsulation
- Selenium Webdriver
  - XPath
  - ActionChains
- Python
  - [virtualenv](#virtualenv)
  - pycache
  - try/except

### Steps to run this

###### virtualenv
Unfortunately, you will have to clone all of the materials in this repository or you can simply copy/pasta the files you need! Additionally, there is an option to use SVN to only clone a specific folder but we won't be using that here.
1. `git clone https://github.com/bqly520/Site-Reliability-Cloud-Learning.git`
2. create and activate your virtual environment, only use `deactivate` to close your virtual environment session. *virtualenv* creates a folder which contains all the necessary executables to use the packages(“site-packages”) that a Python project would need.
   - `virtualenv venv`
   - `source venv/bin/activate`
   - `deactivate`
3. install the following packages 
   - `pip3 install selenium`
   - `pip3 install virtualenv`
4. 

### Functions

###### Class
'''python
# init method that includes an incognito flag with a private attribute called 'name'
# there is a setter function below to make changes to the name attribute if needed
def __init__(self, name, incognito):
'''
