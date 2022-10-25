#!/bin/bash

echo $PWD
docker exec flask pytest test_all.py -v > testResult.txt 
isTestsPassed=$(cat testResult.txt | grep "1 passed")
if [[ -z "$isTestsPassed" ]]; then
    echo 'failure'
    exit 1
else
    echo '=========== Unit Tests Finished Successfully =============='
fi
