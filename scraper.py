import requests;
import html;
from bs4 import BeautifulSoup as soup;
import urllib
import urllib.request
import wget


url = " https://gitlab.com/wireshark/wireshark/-/tags" #user-input
page_content = requests.get(url).content
soup_page = soup(page_content, 'html.parser')
print(soup_page)
zip_links_list_nourl = []
zip_links_list_url= []

links = soup_page.findAll("a",{"class": "gl-button btn btn-sm btn-confirm"})
# for link in soup_page.find_all('a', {"class": "gl-button btn btn-sm btn-confirm"}):
#     zip_link = link.get('href')
#     url_beginning+=zip_link
#     zip_links_list.append(url_beginning)
# print(zip_links_list)

for link in soup_page.find_all('a', {"class": "gl-button btn btn-sm btn-confirm"}):
    zip_link = link.get('href')
    zip_links_list_nourl.append(zip_link)

for link in zip_links_list_nourl:
    url_beginning = "https://gitlab.com"
    url_beginning+=link
    zip_links_list_url.append(url_beginning)
    
for i in zip_links_list_url:
    wget.download(i)
    


