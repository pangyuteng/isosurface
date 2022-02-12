import vtk


reader = vtk.vtkNIFTIImageReader()
reader.SetFileName('static/example.nii.gz')
reader.Update()

threshold = vtk.vtkImageThreshold ()
threshold.SetInputConnection(reader.GetOutputPort())
threshold.ThresholdByLower(50)  #th
threshold.ReplaceInOn()
threshold.SetInValue(0)  # set all values below th to 0
threshold.ReplaceOutOn()
threshold.SetOutValue(1)  # set all values above th to 1
threshold.Update()

dmc = vtk.vtkDiscreteMarchingCubes()
dmc.SetInputConnection(threshold.GetOutputPort())
dmc.GenerateValues(1, 1, 1)
dmc.Update()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(dmc.GetOutputPort())
mapper.Update()

smooth = vtk.vtkSmoothPolyDataFilter()
smooth.SetInputConnection(dmc.GetOutputPort())
smooth.SetNumberOfIterations(100)
smooth.SetRelaxationFactor(1)
smooth.Update()

writer = vtk.vtkPolyDataWriter()
writer.SetInputData(smooth.GetOutput())
writer.SetFileName('static/example.vtk')
writer.Write()
