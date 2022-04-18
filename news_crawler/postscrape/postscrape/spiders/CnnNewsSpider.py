import scrapy
from selenium.webdriver import Chrome, ChromeOptions 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrapy_splash import SplashRequest

CHROME_PATH = './drivers/chromedriver.exe'

class CnnNewsSpider(scrapy.Spider):

    name = 'cnn_news'


    def start_requests(self):
        url = 'https://cnn.com'
        # yield scrapy.Request(url = url, callback = self.parse)
        yield SplashRequest(url, self.parse, args={'wait': 0.5})
    
    def parse(self, response):
        filename = 'cnn_splash.html'
        with open(filename, 'wb') as f:
           f.write(response.body)
        self.log('saved file: ', filename)

        # blogpost = response.xpath('//*[@id="homepage1-zone-1"]/div[2]/div/div[1]/ul/li[1]/article/a/h2/text()').get()
        # yield {
        #     'blogpost': blogpost
        # }

    # def start_requests(self):
    #     chrome_options = ChromeOptions()
    #     chrome_options.add_argument("--ignore-certificate-errors")
    #     chrome_options.add_argument("--ignore-ssl-errors")
    #     chrome_options.headless = True

    #     driver = Chrome(service = Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    #     driver.get('https://cnn.com')
    #     results = driver.find_elements_by_xpath('//*[@id="homepage1-zone-1"]/div[2]/div/div[1]/ul/li[1]/article/a/h2')
    #     for r in results:
    #         print(r)
    #         yield scrapy.Request(r)
    #     driver.quit()

    # def parse(self, response):
    #     print(response)

    # def parse(self, response):
    #     filename = 'playwright.txt'
    #     with open(filename, 'wb') as f:
    #        f.write(response.body)
    #     self.log('saved file: ', filename)