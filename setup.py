from setuptools import setup, find_packages
name="kedro-static-viz"

setup(
    name=name,
    version='0.0.1',
    url='https://github.com/WaylonWalker/kedro-static-viz.git',
    author='Waylon Walker',
    author_email='waylon@waylonwalker.com',
    description='Creates a static visualization of your pipeline',
    packages=find_packages(),    
    zip_safe=False,
    include_package_data=True,
    # package_data={"public": ['**/public/**/*']},
    entry_points={
        "kedro.global_commands": ["kedro-static-viz = kedro_static_viz.cli:cli"],
        'console_scripts': ["kedro-static-viz = kedro_static_viz.cli:cli"]}
)