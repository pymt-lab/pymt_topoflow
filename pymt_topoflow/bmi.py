from __future__ import absolute_import

from topoflow.components.infil_green_ampt import infil_component as InfilGreenAmpt
from topoflow.components.infil_richards_1D import infil_component as InfilRichards1D
from topoflow.components.infil_smith_parlange import (
    infil_component as InfilSmithParlange
)

InfilGreenAmpt.__name__ = "InfilGreenAmpt"
InfilRichards1D.__name__ = "InfilRichards1D"
InfilSmithParlange.__name__ = "InfilSmithParlange"
