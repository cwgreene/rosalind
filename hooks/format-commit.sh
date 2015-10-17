#!/bin/bash
git commit --amend -m "$(git show -s HEAD --format="%s%n%n%b" | hooks/format-commit-message.py)"
