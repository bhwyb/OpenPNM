r"""

**openpnm.models**

----

This module contains a selection of pore-scale models for calculating
geometrical, thermophysical, and multiphysics transport properties.

----

**Using Prewritten Models from the Library**

OpenPNM includes a solid library of pre-written models for most basic and
standard scenarios.  These are broken up into 4 categores: *geometry*,
*phases*, *physics*, and *misc*.  These are further categorized by the type
of information they calculate, such as grouping all models that calculate
viscosity or throat length.

Utilizing a model on a object requires using the ``add_model`` method. This
is demonstrated below:

>>> import openpnm as op
>>> pn = op.network.Cubic([5, 5, 5])
>>> pn.add_model(propname='pore.seed',
...              model=op.models.misc.random,
...              element='pore',
...              num_range=[0.1, 0.9])
>>> pn.add_model(propname='pore.diameter',
...              model=op.models.geometry.pore_size.normal,
...              seeds='pore.seed',
...              loc=0.5, scale=0.1)

Upon being added to the object the models are run.  The resulting data is
placed into the object using the ``propname`` as a key.  Inspecting the
object reveals that these two data items are indeed present.

>>> print(pn.props())
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
1     : pore.coords
2     : pore.diameter
3     : pore.seed
4     : throat.conns
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

The actual models and their respective parameters are also stored on the
object under the ``models`` attribute, which is dictionary with the same keys
as the ``propnames``.  This can also be inspected:

>>> print(pn.models)
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
#   Property Name             Parameter                 Value
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
1   pore.seed                 model:                    random
                              element:                  pore
                              num_range:                [0.1, 0.9]
                              seed:                     None
                              regeneration mode:        normal
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
2   pore.diameter             model:                    normal
                              seeds:                    pore.seed
                              loc:                      0.5
                              scale:                    0.1
                              regeneration mode:        normal
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

Finally, any of the models parameters can be edited by reaching into the
``models`` dictionary as follows:

>>> pn.models['pore.seed']['num_range'] = [0.5, 0.9]

The ``'pore.seed'`` values must be regenerated for this new parameter to take
effect, and the ``'pore.diameter'`` model must also be regenerated to utilized
the new seeds.  This is accomplished using ``regenerate_models`` which
automatically ensures that models are called in the correct order (seeds before
diameters):

>>> pn.regenerate_models()

"""

from . import misc
from . import geometry
from . import phases
from . import physics
