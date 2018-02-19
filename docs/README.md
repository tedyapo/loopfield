LoopField
=========
This is a python module for calculating 3D vector magentic fields induced by filamentary current loops (i.e. turns of wire). The code is based on the formulas presented in:

Simpson J., Lane J., Immer C., Youngquist R., Steinrock, T., Simple  
Analytic Expressions for the Magnetic Field of a Circular Current  
Loop. NASA Technical Report. 2001.  
http://ntrs.nasa.gov/search.jsp?R=20010038494

The loofield.plot module can also generate 2D plots of the field lines in the XY plane.

Installation
============
It is easiest to install the loopfield package and required dependecies in a virtualenv using pip:

sudo apt-get install virtualenv

virtualenv -p python3 LF

source LF/bin/activate

pip install loopfield

git clone https://www.github.com/tedyapo/loopfield

cd loopfield/examples

./helmholtz_coil.py

./maxwell_coil.py

./single_loop.py

Usage
=====
See the examples directory for several simple tests.  For example, the helmholtz_coil.py example produces the following plot:
 
![helmholtz coil plot](/docs/images/helmholtz_coil.png)

More Info
=========
More information about this code can be found in the logs for my [magnetic field scanner project](https://hackaday.io/project/11865-3d-magnetic-field-scanner).
