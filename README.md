# OpenFOAM-Tips

## How to extract water level height using Paraview

 There are a lot of way to extract data using built in tools of OpenFOAM like prob and etc. but sometimes Paraview would more desirable.

It is supposed you have ran your simulation and in your folder you have unsteady results (they are folder named by unsteady time) . 

In the following we had we had results of a free surface flow simulation of OWC (Oscillating Water Column) using two phase flow (air/water) solver. 

To generate such a script you have to open paraview and then click on menu *Tools/Start Trace* then do the following steps and in the end again click on *Tools/Stop Trace*. I have added some more codes to extract actual water level and go through time steps to repeat the calculation. 

1. Open *.foam* file.
2. Convert to point data using *CellDataToPointData*.
3. Clip the domain to have just the chamber.
4. Make a contours of *water* for just one value which is in the interface (is always 0.5).
5. Make a new scalar stored in point data to keep the water level.
6. Integrate the resulting 3D surface contour to have average of values including water level.

### How to use:

Fill the input data of the beginning of the script file. Run script inside paraview by clicking on *Tools/Python Shell/Run Scriptes*. The output file will place in the your OpenFOAM folder and will to your paraview workspace ready to plot.



~~~python
#### INPUT DATA
path='/home/aramezani/Simulation/Leire/test/' #OpenFOAM folder
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



# reset view to fit data
renderView1.ResetCamera()

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=afoam)



# hide data in view
Hide(afoam, renderView1)

# create a new 'Clip'
clip1 = Clip(Input=cellDatatoPointData1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'alpha.water']
clip1.Value = 0.5

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = clip_position



# hide data in view
Hide(cellDatatoPointData1, renderView1)

# create a new 'Contour'
contour1 = Contour(Input=clip1)
contour1.ContourBy = ['POINTS', 'alpha.water']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'



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



# hide data in view
Hide(contour1, renderView1)

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
~~~