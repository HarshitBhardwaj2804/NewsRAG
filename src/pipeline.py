from src.ingestion.fetchers import fetch_news
from src.database import create_connection, create_table, insert_article

"""
File workflow:
    Executes the full ingestion pipeline:
    1. Fetches data from NewsAPI.
    2. Stores the articles in the SQLite database.
"""

def run_ingestion_pipeline():
    print("Starting ingestion pipeline...")

    conn=create_connection()

    if conn is not None:
        # 1. Creating table
        create_table(conn=conn)

        # 2. Fetching articles from newApi.
        articles = fetch_news(topic="generative AI", page_size=50)

        # 3. Insert articles into the table
        if articles:
            with conn:
                for article in articles:
                    insert_article(conn=conn, article=article)
            
            print(f"Pipeline finished. Inserted/Updated{len(articles)} articles.")
        else:
            print("No articles feteched. Pipeline finished.")
        conn.close()
    else:
        print("Error! connection failed.")

if __name__ == "__main__":
    run_ingestion_pipeline()