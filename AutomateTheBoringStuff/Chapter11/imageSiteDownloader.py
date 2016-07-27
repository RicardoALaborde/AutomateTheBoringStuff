'''
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that
has a search feature.
'''

import requests, bs4,sys,os

#start at imgur search url
url = 'https://imgur.com/search?q='+sys.argv[1]
#store the images in ./imgurImages
os.makedirs('imgurImages', exist_ok=True)
#counter for how many images are going to be downloaded
imageCount=0
print('Downloading images from %s...' % url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
#select any element with links to images
imageElem = soup.select('a > img')

#i'm only downloading 5 of these because of space or the lenght of the image search result
while imageCount!=5:
    if len(imageElem) == imageCount:
        break
    imageUrl = 'https:' + imageElem[imageCount].get('src')
    print('Downloading from %s'%(imageUrl))
    res = requests.get(imageUrl)
    #check if it exists
    res.raise_for_status()
    #write contents of the resulting image url
    imageFile = open(os.path.join('imgurImages', os.path.basename(imageUrl)), 'wb')
    for chunk in res.iter_content(1000000):
        imageFile.write(chunk)
    imageFile.close()
    imageCount+=1
