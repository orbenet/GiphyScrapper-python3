import re
import requests
from bs4 import BeautifulSoup
import os
from time import gmtime, strftime




currentdatetime = (strftime("%Y%m%d%H%M%S", gmtime()))

page = requests.get("https://giphy.com/")


if page.status_code > 299:
    print('Page Returns ' + str(page.status_code) + ' Error....\n Sorry Mate :(')
    exit()
elif page.status_code < 200:
    print('Page Returns' + str(page.status_code) + ' Error....\n Sorry Mate :(')
    exit()
else:
    print('Page Returns status: ' + str(page.status_code) + ' \nSUCCESS !!!!')
    print('\n\n\n Page Content: \n')
    pass

soup = BeautifulSoup(page.content, 'html.parser')

Giphy_Script = soup.find_all('script')

GifData = Giphy_Script[21]

GifDataString = str(GifData)

searchObj = re.findall( "(?P<url>https?://[^\s]+)" ,GifDataString)


foundfix = [x[:-2] for x in searchObj]

amountofgifs = 0
ListofGiphyUrls = []

#Checker
for url in foundfix:
    if 'giphy.gif' in url:
        amountofgifs = amountofgifs + 1
        print('1')
        ListofGiphyUrls.append(url)
    else:
        print('0')
filename = 0
filesizes = []
#Create Directory for new files
os.mkdir(currentdatetime)
os.chdir(currentdatetime)


print ('found ' + str(amountofgifs) + ' gif files')


print('\n\n\n\n\n')

print('Performing Duplicate Analysis and downloading')

print('\n\n\n\n\n')

print('')


#Downloader
for Giphyurl in ListofGiphyUrls:
    filedata = requests.get(Giphyurl)

    if len(filedata.content) in filesizes:
        pass
    else:
        filesizes.append(len(filedata.content))
        with open('Giphy' + str(filename) + '.gif', "wb") as fileinstance:
            fileinstance.write(filedata.content)
            fileinstance.close()
            filename = filename + 1
            print('Downloaded Giphy' + str(filename) + '.gif Successfully')





