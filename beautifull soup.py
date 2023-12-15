# 13:28 / 16:27 continue from here


from bs4 import BeautifulSoup 
import requests

website = 'https://subslikescript.com/movies'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')

link =[]

for link in box.find_all('a',href=True):
 link.append(link['hrf'])

 print(link)



#title =  box.find('h1').get_text() 

#transcript = box.find('div',class_='full-script').get_text(strip=True, separator=' ')

#print(transcript)

# Specify the encoding as 'utf-8'
#with open(f'{title}.csv', 'w', encoding='utf-8') as file:
#    file.write(transcript)


