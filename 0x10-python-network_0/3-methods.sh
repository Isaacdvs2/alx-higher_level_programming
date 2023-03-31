#!/bin/bash
# A script that accepts a URL and displays all Http methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
