# NewsRAG
## Project Structure
```
news-summarizer-project/
│
├── .gitignore               # Specifies intentionally untracked files to ignore
├── .env                     # Stores secret keys (API keys, etc.). DO NOT commit to Git.
├── README.md                # Project overview, setup, and usage instructions.
├── requirements.txt         # Project dependencies for pip.
│
├── app.py                   # Main entry point for the Streamlit web application 
├── scheduler.py             # Runs the background pipeline on a schedule (e.g., every 10 mins)
│
├── data/                    # Directory for data storage
│   └── news_data.db         # SQLite database to store articles and summaries.
│
├── notebooks/               # For experiments and exploratory data analysis (EDA).
│   └── data_exploration.ipynb # Jupyter notebook for EDA.
│
└── src/                     # Source code directory for the core logic.
    │
    ├── __init__.py          # Makes 'src' a Python package.
    │
    ├── config.py            # Loads configuration from .env and sets constants.
    ├── database.py          # Handles all database connections and queries.
    ├── pipeline.py          # Orchestrates the end-to-end workflow (ingest -> process -> summarize).
    │
    ├── ingestion/           # Module for fetching data from external sources.
    │   ├── __init__.py
    │   └── fetchers.py      # Functions to get data from NewsAPI, RSS feeds, etc.
    │
    ├── processing/          # Module for cleaning and preparing text data.
    │   ├── __init__.py
    │   └── text_processor.py # Functions for text cleaning, language detection.
    │
    └── summarizer/          # Module for the core AI summarization logic.
        ├── __init__.py
        └── generator.py     # Implements the RAG pipeline and text generation with the model.
```