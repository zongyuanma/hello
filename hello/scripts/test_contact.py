import time

import pytest
from appium import webdriver

from base.base_analyze import analyze_data
from page.add_contact_page import AddContactPage
from page.contact_list_page import ContactListPage
from page.res_page import ResPage


class TestContact:

    def setup(self):
        # 创建一个字典，包装相应的启动参数
        desired_caps = dict()
        # 需要连接的手机的平台(不限制大小写)
        desired_caps['platformName'] = 'Android'
        # 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
        desired_caps['platformVersion'] = '5.1'
        # 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # 需要启动的程序的包名
        desired_caps['appPackage'] = 'com.android.contacts'
        # 需要启动的程序的界面名
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        # 不重置应用
        desired_caps['noReset'] = True

        # 连接appium服务器
        self.driver = webdriver.Remote('http://192.168.1.42:4723/wd/hub', desired_caps)

        # 创建页面对象
        self.add_contact_page = AddContactPage(self.driver)
        self.contact_list_page = ContactListPage(self.driver)
        self.res_page = ResPage(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("contact_data", "test_add_contact"))
    def test_add_contact(self, args):

        name = args["name"]
        phone = args["phone"]

        self.contact_list_page.click_add_contact()
        self.add_contact_page.input_name(name)
        self.add_contact_page.input_phone(phone)
        self.add_contact_page.click_back()
        assert self.res_page.get_title_text() == name