loopfield: compute vector magnetic fields induced by filamentary current loops

loopfile.plot: plot simple 2D visualizations of fields with field lines and thresholded regions

Simple example: calculate field due to single current loop:

#!/usr/bin/env python3

import loopfield as lf

# create empty field with specified units
field = lf.Field(length_units = lf.cm,
                 current_units = lf.A,
                 field_units = lf.uT)

# single-turn 10 cm x-oriented coil at origin
position = [0., 0., 0.]
normal = [1., 0., 0.]
radius = 10.
current = 1.
c = lf.Loop(position, normal, radius, current)

# add loop to field
field.addLoop(c);

# evaluate vector field at origin
B = field.evaluate([0., 0., 0.])
print('B = ', B)


See examples for more usage details.

Uses the formulas presented in:

Simpson J., Lane J., Immer C., Youngquist R., Steinrock, T., Simple
Analytic Expressions for the Magnetic Field of a Circular Current
Loop. NASA Technical Report. 2001.  Retrieved from
http://ntrs.nasa.gov/search.jsp?R=20010038494

