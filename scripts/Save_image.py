#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2011 University of Dundee & Open Microscopy Environment.
#                    All Rights Reserved.
# Use is subject to license terms supplied in LICENSE.txt
#

from sys import argv
import omero
from omero.gateway import BlitzGateway
from Connect_To_OMERO import USERNAME, PASSWORD, HOST, PORT


# Create a connection
# =================================================================
conn = BlitzGateway(USERNAME, PASSWORD, host=HOST, port=PORT)
conn.connect()


# Configuration
# =================================================================
script, imageId = argv





#  Reitrieve an image by Image ID:
# =================================================================
image = conn.getObject("Image", imageId)
print "\nImage:%s" % imageId
print "=" * 50
print image.getName(), image.getDescription()
# Retrieve information about an image.
print " X:", image.getSizeX()
print " Y:", image.getSizeY()
print " Z:", image.getSizeZ()
print " C:", image.getSizeC()
print " T:", image.getSizeT()
# render the first timepoint, mid Z section
z = image.getSizeZ() / 2
t = 0
renderedImage = image.renderImage(z, t)
#renderedImage.show()               # popup (use for debug only)
renderedImage.save("test.jpg")     # save in the current folder
	
