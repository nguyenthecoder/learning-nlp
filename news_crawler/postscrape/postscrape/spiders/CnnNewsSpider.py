import scrapy

class CnnNewsSpider(scrapy.Spider):

    name = 'cnn_news'

    def start_requests(self):
        urls = [
            # 'https://www.cnn.com/europe/live-news/ukraine-russia-putin-news-04-16-22/h_1c5cd943e1bccb410f8fa54d387d718c'
            'https://www.cnn.com/europe/live-news/ukraine-russia-putin-news-04-16-22/index.html'
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        filename = 'cnn_sample.html'
        with open(filename, 'wb') as f:
           f.write(response.body)
        self.log('saved file: ', filename)