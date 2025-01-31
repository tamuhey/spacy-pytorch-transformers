# Stubs for torch.nn.modules.upsampling (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..._jit_internal import weak_module, weak_script_method
from .module import Module
from typing import Any, Optional

class Upsample(Module):
    __constants__: Any = ...
    name: Any = ...
    size: Any = ...
    scale_factor: Any = ...
    mode: Any = ...
    align_corners: Any = ...
    def __init__(self, size: Optional[Any] = ..., scale_factor: Optional[Any] = ..., mode: str = ..., align_corners: Optional[Any] = ...) -> None: ...
    def forward(self, input: Any): ...
    def extra_repr(self): ...

class UpsamplingNearest2d(Upsample):
    def __init__(self, size: Optional[Any] = ..., scale_factor: Optional[Any] = ...) -> None: ...

class UpsamplingBilinear2d(Upsample):
    def __init__(self, size: Optional[Any] = ..., scale_factor: Optional[Any] = ...) -> None: ...
