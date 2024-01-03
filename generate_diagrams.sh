#!/bin/bash

directory="./docs/model_diagrams/"

if [ ! -d "$directory" ]; then
    # If the directory doesn't exist, create it
    mkdir -p $directory
fi


SETTINGS_MODULE="$1"

shift

declare -A unique_apps

MIGRATIONS=$@

declare -a APP_NAMES=()

for migration in $MIGRATIONS; do
    APP_NAMES+=("$(echo "$migration" | cut -d'/' -f1)")
done

FINAL_APP_NAMES=($(echo "${APP_NAMES[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))

for APP in "${FINAL_APP_NAMES[@]}"; do
    python -m django_diagram -a $APP -o ./docs/model_diagrams/$APP.md -s $SETTINGS_MODULE
done

git add ./docs/model_diagrams/
