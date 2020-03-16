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
  - [pycache](#pycache)
  - try/except

### Setup and Execute

##### virtualenv
##### pycache
Unfortunately, you will have to clone all of the materials in this repository or you can simply copy/pasta the files you need! Additionally, there is an option to use SVN to only clone a specific folder but we won't be using that here.
1. Clone the repository to your local system
   - `git clone https://github.com/bqly520/Site-Reliability-Cloud-Learning.git`
2. Create and activate your virtual environment, only use `deactivate` to close your virtual environment session. *virtualenv* creates a folder which contains all the necessary executables to use the packages(“site-packages”) that a Python project would need.
   - `virtualenv venv`
   - `source venv/bin/activate`
   - `deactivate`
3. Install the following packages 
```bash
# installs Selenium framework, drives the interactions on the required web page and rerun them without any manual input
pip3 install selenium
# installs virtual environment for Python
pip3 install virtualenv
```
4. To ensure your secrets aren't getting cached, we will create an environment variable to suppress `__pycache__` to be created. *\_\_pycache\_\_* are bytecode-compiled and optimized bytecode-compiled versions of your program's files(secrets in this case) that enables your program to start a little faster.
   - `vi ~/.bash_profile`
   - `export PYTHONDONTWRITEBYTECODE="bobo"`
   - Restart your terminal
5. 

### Functions

##### Class
```python
class MessengerBot():

# init method that includes an incognito flag with a private attribute called 'name'
# there is a setter function below to make changes to the name attribute if needed
    def __init__(self, name, incognito):


```
