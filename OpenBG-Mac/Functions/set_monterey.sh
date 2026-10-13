#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE}" )" && pwd )"
osascript -e "tell application \"Finder\" to set desktop picture to \"$DIR/../Wallpapers/monterey.heic\" as POSIX file as alias"
