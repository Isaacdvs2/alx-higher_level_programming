#!/bin/bash
#sends a JSON post request to a URL passed as the arg and displays the result
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
