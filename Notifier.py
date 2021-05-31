import requests
import time
from playsound import playsound
dist=314
date='4-06-2021'
URL='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(dist,date)
header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
print('Search for slots!!')
def findslots():
    count=0
    result=requests.get(URL,headers=header)
    response_json=result.json()
    data=response_json["sessions"]
    for each in data:
            if((each["available_capacity"]>0) & (each["min_age_limit"]==45) &(each["available_capacity_dose2"]>0)):
                count=count+1
                print(each["name"])
                print(each["pincode"])
                print(each["vaccine"])
                print(each["available_capacity"])
                print('Dose1:')
                print(each["available_capacity_dose1"])
                print('Dose2:')
                print(each["available_capacity_dose2"])
                print(each["fee_type"])
                print(each["fee"])
                print(each["slots"])

                playsound('D:\Placements\Projects\Cowin_Notifier\ding-sound.mp3')
                return True
            if(count==0):
                print("No Slots Found!!")
                return False
while(findslots() !=True):
    time.sleep(3600)
    findslots()
