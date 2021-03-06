from selenium import webdriver
from time import sleep
from secrets import username, password
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

PYTHONDONTWRITEBYTECODE="bobo"
class MessengerBot():

    # init methods or contructors
    def __init__(self, incognito):
        if incognito == True:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(options=chrome_options)
            self.__name = "Bobo"
        else:
            self.driver = webdriver.Chrome()
            self.__name = "Bobo"

    def login(self):
        self.driver.get("https://www.messenger.com")

        # needed for the element to load into Chrome and display
        sleep(2)

        # passing in username, password, and press login
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

    def spam(self, person, message):
        self.messagePerson(person)

        # an infinite loop to send a funny message
        while True:
            message_in = self.driver.find_element_by_xpath("//*[@data-editor]").click()
            actions = ActionChains(self.driver)
            actions.send_keys(message + " -" + self.__name + "\n")
            actions.perform()

    def emoji(self):
        # send a like emoji too!
        sleep(1)
        self.driver.find_element_by_xpath("//a[@aria-label='Send a Like']").click()
    
    def messagePerson(self, person):
        sleep(2)
        self.driver.get("https://www.messenger.com/t/" + person)
        sleep(2)

    # Need to figure out a more simple dictionary to be able to find stickers :)
    def sticker(self, person):
        self.messagePerson(person)

        # send a sticker too!
        sleep(1)
        self.driver.find_element_by_xpath("//a[@aria-label='Choose a sticker']").click()
        flag = True

        while flag:

            sleep(1)

            word_file = "dictionary"
            randomWords = open(word_file).read().splitlines()
            random = randomWords[randint(0, len(randomWords)-1)]

            self.driver.find_element_by_xpath("//input[@placeholder='Search stickers']").click()
            actions = ActionChains(self.driver)
            actions.send_keys(random)
            actions.perform()
            sleep(2)

            try:
                sticker = self.driver.find_element_by_xpath("//td[@class='_51m-']").click()
                self.driver.find_element_by_xpath("//button[@class=' _2pge _42ft']").click()
                flag = False
            except Exception:
                # clearing out sticker to try again
                self.driver.find_element_by_xpath("//button[@class=' _2pge _42ft']").click()
                print("Oops. There was an exception. Trying again...")
        
    def setName(self, name):
        self.__name = name

if __name__ == '__main__':
    annoyingMsg = "Good morning, sunshine."
    bot = MessengerBot(True)
    bot.login()
    #bot.setName("Hacker")
    #bot.spam("neverlandfairy", annoyingMsg)
    bot.sticker("neverlandfairy")
