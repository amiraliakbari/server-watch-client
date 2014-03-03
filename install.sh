#!/bin/bash

pip install -r /usr/share/server-watch-client/requirements.txt
ln -s /usr/share/server-watch-client/cron.sh /etc/cron.d/server-watch-client
mkdir /etc/server-watch-client/conf --mode=755 --parents
mkdir /var/log/server-watch-client --mode=755 --parents
cp /usr/share/server-watch-client/conf/scans.sample.py /etc/server-watch-client/conf/scans.py
ln -s /etc/server-watch-client/conf/scans.py /usr/share/server-watch-client/conf/scans.py
ln -s /var/log/server-watch-client /usr/share/server-watch-client/logs
