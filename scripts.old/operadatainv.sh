#!/bin/bash

cd /files/Opera

# write the list of top level folders in OperaDB
ls /files/Opera/OperaDB > ~/tmp/topoperadblist

# read the list of top level directories into script that finds plate folders and runs du

for dir in `cat ~/tmp/topoperadblist`
do
   echo $dir >> ~/tmp/inventory
   find "$dir" -iregex '.*Meas_[0-9]*' | sed -e 's/\/Meas_.*$//; s/.*\///' | sort | uniq >> ~/tmp/inventory  
done


