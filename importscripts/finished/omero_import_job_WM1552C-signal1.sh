#!/bin/bash

# This is a simple script for running the OMERO importer command
# as an Orchestra job. Prerequisites include have the source data
# in /sorger/OMERO. I am going to hard code those paths into the script
# for now to get started. 

# change to the directory containing importer-cli

cd OMERO.clients.linux-current

# run the importer

   ./importer-cli \
      -s lincs-omero.hms.harvard.edu \
      -u LINCS \
      -w icbp45 \
      -r 1701 \
      --transfer=ln_s
      -n "20140401_density effects_HS578T MCF7[1048]/140404_230703-V_HS578T_drug1_A[3661]"\
      /sorger/OMERO/mn79/mario-testing/20140401_density\ effects_HS578T\ MCF7\[1048\]/140404_230703-V_HS578T_drug1_A\[3661\]/MeasurementIndex.ColumbusIDX.xml 
