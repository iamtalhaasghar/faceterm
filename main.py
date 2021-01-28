from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from progress.spinner import Spinner

from urllib.request import urlopen
url = 'https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2Fkfueit.official%2F&tabs=timeline&width=12000&_rdc=2&_rdr'
firefox = Firefox(executable_path='/home/talha/Programs/geckodriver')
spinner = Spinner('Loading ')
spinner.start()
firefox.get(url)

# wait until posts are being loaded
posts = []

while len(posts) == 0:
    spinner.next()
    posts = firefox.find_elements_by_tag_name("p")

spinner.finish()

for p in firefox.find_elements_by_tag_name('p'):
    print(p.text, end='\n**************************\n')

firefox.close()