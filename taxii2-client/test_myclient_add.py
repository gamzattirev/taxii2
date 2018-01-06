from taxii2client import Server
from stix2 import CustomObject, properties, TAXIICollectionSource
from taxii2client import Collection
from stix2 import Filter
import json
import sys

collection_url=sys.argv[1]
collection = Collection(collection_url,'user1','Password1')

file=sys.argv[2]
print(file)
f = open(file,'rt',encoding='utf-8')
rowdata = json.load(f)
f.close()

stix_bundle=rowdata

collection.add_objects(stix_bundle)

