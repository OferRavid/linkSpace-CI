#!/bin/bash -x

NEW_TAG=$1

git clean -f
git tag -a ${NEW_TAG} -m "aading new tag: ${NEW_TAG}"
git push -u origin ${NEW_TAG}