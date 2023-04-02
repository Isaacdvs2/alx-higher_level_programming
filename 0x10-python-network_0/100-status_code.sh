#!/bin/bash
# display the status code of the response of a request to a URL passed as as argument
curl -s -o /dev/null -w "%{http_code}" "$1"
