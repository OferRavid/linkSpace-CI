#!/usr/bin/env bash
is_healthy() {
    nginx_health_status="$(docker inspect -f "{{.State.Status}}" nginx)"
    mongo_health_status="$(docker inspect -f "{{.State.Status}}" mongodb)"
    linkspace_health_status="$(docker inspect -f "{{.State.Status}}" linkspace)"
    if [ "$nginx_health_status" = "running" ] && [ "$mongo_health_status" = "running" ] && [ "$linkspace_health_status" = "running" ]; then
        return 0
    else
        return 1
    fi
}

timer=0
while ! is_healthy; do 
    if [ $timer = $1 ]; then
        echo "containers didn't start within" $1 "seconds. Check your code." > testResult.txt 
        exit 1
    fi
    sleep 1
    timer=$((timer+1)); 
done

