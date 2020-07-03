from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVistorTest(unittest.TestCase):


	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(3)

	def tearDown(self):
		self.driver.quit()

	def check_for_row_in_list_table(self):
		table = self.driver.find_elemeny_by_id('id_list_table')
		row = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.driver.get('http://localhost:8000')

		self.assertIn('To-Do', self.driver.title)
		header_text = self.driver.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		inputbox = self.driver.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		# inputbox.send_keys('Buy peacock feathers')
		# inputbox.send_keys(Keys.ENTER)
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: But peacock feathers')
		# 
		inputbox = self.driver.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)


		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		# table = self.driver.find_element_by_id('id_list_table')
		# rows = table.find_elements_by_tag_name('tr')
		# # self.assertTrue(
		# # 	any(row.text == '1: Buy peacock feathers' for row in rows),
		# # 	"New to-do item did not appear in table -- its text was:\n%s" % (
		# # 		table.text,
		# # 	)
		# # )
		# self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		# self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

		# self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main()