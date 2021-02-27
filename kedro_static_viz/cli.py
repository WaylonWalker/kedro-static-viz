"module to provide command line interface for kedro-static-viz"
from pathlib import Path

import click

from .core import static_viz as _static_viz

__version__ = "0.4.1"


@click.group(name="Kedro-Static-Viz")
def cli() -> None:
    "kedro-static-viz command line interface"
    pass


@cli.command()
@click.option(
    "--port",
    default=4141,
    type=int,
    help="TCP port that viz will listen to. Defaults to 4141.",
)
@click.option(
    "--browser/--no-browser",
    default=True,
    help="Whether to open viz interface in the default browser or not. "
    "Defaults to True.",
)
@click.option(
    "--load-file",
    default=None,
    type=click.Path(exists=True, dir_okay=False),
    help="Path to load the pipeline JSON file",
)
@click.option(
    "--pipeline",
    type=str,
    default=None,
    help="Name of the modular pipeline to visualize. "
    "If not set, the default pipeline is visualized",
)
@click.option(
    "--env",
    "-e",
    type=str,
    default=None,
    multiple=False,
    envvar="KEDRO_ENV",
    help="Kedro configuration environment. If not specified, "
    "catalog config in `local` will be used",
)
@click.option(
    "--directory",
    default="public",
    type=click.Path(exists=False, file_okay=False),
    help="Path to save the static site to",
)
@click.option("--version", default=False, is_flag=True, help="Prints version and exits")
@click.option(
    "--serve/--no-serve",
    default=True,
    help="Whether or not to serve the site after creating. Defaults to True.",
)
def static_viz(
    port: int,
    browser: bool,
    load_file: Path,
    pipeline: str,
    env: str,
    directory: Path,
    version: bool,
    serve: bool,
) -> None:
    "main kedro-static-viz command"
    if version:
        click.echo(__version__)
        return
    _static_viz(
        port=port,
        browser=browser,
        load_file=load_file,
        pipeline=pipeline,
        env=env,
        directory=directory,
        serve=serve,
    )


if __name__ == "__main__":
    cli()
