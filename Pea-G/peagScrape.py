'''
Scraping service for Pea-G

Source: http://www.dtop.gov.pr/
'''

import requests, bs4, re,sqlite3,shelve,getpass,smtplib,sys
from re import sub

to=[]
lstTo = []
if len(sys.argv) > 1:
    if sys.argv[1] == 'to':
        print('Enter the email addresses which you\'d like to send the email to.')
        shelvefi=shelve.open('credentials')
        while True:
            try:
                del shelvefi['toEmail']
                while True:
                    toAddr = input('Add an email address: ')
                    lstTo.append(toAddr)
                    if input('Add another? ').upper() == 'Y':
                        pass
                    else:
                        shelvefi['toEmail'] = lstTo
                        shelvefi.close()
                        break
                break
            except:
                print('First time use of this app has been detected. Please enter your desired email recipients. These will be stored locally on your PC.')
                while True:
                    toAddr = input('Add an email address: ')
                    lstTo.append(toAddr)
                    if input('Add another? ').upper() == 'Y':
                        pass
                    else:
                        shelvefi['toEmail'] = lstTo
                        shelvefi.close()
                        break
                break
try:
    fileShelve=shelve.open('credentials')
    cr = fileShelve['credentials']
    username = cr[0]
    password = cr[1]
    shelvefi.close()
except:
    shelvefi=shelve.open('credentials')
    print('First time use of this app has been detected. Please enter your gmail account credentials. These will be stored locally on your PC.')
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    credentials=[]
    credentials.append(username)
    credentials.append(password)
    shelvefi['credentials']=credentials
    shelvefi.close()

def email_sender(user,passwd,input_message):
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    #tracking the mainframe ip address with a visual basic gui
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    try:
        smtpserver.login(user, passwd)
    except:
        while True:
            print('It seems like your email credentials are wrong, try giving them again!')
            Exit = input('Do you want to try again? (Y/N)').upper()
            if Exit == 'N':
                sys.exit()
            shelvefi=shelve.open('credentials')
            del shelvefi['credentials']
            user = input('Enter your username: ')
            passwd = getpass.getpass('Enter your password: ')
            credentials=[]
            credentials.append(user)
            credentials.append(passwd)
            shelvefi['credentials']=credentials
            shelvefi.close()
            try:
                smtpserver.login(user,passwd)
                break
            except:
                print('ERROR LOGGING IN')
    to = shelvefi['toEmail']
    header = 'To:' + ", ".join(to) + '\n' + 'From: ' + user + '\n' + 'Subject:Changes in DTOP Toll Booth Data \n'
    msg = header+input_message
    smtpserver.sendmail(user,to,msg)
    smtpserver.close()

connect = sqlite3.connect('peag.db')
crs = connect.cursor()

url = 'http://www.dtop.gov.pr/carretera/det_content.asp?cn_id=119'

res = requests.get(url)

soup = bs4.BeautifulSoup(res.text,'html.parser')

#look for road names
carreteras = re.compile(r'PR-[0-9]*')

lstP = []
lstStations = []
lstPeajes = []
lstRoad = []
lstDBRoads=[]
lstRoadNames = []
lstDBStations =[]
lstStationNames =[]
lstDBPrices=[]
lstPrices=[]
hasChanged=0

for row in soup.find_all('tbody'):
    for paragraph in row.find_all('p'):
        lstP.append(sub('<>',' ',sub('><','',sub(' ','<>',sub('\$','',sub('\\r','',sub('\\n','',paragraph.get_text())))))))

#index for pk of carretera
pkCarr = 1

#road names
for i in range(len(lstP)):
    if carreteras.search(lstP[i]) != None:
        #get index position of each road
        lstRoad.append(i)

#compare road names to data in db
for i in lstRoad:
    lstRoadNames.append(lstP[i])
for item in crs.execute('SELECT carrName FROM CARRETERA'):
    lstDBRoads.append(item[0])
if lstRoadNames != lstDBRoads:
    hasChanged=1
if hasChanged ==1:
    #some data has changed, let's remake the whole damn thing!
    print('DATA CHANGED AT CARRETERA')
    crs.execute('DELETE FROM CARRETERA')
    crs.execute('DELETE FROM sqlite_sequence WHERE name = "CARRETERA"')
    #insert road names into db
    for item in lstRoadNames:
        crs.execute('INSERT INTO CARRETERA(carrName) VALUES(?)',(item,))
    hasChanged=1

#index for getting next iterator of lstRoad
idx = 1

#toll booths
for i in range(len(lstP)):
    for item in lstRoad:
        if i == item:
            #this statement grabs the last station in the list of stations
            if lstRoad[len(lstRoad)-1] == i:
                lstStations.append(lstP[item+1:])
            else:
                lstStations.append(lstP[item+1:lstRoad[idx]])
                idx+=1

for i in range(len(lstStations)):
    #toll costs
    lstPeajes.append([lstStations[i][x+1:x+8] for x in range(0, len(lstStations[i]), 8)])

#compare station names to data in db
for i in range(len(lstStations)):
    for item in [lstStations[i][x:x+1] for x in range(0, len(lstStations[i]), 8)]:
        lstStationNames.append(item[0])
for item in crs.execute('SELECT stationName FROM ESTACIONES'):
    lstDBStations.append(item[0])
if lstStationNames != lstDBStations:
    hasChanged=1
if hasChanged==1:
    print('DATA HAS CHANGED AT COMPARE STATIONS')
    #some data has changed, let's remake the whole damn thing?
    crs.execute('DELETE FROM ESTACIONES')
    crs.execute('DELETE FROM "sqlite_sequence" WHERE name = "ESTACIONES"')
    for item in lstStationNames:
        #insert station names into db
        crs.execute('INSERT INTO ESTACIONES(stationName) VALUES(?)',(item,))
    hasChanged=1

idx=0

for i in range(len(lstPeajes)):
    for v in range(len(lstPeajes[i])):
        lstPeaG = []
        lstPeaG.insert(i,lstP[lstRoad[i]])
        lstPeaG.insert(i+1,lstStations[i][idx])
        t=i+2
        for item in lstPeajes[i][v]:
            lstPeaG.insert(t,item)
            t+=1
        lstPrices.append(lstPeaG)
        idx+=8
    idx=0

#compare prices to data in db
#seems like an ugly workaround but hey it works
for item in crs.execute('SELECT road_name,booth_name,two_axes,double_rim,three_axes,four_axes,five_axes,six_axes,seven_axes FROM "pea-g"'):
    for i in range(9):
        try:
            lstDBPrices.append("{:.2f}".format(float(item[i])))
        except:
            lstDBPrices.append(item[i])
if lstDBPrices!=[item.lstrip() for lstPrices in lstPrices for item in lstPrices] or hasChanged ==1:
    print('DATA HAS CHANGED AT PRICES')
    email_sender(username,password,'The database has gone through some changes, please update accordingly.')
    #some data has changed, let's remake the whole damn thing?
    crs.execute('DELETE FROM "pea-g"')
    crs.execute('DELETE FROM sqlite_sequence WHERE name = "pea-g"')
    #insert pea-g info to db
    for item in lstPrices:
        crs.execute('INSERT INTO "pea-g"(road_name,booth_name,two_axes,double_rim,three_axes,four_axes,five_axes,six_axes,seven_axes) VALUES(?,?,?,?,?,?,?,?,?)',item,)

connect.commit()
connect.close()
