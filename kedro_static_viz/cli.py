import http.server
import socketserver
import webbrowser
from functools import partial
from pathlib import Path
import shutil
import click
from kedro_viz.server import _call_viz

__version__ = "0.0.1"

VIZ_FILE = "./public/pipeline.json"


@click.group(name="Kedro-Static-Viz")
def cli():
    pass


def copy_files(directory):
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
@click.option(
    "--version",
    default=False,
    is_flag=True,
    help="Prints version and exits" "Defaults to True.",
)
def static_viz(port, browser, load_file, pipeline, env, directory, version):
    copy_files(directory)
    if version:
        click.echo(__version__)
        return True
    if load_file:
        shutil.copy(load_file, VIZ_FILE)
    else:
        _call_viz(save_file=VIZ_FILE, pipeline_name=pipeline, env=env)

    if not Path(directory).exists():
        raise FileNotFoundError(f"Directory was not found at: {directory}")
    if browser:
        webbrowser.open_new("http://localhost:{:d}/".format(port))
    here = Path(directory).absolute()
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(here))
    with socketserver.TCPServer(("", port), handler) as httpd:
        print("kedro-static-viz serving at port", port)
        httpd.serve_forever()


if __name__ == "__main__":
    cli()
