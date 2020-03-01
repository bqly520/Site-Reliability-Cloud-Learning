# Created an alias inside .bash_profile to default to python3
vi .bash_profile
    - alias python="python3"

# Updated pip and then used pip3 to install SSL packages
pip install --upgrade pip
pip install --upgrade pyOpenSSL

# Install Google search python library, which installed it for python 2.7...
pip install google

# Troubleshooting to install Google search for python 3.x...
# https://stackoverflow.com/questions/41328451/ssl-module-in-python-is-not-available-when-installing-package-with-pip3
brew update && brew upgrade
brew uninstall --ignore-dependencies openssl
brew install openssl

pip3 install google, worked!


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Wall Street Bets ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
# Helpful Links:
# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
# https://praw.readthedocs.io/en/latest/getting_started/authentication.html#