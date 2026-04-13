#!/bin/bash

echo "Container started..."
sleep 2

echo "Trying to ping host..."
ping -c 4 172.17.0.1

echo "Done!"
