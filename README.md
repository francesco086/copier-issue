# Docker Image Creator

This repository contains a [Copier](https://copier.readthedocs.io/en/stable/) project template.

## What is it?

This template sets up a GitLab repository dedicated to building a Docker image.
It ships a GitLab CI/CD pipeline that builds, tests, and pushes the image to the registry `eoncds.azurecr.io` (the default GitLab one).

## Quickstart

1. Install [Copier](https://copier.readthedocs.io/en/stable/) in your python environment of choice

   ```console
   pip install copier
   ```

2. Copy the template by running the following command and answering to the prompted questions

   ```console
   copier copy https://git.eon-cds.de/repos/data-science-lib/templates/docker-image-creator.git path/to/destination
   ```

3. Fill the files `Dockerfile`, `determine-docker-image-tags.sh`, (optional) `test.sh`
4. Push to GitLab and watch CI/CD do everything for you 😉
