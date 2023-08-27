import pandas as pd
import numpy as np
import json
import time as tm

class dataSet : 
    def __init__(self, row, column, status):
        self.row = row
        self.column = column
        self.status = status
    def __init__(self, row, column):
        self.row = row
        self.column = column

def getLockers():
     # Opening JSON file
    with open('lockerstatus.json', 'r') as openfile:
 
        # Reading from json file in to dict
        lockers = json.load(openfile)
    return lockers

def getLocker(locker):
    lockers = getLockers()
    return lockers[locker]

def updateLocker(locker,pt,size,status):
    lockers = getLockers()
    lockers[locker]["pt"]=pt
    lockers[locker]["cst_size"]=size
    lockers[locker]["status"]=status
    lockers[locker]["time_in"]=tm.strftime('%H:%M:%S')
    lockers[locker]["tick_in"]=tm.time()

    with open("lockerstatus.json", "w") as outfile:
        json.dump(lockers, outfile)

def clearLocker(locker):
    lockers = getLockers()
    lockers[locker]["pt"]=""
    lockers[locker]["cst_size"]=""
    lockers[locker]["status"]="available"
    lockers[locker]["time_in"]=""
    lockers[locker]["tick_in"]=0

    with open("lockerstatus.json", "w") as outfile:
        json.dump(lockers, outfile)

#Return data in column "row", "column" / input in "barcode" column
def GetData(barcode) :
    print(barcode)
    print("___________________")
    barcode=int(barcode)
    df = pd.read_csv('mockup.csv')
    # Remove duplicates (Optional)
    df = df.drop_duplicates()

    print(df)
    lData = df.to_dict('list')
    print(lData)
    
    i=0
    for y in lData['Barcode']:
        if y == barcode :
            row = lData['Row'][i]
            column = lData['Column'][i]
            print("Row is "+ str(row) + " Column is "+ str(column))
            break
        i=i+1            
    data = dataSet(row, column)
    return data
    
    # class ReturnGetData():
    #     row = df['Row']
    #     column = df['Column']
    # return ReturnGetData
    # for x in df.iterrows():
        # print(x)

# print(GetData("1234"))