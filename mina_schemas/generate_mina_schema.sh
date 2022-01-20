#!/bin/sh

python generate_mina_schema.py
sgqlc-codegen schema mina_schema.json mina_schema.py