#!/usr/bin/python3

from MinaClient import Client
from sgqlc.introspection import query
import json

mina_client = Client()

variables = {"includeDescription": True, "includeDeprecated": False}

mina_schema = mina_client.send_any_query(query, variables=variables)

with open("mina_schema.json", "w") as f:
    json.dump(mina_schema, f, sort_keys=True, indent=2, default=str)
