#!/bin/bash


# echo

md5_str=$1

ssh_pid=`ps -ef |grep $md5_str |grep -v grep |grep -v session_tracker.sh |grep -v sshpass |awk '{print $2}'`
echo "ssh session pid:$ssh_pid"

echo 123456 | sudo -S /usr/bin/strace -ttt -p $ssh_pid -o "$md5_str.log"
