#!/bin/bash
NEW_TAG=$1

aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 449814578585.dkr.ecr.eu-north-1.amazonaws.com
docker tag linkspace 449814578585.dkr.ecr.eu-north-1.amazonaws.com/linkspace:$NEW_TAG
docker push 449814578585.dkr.ecr.eu-north-1.amazonaws.com/linkspace:$NEW_TAG