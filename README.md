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
└── README.md
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
* `pyproject.toml` describes the package. It includes the metadata (name, version,
  author, etc.), the dependencies (other python modules), and some options
  for the tools involved in the development process (see more
  [in the documentation](
  https://packaging.python.org/en/latest/guides/writing-pyproject-toml)).

## Workflow

### Initialization of the environment

#### External tools

Make sure the following tools are available on your computer:

* [pip](https://pip.pypa.io/en/stable/), the package installer for Python;
* [uv](https://docs.astral.sh/uv/), a package and project manager for Python;
* [pre-commit](https://pre-commit.com/), a framework for managing (git)
   pre-commit hooks.

On Debian, you can install those dependencies with:

```sh
sudo apt-get install python3-pip
pip3 install --user pip uv pre-commit
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

Several venv manager exists. [uv](https://docs.astral.sh/uv/)
makes `venvs` easy to use: you basically only need to prefix your commands with
`uv run`.

For further information,
[read the documentation](https://docs.astral.sh/uv/getting-started/features/#projects).

### Development

#### Dependencies management

It is high likely that the project depends on several external libraries, called
dependencies. Those are stored in `pyproject.toml`:

* runtime dependencies are dependencies that must be present on the target system
  (where the package will be used) to work properly;
* development dependencies (tests, packaging, etc.) are only needed for the development
  of the project.

Dependencies can be installed and added to `pyproject.toml` thanks to the commands
`uv add <my-dep>` and/or `uv add --dev <my-dep>`.

#### Quality checks

Linters are static analysis softwares, which can detect a number of errors in
the code, before the execution, and thus makes it possible to measure the
quality.

A popular linter (as well as formatter) for Python is [`ruff`](https://docs.astral.sh/ruff/).
The pre-commit configuration enforces its use. The problems identified by these
software must be corrected, except when there is a (really) relevant argument
against them.

Once installed, `ruff` can also be called with `uv run ruff check --fix` and `uv run ruff format`.
You do not need to prefix the command with `uv run` if the tool is installed globally.

## Packaging

There are two common way of packaging a Python project:

* a source distribution, which should contain everything needed to recreate
  the project (the source, the tests, etc.). Roughly speaking, it contains
  the same files as the git project;
* a binary ("wheel") distribution, containing the "runtime" code and some
  metadata (the version, the dependencies), but not the tests (for instance).

Run `uv build` to create both distributions in the `dist` directory.

## Pre-commit

The quality of the project can be ensured thanks to
[pre-commit](https://pre-commit.com/),
a tool that adds a git-hook in the repository, called automatically before each `commit`.

The hook executes instructions listed in a `.pre-commit-config.yaml` file,
provided by the developper (see [this example](./.pre-commit-config.yaml)),
and put at the root-level of the git directory.

When run, the tool will mark all lines that are not rule-compliant and outline
the reason and the source of the problem.

To install pre-commit (for your user), run

```sh
    pip3 install --user pre-commit
```

In order to create the hook, the following command must be run in the git
repository. The `git clone` operation will download `.pre-commit-config.yaml` if it
exists in the repository, but will not create the hook.

```sh
    pre-commit install
```

Once installed, to call the tool manually (rather than relying on the "hook"
aspect), you can use

```sh
    pre-commit run --files <file1> <file2> ...
    pre-commit run --all-files
```

## Unit tests

Unit tests are typically automated tests run to ensure that a section of an
application meets its design and behaves as intended. To run the tests
manually, execute

```sh
uv run pytest
```

For further information on the unit tests one can use the commands:

```
uv run pytest -v
uv run pytest -vv
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
uv add jupyter jupyter_contrib_nbextensions
```

Some packages commonly used with `Jupyter` are:

* `numpy`, `scipy`, `polars` (numerical tools)
* `plotly`, `matplotlib`, `hvplot` (graphics libraries)
* `colorcet`, `colorlover` (color bank for visualization)

### Installation of jupyter extensions

It is possible to add Jupyter extensions with the module nbextension:

```sh
uv run jupyter contrib nbextension install --user
uv run jupyter nbextensions_configurator enable
uv run jupyter nbextension enable <extension>
```

Extension examples:

* `codefolding/main` (hides some of the code to make the page lighter)
* `execute_time/ExecuteTime` (display of execution time)

#### Launching the application

```sh
uv run jupyter notebook
uv run jupyter notebook --no-browser
```

In both cases, these commands provide a URL to access the service. In the first
case, a browser is launched (desirable in the local case), in the second case
it is not (desirable in the remote case).

URL example: `http://localhost:8888/?token=7c35e29aacf2019572b4c526496bfa21b8b0218fd9206d66`.

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
