from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(3)
    url = "https://scrapeme.live/shop/"
    driver.get(url)
    #elements = driver.find_elements_by_xpath("//div[@class='expeties-block']/div/a/h4")
    elements = driver.find_elements_by_class_name('woocommerce-loop-product__title')

    expertise = []
    for element in elements:
        expertise.append(element.get_attribute('innerHTML'))
    print(r'Defined expertise in %s' % url)
    print(expertise)

if __name__ == '__main__':
    main()