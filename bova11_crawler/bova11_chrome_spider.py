import logging
import scrapy
import settings
import time

from selenium import webdriver
from scrapy.http import Request
from helpers.operating_system_helper import get_download_folder, move_file, delete_file


class IndexesUpdaterSpider(scrapy.Spider):
    """
    Spider to download BOVA11 data using Selenium and Chrome Web Driver.
    Opens the web browser, downloads the file and then closes the web browser window.
    """
    name = 'bova11_spider'
    allowed_domains = ['www.blackrock.com']
    start_urls = ['http://www.blackrock.com/br/tracking-page?document=/br/literature/pcf/pcf-bova11-pt_br.xls']

    def __init__(self):
        """
        Unlike firefox web driver's needs, Chrome drive needs to point to chromedriver.exe
        file, so that the web driver can execute successfully.
        """
        self.driver = webdriver.Chrome(settings.web_driver_location)

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

        # Waiting to close browser... This gives enough time to download the file.
        time.sleep(settings.sleep_time)

        downloaded_file = get_download_folder() + '\\' + settings.downloaded_file_name
        moved_file = settings.destination_path + settings.new_file_name
        move_file(downloaded_file, moved_file)
        delete_file(downloaded_file)

    def parse_callback(self, response):
        """
        Callback for request parsing. Just closes the driver
        """
        self.driver.close()
