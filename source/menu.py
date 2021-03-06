import re
from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString
def info():

    '''
    (None) -> (list1, list2)
    Function which parses HTML document to return lists with menu and weidth of dishes
    '''

    
    html = urlopen(r"https://docs.google.com/spreadsheets/d/1dtpfEkxVrdHKfAg3cDl2vUl4f204tFT4PRwF9KpsFLE/pubhtml?&amp;gid=1030797794&amp;single=true&amp;widget=false&amp")
    info = html.read().decode('utf-8').replace('\u0456', 'i').replace('\u0406', 'I')
    soup = BeautifulSoup(info, features="html.parser")
    film_list1 = soup.findAll('td', {'class': 's4'})
    film_list2 = soup.findAll('td', {'class': 's5'})
    film_list3 = soup.findAll('td', {'class': 's6'})
    menu = []
    for p in film_list1:
        p = p.text.strip()
        if p != '':
            menu.append(p)
    for p in film_list2:
        p = p.text.strip()
        if p != '':
            menu.append(p)
    for p in film_list3:
        p = p.text.strip()
        if p != '':
            menu.append(p)
    list1, list2 = [], []
    for i in range(0, int(len(menu)), 2):
        list1.append(menu[i])
        try:
            list2.append(int(menu[i + 1]))
        except:
            pass
    return (list1, list2)
