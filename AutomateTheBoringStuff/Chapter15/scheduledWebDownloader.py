'''
Write a program that checks the websites of several web comics and
automatically downloads the images if the comic was updated since the
program’s last visit. Your operating system’s scheduler
(Scheduled Tasks on Windows, launchd on OS X, and cron on Linux)
can run your Python program once a day. The Python program itself can
download the comic and then copy it to your desktop so that it is easy to
find. This will free you from having to check the website yourself to see
whether it has updated. (A list of web comics is available at
'''

import requests,os,bs4,shelve,sys
#im going to save the latest comic # into the shelve, afterwards, the Windows
#scheduler will just run everyday and check if there are any comics later than
#the one stored on the shelve

sh = shelve.open('latestComics')

latestComic = int(sh['latest'].strip('/'))

url = 'http://xkcd.com/'+str(latestComic+1)

os.makedirs('D:\\xkcd', exist_ok=True)

while not url.endswith('#'):
    print('Looking for page %s...' % url)
    res = requests.get(url)
    try:
        res.raise_for_status()
    except:
        print('Currently up to date')
        sys.exit()

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl,timeout=5)
        res.raise_for_status()
    # Save the image to ./xkcd.
    imageFile = open(os.path.join('D:\\xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    # Get the Prev button's url.
    nextLink = soup.select('a[rel="next"]')[0]
    url = 'http://xkcd.com' + nextLink.get('href')
    if url.endswith('#') == False:
        del sh['latest']
        sh['latest'] = nextLink.get('href')
    else:
        break
sh.close()
