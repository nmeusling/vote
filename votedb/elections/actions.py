import sqlite3


def create_database():
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_creation_query = """
    CREATE TABLE ELECTIONS (
        Name VARCHAR(255) NOT NULL
    );
"""
    cursor.execute(table_creation_query)
    connection_obj.close()


def view_elections():
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_selection_query = """
    SELECT Name FROM ELECTIONS;
"""

    results = cursor.execute(table_selection_query)
    elections = results.fetchall()
    connection_obj.close()
    return elections


def insert():
    connection_obj = sqlite3.connect("elections.db")
    cursor = connection_obj.cursor()
    table_insertion_query = """
    INSERT INTO ELECTIONS (Name) VALUES ('Test');
    """
    cursor.execute(table_insertion_query)
    connection_obj.commit()
    connection_obj.close()
