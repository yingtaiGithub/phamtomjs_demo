import signal

from selenium import webdriver

def init_phantomjs_driver(*args, **kwargs):

    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

    driver =  webdriver.PhantomJS(*args, **kwargs)
    driver.set_window_size(1400, 1000)

    return driver


class Crawler():
    def __init__(self):

        self.driver = init_phantomjs_driver(executable_path='driver/phantomjs')

        self.driver.implicitly_wait(10)  # seconds
        self.driver.set_page_load_timeout(30)

        self.starting()


    def starting(self):
        self.driver.get("http://formyip.com")
        print (self.driver.current_url)
        self.driver.save_screenshot('check.png')

    def quit(self):
        try:
            self.driver.service.process.send_signal(signal.SIGTERM)
            self.driver.quit()
        except:
            self.driver.quit()


crawler = Crawler()
