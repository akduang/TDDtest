from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])
    def test_can_start_a_list_and_retrieve_it_later(self):
        #伊迪斯听说有一个很酷的在线待办事项应用
        #她去看了这个应用的首页
        self.browser.get('http://localhost:8000')
        #她注意到网页的标题和头部都包含“To-Do”这个词
        print(self.browser.title)
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)
        # print(self.browser.title)
        # self.fail('Finish the test!')

        #应用邀请她输入一个待办事项
        inputbox = self.browser.find_element(By.ID,'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #她在一个文本框中输入了“Buy peacock feathers”（购买孔雀）
        #伊迪斯的爱好是使用假蝇做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        #她按回车键后，页面更新了
        #待办事项表格中显示了“1：Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        #页面中又显示了一个文本框，可以输入其他的待办事项
        #她输入了“Use peacock feathers to make a fly”
        #伊迪斯做事很有条理
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        #页面再次更新，她的清单中显示了这两个待办事项
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')
        #伊迪斯想知道这个网站是否会记住她的清单
        #她看到网站为她生成了一个唯一的URL
        #而且页面有一些文字解说这个功能
        self.fail('Finish the test')
        #她访问那个URL，发现她的待办事项列表还在
        #她很满意，去睡觉了
if __name__=='__main__':
    unittest.main(warnings='ignore')

# browser = webdriver.Firefox()
#伊迪斯听说有一个很酷的在线待办事项应用
#她去看了这个应用的首页
# browser.get('http://localhost:8000')

#她注意到网页的标题和头部都包含“To-Do”这个词
# assert 'To-Do' in browser.title, "Browser title was" + browser
#应用邀请她输入一个待办事项
#她在一个文本框中输入了“Buy peacock feathers”（购买孔雀）
#伊迪斯的爱好是使用假蝇做饵钓鱼
#她按回车键后，页面更新了
#待办事项表格中显示了“1：Buy peacock feathers”
#页面中又显示了一个文本框，可以输入其他的待办事项
#她输入了“Use peacock feathers to make a fly”
#伊迪斯做事很有条理
#页面再次更新，她的清单中显示了这两个待办事项
#伊迪斯想知道这个网站是否会记住她的清单
#她看到网站为她生成了一个唯一的URL
#而且页面有一些文字解说这个功能
#她访问那个URL，发现她的待办事项列表还在
#她很满意，去睡觉了

# browser.quit()