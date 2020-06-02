#!/usr/bin/env bash

set -x

ALGO_BASE_PATH=/root
PIPELINE_ENTRY=default.py
BRANCH=master
OPTIONS=""

while [ "${1:-}" != "" ]; do
  case "$1" in
  "--branch")
    shift
    BRANCH=$1
    ;;
  "--entry")
    shift
    PIPELINE_ENTRY=$1
    ;;
  *)
    OPTIONS="${OPTIONS} $1=$2 "
    shift
    ;;
  esac
  shift
done

echo "Pipeline Params:"
echo "BRANCH : "${BRANCH}
echo "PIPELINE_ENTRY: "${PIPELINE_ENTRY}
echo "TRAINING OPTIONS: "${OPTIONS}

# Launch TrainingPipeline entry script.
export PYTHONPATH=${PYTHONPATH}:./
python -u ${ALGO_BASE_PATH}${PIPELINE_ENTRY} ${OPTIONS}
training_result=$?

if [ ${training_result} = "0" ]; then
  exit 0
else
  exit ${training_result}
fi
