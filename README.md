# Linux Auto-Sync Wi-Fi Hotspot

A lightweight Python automation script that seamlessly shares your active Wi-Fi connection over a new Wi-Fi hotspot on Linux. 

This script was specifically built to solve the notorious errors common with Intel Wi-Fi cards on Fedora and other Linux distributions. It dynamically detects your active Wi-Fi channel and forces the virtual Access Point (AP) to use the exact same frequency, bypassing strict driver limitations.

## Features
* Automatically detects your current active Wi-Fi channel and syncs the hotspot to it.
* Prevents Intel driver crashes by ensuring the physical and virtual interfaces don't fight over radio frequencies.
* Hardcode your SSID and password once, and launch your hotspot with a single command.

