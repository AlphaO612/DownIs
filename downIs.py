# This script made by Alpha Satellite
import requests
from bs4 import BeautifulSoup

reg = 'com' # ru - russian version site, com - american version site or other region

def status(input):
    rs = None
    siteList = f'https://downdetector.{reg}/ne-rabotaet/rrr/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    pageList = requests.get(siteList, headers=headers)
    soup = BeautifulSoup(pageList.content, "html.parser")
    medium = soup.findAll("div", {"class": "container", "class": "px-3", "class": "px-md-0"})
    soup = BeautifulSoup(str(medium[0]), "html.parser")
    medium = soup.findAll("div", {"class": "col"})
    soup = BeautifulSoup(str(medium[0]), "html.parser")
    a_tags = soup.findAll("a")
    arg = input
    for i in range(len(a_tags)):
        if i != 0:
            if arg in str(a_tags[i]):
                tag = str(a_tags[i])
                word = ""
                i = 0
                while i != len(tag):
                    if i >= 9:
                        if tag[i] + tag[i+1] == '">':
                            break
                        else:
                            word += tag[i]
                    i += 1
                rs = True
                break
            else:
                rs = False
    if rs == True:
        site = f'https://downdetector.{reg}/{word}'
        full_page = requests.get(site, headers=headers)
        soup = BeautifulSoup(full_page.content,"html.parser")
        convert = soup.findAll("div", {"class": "h2", "class": "entry-title"})
        final = BeautifulSoup(str(convert[0]), "html.parser")
        try:
            final.img.decompose()
        except AttributeError:
            print("Img isn't in tag")
        t = str(final.get_text())
        word = ""
        for i in range(len(t)):
            gg = len(t) - 1
            if i != gg:
                if t[i] != " " and t[i] != "\n":
                    word += t[i]
                elif t[i] == " " and t[i+1] != " ":
                    word += t[i]
            elif i == gg:
                if t[i] != " " and t[i] != "\n":
                    word += t[i]
        return word
    else:
        return None


def list():
    word = ''
    siteList = f'https://downdetector.{reg}/ne-rabotaet/rrr/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    pageList = requests.get(siteList, headers=headers)
    soup = BeautifulSoup(pageList.content, "html.parser")
    medium = soup.findAll("div", {"class": "container", "class": "px-3", "class": "px-md-0"})
    soup = BeautifulSoup(str(medium[0]), "html.parser")
    medium = soup.findAll("div", {"class": "col"})
    soup = BeautifulSoup(str(medium[0]), "html.parser")
    a_tags = soup.findAll("a")
    for i in range(len(a_tags)):
        if i != 0:
            word += str(i) + '. ' + a_tags[i].text + ';\n'
    return word

def launch():
    try:
        type = input("Write here name or \"list\" - ")
        if type != "list":
            ready = status(type)
            if ready != None:
                print(f'Answer for {type} -{ready}')
                launch()
            else:
                print(f'{type} service not in system! Please, check name in "list".')
                launch()
        elif type == "list":
            info = list()
            print(f'Sites in system: \n{info}')
            launch()
    except Exception as e:
        print(f'This answer isn\'t correct! Try again...\nFull info about error: {e}')
        launch()

launch()