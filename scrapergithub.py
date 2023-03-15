import requests;
import json;
import html;
from bs4 import BeautifulSoup as soup;
import urllib
import urllib.request
import wget
import re
import pathlib;

print("Enter the link")
urluser = input()
page_content = requests.get(urluser).content
soup_page = soup(page_content, 'html.parser')
zip_links_list_nourl = []
zip_links_list_url= []
# print(soup_page)
 
for link in soup_page.find_all('a', attrs={"class": "Link--muted", "rel": "nofollow"}):
    zip_link = link.get('href')
    zip_links_list_nourl.append(zip_link)
for link in zip_links_list_nourl:
    url_beginning = "https://github.com"
    url_beginning+=link
    zip_links_list_url.append(url_beginning)
for link in zip_links_list_url:
    if(pathlib.Path(link).suffix==".gz"):
        zip_links_list_url.pop(zip_links_list_url.index(link))
        
# print(zip_links_list_url)

html_content = requests.get(urluser).text
souppagecontent = soup(html_content, "html.parser")
texts = souppagecontent.find_all('h2', {"class": "f4 d-inline"} )
contenttext = []
for text in texts:
    contenttext.append(text.get_text())
# print(contenttext[len(contenttext)-1])
newlink = urluser + "?after="  + contenttext[len(contenttext)-1]

# #check if we are at last page or not
while len(contenttext)!=0:
    page_content = requests.get(newlink).content
    soup_page = soup(page_content, 'html.parser')
    for link in soup_page.find_all('a', attrs={"class": "Link--muted", "rel": "nofollow"}):
        zip_link = link.get('href')
        zip_links_list_nourl.append(zip_link)
    for link in zip_links_list_nourl:
        url_beginning = "https://github.com"
        url_beginning+=link
        zip_links_list_url.append(url_beginning)
    for link in zip_links_list_url:
        if(pathlib.Path(link).suffix==".gz"):
            zip_links_list_url.pop(zip_links_list_url.index(link))

#get content to find the last tag for each page 
    html_content = requests.get(newlink).text
    souppagecontent = soup(html_content, "html.parser")
    texts = souppagecontent.find_all('h2', {"class": "f4 d-inline"} )
    contenttext = []
    for text in texts:
        contenttext.append(text.get_text())
        newlink = urluser +"?after="  + contenttext[len(contenttext)-1]
# print(zip_links_list_url)
for i in zip_links_list_url:
    wget.download(i)




