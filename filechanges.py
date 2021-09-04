#!/usr/bin/env python3

import sqlite3

def create_database(dbname):
    conn = sqlite3.connect(dbname)


if __name__ == "__main__":
    dbname = 'file_changes.db'
    conn = sqlite3.connect(dbname)

