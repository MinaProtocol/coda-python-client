#!/usr/bin/python3

from MinaClient import Client
from sgqlc.introspection import query
import json

MINA_EXPLORER_ENDPOINT = "https://graphql.minaexplorer.com/"

mina_client = Client(endpoint=MINA_EXPLORER_ENDPOINT)

variables = {"includeDescription": True, "includeDeprecated": False}

mina_schema = mina_client.send_any_query(query, variables=variables)

with open("mina_explorer_schema.json", "w") as f:
    json.dump(mina_schema, f, sort_keys=True, indent=2, default=str)
