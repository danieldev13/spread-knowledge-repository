import logging
import scrapy
import settings
import time

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from scrapy.http import Request
from helpers.operating_system_helper import get_download_folder, move_file


class IndexesUpdaterSpider(scrapy.Spider):
    """
    Spider to download BOVA11 data using Selenium and Firefox Web Driver.
    Unlike the default chrome's behavior, Firefox opens a download window confirmation.
    We can disable this feature on firefox's settings page.
    """
    name = 'bova11_spider'
    allowed_domains = ['www.blackrock.com']
    start_urls = ['http://www.blackrock.com/br/tracking-page?document=/br/literature/pcf/pcf-bova11-pt_br.xls']

    def __init__(self):
        """
        For firefox web driver's sake, we need to point to the location of the browser's installation.
        We, then can pass that in the firefox_binary variable to the Firefox web driver parameter.
        """
        binary = FirefoxBinary(settings.web_browser_location)
        self.driver = webdriver.Firefox(firefox_binary=binary)

    def parse(self, response):
        """
        Parses the first request and request the click event on the confirmation button
        """
        self.driver.get(settings.request_url)

        while True:
            try:
                next_req = self.driver.find_element_by_class_name('submit')
                yield Request(settings.confirmation_url, callback=self.parse_callback)
                next_req.click()
                break
            except Exception as err:
                logging.error(err)
                break

        self.driver.close()

        # Waiting to close browser... This gives enough time to download the file.
        time.sleep(settings.sleep_time)

        downloaded_file = get_download_folder() + '\\' + settings.downloaded_file_name
        moved_file = settings.destination_path + settings.new_file_name
        move_file(downloaded_file, moved_file)

    def parse_callback(self, response):
        """
        Callback for request parsing.
        """
        pass
