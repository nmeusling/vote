import sqlite3


def create_database():
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
