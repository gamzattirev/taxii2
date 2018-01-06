from taxii2client import Server
from stix2 import CustomObject, properties, TAXIICollectionSource
from taxii2client import Collection
from stix2 import Filter
import sys

discovery_url=sys.argv[1]
poll_url=sys.argv[2]

#descovery
server = Server(discovery_url,'user1','Password1')
print(server.title)

#poll
collection = Collection(poll_url,'user1','Password1')
tc_source = TAXIICollectionSource(collection)

f1 = Filter("type","=", "indicator")
indicators = tc_source.query([f1])
for indicator in indicators:
    print(indicator)


