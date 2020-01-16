#!/bin/bash
poetry run pytest --cov-report=xml --cov-report=term --cov=comcrawl -s tests