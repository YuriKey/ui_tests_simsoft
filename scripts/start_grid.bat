@echo off
setlocal
pushd "%~dp0"

set SELENIUM_JAR="selenium-server-4.33.0.jar"
set HUB_PORT=4444
set NODE_COUNT=3

if not exist %SELENIUM_JAR% (
    echo Downloading Selenium Server...
    curl -O "https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.33.0/selenium-server-4.33.0.jar" || (
        echo Error: Download failed
        exit /b 1
    )
)

taskkill /FI "IMAGENAME eq java*" /F >nul 2>&1

start "Selenium Hub" cmd /k java -jar %SELENIUM_JAR% hub --port %HUB_PORT% --log-level INFO

timeout /t 5 >nul

for /L %%i in (1,1,%NODE_COUNT%) do (
    start "Node %%i" cmd /k java -jar %SELENIUM_JAR% node --hub http://localhost:%HUB_PORT% --port 55%%i
    timeout /t 1 >nul
)

echo Selenium Grid ready at http://localhost:%HUB_PORT%
