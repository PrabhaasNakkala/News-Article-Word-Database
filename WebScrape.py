from bs4 import BeautifulSoup
import requests


#different sections: {word, frequency, year, month, topic}

url_list  = []
html_page = requests.get("https://www.cnn.com/investing/article/sitemap-2019-6.html")
sup = BeautifulSoup(html_page.text, 'lxml')
for link in sup.findAll('span', {'class' : 'sitemap-link'}):
    for lk in link.find_all('a'):
        url_list.append(lk.get('href'))
#print(url_list.split())


#for i in url_list:
 #   raw_text = requests.get(i)
  #  soup = BeautifulSoup(raw_text.text, 'lxml')
   # words = soup.find_all('p', class_ = 'paragraph inline-placeholder')
    #paragraph = ""
    #for i in words:
     #   paragraph += i.text + " "
     #   print(paragraph)


raw_text = requests.get(url_list[3])
soup = BeautifulSoup(raw_text.text, 'lxml')
words = soup.find_all('p', class_ = 'paragraph inline-placeholder')
print(words)    
paragraph = ""
for i in words:
   paragraph += i.text + " "
print(paragraph.strip())