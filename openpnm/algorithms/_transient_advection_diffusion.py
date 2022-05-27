import logging
from openpnm.algorithms import TransientReactiveTransport, AdvectionDiffusion
from openpnm.utils import Docorator


__all__ = ['TransientAdvectionDiffusion']


docstr = Docorator()
logger = logging.getLogger(__name__)


@docstr.dedent
class TransientAdvectionDiffusionSettings:
    r"""
    Parameters
    ----------
    %(AdvectionDiffusionSettings.parameters)s
    %(TransientReactiveTransportSettings.parameters)s

    """


class TransientAdvectionDiffusion(TransientReactiveTransport,
                                  AdvectionDiffusion):
    r"""
    A subclass of GenericTransport to perform steady and transient simulations
    of pure diffusion and advection-diffusion problems.
    """

    def __init__(self, **kwargs):
        if 'name' not in kwargs.keys():
            kwargs['name'] = 'trans_ad_01'
        super().__init__(**kwargs)
        self.settings._update(TransientAdvectionDiffusionSettings())
