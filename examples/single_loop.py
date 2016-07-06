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

# evaluate vector field 100 cm along axis
B = field.evaluate([100., 0., 0.])
print('B = ', B)

# evaluate vector field on loop (infinite result)
B = field.evaluate([0., radius, 0.])
print('B = ', B)
