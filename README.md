# Cardslicer


Script to slice a mesh into multiple slices and output them as images. Can be used to design pop-up cards of the mesh. 


## Prerequisites

PyVista (https://github.com/pyvista/pyvista) and dependencies


## Usage

Run cardslicer.py

```
usage: cardslicer.py [h] [file] [dir] [nx] [ny]

arguments:
	h	 help, show usage
	file	 mesh file (accepts any format PyVista accepts)
	dir	 directory to store image results
	nx	 slices in x-dir
optional arguments:
	ny	 slices in y-dir. default = nx
```

