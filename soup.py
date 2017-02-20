import urllib2
from bs4 import BeautifulSoup

url = 'https://ballotpedia.org/Municipal_elections_in_Seattle,_Washington_(2017)'

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, 'lxml')

div = soup.find_all('div', id='General_election')

def org(div):
    res = {}
    print div.h3


def find(elem, res={}):

    try:
        if elem.name == 'h3':
            if elem.span['class'] == ['mw-headline']:
                position = elem.span.text
                # print elem.next_sibling.next_sibling
                if elem.next_sibling.next_sibling.name == 'dl':
                    cands = elem.next_sibling.next_sibling
                    names = getNames(cands.dd)
                    res[position] = names

                elif elem.next_sibling.next_sibling.name == 'h4':
                    # elem = elem.next_sibling.next_sibling
                    if elem.span['class'] == ['mw-headline']:
                        res[position] = {}
                        subpos = elem.span.text
                        if elem.next_sibling.next_sibling.name == 'dl':
                            cands = elem.next_sibling.next_sibling
                            names = getNames(cands.dd)
                            res[subpos] = names
    except:
        pass

    if elem.next_sibling:
        return find(elem.next_sibling, res)
    else:
        print res

def getNames(cand, res=[]):
    try:
        res.append(cand.find_all('a')[1].text)
    except:
        pass

    if cand.next_sibling:
        return getNames(cand.next_sibling, res)
    else:
        return res


find(div[0].div.h3)
