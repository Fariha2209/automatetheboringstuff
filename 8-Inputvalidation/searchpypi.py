# searchpypi.py - opens several google results.
# pypisearchURL = https://pypi.org/search/?q=<SEARCH_TERM_HERE>

import requests, sys, webbrowser, bs4 
print('Searching...')    #display text while downloading the search result page

res = requests.get('https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

print("Line 10: ")

#print(res.text)
# retrieve top results links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# open browser tab for each result

linkElems = soup.select('.package-snippet')
print(linkElems)

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)




#Editing file test for github
