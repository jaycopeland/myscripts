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
    print >> sys.stderr, """%s%s:%s  Name:"%s" (owner=%s)""" % (\
            " " * indent,
            obj.OMERO_CLASS,\
            obj.getId(),\
            obj.getName(),\
            obj.getOwnerOmeName())


# Retrieve a list of all screens owned by user:
# =================================================================
conn.SERVICE_OPTS.setOmeroGroup('-1') ### Set the group to search within. -1 for all groups.
print "\nList Screens:"
print "=" * 50
for screen in conn.getObjects("Screen"):
    print_obj(screen)
    for plate in screen.listChildren():
        print_obj(plate, 2)
        plateId = plate.getId()

# Close connection:
# =================================================================
# When you're done, close the session to free up server resources.

conn._closeSession()
