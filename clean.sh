#!/bin/bash

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 查找并删除名为 __pycache__ 的目录
find "$SCRIPT_DIR" -type d -name '__pycache__' -exec rm -rf {} +

# 查找并删除名为 media 的目录
find "$SCRIPT_DIR" -type d -name 'media' -exec rm -rf {} +

echo "所有 __pycache__ 和 media 目录已删除。"
