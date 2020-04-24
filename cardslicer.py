import sys
import pyvista as pv
import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt

def cardslice(mesh, nx, ny):

    # slices_x = mesh.slice_along_axis(n=nx, axis="x")
    # slices_y = mesh.slice_along_axis(n=ny, axis="y")
    plotter = pv.Plotter()    # instantiate the plotter
    plotter.add_mesh(mesh, opacity = 0.75)
    center = mesh.center
    plotter.show_grid()
    plotter.show_axes()
    sc = pv.Plotter(off_screen=True)
    sc.set_background('white')

    xmin = mesh.bounds[0]
    xmax = mesh.bounds[1]
    ymin = mesh.bounds[2]
    ymax = mesh.bounds[3]
    for x in np.linspace(xmin,xmax,nx):
        orig = (x, mesh.center[1], mesh.center[2])
        slice_x = mesh.slice(origin = orig, normal = 'x')
        if len(slice_x.points) > 0:
            print("added x-slice")
            plotter.add_mesh(slice_x, color='red')
            sc.clear()
            sc.add_mesh(slice_x, color="black")
            sc.set_position((3*xmax, slice_x.center[1], slice_x.center[2])) #does not work correctly, need variable distance
            sc.show(screenshot='x_'+str(x)+'.png', auto_close=False)
    for y in np.linspace(ymin,ymax,ny):
        orig = (mesh.center[0], y, mesh.center[2])
        slice_y = mesh.slice(origin = orig, normal = 'y')
        if len(slice_y.points) > 0:
            print("added y-slice")
            plotter.add_mesh(slice_y, color='blue')
            sc.clear()
            sc.add_mesh(slice_y, color="black")
            sc.set_position((slice_y.center[1], 3*ymax, slice_y.center[2])) #does not work correctly, need variable distance
            sc.show(screenshot='y_'+str(y)+'.png', auto_close=False)
    sc.close()
    plotter.show(full_screen=False)
<<<<<<< HEAD
    testplot = pv.Plotter()
    test_slice = mesh.slice()
    testplot.add_mesh(test_slice)
    points = test_slice.points
    points = np.delete(points, np.s_[0], 1)
    points = points.astype(int)
    x, y = [int(i[0]) for i in points], [int(i[1]) for i in points]
    plt.scatter(x,y)
    plt.show()
    max_x, max_y = max(x), max(y)
    
    image = np.zeros((max_y + 1, max_x + 1))

    for i in range(len(points)):
        image[max_y - y[i], x[i]] = 1
    img = Image.fromarray(image, "RGB")
    img.show()
    


=======
    # testplot = pv.Plotter()
    # test_slice = mesh.slice()
    # testplot.add_mesh(test_slice)
    # points = test_slice.points
    # points = np.delete(points, np.s_[0], 1)
    # testplot.show(screenshot="test.png")
    # #testplot.save_graphic("test.svg")
    # x, y = [int(i[0]) for i in points], [int(i[1]) for i in points]
    # plt.scatter(x,y)
    # plt.show()
>>>>>>> d61bebd5222b47d0ea29e6a02347b4375e764c0b





    # show the rendering window
    #pv.save_meshio("mesh.svg", slices_x)

if __name__ == "__main__":
    args = sys.argv
    mesh = pv.read(args[1])
    #python3 cardslicer.py -filename -nx -ny
    nx = int(args[2])
    ny = nx
    if len(args) > 3:
        ny = int(args[3])
    cardslice(mesh, nx, ny)
