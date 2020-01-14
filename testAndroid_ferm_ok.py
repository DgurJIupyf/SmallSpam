__author__ = "User"

import unittest
from appium import webdriver
import tracemalloc

class FirstAndroidTest(unittest.TestCase):
    tracemalloc.start()
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'My test'
    accessKey = "eyJ4cC51Ijo3ODU5MTkwLCJ4cC5wIjo3ODU5MTg5LCJ4cC5tIjoiTVRVM09Ea3dNelE0TWpNeE13IiwiYWxnIjoiSFMyNTYifQ.eyJleHAiOjE4OTQyNjU1OTAsImlzcyI6ImNvbS5leHBlcml0ZXN0In0.xtNhV9oaJ0P_RzHrX8xYGV_R_ugEC-74kziUD_bLGD0"
    driver = None
    
    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['accessKey'] = self.accessKey
        self.dc['app'] = 'cloud:com.fantasybattles.game'
        self.dc['appPackage'] = 'com.fantasybattles.game'
        self.dc['appActivity'] = 'com.epicgames.ue4.SplashActivity'
        self.dc['platformName'] = 'android'
        self.dc['deviceQuery'] = "@os='android' and @category='PHONE'"
        self.driver = webdriver.Remote("https://cloud.seetest.io/wd/hub",self.dc)
    
    def testProfile(self):
        self.driver.find_element_by_xpath("xpath=//*[@id='usernameTextField']").send_keys('company')

    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities["reportUrl"])
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
