from selenium import webdriver

def check_sites():
    # @TODO add browser driver to /usr/bin or /usr/local/bin for deployment
    browser = webdriver.Firefox()
    browser.get("https://www.newegg.com/evga-geforce-rtx-3090-24g-p5-3987-kr/p/N82E16814487526?Description=rtx%203090&cm_re=rtx_3090-_-14-487-526-_-Product")
    elem = browser.find_element_by_class_name("product-inventory")
    print(elem)
    if "out of stock" in elem.text.lower():
        print("site out of stock")
    else:
        print("in stock, link: ")
    browser.quit()
check_sites()