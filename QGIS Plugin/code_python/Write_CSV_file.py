#import csv
import csv
#i = 'D:/TMD_water.csv'
#with open(i, 'w',encoding="utf-8") as file:
#    file.write('NO,NAME ,Latitude ,Longitude ,Date \n')
#    file.write('1,Anon bianglae ,18.222 ,100.2 ,10/29/2019 \n')
#file.close()


#output path
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