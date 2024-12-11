# Test Submission Schema

This repository contains the test submission schemas for different testing frameworks.


## Table of Contents

- [Installation Guide](#installation-guide)

<a name="installation-guide"></a>

## Installation Guide

### Requirements

This repository requires the following dependencies

- [Python 3.13](https://www.python.org/downloads/release/python-3131/)
- [uv](https://docs.astral.sh/uv/)
- [Snapcraft](https://snapcraft.io/docs/installing-snapcraft)

### Installing for contribution

1. **Installing YARF with dependencies on a virtual environment**

   We can install test submission schema along with the dependencies specified in
   `pyproject.toml` in the virtual environment using the command:

   ```
   uv sync
   ```

   After that, we enter the virtual environment:

   ```
   source .venv/bin/activate
   ```

   Then, we install the development dependencies:
   ```
   uv pip install .[develop]
   ```

   We can start working on the repository here.

1. **Leaving the virtual environment**

   When we finish working with the repository and leaving the virtual environment,
   we can execute:

   ```
   deactivate
   ```
