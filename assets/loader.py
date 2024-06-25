import pandas as pd
import json
from pymongo import MongoClient
import urllib.parse
import os

username = urllib.parse.quote_plus(os.getenv('USERNAME'))
password = urllib.parse.quote_plus(os.getenv('PASSWORD'))
host = os.getenv('DOCDB_ENDPOINT')

client = MongoClient('mongodb://%s:%s@%s' % (username, password, host), ssl=True, retryWrites=False, tlsCAFile='global-bundle.pem')
db = client['productreviewdb']
coll = db['productreviews']

print("retrieving review sample data")
df = pd.read_csv (r'https://aws-blogs-artifacts-public.s3.amazonaws.com/artifacts/DBBLOG-3344/sample-reviews.csv', compression='infer', lineterminator='\n', delimiter=",")
records = df.to_dict(orient='records')

print("\nsending to DocumentDB host " + host)
i = 0
for item in records:
    i += 1
    print("%s. review ID: %s \n" % (i, item["review_id"]))
    coll.insert_one(item)