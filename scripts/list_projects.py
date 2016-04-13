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

conn.SERVICE_OPTS.setOmeroGroup('-1')

# Retrieve a list of all projects owned by user:
# =================================================================
print "\nList Projects:"
print "=" * 50
for project in conn.getObjects("Project"):
    print_obj(project)
    for dataset in project.listChildren():
        print_obj(dataset, 2)
        datasetId = dataset.getId()

# Close connection:
# =================================================================
# When you're done, close the session to free up server resources.

conn._closeSession()
