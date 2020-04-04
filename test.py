import unittest
from selenium.webdriver import Chrome
import app


class YATest(unittest.TestCase):
    def setUp(self):
        self.login = 'fdfgg'
        self.password = 'dsf'
        self.driver = Chrome()

    def tearDown(self):
        self.driver.close()

    def test_login(self):
        self.driver.get(app.URL)
        login_field = app.get_login_field(self.driver)
        self.assertIsNotNone(login_field, 'поле с логтном не найдено')
        login_field.send_keys(self.login)
        btn = app.get_btn(self.driver)
        self.assertIsNotNone(btn, 'кнопку не нашли')
        btn.click()
        self.assertTrue(app.check(self.driver), 'логин неправильный')
        password_field = app.get_password_field(self.driver)
        self.assertIsNotNone(password_field, 'поле с паролем не найдено')
        password_field.send_keys(self.password)
        btn = app.get_btn(self.driver)
        self.assertIsNotNone(btn, 'кнопку не нашли')
        btn.click()
        self.assertTrue(app.check(self.driver), 'пароль неправильный')


if __name__ == "__main__":
    unittest.main()
