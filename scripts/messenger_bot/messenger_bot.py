from selenium import webdriver

class MessengerBot():

    # init methods or contructors
    def __init__(self, name):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.name = name

    def login(self):
        self.driver.get("https://www.messenger.com")


if __name__ == '__main__':
    bot = MessengerBot("Bobo")
    bot.login()