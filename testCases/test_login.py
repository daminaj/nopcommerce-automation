
from pageObject.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen




class Test_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homepagetitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening Application URL ****")
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "nopCommerce demo store. Login":
            assert True
            self.logger.info("****Home page title test passed****")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_homepagetitle.png")
            self.logger.info("****Home page title test failed****")
            self.driver.close()
            assert False




    def test_login(self, setup):
        self.logger.info("****Started Login test ****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.set_UserName(self.username)
        self.lp.set_Password(self.password)
        self.lp.click_Login()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****Login test passed****")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.logger.info("****Login test failed****")
            self.driver.close()
            assert False


