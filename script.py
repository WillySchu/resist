from lxml import html
import requests

url = 'https://ballotpedia.org/Municipal_elections_in_Seattle,_Washington_(2017)'

page = requests.get(url)
tree = html.fromstring(page.content)

div = tree.xpath('//*[@id="General_election"]/div')

a = tree.xpath('//*[@id="General_election"]/div/dl[1]/dd[1]/a[2]/text')
print a
