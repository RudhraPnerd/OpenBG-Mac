#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE}" )" && pwd )"
osascript -e "tell application \"Finder\" to set desktop picture to POSIX file \"$DIR/Wallpapers/seququoia.heic\""
