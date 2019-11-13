layer = iface.activeLayer() 
layer_data = QgsInterpolator.LayerData()
layer_data.source = layer
layer_data.zCoordInterpolation = False
layer_data.interpolationAttribute = 5
layer_data.sourceType = QgsInterpolator.SourcePoints

tin_interpolator = QgsIDWInterpolator([layer_data])
tin_interpolator.setDistanceCoefficient(2)

export_path = r"D:\\123.tiff"
#cos = iface.mapCanvas().extent()
#0-25 เล็กน้อย  25-40 ปานกลาง  41-55 ตกหนัก  55>ตกหนักมาก

#extent and col rows
rect = layer.extent()
res = 1000
ncol = int( ( rect.xMaximum() - rect.xMinimum() ) / res )
nrows = int( (rect.yMaximum() - rect.yMinimum() ) / res)

output = QgsGridFileWriter(tin_interpolator,export_path,rect,ncol,nrows)
output.writeFile()

rlayer = iface.addRasterLayer(export_path, "interpolation_output")


























