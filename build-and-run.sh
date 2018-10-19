#!/usr/bin/env bash
echo "Building ..."
docker build -t ru18wip .
echo "Built done so run:"
docker run --rm -it ru18wip
