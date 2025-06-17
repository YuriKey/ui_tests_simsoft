#!/bin/bash
cd "$(dirname "$0")/scripts"

SELENIUM_JAR="selenium-server-4.33.0.jar"
HUB_PORT=4444
NODE_COUNT=3

if [ ! -f "$SELENIUM_JAR" ]; then
    echo "Downloading Selenium Server..."
    curl -O "https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.33.0/selenium-server-4.33.0.jar" || {
        echo "Error: Download failed"
        exit 1
    }
fi

pkill -f "java.*selenium-server" 2>/dev/null

echo "Starting Hub on port $HUB_PORT..."
java -jar "$SELENIUM_JAR" hub --port $HUB_PORT --log-level INFO &
HUB_PID=$!
sleep 5

echo "Starting $NODE_COUNT nodes..."
NODE_PIDS=()
for ((i=1; i<=NODE_COUNT; i++)); do
    java -jar "$SELENIUM_JAR" node --hub "http://localhost:$HUB_PORT" --port "55$i" &
    NODE_PIDS+=($!)
    sleep 1
done

echo "Selenium Grid ready at: http://localhost:$HUB_PORT"
echo "Press Ctrl+C to stop all nodes and hub"

trap "kill ${NODE_PIDS[@]} $HUB_PID 2>/dev/null; echo 'Grid stopped'; exit" SIGINT
wait