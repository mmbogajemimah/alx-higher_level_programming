#/bin/bash
#Takes URL, sends request to URL, displays content length
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2 
