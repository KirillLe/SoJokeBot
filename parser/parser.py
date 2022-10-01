import requests
from bs4 import BeautifulSoup
import random


URL ="https://anekdoty.ru"
def parser(url):
    get_url = requests.get(url)
    get_soup = BeautifulSoup(get_url.text, "html.parser")
    get_joke = get_soup.find_all("div", class_="holder-body")
    return [c.text for c in get_joke]


clear_list_joke = parser(URL)
random.shuffle(clear_list_joke)
