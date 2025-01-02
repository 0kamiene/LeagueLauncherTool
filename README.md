# LeagueLauncherTool

A Python tool to manage and launch League of Legends client with enhanced control and troubleshooting features.

A Python tool to manage and launch the League of Legends client, ensuring that necessary processes are handled and potential conflicts are resolved. Designed for convenience, this script manages conflicting processes, checks for admin privileges, and ensures a smooth launch experience.

Features Process Management: 
Automatically terminates conflicting processes (LeagueClient.exe, RiotClientServices.exe) before launching the League client. 
Admin Privileges: Ensures the script runs with the required admin rights for seamless operation. 
Customizable Paths: Users can update the file paths directly in the script for their setup. 
Lightweight: Minimal dependencies and simple usage.

Prerequisites Python Version: 
Python 3.8 or later. 
Required Libraries: psutil ctypes subprocess

Notes 
Ensure the specified file paths (league_path and riot_path) match your League of Legends installation. 
The script requires admin rights to manage processes.
Use the --uac-admin flag when building with PyInstaller to ensure the executable runs with elevated privileges.
