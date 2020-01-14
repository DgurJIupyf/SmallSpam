__author__ = "User"

import unittest
from appium import webdriver
from airtest.core.api import *
from airtest.report.report import simple_report

class FirstAndroidTest(unittest.TestCase):
    f = open('fullReport.html', 'w').close()
    x = {}
    
    def setUp(self):
        init_device("Android")
        start_app("com.fantasybattles.game")
    
    def testProfile(self, x):
        auto_setup(__file__, logdir=True)
        touch(Template(r"tpl1578653206245.png", record_pos=(-0.398, -0.176), resolution=(2310, 1080)))
        wait(Template(r"tpl1578664637506.png", record_pos=(-0.054, -0.089), resolution=(2310, 1080)))
        snapshot(filename="PofileMenu.png", msg="Please fill in the test point.")        
        assert_exists(Template(r"tpl1578653371049.png", record_pos=(-0.09, 0.097), resolution=(2310, 1080)), "Смена имени на месте")
        assert_exists(Template(r"tpl1578653392440.png", record_pos=(-0.365, 0.187), resolution=(2310, 1080)), "Поддержка на месте")
        assert_exists(Template(r"tpl1578653426063.png", record_pos=(-0.413, -0.192), resolution=(2310, 1080)), "Назад на месте")
        assert_exists(Template(r"tpl1578653574481.png", record_pos=(0.154, 0.001), resolution=(2310, 1080)), "Настройки звука на месте")
        simple_report(__file__, logpath=True, output='reportProfile.html')

    def testSkillSelect1(self):
        auto_setup(__file__, logdir=True)
        touch(Template(r"tpl1578657509331.png", target_pos=6, record_pos=(0.165, 0.059), resolution=(2310, 1080)))
        assert_exists(Template(r"tpl1578657165257.png", record_pos=(-0.382, 0.052), resolution=(2310, 1080)), "На месте")
        touch(Template(r"tpl1578668006338.png", record_pos=(-0.385, 0.047), resolution=(2310, 1080)))
        assert_exists(Template(r"tpl1578668271653.png", record_pos=(-0.29, 0.044), resolution=(2310, 1080)), "первый скилл открыт")
        assert_exists(Template(r"tpl1578668298982.png", record_pos=(-0.384, 0.046), resolution=(2310, 1080)), "Ветка стрелка выбрана")       
        touch(Template(r"tpl1578668055794.png", record_pos=(-0.385, 0.136), resolution=(2310, 1080)))
        assert_exists(Template(r"tpl1578668160579.png", record_pos=(-0.29, 0.045), resolution=(2310, 1080)), "Первый скил открыт")
        assert_exists(Template(r"tpl1578668184565.png", record_pos=(-0.384, 0.133), resolution=(2310, 1080)), "Ветка магии выбрана")
        simple_report(__file__, logpath=True, output='reportSkillSelect1.html')

    def tearDown(self):
        stop_app("com.fantasybattles.game")
       
if __name__ == '__main__':
    unittest.main()
