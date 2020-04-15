import sys
import pyvista as pv

def cardslice(mesh, nx, ny = None):
    if ny is None:
        ny = nx
    slices_x = mesh.slice_along_axis(n=nx, axis="x")
    slices_y = mesh.slice_along_axis(n=ny, axis="y")

    plotter = pv.Plotter()    # instantiate the plotter
    plotter.add_mesh(slices_x)
    plotter.add_mesh(slices_y)    # add a mesh to the scene
    cpos = plotter.show()     # show the rendering window

if __name__ == "__main__":
    args = sys.argv
    mesh = pv.read(args[1])
    #python3 cardslicer.py -filename -starting_slices
    nx = int(args[2])
    ny = nx
    if len(args) > 3:
        ny = int(args[3])
    cardslice(mesh, nx, ny)
