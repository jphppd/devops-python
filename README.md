# An opinionated demo project for python

## Repository layout

The layout is the following:

```
.
├── my_devops_package
│   ├── __init__.py
│   ├── __main__.py
│   ├── app.py
│   ├── app2.py
│   ├── utils
│   │   ├── init_logging.py
│   │   └── __init__.py
│   └── data
│       └── data.json
├── tests
│   ├── __init__.py
│   └── test_main.py
├── CHANGELOG
├── LICENSE
├── MANIFEST.in
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

```sh
sudo apt-get install make python3-pip
pip3 install --user pip
pip3 install --user pew pre-commit
```

#### The python package manager

`pip` is the package installer for Python. `pip` is the preferred way to install
packages from the [Python Package Index](https://pypi.org/) and other indexes.

Some common commands are:

* `pip3 install <some_package>`
* `pip3 install --upgrade <some_package>`
* `pip3 uninstall <some_package>`
* `pip3 list`

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

In the following documentation, working inside a virtual environment is
indicated with:

```sh
(venv) $ run-some-command
```

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

`zest` will take care of creating the git tag, updating the version in
`setup.cfg`
as well as the changelog.

## Packaging

There are two common way of packaging a Python project:

* a source distribution, which should contain everything needed to recreate
  the project (the source, the tests, etc.). Roughly speaking, it contains
  the same files as the git project;
* a binary ("wheel") distribution, containing the "runtime" code and some
  metadata (the version, the dependencies), but not the tests (for instance).

Run `make package` to create both distributions.

## Coding and naming conventions

The conventions of Python are gathered in the [PEP 8](https://www.python.org/dev/peps/pep-0008/).
The package [pycodestyle](https://pycodestyle.readthedocs.io/en/latest)
verifies compliance with these conventions by the code.

## Linters

Linters are static analysis softwares, which can detect a number of errors in
the code, before the execution, and thus makes it possible to measure the
quality.

A popular linter for Python is [pylint](https://www.pylint.org/). The
pre-commit configuration enforces their use. The problems identified by these
software must be corrected, except when there is a (really) relevant argument
against them.

## Pre-commit

The package pydocstyle, pylint and other python conventions can be checked
automatically thanks to [pre-commit](https://pre-commit.com/). This tool adds a
git-hook in the repository, called automatically before each `commit`
operation. The hook executes instructions listed in a `.pre-commit-config.yaml`
file, provided by the developper
(see [this example](./.pre-commit-config.yaml)), and put at the root-level of
the git directory.
When run, the tool will mark all lines that are not rule-compliant and outline
the reason and the source of the problem.

To install pre-commit (for your user), run

```sh
    $ pip3 install --user pre-commit
```

In order to create the hook, the following command must be run in the git
repository. The `clone` operation will download `.pre-commit-config.yaml` if it
exists, but will not create the hook.

```sh
    $ pre-commit install
```

Once installed, to call the tool manually (rather than relying on the "hook"
aspect), you can use

```sh
    $ pre-commit run --files <file1> <file2> ...
    $ pre-commit run --all-files
```

## Unit tests

Unit tests are typically automated tests run to ensure that a section of an
application meets its design and behaves as intended. To run the tests
manually, execute

```sh
(venv) $ pytest
```

For further information on the unit tests one can use the commands:

```
(venv) $ pytest -v
(venv) $ pytest -vv
```

The unit tests are saved in a seperate folder `/tests` containing all tests and
test documents.

## Jupyter

[Jupyter](http://jupyter.org/) is a working environment to develop in
"notebook" mode (like matlab). This is mostly convenient for "algorithms"
development, for instance where commands must be frequently re-run with
different parameter values. It is not appropriate for the development of
a package meant to run as a service or a command-line tool. In this mode of
operation, we interact with the jupyter server via a web browser.

### Installation of Jupyter

```sh
(venv) $ pip3 install jupyter jupyter_contrib_nbextensions
```

Some packages commonly used with `Jupyter` are:

* `numpy`, `scipy`, `pandas` (numerical tools)
* `plotly`, `matplotlib` (graphical libraries)
* `psycopg2-binary` (database connector)
* `peewee` (ORM database)
* `shapely` (manipulation of geometric objects: lines, segments, polygons)
* `pyproj` (map projections conversion)
* `autopep8` (automatic formatting)
* `colorlover` (color bank for visualization)

### Installation of jupyter extensions

It is possible to add Jupyter extensions with the module nbextension:

```sh
(venv) $ jupyter contrib nbextension install --user
(venv) $ jupyter nbextensions_configurator enable
(venv) $ jupyter nbextension enable <extension>
```

Extension examples:

* `codefolding/main` (hides some of the code to make the page lighter)
* `code_prettify/autopep8` (formatting following pep8)
* `execute_time/ExecuteTime` (display of execution time)

#### Launching the application

```sh
(venv) $ jupyter notebook
(venv) $ jupyter notebook --no-browser
```

In both cases, these commands provide a URL to access the service. In the first
case, a browser is launched (desirable in the local case), in the second case
it is not (desirable in the remote case).

URL example: `http://localhost:8888/?token=7c35e29aacf2019572b4c526496bfa21b8b0218fd9206d66`.

### Remote access

By default, Jupyter only allows local connections (with a client on the
server). To access it from a remote station, the procedure is as follows.

#### Creation of a configuration file

```sh
(venv) $ jupyter notebook --generate-config
```

This command creates `~/.jupyter/jupyter_notebook_config.py`

#### Modification of the default configuration

To allow access to the service from any extension, you must change the
`c.NotebookApp.ip` parameter configuration file (by default, it is present but
commented), and put either `'*'`, or `'<server address>'`. Two examples:

```sh
c.NotebookApp.ip = '*'
```

Depending on the case, the server address in the proposed URL to connect to the
service may require modification.

#### Changing the notebook size

To increase the width of the notebook in the window, create the file
`~/.jupyter/custom/custom.css` with the content:

```css
.container {
    width: 99% !important;
}
div.cell.selected {
    border-left-width: 1px !important;
}
div.output_scroll {
    resize: vertical !important;
}
```
