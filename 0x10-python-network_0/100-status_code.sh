#!/bin/bash
# sends request to a URL, and displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
