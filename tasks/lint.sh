#!/usr/bin/bash
set -eu pipefail
set +e

FAILURE=false

echo "poetry check"
poetry check

echo "pylint"
poetry run pylint --ignore=snapshots comcrawl tests || FAILURE=true

echo "pycodestyle"
poetry run pycodestyle --exclude=snapshots comcrawl tests || FAILURE=true

echo "mypy"
poetry run mypy comcrawl tests || FAILURE=true

echo "bandit"
poetry run bandit -ll -r comcrawl tests || FAILURE=true

echo "shellcheck"
shellcheck tasks/*.sh || FAILURE=true

if [ "$FAILURE" = true ]; then
  echo "Linting failed"
  exit 1
fi
echo "Linting passed"
exit 0