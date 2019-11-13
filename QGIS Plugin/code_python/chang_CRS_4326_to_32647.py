#save for  chang CRS 4326 to 32647
layer = iface.activeLayer() 

exp_crs = QgsCoordinateReferenceSystem(32647, QgsCoordinateReferenceSystem.EpsgCrsId)
ly_csv = QgsVectorLayer(layer.source(),layer.name(),'delimitedtext')
writer = QgsVectorFileWriter.writeAsVectorFormat(ly_csv,'D:/test_chengeCRS.shp','UTF-8',exp_crs,'ESRI Shapefile',False)
























