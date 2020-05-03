# An opinionated demo project for python

## Repository layout

The layout is the following:

```
.
├── my_devops_package
│   ├── app2.py
│   ├── app.py
│   ├── data
│   │   └── data.json
│   └── __init__.py
├── my_other_package
│   └── __init__.py
├── tests
│   └── test_main.py
├── CHANGELOG
├── LICENSE
├── MANIFEST.in
├── setup.cfg
├── setup.py
├── README.md
└── Makefile
```

Here are some explanations:

* `devops_package` and `my_other_package` are the names of the modules
  contained in the package. The name of the package is the identifier of the
  package in the indexes (see below the introduction to `pip`). The name of the
  modules is the identifier used in an `import` statement. Usually, there is
  only one module in the package, and the name of the module matches the name
  of the package, except for dashes and underscores: packages are usually named
  with dashes `-` whereas modules are named with underscores `_`;
* `tests` contain the tests of the package;
* `CHANGELOG` lists the modifications made between the releases (versions);
* `LICENSE` contains the license of the code (who is allowed to do what);
* `MANIFEST.in` lists the files to be included (or excluded) in the source
  distribution ([see the syntax](
  https://packaging.python.org/guides/using-manifest-in/));
* `setup.cfg` describes the package. It includes the metadata (name, version,
  author, etc.), the dependencies (other python modules), and some options
  for the tools involved in the development process (see more
  [in the documentation](
  https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files));
* `setup.py` is the script, relying on `setuptools`, responsible for
  packaging and/or building the package;
* `Makefile`, associated with the software `make`, calls various commands
  during the build process.

## Workflow

### Initialization of the environment

#### External tools

Make sure the following tools are available on your computer:

* [make](https://www.gnu.org/software/make/), a tool which controls the
  development workflow;
* [pip](https://pip.pypa.io/en/stable/), the package installer for Python;
* [pew](https://github.com/berdario/pew), a virtual environment manager for
  Python;
* [pre-commit](https://pre-commit.com/), a framework for managing (git)
   pre-commit hooks.

On Debian, you can install those dependencies with:

```bash
sudo apt-get install make python3-pip
pip3 install --user pip
pip install --user pew pre-commit
```

#### The python package manager

`pip` is the package installer for Python. `pip` is the preferred way to install
packages from the [Python Package Index](https://pypi.org/) and other indexes.

Some common commands are:

* `pip install <some_package>`
* `pip install --upgrade <some_package>`
* `pip uninstall <some_package>`
* `pip list`

#### Virtual environments: a quick introduction

When working on different projects, it may happen that two of these projects
depend on different versions of some library: project A depends on `some-lib`,
version 1.2, whereas project B depends on `some-lib` version 2.3.

At the [versions](https://semver.org/) suggests, those two versions are
incompatible (a breaking change was introduced in version 2). A virtual
environment is a way of avoiding installing and uninstalling the library
 continuously, depending on the project you're working on.

A virtual environment (venv) is a dedicated space in the (global) tree file
structure, where dependencies can be installed safely without interfering
with other (virtual) environments. Hence, working on project A and B can be
done at the same time, and it is highly recommended to work with virtual
 environments.

Several venv manager exists. Among them, [`pew`](https://github.com/berdario/pew)
is easy to use:

* `pew ls` lists the existing venvs;
* `pew new <my_name>` creates a new venv;
* `pew rm <my_name>` removes an existing venv (delete the files);
* `pew workon <my_name>` "activates" the venv, that is, allows one to work
  within the venv; commands like `pip` will install the dependencies in that
  particular environment;
* `pew in <my_name> <some_command>` runs `<some_command>` in the venv without
  activating it.

For further information, [read the documentation](https://github.com/berdario/pew#command-reference).

#### Bootstrap the project

In order to boostrap the project (i.e. to get everything in order to work
), simply run `make bootstrap`:

* if you are in a previously created venv, it will install all the dependencies,
  including development-dependencies (which are required for the development
   process but not for the runtime, like tests and packaging libraries);
* otherwise, it will suggest to create a new venv whose name is based on the
  current path. Once created, run `make bootstrap` a second time.

### Development

During the development process, you must always work within the venv.

#### Dependencies management

It is high likely that the project depends on several external libraries, called
dependencies. Those are stored in `setup.cfg`:

* runtime dependencies are listed under `install_requires` in the `[options]`
  section; those are dependencies that must be present on the target system
  (where the package will be used) to work properly;
* additional development dependencies (tests, packaging, etc.) are listed under
 `dev=` in the `[options.extras_require]`, and installed alongside required
  dependencies by specifying the `[dev]` extra marker.

To install the dependencies, either run `make bootstrap`, or `pip install -e .`,
 or `pip install -e .[dev]`.

Avoid installing dependencies directly with `pip install <some_deps>`: the
synchronisation with `setup.cfg` is not automatic.

#### Quality checks

`make quality`, which run a few checks, should be run on a regular basis.

### Releasing a new version

When the new functionality is ready, and the code clean, it's time to create a
new release. [`zest`](https://zestreleaser.readthedocs.io/en/latest/) is in
charge of the process:

* make sure your code is in clean state;
* fill the `CHANGELOG` file, if not already done;
* run `make release` (this will trigger `zest`), and follow the instructions.

`zest` will take care of creating the git tag, updating the version in `setup.cfg`
as well as the changelog.

## Packaging

There are two common way of packaging a Python project:

* a source distribution, which should contain everything needed to recreate
  the project (the source, the tests, etc.). Roughly speaking, it contains
  the same files as the git project;
* a binary ("wheel") distribution, containing the "runtime" code and some
  metadata (the version, the dependencies), but not the tests (for instance).

Run `make package` to create both distributions.
