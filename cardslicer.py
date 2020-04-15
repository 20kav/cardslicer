import sys
import pyvista as pv
import numpy as np

def cardslice(mesh, nx, ny = None):
    if ny is None:
        ny = nx
    # slices_x = mesh.slice_along_axis(n=nx, axis="x")
    # slices_y = mesh.slice_along_axis(n=ny, axis="y")
    plotter = pv.Plotter()    # instantiate the plotter
    plotter.add_mesh(mesh)
    center = mesh.center
    xmin = mesh.bounds[0]
    xmax = mesh.bounds[1]
    ymin = mesh.bounds[2]
    ymax = mesh.bounds[3]
    for x in np.linspace(xmin,xmax,nx):
        orig = (x, mesh.center[1], mesh.center[2])
        slice_x = mesh.slice(origin = orig, normal = 'x')
        if len(slice_x.points) > 0:
            println("added x-slice")
            plotter.add_mesh(slice_x, color='red')
    for y in np.linspace(ymin,ymax,ny):
        orig = (mesh.center[0], y, mesh.center[2])
        slice_y = mesh.slice(origin = orig, normal = 'y')
        if len(slice_y.points) > 0:
            println("added y-slice")
            plotter.add_mesh(slice_y, color='blue')

    slices_y = mesh.slice(normal = 'y')

    cpos = plotter.show()     # show the rendering window
    #pv.save_meshio("mesh.svg", slices_x)

if __name__ == "__main__":
    args = sys.argv
    mesh = pv.read(args[1])
    #python3 cardslicer.py -filename -starting_slices
    nx = int(args[2])
    ny = nx
    if len(args) > 3:
        ny = int(args[3])
    cardslice(mesh, nx, ny)
