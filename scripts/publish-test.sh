#!/bin/bash
poetry build
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish -r testpypi