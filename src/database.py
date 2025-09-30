import sqlite3
from sqlite3 import Error

DB_FILE = "data/news_data.db"

# Function to create a databse connection to the sqlite3 database.
def create_connection(): 
    conn=None
    try:
        conn=sqlite3.connect(DB_FILE)
        return conn
    except Error as e:
        print(e)
    
    return conn

# Function to create the articles table
def create_table(conn):
    try:
        sql_create_articles_table = """
        CREATE TABLE IF NOT EXISTS articles(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_name TEXT,
            author TEXT,
            title TEXT NOT NULL,
            description TEXT,
            url TEXT NOT NULL UNIQUE,
            published_at TEXT,
            content TEXT,
            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_articles_table)
        conn.commit()
    except Error as e:
        print(f"Error creating table: {e}")

# Function to insert data into the database
def insert_article(conn, article):
    """Insert a new article into the articles table, ignoring duplicates."""
    sql = '''INSERT OR IGNORE INTO articles(source_name, author, title, description, url, published_at, content)
             VALUES(?,?,?,?,?,?,?)'''
    cursor = conn.cursor()
    try:
        article_data = (
            article.get('source', {}).get('name'),
            article.get('author'),
            article.get('title'),
            article.get('description'),
            article.get('url'),
            article.get('publishedAt'),
            article.get('content')
        )
        cursor.execute(sql, article_data)
    except Error as e:
        print(f"Error inserting article {article.get('url')}: {e}")
    


