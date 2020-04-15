import sys
import pyvista as py

args = sys.argv
mesh = py.read(args[1])

#python3 cardslicer.py -filename -starting_slices

n = args[2]

slices_x = mesh.slice_along_axis(n=n, axis="x")
slices_y = mesh.slice_along_axis(n=n, axis="y")

