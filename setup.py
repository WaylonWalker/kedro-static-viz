from setuptools import setup, find_packages
from pathlib import Path

NAME="kedro-static-viz"

README = (Path(__file__).parent / "README.md").read_text()

setup(
    name=NAME,
    version='0.0.1',
    url='https://github.com/WaylonWalker/kedro-static-viz.git',
    author='Waylon Walker',
    author_email='waylon@waylonwalker.com',
    description='Creates a static visualization of your pipeline',
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),    
    zip_safe=False,
    include_package_data=True,
    license="MIT",
    install_requires=["kedro", "kedro-viz"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    # package_data={"public": ['**/public/**/*']},
    entry_points={
        "kedro.global_commands": ["kedro-static-viz = kedro_static_viz.cli:cli"],
        'console_scripts': ["kedro-static-viz = kedro_static_viz.cli:cli"]}
)
