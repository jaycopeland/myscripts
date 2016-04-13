#!/bin/bash

# This is a simple script for running the OMERO importer command
# as an Orchestra job. Prerequisites include have the source data
# in /groups. I am going to hard code those paths into the script
# for now to get started. 



# run the importer

   ~/OMERO.clients.linux-current/importer-cli \
      -s lincs-omero.hms.harvard.edu \
      -u LINCS \
      -w icbp45 \
      -r 1802 \
      --transfer=ln_s
      "$plate" ; 

done
