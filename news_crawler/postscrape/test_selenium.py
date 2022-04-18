from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CHROME_PATH = './drivers/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.headless = True

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), chrome_options=chrome_options)
driver.get("https://cnn.com")


results = driver.find_elements_by_tag_name('a')

to_write = list()
for r in results:
    to_write.append(r.get_attribute('href'))

print(to_write)
with open('cnn_links.txt', 'w')  as f:
    for line in to_write:
        f.writelines(str(line) + "\n")

html = driver.page_source

with open("cnn_homepage_sel.txt", 'w', encoding='utf-8') as f:
    f.write(html)
driver.quit()
