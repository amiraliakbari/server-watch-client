Server-Watch: client
====================

Server-Watch is a distributed system for monitoring status and performance of your servers.
On each monitored server, this client should be installed (see instructions below) to log 
server status reports to local log files. Then the log files can be sent to a central Server-Watch
server for further analysis.

Monitoring is done using modules. Each module monitor an specific ascpet of the system, like
server uptime, load, memory usage, and service status. Modules are prediocally run by the client to
collect data from the server (called a scan), and the scan reports are saved in local log files.


Installation
------------
To install the client, run these commands as root on the server(s) you want to monitor:

    cd /usr/share
    git clone git@github.com:amiraliakbari/server-watch-client.git
    cd server-watch-client
    ./install.sh

This will copy the required files and also setup a cron task to run the client every 10 minutes.
After the initial installation, for getting the latest updates, you can run the following any time
you want (application data is preserved):

    ./usr/share/server-watch-client/update.sh


Configuration
-------------

No monitoring module is enabled by default. To enable modules, edit the `/etc/server-watch-client/conf/scans.py`
file and put needed modules in `modules_enabled` list. There are some commented sample module in this file
which you can easily uncomment to use, and also any other module in the `/usr/share/server-watch-client/modules`
directory files can be added to the enabled modules.


Viewing the Results
-------------------

After enabling modules, you can see the scan reports in `/var/log/server-watch-client/localhost/latest` log
file. Optionally, if you setup a central Server-Watch server, clients can be configured to also send the logs
to the central server for better results aggregation and viewing.


Comparison
----------

Server-Watch is intended to be a light-weight alternative to systems like nagios to be easier to use and extend.
Specifically, the modules system is designed for easy extention by the users and the whole software code, modules,
and config files are written in Python. This will extermely facilitate writting custom monitoring modules, 
especially by using the extensive Python standard and third party libraries, like `http` or `twisted`.

The distributed architecture and offline logging feature of the system will ensure that the status reports of all
servers are preserved even in case of losing central server connection to the clients. Additionaly, the clients
can be used to monitor each other (called remote scanning modules) for analysing nodes from different networks and
geographical locations without needing to setup multiple servers.


Contribution
------------
Contributions are really welcome, just fork, see some of the current modules (e.g. `modules/local.py: LoadMonitor`)
and start writing your own new monitoring modules! Or just report bugs or request feature in issues page.
