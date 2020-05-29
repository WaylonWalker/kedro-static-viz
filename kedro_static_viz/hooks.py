"""
kedro-static-viz hooks module

This hook will run kedro-static-viz before pipeline run. Set up the hook by adding
`static_viz_hook()` to your hooks list in your `ProjectContext` class as shown
below.

Example:

    >>> from kedro_static_viz.hooks import StaticViz
    >>> hooks = [StaticViz()]
"""


from pathlib import Path
from typing import Union

from kedro.framework.hooks import hook_impl

from .core import static_viz


class StaticViz:
    """
    creates static viz before pipeline run

    This hook will run kedro-static-viz before pipeline run. Set up the hook by adding
    `static_viz_hook()` to your hooks list in your `ProjectContext` class as shown
    below.nv

    Arguments:
        pipeline (str): The name of the modular pipeline to visualize, default is None
        env (str): Kedro configuration environment. If not specified,
            catalog config in `local` will be used, default is None
        directory (str, Path): Path to save the static site to, default is 'public'

    Example:

        >>> from kedro_static_viz.hooks import StaticViz
        >>> hooks = [StaticViz()]
    """

    def __init__(
        self,
        pipeline: str = None,
        env: str = None,
        directory: Union[str, Path] = "public",
    ) -> None:
        "initializes static_viz_hook"
        self.pipeline = pipeline
        self.env = env
        self.directory = directory

    @hook_impl
    def before_pipeline_run(self) -> None:
        "createts static viz before pipeline run"
        # breakpoint()
        static_viz(
            browser=False,
            load_file=None,
            pipeline=self.pipeline,
            env=self.env,
            directory=self.directory,
            serve=False,
        )
