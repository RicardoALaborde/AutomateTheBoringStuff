'''
Write a program that, given the URL of a web page, will attempt to download every
linked page on the page. The program should flag any pages that have a 404
“Not Found” status code and print them out as broken links.
'''

import requests, bs4,sys,re
#go to website as indicated on user input at the cmd line
url = sys.argv[1]
print('Checking links in %s... ' % url)
try:
    res = requests.get(url)
    #check if url exists
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    #select any element with links
    linkElem = soup.select('a')
    print('Found %s links. Exctracting all links which begin with "http"'%(len(linkElem)))
    #use regex to see which links are the ones leading to other http elements
    for a in soup.find_all('a', href=re.compile(r'^http')):
        checkLink = requests.get(str(a['href']))
        try:
            #check if link works
            checkLink.raise_for_status()
            print("OK: ",a['href'])
        except:
            #some urls were going crazy because of an encoding error
            print ("Found broken URL:", a['href'].encode('utf-8'))
except:
    #the url specified at the start was not valid
    print('There was a proble connecting to %s. Verify that the url is correct'%(url))
    exit
