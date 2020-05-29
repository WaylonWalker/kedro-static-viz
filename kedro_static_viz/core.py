"""
core python functionality to create a static viz site with python from inside the
project directory

Example:
    >>> from kedro_static_viz import static_viz
    >>> static_viz()
"""
import http.server
import shutil
import socketserver
import webbrowser
from functools import partial
from pathlib import Path
from typing import Union

from .vendored import _call_viz


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


def static_viz(
    port: int = 4141,
    browser: bool = False,
    load_file: Union[str, Path, None] = None,
    pipeline: str = None,
    env: str = None,
    directory: Union[str, Path] = "public",
    serve: bool = False,
) -> None:
    """
    creates kedro-static-viz as a directory of html/css/js/json that can be hosted
    without a backend server running continuously.

    Arguments:
        port (int): TCP port that viz will listen to. Default is 4141.
        brower (bool): Whether to open viz interface in the default browser or not.
            Default is False
        load_file (str, Path, None): Path to load the pipeline JSON file
        pipeline (str): The name of the modular pipeline to visualize. Default is None
        env (str): Kedro configuration environment. If not specified,
            catalog config in `local` will be used. Default is None
        directory (str, Path): Path to save the static site to. Default is 'public'
        serve (bool): Whether or not to serve the site after creating. Default is False.

    Returns (None): None

    """

    if isinstance(directory, str):
        directory = Path(directory)
    copy_site(directory)
    viz_file = f"{directory}/pipeline.json"

    if isinstance(load_file, str):
        load_file = Path(load_file)

    if load_file is not None:
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
