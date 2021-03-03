from pathlib import Path

from setuptools import find_packages, setup

NAME = "kedro-static-viz"

README = (Path(__file__).parent / "README.md").read_text()


def get_requirements(file):
    """get the dependencies and installs"""
    with open(file, "r", encoding="utf-8") as f:
        # Make sure we strip all comments and options (e.g "--extra-index-url")
        # that arise from a modified pip.conf file that configure global options
        # when running kedro build-reqs
        requires = []
        for line in f:
            req = line.split("#", 1)[0].strip()
            if req and not req.startswith("--"):
                requires.append(req)
        return requires


requires = get_requirements("requirements.txt")

setup(
    name=NAME,
    version="0.4.4",
    url="https://github.com/WaylonWalker/kedro-static-viz.git",
    author="Waylon Walker",
    author_email="waylon@waylonwalker.com",
    description="Creates a static visualization of your pipeline",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    license="MIT",
    install_requires=requires,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    # package_data={"public": ['**/public/**/*']},
    entry_points={
        "kedro.global_commands": ["kedro-static-viz = kedro_static_viz.cli:cli"],
        "console_scripts": ["kedro-static-viz = kedro_static_viz.cli:cli"],
    },
)
