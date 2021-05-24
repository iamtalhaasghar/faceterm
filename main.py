from selenium.webdriver import Firefox
from progress.spinner import Spinner
from selenium.webdriver.firefox.options import Options

pageUrl = 'https://www.facebook.com/GitHub'
url = 'https://www.facebook.com/plugins/page.php?href={{href_value}}&tabs=timeline&width=500'
url = url.replace('{{href_value}}', pageUrl)

options = Options()
options.headless = True
firefox = Firefox(options=options)
print('Opening browser...')
firefox.get(url)

# wait until posts are being loaded
posts = []
spinner = Spinner('Loading ')
spinner.start()
while len(posts) == 0:
    spinner.next()
    posts = firefox.find_elements_by_xpath('//div[@data-testid="post_message"]')

spinner.finish()

for p in posts:
    print(p.text, end='\n**************************\n')

firefox.close()
