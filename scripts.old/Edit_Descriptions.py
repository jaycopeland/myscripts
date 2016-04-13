"""
 examples/ScriptingService/Edit_Descriptions.py

-----------------------------------------------------------------------------
  Copyright (C) 2006-2010 University of Dundee. All rights reserved.


  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  
  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

------------------------------------------------------------------------------

This script demonstrates the minimum framework of a script that can be run by the 
scripting service on an OMERO server. 
It defines a name, description and parameter list for the script. 
    
@author  Will Moore &nbsp;&nbsp;&nbsp;&nbsp;
<a href="mailto:will@lifesci.dundee.ac.uk">will@lifesci.dundee.ac.uk</a>
@version 3.0
<small>
(<b>Internal version:</b> $Revision: $Date: $)
</small>
@since 3.0-Beta4.2
 
"""

import omero
#import omero.clients
from omero.rtypes import *
import omero.scripts as scripts

import time
startTime = 0

def printDuration():
    global startTime
    if startTime == 0:
        startTime = time.time()
    print "script time = %s secs" % (time.time() - startTime)
    
def editDescriptions(session, parameterMap):
    """
    Does the main work of the script, setting Description for each Image in a Dataset
    
    @param session          The OMERO session
    @param parameterMap     A map of the input parameters
    """
    # create the services we need - NB: Be careful to only create services as necessary
    gateway = session.createGateway()
    
    datasetId = parameterMap["Dataset_ID"]      # since Dataset_ID is not optional
    
    # for optional parameters - need to define a default
    newDescription = "No description specified"  
    if "New_Description" in parameterMap:
        newDescription = parameterMap["New_Description"]
        
    dataset = gateway.getDataset(datasetId, True)   # True = get Images too
    print "Dataset:", dataset.getName().getValue()

    for image in dataset.linkedImageList():
        image.setDescription(rstring(newDescription))
        gateway.saveObject(image)
        
    # use this in Output_Message
    return dataset.getName().getValue()


if __name__ == "__main__":
    """
    The main entry point of the script, as called by the client via the scripting service, passing the required parameters. 
    """
    printDuration()
    client = scripts.client('Edit_Descriptions.py', 'Edits the descriptions for all the images in a given Dataset.', 
    scripts.Long("Dataset_ID", optional=False, description="Specifiy the Dataset by ID"),
    scripts.String("New_Description", description="The new description to set for each Image in the Dataset"),
    )
    
    session = client.getSession()
    
    try:
        # process the list of args above. Not scrictly necessary, but useful for more complex scripts
        parameterMap = {}
        for key in client.getInputKeys():
            if client.getInput(key):
                parameterMap[key] = client.getInput(key).getValue() # convert from rtype to value (String, Integer etc)
    
        # do the editing and handle the result
        datasetName = editDescriptions(session, parameterMap)
        if datasetName:
            ouputMessage = "Script Ran OK on Dataset: %s" % datasetName
        else:
            ouputMessage = "Script failed. See error message"
        
        client.setOutput("Message", rstring(ouputMessage))
    finally:
        client.closeSession()
        printDuration()
    