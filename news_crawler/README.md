### News source APIs

newscatcher FREE 1000 calls / month
newsapi 100 requests / day
bingsearch api 1000 transactions / month

### Install scrapy
pip install scrapy

### Start scrapy project
scrapy startproject <project_name>

### Configure splash engine to handle javascript render websites like cnn.com
github: https://github.com/scrapy-plugins/scrapy-splash
1 .pip install scrapy-spash
2. docker pull scrapinghub/splash
3. then start docker spash container: 
    docker run -p 8050:8050 scrapinghub/splash