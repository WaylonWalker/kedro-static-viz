"kedro-static-viz"
__version__ = "0.3.0"

__all__ = ["cli", "static_viz", "static_viz_hook"]

from .cli import cli
from .core import static_viz
from .hooks import static_viz_hook
