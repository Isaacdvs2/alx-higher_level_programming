#!/usr/bin/env bash
# dispalys the size of the body of the response from a request URL using curl
curl -s "$1" | wc -c

