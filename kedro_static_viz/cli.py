"module to provide command line interface for kedro-static-viz"
import http.server
import socketserver
import webbrowser
from functools import partial
from pathlib import Path
import shutil
import click
from .vendored import _call_viz

from typing import Union

__version__ = "0.2.3"


@click.group(name="Kedro-Static-Viz")
def cli() -> None:
    "kedro-static-viz command line interface"
    pass


def copy_site(directory: Path) -> None:
    """
    unzips the prebuilt gatsby site inside the install directory if needed
    then copies it into the public directory
    """
    public = Path(__file__).parent / "public"
    if public.exists() is False:
        import tarfile

        f = Path(__file__).parent / "public.tar.gz"
        tar = tarfile.open(str(f))
        tar.extractall(f.parent)
        tar.close()
    here = Path(directory).absolute()
    if here.exists():
        shutil.rmtree(str(here))

    shutil.copytree(str(public), str(here), copy_function=shutil.copy)


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
    copy_site(directory)
    viz_file = f"{directory}/pipeline.json"
    if version:
        click.echo(__version__)
        return
    if load_file:
        shutil.copy(load_file, viz_file)
    else:
        _call_viz(save_file=viz_file, pipeline_name=pipeline, env=env)

    if not Path(directory).exists():
        raise FileNotFoundError(f"Directory was not found at: {directory}")
    if browser and serve:
        webbrowser.open_new("http://localhost:{:d}/".format(port))

    if serve:
        run_static_server(directory=directory, port=port)


def run_static_server(directory: Union[str, Path], port: int = 4141) -> None:
    """Serves content from the given directory on the given port

    FOR DEVELOPMENT USE ONLY, use a real server for production.

    behaves very much like `python -m http.server`

    Arguments:
        directory {[str]} -- Path to the directory to serve.
        port {[int]} -- TCP port that viz will listen to
    """
    here = Path(directory).absolute()
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(here))
    with socketserver.TCPServer(("", port), handler) as httpd:
        print("kedro-static-viz serving at port", port)
        httpd.serve_forever()


if __name__ == "__main__":
    cli()
