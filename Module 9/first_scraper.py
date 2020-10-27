import requests
import bs4

url = 'https://netforum.avectra.com/eweb/StartPage.aspx?Site=MSA'
response = requests.get(url)
html = response.content
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close
soup = bs4.BeautifulSoup(open("requestResult.txt"), 'html.parser')
print(soup.prettify())