# File Sync Application
Developed By: TyReesh Boedhram  
Current Version: 3.2

## Overview
This application automatically syncs files between a server computer and client computers on the same network.
This application runs entirely in the background after setup.

## Running Application
You must have python 3.7+ installed to run this application.  
To run this application, double click on main.pyw

## Configuration
The configuration setup runs the first time the application is run, or if the config.txt file gets deleted.  
The configuration setup allows modifications to the following settings.

**Mode:** This configuration tell the application to run in either server mode or client mode.

**File Transfer Mode:** This configuration tells the application which direction to sync files.  
Options are Send, Receive, and Bidirectional.  
*This configuration only applies in Server mode*  
*The Server will tell the Client which mode to be in.*

**Server IP:** This configuration is the local IP address of the server computer.

**Server Network SSID *(Optional)*:** This configuration is the Wi-Fi SSID of the network the server is on.  
This forces the client to check if they are on the same network as the server before trying to connect.  

*This is labeled as "Wi-Fi Name" during setup*   
*This configuration only applies in client mode.*  
*This configuration is only enforced on Windows currently.*

**Root Location:** This configuration tells the application which directory to start in.  
In Send mode, this is the location to copy files from.  
In Receive mode, this is the location to copy files to.  

*Example:* Entering `C:\Users` will copy all files in `C:\Users` folder in Send mode, 
and place files in the `C:\Users` folder in Receive mode.  
The root location should be an absolute path *(ie: it starts with a drive letter on Windows and a forward-slash on UNIX)*

**Ignore Files *(Optional)*:** This configuration tells the application to skip over certain files or directories.  
To specify more than one file/directory, enter each file/directory on a new line in the text field.  

*File paths should be relative to the location specified for Root Location.*  
*This is labeled as "Files to Ignore" during setup*   
*This configuration only applies in Send mode and Bidirectional mode.*