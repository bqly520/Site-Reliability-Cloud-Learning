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
# virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.
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

# Use this python package to generate random words
pip install random-word

