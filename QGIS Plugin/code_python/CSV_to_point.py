
url = "file:///D:/test.csv?encoding=UTF-8&delimiter,&xField=longitude&yField=latitude&crs=epsg:4326"

#Make a vector layer
TMD_layer=QgsVectorLayer(url,"TMD-data","delimitedtext")

#Add CSV data    
QgsProject.instance().addMapLayer(TMD_layer)