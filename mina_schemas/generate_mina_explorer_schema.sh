#!/bin/sh

python generate_mina_explorer_schema.py
sgqlc-codegen schema mina_explorer_schema.json mina_explorer_schema.py