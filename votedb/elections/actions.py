import sqlite3
from typing import List


def create_database():
    create_elections_table()
    create_election_options_database()


def create_election_options_database():
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_creation_query = """
    CREATE TABLE IF NOT EXISTS ELECTION_OPTIONS (
        id INTEGER PRIMARY KEY,
        election_id INTEGER NOT NULL,
        name VARCHAR(255) NOT NULL,
        FOREIGN KEY (election_id) REFERENCES ELECTIONS (id)
    );
"""
    cursor.execute(table_creation_query)
    connection_obj.close()


def create_elections_table():
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_creation_query = """
    CREATE TABLE IF NOT EXISTS ELECTIONS (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL UNIQUE
    );
"""
    cursor.execute(table_creation_query)
    connection_obj.close()


def view_elections():
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_selection_query = """
    SELECT id, name FROM ELECTIONS;
"""

    results = cursor.execute(table_selection_query)
    elections = results.fetchall()
    connection_obj.close()
    return elections


def view_election_by_name(name: str):
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_selection_query = """
    SELECT name FROM ELECTIONS WHERE name = (?);
    """
    results = cursor.execute(table_selection_query, (name,))
    election = results.fetchone()
    connection_obj.close()
    return election


def insert(election_name: str):
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_insertion_query = """
    INSERT INTO ELECTIONS (name) VALUES (?);
    """
    cursor.execute(table_insertion_query, (election_name,))
    connection_obj.commit()
    connection_obj.close()


def delete_by_name(election_name: str):
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_deletion_query = """
    DELETE FROM ELECTIONS WHERE (name) = (?);
    """
    cursor.execute(table_deletion_query, (election_name,))
    connection_obj.commit()
    connection_obj.close()


def add_options_to_election(election_name: str, options: List[str]):
    election_id = get_election_id(election_name)
    insert_options = [(election_id, option) for option in options]
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_insertion_query = """
    INSERT INTO ELECTION_OPTIONS (election_id, name) VALUES (?, ?);
    """
    cursor.executemany(table_insertion_query, insert_options)
    connection_obj.commit()
    connection_obj.close()


def view_election_options(election_name: str):
    election_id = get_election_id(election_name)
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    election_option_query = """
    SELECT * FROM ELECTION_OPTIONS WHERE election_id = (?);
    """
    results = cursor.execute(election_option_query, (election_id,))
    options = results.fetchall()
    connection_obj.close()
    return options


def get_election_id(election_name: str):
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_selection_query = """
        SELECT id FROM ELECTIONS WHERE name = (?);
        """
    results = cursor.execute(table_selection_query, (election_name,))
    election = results.fetchone()
    connection_obj.close()
    return election[0]
