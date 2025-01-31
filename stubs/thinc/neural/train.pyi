# Stubs for thinc.neural.train (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .optimizers import Adam, linear_decay
from typing import Any

class Trainer:
    ops: Any = ...
    model: Any = ...
    L2: Any = ...
    optimizer: Any = ...
    batch_size: Any = ...
    nb_epoch: Any = ...
    i: int = ...
    dropout: Any = ...
    dropout_decay: Any = ...
    each_epoch: Any = ...
    def __init__(self, model: Any, **cfg: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def iterate(self, train_X: Any, train_y: Any, progress_bar: bool = ...) -> None: ...
