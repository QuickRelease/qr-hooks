#!/bin/bash

DIRECTORY="./docs/model_diagrams/"

# If the directory doesn't exist, create it
mkdir -p $DIRECTORY

# the settings module is the first argument
SETTINGS_MODULE="$1"

# remove the first argument passed to the script
shift

# the rest of the arguments are migration file names
MIGRATIONS=$@

# declare an array to hold the app names
declare -a APP_NAMES=()

# loop through the migrations and get the app names
for migration in $MIGRATIONS; do
    APP_NAMES+=("$(echo "$migration" | cut -d'/' -f1)")
done

# declare an array and use it to get the unique app names
FINAL_APP_NAMES=($(echo "${APP_NAMES[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))

# loop through the unique app names and generate the diagrams
for APP in "${FINAL_APP_NAMES[@]}"; do
    python -m django_diagram -a $APP -o $DIRECTORY/$APP.md -s $SETTINGS_MODULE
done

# add the diagrams to git
git add $DIRECTORY
