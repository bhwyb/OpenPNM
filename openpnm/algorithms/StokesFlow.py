import numpy as np
from copy import deepcopy
from openpnm.algorithms import ReactiveTransport
from openpnm.utils import logging, Docorator, SettingsAttr
logger = logging.getLogger(__name__)
docstr = Docorator()


class StokesFlowSettings:
    prefix = 'stokes'
    quantity = 'pore.pressure'
    conductance = 'throat.hydraulic_conductance'


class StokesFlow(ReactiveTransport):
    r"""
    A subclass of GenericLinearTransport to simulate viscous flow.

    """

    def __init__(self, settings={}, **kwargs):
        self.settings = SettingsAttr(StokesFlowSettings, settings)
        super().__init__(settings=deepcopy(self.settings), **kwargs)
