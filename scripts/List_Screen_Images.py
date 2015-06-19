#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2011 University of Dundee & Open Microscopy Environment.
#                    All Rights Reserved.
# Use is subject to license terms supplied in LICENSE.txt
#
#  This is derived from Read_Data.py for use in the HMS LINCS project.

from sys import argv

script, screennum = argv
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
screenId = screennum

# Retrieve Wells and Images within a Screen:
# =================================================================
conn.SERVICE_OPTS.setOmeroGroup('-1')

if screenId >= 0:
    screen = conn.getObject("Screen", screenId)
    for plate in screen.listChildren():
        index = plate.countPlateSample()
        for index in xrange(0, index):
            print "ScreenID:", screenId, "Name:", screen.getName()  



# Close connection:
# =================================================================
# When you're done, close the session to free up server resources.
conn._closeSession()
