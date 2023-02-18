#!/bin/bash
ps -ef | grep 'python3.10 pausing.py' | awk  '{print $2}'| xargs -I pid kill -9 pid;


