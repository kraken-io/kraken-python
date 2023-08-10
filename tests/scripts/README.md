# Helper scripts for package testing

This scripts is used to test/debug package using certain python version during development process.

## Docker compose

Docker compose configuration (`tests/docker-compose.yml`) contains configuration for 2 images/services:

1. `python` - debian based image with `pyenv` and all python versions
2. `test` - image based on first image to run tests

### Requirements

-   ~30-35GB for `python` image
-   Installed `docker` and `docker-compose`

## Scripts

-   `build-docker.sh` - build docker image using `docker-compose`, it will take up to ~2-4 hours, because image will contain all python versions
-   `docker-run-all.sh` - run all tests using docker image `test`
-   `pyenv-install.sh` - install `pyenv` and all selected python versions (usually used inside docker image), versions list defined in script
-   `rm-docker.sh` - remove docker images
-   `run-all.sh` - run all tests for each installed by `pyenv` python versions
