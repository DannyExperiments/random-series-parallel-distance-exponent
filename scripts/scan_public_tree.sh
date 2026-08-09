#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root"

patterns=(
  '/Users/'
  'chatgpt\.com/c/'
  'sandbox:/mnt/data'
  '-----BEGIN [A-Z ]*PRIVATE KEY-----'
  'ghp_[A-Za-z0-9]+'
  'github_pat_[A-Za-z0-9_]+'
  'sk-[A-Za-z0-9_-]{16,}'
  '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
)

for pattern in "${patterns[@]}"; do
  if grep -RInE --exclude='SHA256SUMS.txt' --exclude='scan_public_tree.sh' --exclude-dir='.git' -- "$pattern" .; then
    echo "public-tree scan: FAIL pattern=$pattern" >&2
    exit 1
  fi
done

echo "public-tree scan: PASS"
