#!/usr/bin/env python3

import math
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class plotXY:
  def __init__(self,
               field,
               min_x, max_x, n_x,
               min_y, max_y, n_y):
 
    self.field = field
    self.min_x = min_x
    self.max_x = max_x
    self.n_x = n_x
    self.min_y = min_y
    self.max_y = max_y
    self.n_y = n_y
    self.X = np.linspace(min_x, max_x, n_x)
    self.Y = np.linspace(min_y, max_y, n_y)
    self.B = np.empty([n_y * n_x, 3])
    for i in range(0, n_y):
      for j in range(0, n_x):
        self.B[n_x * i + j, :] = self.field.evaluate(np.array([self.X[j],
                                                               self.Y[i],
                                                               0.]))

    self.legend_handles = []
    mp.use('Agg')
    plt.axis('equal')
    plt.grid(b = True, which = 'major')
    plt.grid(b = True, which = 'minor', color="0.75")
    plt.minorticks_on()
    plt.ylim([min_y, max_y])
    plt.xlim([min_x, max_x])

  def fieldLines(self, n_lines = None, density = None):
    if n_lines is None:
      n_lines = math.floor(self.n_x / 2)
    if density is None:
      density = 10
    start_points = (
      np.array([np.zeros(n_lines),
                self.min_y + (self.max_y - self.min_y) *
                (0.5 + np.linspace(0, n_lines-1, n_lines)) /
                (n_lines)]).transpose())
    strm = plt.streamplot(self.X, self.Y,
                          np.reshape(self.B[:, 0], [self.n_y, self.n_x]),
                          np.reshape(self.B[:, 1], [self.n_y, self.n_x]),
                          linewidth = 1, density = density,
                          color="0.5",
                          arrowsize = 1.,
                          start_points = start_points)
    
  def loopSymbols(self, scale = 1.):
    pos_X = []
    pos_Y = []
    neg_X = []
    neg_Y = []  
    for loop in self.field.loops:
      dp = loop.r * np.array([loop.n[1], -loop.n[0], 0])
      p0 = loop.p - dp
      pos_X.append(p0[0])
      pos_Y.append(p0[1])
      p1 = loop.p + dp
      neg_X.append(p1[0])
      neg_Y.append(p1[1])    
      
      plt.plot(pos_X, pos_Y, 'o', fillstyle='none',
               linewidth = 3*scale, markersize=20*scale,
               color = 'black', markeredgewidth=3*scale)
      plt.plot(pos_X, pos_Y, 'o', fillstyle='full',
               linewidth=3*scale, markersize=7*scale,
               color = 'black', markeredgewidth=1*scale)
      plt.plot(neg_X, neg_Y, 'o', fillstyle='none',
               linewidth=3*scale, markersize=20*scale,
               color = 'black', markeredgewidth=3*scale)
      plt.plot(neg_X, neg_Y, 'x', fillstyle='none',
               linewidth=3*scale, markersize=9*scale,
               color = 'black', markeredgewidth=3*scale)

  def region(self, function, bounds, color='black', alpha=1.0, label=None):
    scalar_field = np.reshape(np.apply_along_axis(function, 1, self.B),
                              [self.n_y, self.n_x])  
    ctr = plt.contourf(self.X, self.Y, 
                       scalar_field, bounds,
                       colors = color, alpha = alpha)
    if label is not None:
      handle = mpatches.Patch(color = color, alpha = alpha, label = label)
      self.legend_handles.append(handle)

  def circle(self, center, radius, color='black', alpha=1.0, label=None):
    circle1 = plt.Circle(center, radius, color = color, alpha = alpha)
    plt.gcf().gca().add_artist(circle1)

    if label is not None:
      handle = mpatches.Patch(color = color, alpha = alpha, label = label)
      self.legend_handles.append(handle)

  def rectangle(self, coords, color='black', alpha=1.0, label = None):
    plt.gcf().gca().add_patch(mpatches.Rectangle((coords[0], coords[2]),
                                                 coords[1] - coords[0],
                                                 coords[3] - coords[2],
                                                 color = color, alpha = alpha))
    if label is not None:
      handle = mpatches.Patch(color = color, alpha = alpha, label = label)
      self.legend_handles.append(handle)

  def labels(self, title=None, xlabel=None, ylabel=None):
    if title is not None:
      plt.title(title, size=20)
    if xlabel is not None:
      plt.xlabel(xlabel, size=15)
    if ylabel is not None:
      plt.ylabel(ylabel, size=15)

  def plt(self):
    return plt
    
  def save(self, filename):
    plt.legend(handles = self.legend_handles)
    plt.savefig(filename, bbox_inches = 'tight')
