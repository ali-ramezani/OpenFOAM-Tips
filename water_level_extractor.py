#### INPUT DATA
path='/home/aramezani/Simulation/test/' #OpenFOAM folder
output_file_name="waterlevel.csv"
g_direction="Y"
clip_position=[1.695, 0.3, 0.05]
#### END INPUT DATA

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
afoam = OpenFOAMReader(FileName=path+'a.foam')
afoam.MeshRegions = ['internalMesh']
afoam.CellArrays = ['alpha.water']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1383, 796]

# show data in view
afoamDisplay = Show(afoam, renderView1)
# trace defaults for the display properties.
afoamDisplay.AmbientColor = [0.0, 0.0, 0.0]
afoamDisplay.ColorArrayName = [None, '']
afoamDisplay.EdgeColor = [1.0, 1.0, 0.4980392156862745]
afoamDisplay.OSPRayScaleArray = 'alpha.water'
afoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
afoamDisplay.SelectOrientationVectors = 'None'
afoamDisplay.ScaleFactor = 0.17790000438690187
afoamDisplay.SelectScaleArray = 'None'
afoamDisplay.GlyphType = 'Arrow'
afoamDisplay.ScalarOpacityUnitDistance = 0.06996493003392046
afoamDisplay.GaussianRadius = 0.08895000219345094
afoamDisplay.SetScaleArray = ['POINTS', 'alpha.water']
afoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
afoamDisplay.OpacityArray = ['POINTS', 'alpha.water']
afoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=afoam)

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)
# trace defaults for the display properties.
cellDatatoPointData1Display.AmbientColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.ColorArrayName = [None, '']
cellDatatoPointData1Display.EdgeColor = [1.0, 1.0, 0.4980392156862745]
cellDatatoPointData1Display.OSPRayScaleArray = 'alpha.water'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'None'
cellDatatoPointData1Display.ScaleFactor = 0.17790000438690187
cellDatatoPointData1Display.SelectScaleArray = 'None'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 0.06996493003392046
cellDatatoPointData1Display.GaussianRadius = 0.08895000219345094
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'alpha.water']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'alpha.water']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(afoam, renderView1)

# create a new 'Clip'
clip1 = Clip(Input=cellDatatoPointData1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'alpha.water']
clip1.Value = 0.5

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = clip_position

# show data in view
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.AmbientColor = [0.0, 0.0, 0.0]
clip1Display.ColorArrayName = [None, '']
clip1Display.EdgeColor = [1.0, 1.0, 0.4980392156862745]
clip1Display.OSPRayScaleArray = 'alpha.water'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.05250000208616257
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.ScalarOpacityUnitDistance = 0.051863918563306695
clip1Display.GaussianRadius = 0.026250001043081284
clip1Display.SetScaleArray = ['POINTS', 'alpha.water']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'alpha.water']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(cellDatatoPointData1, renderView1)

# create a new 'Contour'
contour1 = Contour(Input=clip1)
contour1.ContourBy = ['POINTS', 'alpha.water']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.AmbientColor = [0.0, 0.0, 0.0]
contour1Display.ColorArrayName = [None, '']
contour1Display.EdgeColor = [1.0, 1.0, 0.4980392156862745]
contour1Display.OSPRayScaleArray = 'Normals'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 0.010000000149011612
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GaussianRadius = 0.005000000074505806
contour1Display.SetScaleArray = [None, '']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = [None, '']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(clip1, renderView1)

# create a new 'Calculator'
calculator1 = Calculator(Input=contour1)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'ylevel'
calculator1.Function = 'coords'+g_direction

# get color transfer function/color map for 'ylevel'
ylevelLUT = GetColorTransferFunction('ylevel')

# show data in view
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.AmbientColor = [0.0, 0.0, 0.0]
calculator1Display.ColorArrayName = ['POINTS', 'ylevel']
calculator1Display.LookupTable = ylevelLUT
calculator1Display.EdgeColor = [1.0, 1.0, 0.4980392156862745]
calculator1Display.OSPRayScaleArray = 'ylevel'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 0.010000000149011612
calculator1Display.SelectScaleArray = 'ylevel'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GaussianRadius = 0.005000000074505806
calculator1Display.SetScaleArray = ['POINTS', 'ylevel']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'ylevel']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'ylevel'
ylevelPWF = GetOpacityTransferFunction('ylevel')

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(Input=calculator1)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, spreadSheetView1)

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1)
# trace defaults for the display properties.
integrateVariables1Display.CompositeDataSetIndex = [0]


time_steps=afoam.TimestepValues
view = GetActiveView()
f=open(path+output_file_name,"w")
f.write("t,water_level\n")
for t in time_steps:
	view.ViewTime = t	
	Render()
	integrateVariables1.UpdatePipeline() # Perform the calculation
	Integrate_Var_Fetch = servermanager.Fetch(integrateVariables1)
	Integrate_Var_Pointdata = Integrate_Var_Fetch.GetPointData()
	mylevel = Integrate_Var_Pointdata.GetArray('ylevel')
	Integrate_Var_Celldata = Integrate_Var_Fetch.GetCellData()
	mArea= Integrate_Var_Celldata.GetArray('Area')
	Area = mArea.GetValue(0)
	ylevel = mylevel.GetValue(0)
	f.write("{0},{1}\n".format(t,ylevel/Area))
	print "{0},{1}".format(t,ylevel/Area)
	
f.close()

# create a new 'CSV Reader'
surface_levelcsv = CSVReader(FileName=[path+output_file_name])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.8895000219345093, 0.30000001192092896, 3.682107777103769]
renderView1.CameraFocalPoint = [0.8895000219345093, 0.30000001192092896, 0.05000000074505806]
renderView1.CameraParallelScale = 0.9400586663866015

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).