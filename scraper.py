import requests;
import json;
import html;
from bs4 import BeautifulSoup as soup;
import urllib
import urllib.request
import wget

#get total number of pages

#get project id
urluser = " https://gitlab.com/wireshark/wireshark"
page_content = requests.get(urluser).content
soup_page = soup(page_content, 'html.parser')
for id in soup_page.findAll('div', {"id": "js-tree-ref-switcher"}):
    projectid = id.get('data-project-id')
print(projectid)


urluser = "https://gitlab.com/wireshark/wireshark"
urlchangedapi = "https://gitlab.com/api/v4/projects/" + projectid + "/repository/tags/?per_page=20&page=1"
data = requests.get(urlchangedapi)
totalpages = data.headers["X-Total-Pages"]
print(totalpages)

index = 1
while index <= int(totalpages) :

    pagenumber = index 
    url = urluser + "/-/tags?page=" + str(pagenumber)
    page_content = requests.get(url).content
    soup_page = soup(page_content, 'html.parser')
    zip_links_list_nourl = []
    zip_links_list_url= []

    # links = soup_page.findAll("a",{"class": "gl-button btn btn-sm btn-confirm"})

    for link in soup_page.find_all('a', {"class": "gl-button btn btn-sm btn-confirm"}):
           zip_link = link.get('href')
           zip_links_list_nourl.append(zip_link)

    for link in zip_links_list_nourl:
        url_beginning = "https://gitlab.com"
        url_beginning+=link
        zip_links_list_url.append(url_beginning)
    
    for i in zip_links_list_url:
        wget.download(i)
    index+=1




    












































