#!/usr/bin/env python3

#
# Maxwell coil plot example
#

import math
import loopfield as lf
import loopfield.plot as lfp

# field object
field = lf.Field(length_units = lf.cm,
                 current_units = lf.A,
                 field_units = lf.uT)


# Maxwell coil model with single current loops

R = 10

# center winding
c1 = lf.Loop([0, 0, 0], [1, 0, 0], R, 64)

# outer windings
c2 = lf.Loop([-R*math.sqrt(3./7.), 0, 0], [1, 0, 0], R*math.sqrt(4./7.), 49)
c3 = lf.Loop([+R*math.sqrt(3./7.), 0, 0], [1, 0, 0], R*math.sqrt(4./7.), 49)

# add windings to field
field.addLoop(c1)
field.addLoop(c2)
field.addLoop(c3)

# evaluate field at center of coil
Bc = field.evaluate([0., 0., 0.])
print('Bc = ', Bc)

print('Calculating plot...')

# function returns ratio of x-component to that at coil center
def x_ratio(B):
  return B[0] / Bc[0]

# create XY plot
min_x = -15
max_x = +15
min_y = -15
max_y = +15
n_x = 101
n_y = 101
plot = lfp.plotXY(field,
                  min_x, max_x, n_x,
                  min_y, max_y, n_y)

# add field lines
plot.fieldLines()

# add loop symbols
plot.loopSymbols(scale = 1.)

# add 1% error bound region
tol = 0.01
plot.region(x_ratio, [1.-tol, 1.+tol], color='red', alpha=0.5,
            label = ('Field error < %2.1f%%' % (100*tol)))

# add rectangular area hand-adjusted to fit in 1% error volume
area_x = 3.7
area_y = 4.2
plot.rectangle([-area_x, +area_x, -area_y, +area_y],
               color='blue', alpha = 0.5,
               label = (' %2.1f x %2.1f cm' % (2*area_x, 2*area_y)))

# add text
plot.labels(title = '10cm 49/64/49-Turn Maxwell Coil',
            xlabel = 'x (cm)', ylabel = 'y (cm)')

# save plot
plot.save('maxwell_coil.png')
print('Plot written to "maxwell_coil.png"')
