#!/bin/bash
# send a delete req and display the http response.
curl -s "$1" -X DELETE
