from selenium import webdriver
import os
import time

class InstagramBot:
    
    def __init__(self, username, password):


        """

        Args:
            username:str: the instagram username for a user
            password:str: insta password for a user

        Attributes:

        driver:selenium.webdriver.Chrome  Chrome webdriver

        """


        
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'

        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()


    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))

        time.sleep(2)
        '''self.driver.implicitly_wait(10)'''
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

        time.sleep(2)
        

    def nav_user(self, user):

        self.driver.get('{}/{}/'.format(self.base_url, user))
        time.sleep(2)

    def follow_user(self, user):

        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()
        time.sleep(10)

    def unfollow_user(self, user):

        self.nav_user(user)

        following_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Following')]")[0]
        following_button.click()
        time.sleep(2)

        unfollow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")[0]
        unfollow_button.click()


if __name__ == '__main__':

    ig_bot = InstagramBot('temp_username', 'temp_password')

    test_user = 'manchesterunited'
    ig_bot.follow_user(test_user)
    ig_bot.unfollow_user(test_user)

