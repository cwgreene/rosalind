#!/bin/bash
git commit --amend -m "$(git show -s HEAD --format="%sn%n%b" | hooks/format-commit-message.py)"
