#!/bin/bash

cat ./scripts/start.sql | sqlite3 database.db
cat ./scripts/data.sql | sqlite3 database.db