import json

dictionary = {
    "Locker" : [1,2,3,4,5,6],
    "Status" : ["valid","valid","invalid","invalid","invalid","invalid"]
}
#return ldiction 
def getLockerStatus():
     # Opening JSON file
    with open('lockerstatus.json', 'r') as openfile:
 
        # Reading from json file in to dict
        dict_lk = json.load(openfile)
    return dict_lk

# get input as locker number, and status
def updateLockerStatus(lk_number,lk_status):
    # Opening JSON file
    dict_lk = getLockerStatus()
    i=0
    for x in dict_lk["Locker"] :
        if x==lk_number:
            dict_lk["Status"][i] = lk_status
            break
        i=i+1

    # Serializing json
    json_object = json.dumps(dict_lk, indent=4)
 
    # Writing to sample.json
    with open("lockerstatus.json", "w") as outfile:
        outfile.write(json_object)

    print(json_object)

updateLockerStatus(3,"invalid")