# SSH Session Generator
Desktop application for generating multiple ssh sessions with executing commands for testing purposes. 

### Overview

This is application written in Python 2.7, using Tkinter GUI package. It was created to automate tests consisting of generating multiple
ssh sessions with few commands used in each. I made it desktop so it will be easy to use for "non-command-line-users" too. 

You can find .exe file in the dist/session_generator/session_generator.exe

### How to use?

The application is divided by 3 sections:
* in the first enter details about the host: ip, port and credentials,
* in the second add commands You wanted to be executed and divide each by &&,
* in the third choose "Multiple sessions" if You want to have more than 1. Specify the number in the next area. 

Click Start and wait. When all sessions will be generated You will get popup with executed time included. 

When You close program the current filled data will be stored in the "sessionData" folder (created on Your drive when first run the application)
Next time when You want to run generator for those data, **first** click "Clear" and then "Restore previous session config". Unforunately
right now it supports only one entry. 
