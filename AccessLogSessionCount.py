import pandas as pd # here i used pandas library from pip which gives access to a lot of useful tools
from datetime import datetime

ipList = []
dateList = []
timeList = []
OpSysList = []
myDict = {}
scount = {}

with open('AccessData.txt', 'rb+') as file:
#Split method splits a particular string #into desired number of substring where from exactly where it is parted

for line in file:
    y = line.split("]")
    getLastIndex = y[1].rfind('"')
    indexOfBO = y[1].rfind('"', 0, getLastIndex)
    bOData = y[1][indexOfBO+1:indexOfBO]
    print bOData
    OpSysList = bOData
    nsplit = (y[0].split("["))
    k = nsplit[0].split("-")
    ipList.append(k[0])
    nsplit_1 = (nsplit[1].split("-"))
    timeSplit = nsplit_1[0].split(":")
    date1 = timeSplit[0].split("/")

    m1 = date1[2] + ":" + date1[1] + ":" + date1[0]
    dateList.append(m1)
    m = timeSplit[1] + ":" + timeSplit[2] + ":" + timeSplit[3]
    timeList.append(m)

DFrame = pd.DataFrame(dateList, columns=['Date']) # dataframe is used to indicate the Timestamp and the date
DFrame['Time'] = timeList
DFrame['IP'] = ipList
DFrame['OpSys'] = OpSysList
FrameLength = len(DFrame)
Dateformat = '%H:%M:%S'

for i in range(len(DFrame)):
    if DFrame['Date'][i] in myDict:
        jp = myDict.get(DFrame['Date'][i])
        if jp[0] != DFrame['IP'][i]:
            jp2 = scount.get(DFrame['Date'][i])
            myDict[DFrame['Date'][i]] = [DFrame['IP'][i], DFrame['Time'][i], DFrame['OpSys'][i]]
            scount[DFrame['Date'][i]] = jp2 + 1
        else:
            if jp[2] != DFrame['OpSys'][i]:
                jp2 = scount.get(DFrame['Date'][i])
                myDict[DFrame['Date'][i]] = [DFrame['IP'][i], DFrame['Time'][i], DFrame['OpSys'][i]]
                scount[DFrame['Date'][i]] = jp2 + 1
            else:
                lor = jp[1].strip()
                lor1 = DFrame['Time'][i].strip()
                m1 = datetime.strptime(lor, Dateformat)
                m2 = datetime.strptime(lor1, Dateformat)
                Difference = (m2-m1).total_seconds() / 60
                if Difference > 20:
                    jp1 = scount.get(DFrame['Date'][i])
                    myDict[DFrame['Date'][i]] = DFrame['Time'][i]
                    scount[DFrame['Date'][i]] = jp1 + 1
    else:
        myDict[DFrame['Date'][i]] = [DFrame['IP'][i], DFrame['Time'][i], DFrame['OpSys'][i]]
        scount[DFrame['Date'][i]] = 1
print scount #Total Session count is printed here


