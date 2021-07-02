# @author       Jiawei Lu (jiaweil9@asu.edu)
# @time         2021/6/25 15:21
# @desc         [script description]


import osm2gmns as og


# quick tip: please use the latest version of osm2gmns to aviod any potential issues
#       the lateest version is 0.5.4 (6/25/2021)

# specify link types that we need with the link_type argument
#       link types that osm2gmns supports include:
#       motorway, trunk, primary, secondary, tertiary, residential,
#       service,cycleway, footway, track, unclassified

# combine short links
#       set combine as True to enable osm2gmns combine short links with the exact same attributes
#       note: alouthgh osm2gmns has this function, the number of links that will be combined is limited.

# default values for free_speed, lanes, capacity
#       some links (about 25% in the US) in osm do not have free_speed, lanes, capacity values, which may be essential for simulation or ODME
#       osm2gmns is able to assign a default value for these links acoording to their link type
#       for speed, set default_speed=True. similar for the other two fields

# to clarify the is_link field in link.csv
#       In raw OpenStreetMap datasets, each link type includes two sub-types
#       take motorway as an example. They have motoryway and motorway_link
#       In link.csv files produced by osm2gmns, the link_type of motoryway and motorway_link are both motoryway, but is_link=1 for motorway_link
#       you can check the osm wiki page for a detailed introduction about the meaning of '_link' for different types of roads
#       https://wiki.openstreetmap.org/wiki/Key:highway



net = og.getNetFromFile('L101N.osm', link_type=('motorway','trunk','primary','secondary'), POIs=True, POI_sampling_ratio=1.0,combine=True)
og.consolidateComplexIntersections(net)
og.connectPOIWithNet(net)
og.generateNodeActivityInfo(net)
og.outputNetToCSV(net, output_folder='consolidatedwPOI_partial')