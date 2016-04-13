#!/bin/bash

# This is a simple script for running the OMERO importer command
# as an Orchestra job. Prerequisites include have the source data
# in /groups. I am going to hard code those paths into the script
# for now to get started. 

# change to the directory containing importer-cli

cd OMERO.clients-5.0.6.172-gs-ice34.linux

# run the importer

   ./importer-cli \
      -s lincs-omero.hms.harvard.edu \
      -u LINCS \
      -w icbp45 \
      -r 1651 \
      -n WM1552C-signal2\
      /groups/omero/HMS_LINCS_Dataset_20219/2013_10_29_signals_Corrected\[613\]/WM1552C-signal2\[1649\]/MeasurementIndex.ColumbusIDX.xml
 
