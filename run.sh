#!/usr/bin/env bash
# 4 修改为 内核数*2+1, 线程数没有明确限制, 可以根据需求动态调整, 暂时定为20

gunicorn -w4 -b0.0.0.0:5000 server:app

gunicorn -w5 -b0.0.0.0:5000 --threads 6 server:app