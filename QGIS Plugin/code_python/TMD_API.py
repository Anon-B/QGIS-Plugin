#import requests A
import requests

# get api
response =requests.get('http://data.tmd.go.th/api/WeatherToday/V1/?type=json')
data=(response.json())

#check status_code
if response.status_code == 200:
    print(len(data['Stations'])) #  check data from api

else:
    print('requests Fail')
    
output = 'D:/test.csv'


#writ csv file
with open(output, 'w',encoding="utf-8") as file:
    file.write('Province,StationNameTh ,Latitude ,Longitude ,Date  ,Rainfall\n')
    for line in data['Stations']:
        print(line)
        try:
            file.write(str(line["StationNameEng"])+','+str(line["StationNameTh"])+','+str(line["Latitude"]["Value"])+','+str(line["Longitude"]["Value"])+','+str(line["Observe"]["Time"])+','+str(line["Observe"]["Rainfall"]["Value"])+','+str('\n'))
        except:
            pass
    
file.close()