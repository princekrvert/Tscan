#!/data/data/com.termux/files/usr/bin/bash
#@Author prince kumar
#Date 10 dec 2020
#VersionV1.0
apt update && apt upgrade
apt-git install python
apt-git install python2
pkg install python3
pip install -r requirements.txt
pip install tqdm
pip install socket
clear
python3 Tscan.py
