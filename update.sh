#!/bin/bash
set -e

echo "Updating to latest version..."
cd /usr/share/server-watch-client
git stash save
git pull
git stash pop
