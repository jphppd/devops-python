.DEFAULT_GOAL := help

all: mrproper bootstrap quality package ## Clean and run all steps except release.

###############
## Bootstrap ##
###############

.PHONY: bootstrap
bootstrap: _assert_venv ## Bootstrap the project in the venv (with dev dependencies).
	$(info $(cyan)*** Bootstrap$(reset))
	pip install --editable .[dev]

.PHONY: bootstrap-release
bootstrap-release: _assert_venv ## Bootstrap the project in the venv.
	$(info $(cyan)*** Bootstrap-release$(reset))
	pip install --editable .

#########################
## Package and release ##
#########################

.PHONY: package
package: _assert_venv ## Package the project.
	$(info $(cyan)*** Package$(reset))
	python setup.py sdist
	python setup.py bdist_wheel

.PHONY: release
release: _assert_venv quality ## Create a full release with a new tag.
	$(info $(cyan)*** Release$(reset))
	# Requires zest
	fullrelease

#############
## Quality ##
#############

.PHONY: quality
quality: _assert_venv check-manifest test precommit ## Run quality checks.

.PHONY: check-manifest
check-manifest: _assert_venv
	$(info $(cyan)*** Check manifest$(reset))
	@check-manifest

.PHONY: test
test: _assert_venv
	$(info $(cyan)*** Run tests$(reset))
#	Pytest returns 5 when no tests were found or run.
	@pytest || test $$? -eq 5

.PHONY: precommit
precommit: _assert_venv
	$(info $(cyan)*** Run precommit$(reset))
	@pre-commit run

##########################
## Clean the repository ##
##########################

.PHONY: clean
clean: ## Delete all intermediate and cached files.
	$(info $(cyan)*** Clean$(reset))
	@rm --recursive --force *.egg-info build
	@find . -name '*pyc' -type f -delete
	@find . -name '*pyo' -type f -delete
	@find . -name '__pycache__' -type d -empty -delete

.PHONY: mrproper
mrproper: clean ## Delete all generated files.
	$(info $(cyan)*** Mrproper$(reset))
	@rm --recursive --force dist

####################
## Makefile utils ##
####################

cyan:=$(shell tput setaf 6 ; tput bold)
red:=$(shell tput setaf 1 ; tput bold)
reset:=$(shell tput sgr0)
NULL :=
TAB  := $(NULL)	$(NULL)

VENV := $(shell pwd | md5sum --zero | cut -d" " -f1)

.PHONY: _assert_venv
_assert_venv: # Simple target to make sure the command is run inside a virtual environment
ifndef VIRTUAL_ENV
	$(info )
	$(info $(TAB)$(red)** Error **$(reset))
	$(info )
	$(info This command must be run in a Python virtualenv. Try:$(reset))
	$(info )
	$(info $(TAB)$$ $(cyan)pip install --user pew$(reset))
	$(info $(TAB)$$ $(cyan)pew new $(VENV)$(reset))
	$(info or)
	$(info $(TAB)$$ $(cyan)pew workon $(VENV)$(reset))
	$(info )
	$(info See more: https://github.com/berdario/pew#command-reference)
	$(info )
	$(error Aborting)
endif

.PHONY: help
help: ## Print the help and exit.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[96mmake %-20s\033[0m %s\n", $$1, $$2}'
