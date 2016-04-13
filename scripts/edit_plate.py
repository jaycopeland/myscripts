#
# To be run in OMERO CLI shell as follows:
#
#     # Download script to current working directory
#     omero shell --login
#     ...
#     %run -i edit_plate.py plate_id attribute value
#
import sys

from omero.gateway import omero_type

try:
    plate_id, attribute, value = sys.argv[1:]
except ValueError:
    print "Usage: %s <plate_id> <attribute> <value>"
    sys.exit(1)
plate_id = long(plate_id)

session = client.getSession()
iquery = session.getQueryService()
iupdate = session.getUpdateService()

plate = iquery.find('Plate', plate_id)
if not hasattr(plate, attribute):
    print 'Plate has no attribute %r' % (attribute)
    sys.exit(1)
setattr(plate, attribute, omero_type(value))
iupdate.saveObject(plate)
print 'Successfully set attribute %r of Plate:%d to %r' % \
        (attribute, plate_id, value)

