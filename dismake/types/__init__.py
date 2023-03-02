from .interactions import *
from .command import *
from collections.abc import Coroutine
from typing import Any, Callable

AsyncFunction = Callable[..., Coroutine[Any, Any, Any]]