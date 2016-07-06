#!/usr/bin/env python3

#
# Helmholtz coil plot example
#

import math
import loopfield as lf
import loopfield.plot as lfp

# field object
field = lf.Field(length_units = lf.cm,
                 current_units = lf.A,
                 field_units = lf.uT)


# Helmholtz coil model with single current loops
R = 10.

# 2 windings
c1 = lf.Loop([-R/2., 0, 0], [1, 0, 0], R, 1)
c2 = lf.Loop([+R/2., 0, 0], [1, 0, 0], R, 1)

# add windings to field
field.addLoop(c1)
field.addLoop(c2)

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

# add circled area hand-adjusted to fit in 1% error volume "octopus"
center_r = 3.2
plot.circle([0., 0.], radius = center_r, color='blue', alpha=0.5,
            label = ('r = %2.1f cm' % center_r))


# add text
plot.labels(title = '10cm Helmholtz Coil',
            xlabel = 'x (cm)', ylabel = 'y (cm)')

# save plot
plot.save('helmholtz_coil.png')
print('Plot written to "helmholtz_coil.png"')
