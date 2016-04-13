#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2011 University of Dundee & Open Microscopy Environment.
#                    All Rights Reserved.
# Use is subject to license terms supplied in LICENSE.txt
#
#  This is derived from Read_Data.py for use in the HMS LINCS project.

from sys import argv

script, platenum = argv
# platenum = argv

import omero
from omero.gateway import BlitzGateway
from Connect_To_OMERO import USERNAME, PASSWORD, HOST, PORT


# Create a connection
# =================================================================
conn = BlitzGateway(USERNAME, PASSWORD, host=HOST, port=PORT)
conn.connect()


# Configuration
# =================================================================
plateId = platenum       # this should be changed to set from a command
# line argument. 

# Retrieve Wells and Images within a Plate:
# =================================================================
#conn.SERVICE_OPTS.setOmeroGroup('-1')
#if plateId >= 0:
#    print "\nPlate:%s" % plateId
#    print "=" * 50
#    plate = conn.getObject("Plate", plateId)
#    print "\nNumber of fields:", plate.getNumberOfFields()
#    print "\nGrid size:", plate.getGridSize()
#    print "\nWells in Plate:", plate.getName()
#    for well in plate.listChildren():
#        index = well.countWellSample()
#        print "  Well: ", well.row, well.column, " Fields:", index
#        for index in xrange(0, index):
#            print "    Image: ", \
#                    well.getImage(index).getName(),\
#                    well.getImage(index).getId()


# Retrieve Wells and Images within a Plate:
# =================================================================
conn.SERVICE_OPTS.setOmeroGroup('-1')

if plateId >= 0:
    plate = conn.getObject("Plate", plateId)
    for well in plate.listChildren():
        index = well.countWellSample()
        for index in xrange(0, index):
            print "PlateID:", plateId, "PlateName:", plate.getName(), "Image: ",well.getImage(index).getName(),well.getImage(index).getId() 

# Close connection:
# =================================================================
# When you're done, close the session to free up server resources.
conn._closeSession()
