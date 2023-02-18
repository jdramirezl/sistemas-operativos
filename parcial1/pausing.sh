#!/bin/bash
ps -ef | grep 'python3.8 pausing.py' | awk  '{print $2}'| xargs -I pid kill -9 pid;


