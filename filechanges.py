#!/usr/bin/env python3

import sqlite3
import sys
import os

def create_database(dbname):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        print(f"Connection is established: {dbname}")
    except sqlite3.Error:
        print(sqlite3.Error)
    finally:
        conn.close()

def query_database(dbname):
    

if __name__ == "__main__":
    dbname = 'file_changes.db'
    create_database(dbname)
    query_database(dbname)
