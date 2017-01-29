import datetime


request_url = 'http://www.blackrock.com/br/literature/pcf/pcf-bova11-pt_br.xls'
confirmation_url = 'http://www.blackrock.com/br/compliance/terms-and-conditions?targetUrl=%2Fbr%2Fliterature%2Fpcf%2Fpcf-bova11-pt_br.xls&action=ACCEPT'
web_driver_location = 'path\\to\\chromedriver.exe'
web_browser_location = 'path\\to\\firefox.exe'
downloaded_file_name = 'pcf-bova11-pt_br.xls'
new_file_name = 'Bova11_{0}.xls'.format(str(datetime.datetime.now().date().strftime('%d%m%Y')))
destination_path = 'path\\to\\drop\\'
sleep_time = 3
