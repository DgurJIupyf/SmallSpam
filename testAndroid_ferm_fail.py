__author__ = "User"

import unittest
from appium import webdriver
from airtest.core.api import *
from airtest.report.report import simple_report
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
        auto_setup(__file__, logdir=True)
        wait(Template(r"waitAllow.png", record_pos=(-0.008, -0.068), resolution=(2310, 1080)))
        touch(Template(r"allow.png", record_pos=(0.094, 0.127), resolution=(2310, 1080)))
        touch(Template(r"tpl1578653206245.png", record_pos=(-0.398, -0.176), resolution=(2310, 1080)))
        wait(Template(r"tpl1578664637506.png", record_pos=(-0.054, -0.089), resolution=(2310, 1080)))
        snapshot(filename="PofileMenu.png", msg="Please fill in the test point.")        
        assert_exists(Template(r"tpl1578653371049.png", record_pos=(-0.09, 0.097), resolution=(2310, 1080)), "Смена имени на месте")
        assert_exists(Template(r"tpl1578653392440.png", record_pos=(-0.365, 0.187), resolution=(2310, 1080)), "Поддержка на месте")
        assert_exists(Template(r"tpl1578653426063.png", record_pos=(-0.413, -0.192), resolution=(2310, 1080)), "Назад на месте")
        assert_exists(Template(r"tpl1578653574481.png", record_pos=(0.154, 0.001), resolution=(2310, 1080)), "Настройки звука на месте")
        simple_report(__file__, logpath=True, output='reportProfile.html')

    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities["reportUrl"])
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
