import requests
from bs4 import BeautifulSoup
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKGREENFAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "" + bcolors.ENDC)


urls = ["https://www.newegg.com/p/pl?d=3080%20combo&cm_mmc=snc-twitter-_-pm-restock-_-3080combos-_-na",
        "https://www.newegg.com/p/pl?d=3070%20combo&cm_mmc=snc-twitter-_-pm-restock-_-3070combos-_-na",
        "https://www.newegg.com/p/pl?d=rtx%203060%20combo&cm_mmc=snc-twitter-_-pm-restock-_-3060combos-_-na"]


def check_stock_on_newegg(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers, timeout=(3, 3))
    soup = BeautifulSoup(response.text, "lxml")
    item_div = soup.findAll("div", {"class": "item-cell"})
    for item in item_div:  
        title_soup= item.find("a", {"class": "item-title"})
        try:
            title = title_soup.text[:60]
        except:
            pass
        try:
            href = title_soup.attrs['href']
        except:
            pass
        stock_soup = item.find("p", {"class": "item-promo"})
        try:   
            stock_status = stock_soup.text
        except:
            pass
        if stock_status == "OUT OF STOCK":
            print(bcolors.FAIL + stock_status, "-", title, "-", href + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + stock_status, "-", title, "-", href + bcolors.ENDC)

        # print(stock_status, "-", title, "-", href)


while True:
    for url in urls:
        check_stock_on_newegg(url)
        time.sleep(1)
    time.sleep(1)

