#!/bin/bash
# a bash script  that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sx DELETE "$1"
