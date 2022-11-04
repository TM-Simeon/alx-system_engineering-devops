#!/usr/bin/env bash
# script to find the size of a url
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
