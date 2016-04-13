#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2011 University of Dundee & Open Microscopy Environment.
#                    All Rights Reserved.
# Use is subject to license terms supplied in LICENSE.txt
#


import omero
import sys
from omero.gateway import BlitzGateway
from Connect_To_OMERO import USERNAME, PASSWORD, HOST, PORT


# Create a connection
# =================================================================
conn = BlitzGateway(USERNAME, PASSWORD, host=HOST, port=PORT)
conn.connect()

def print_obj(obj, indent=0):
    """
    Helper method to display info about OMERO objects.
    Not all objects will have a "name" or owner field.
    """
#    print >> sys.stderr, """%s%s:%s  Name:"%s" (owner=%s)""" % (\
#            " " * indent,
#            obj.OMERO_CLASS,\
#            obj.getId(),\
#            obj.getName(),\
#            obj.getOwnerOmeName())


# Retrieve Screening data:
# =================================================================
conn.SERVICE_OPTS.setOmeroGroup('-1') ### Set the group to search within. -1 for all groups.
print "ScreenID,Screen Name,PlateID,Plate Name,Image,ImageID" 
for screen in conn.getObjects("Screen"):
    print_obj(screen)
    for plate in screen.listChildren():
        print_obj(plate, 5)
        plateId = plate.getId()
        for well in plate.listChildren():
            index = well.countWellSample()
            for index in xrange(0, index):
                print ",".join(map(str, [\
                    screen.getId(),\
                    screen.getName(),\
                    plateId, '"' + \
                    plate.getName(),\
                    well.getImage(index).getName() + '"',\
                    well.getImage(index).getId()]))

# Close connection:
# =================================================================
# When you're done, close the session to free up server resources.

conn._closeSession()
