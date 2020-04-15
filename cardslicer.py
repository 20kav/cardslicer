import sys
import pyvista as pv

args = sys.argv
mesh = pv.read(args[1])

#python3 cardslicer.py -filename -starting_slices

n = int(args[2])

slices_x = mesh.slice_along_axis(n=n, axis="x")
slices_y = mesh.slice_along_axis(n=n, axis="y")

plotter = pv.Plotter()    # instantiate the plotter
plotter.add_mesh(slices_x)
plotter.add_mesh(slices_y)    # add a mesh to the scene
cpos = plotter.show()     # show the rendering window
