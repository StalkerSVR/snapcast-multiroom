#!/bin/bash

echo "WARNING. Mopidy-Youtube is removed."
echo "There are a lot of issues with it and there is currently no maintainer."
echo "I'll add it back once there is a mainainer found for the package."
echo ""
echo ""
echo "Starting container..."
echo "Current user: $(whoami)"
echo "Current user id: $(id -u $(whoami))"
cd ~
echo $PWD
ls -lsa
echo ""
echo ""
exec /usr/bin/mopidy --config /etc/mopidy.conf:/mopidy.conf
