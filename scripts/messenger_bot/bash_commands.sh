# https://chromedriver.chromium.org/
## WebDriver is an open source tool for automated testing of webapps across many browsers. 
## It provides capabilities for navigating to web pages, user input, JavaScript execution, and more.
## Download chromedrive and move it to /usr/local/bin folder

mv ~/Downloads/chromedrive /usr/local/bin

# Installing Selenium, SELENIUM is a free (open-source) automated testing framework used to validate web applications across different browsers and platforms.
# Selenium Framework is a suite of automation testing tools that is based on the JavaScript framework. 
# It could run the tests directly on the target browser, drive the interactions on the required web page and rerun them without any manual input.
pip3 install selenium

# We use a module named virtualenv which is a tool to create isolated Python environments. 
# virtualenv creates a folder which contains all the necessary executables to use the packages(“site-packages”) that a Python project would need.
# In a scenario where we're using Two versions of Django, Python can’t differentiate between versions in the “site-packages” directory.
# https://www.geeksforgeeks.org/python-virtual-environment/
pip3 install virtualenv

# Create Virtual Environment
virtualenv venv

# Now after creating virtual environment, you need to activate it. 
# Remember to activate the relevant virtual environment every time you work on the project. This can be done using the following command
source venv/bin/activate

# To Exit Virtual Environment
deactivate

# Run script as an interactive session
python -i messenger_bot.py

# https://stackoverflow.com/questions/48339682/using-python-selenium-to-send-message-to-friend-in-facebook
# Had to follow this to figure out how to send messages... :)

# Use this python package to generate random words, used my own dictionary instead :p
pip install random-word

# https://stackoverflow.com/questions/16869024/what-is-pycache
# Best to remove pycache so someone doesn't accidentally push their secrets into Github if they forget to update .gitignore
# -i flag is for interactive session, -B suppresses the use of pycache
# A __pycache__ folder is created when you use the line:
# import file_name
# or try to get information from another file you have created. 
# This makes it a little faster when running your program the second time to open the other file.
python -B -i messenger_bot.py
vi ~/.bash_profile
export PYTHONDONTWRITEBYTECODE="bobo"