from __future__ import print_function
from __future__ import division
# Authors:
#     Loic Gouarin <loic.gouarin@math.u-psud.fr>
#     Benjamin Graille <benjamin.graille@math.u-psud.fr>
#
# License: BSD 3 clause

"""
Example of a 9 velocities scheme in 2D
"""
from six.moves import range
import pylbm
dsten = {
    'dim':2,
    'schemes':[{'velocities':list(range(9))}],
}
s = pylbm.Stencil(dsten)
print(s)
s.visualize()
