#!/bin/bash

docker exec flask pytest -l > testResult.txt 
isTestsPassed=$(cat testResult.txt | grep "1 passed")
if [[ -z "$isTestsPassed" ]]; then
    echo 'failure'
    exit 1
else
    echo '=========== Unit Tests Finished Successfully =============='
fi
