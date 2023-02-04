from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import PyPDF2
import urllib.request

url = 'https://www.simplyscripts.com/movie-screenplays.html'
driver = webdriver.Chrome()
try:
    driver.get(url=url)
    god = driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Lord of the Rings: The Fellowship of the Ring').get_attribute('href')
    browser = webdriver.Chrome()
    browser.get(url=god)
    url2 = god
    
    urllib.request.urlretrieve(url2, "fuck.pdf")
    r = requests.get(url2)
    with open("fuck1.pdf", "wb") as code:
        code.write(r.content)
    
    file = open('fuck1.pdf', 'rb')
    pdfreader = PyPDF2.PdfFileReader(file, strict=False)
    x = pdfreader.numPages
    for chapter in range(x):
        page = pdfreader.getPage(chapter)
        text = page.extractText()
        print(text)
        file1 = open(r"C://Users//79265//Desktop//fuck.txt", "a", errors="ignore")#там были какие-то ошибки, из-за которых файл не читался нормально
        # вместо C://Users//79265//Desktop// нужно вставить свой путь
        file1.writelines(text)
        file1.close()
        
    os.remove('fuck.pdf')
    file.close()
    os.remove('fuck1.pdf')
except Exception as ex:
    print(ex)
