#!/bin/bash
echo "$BRANCH_NAME" 
echo $BUILD_NUMBER
NEW_TAG=$1
echo ${NEW_TAG}
git clone git@github.com:OferRavid/linkspace-helm.git
cd linkspace-helm/linkspace
sed -i "s/tag:\ [0-9]*.[0-9]*.[0-9]*/tag:\ ${NEW_TAG}/g" values.yaml
git add .
git commit -m "Update backend tag to ${NEW_TAG}"
git push origin master
