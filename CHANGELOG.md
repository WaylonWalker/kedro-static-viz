# 0.4.3

* FIX: add missing dependency flask added in vendored module

# 0.4.1, 0.4.2

* FIX: Botched release

# 0.4.0

* FEAT: upgrade kedro-viz to 3.9.0

# 0.3.1

* FIX: add semver to requirements.txt

Also added requirements_dev.txt and run interrogate on test-lint.

# 0.3.0

* made `kedro_static_viz.static_viz` callable from python
* created `kedro_static_viz.hooks.StaticViz` to create static viz before pipeline run

# 0.2.3

_release went sideways causing the patches_

* remove kedro_viz as a dependency
* allow for python 3.8

# 0.1.3

* integrate LICENSE into manifest.in for conda build

# 0.1.2

* FIX FileNotFound directory not rendered in f string

# 0.1.1

* FIX FileNotFound directory not passed to _call_viz

# 0.1.0

* implemented --serve/--no-serve

# 0.0.1

* initial release
