"""
processing package — CSV ingestion and data pipeline.

Responsible for reading, cleaning, normalising, and categorising
raw bank transaction CSV data before it reaches the feature layer.

Modules:
    csv_parser          Read and validate raw CSV files.
    normaliser          Standardise column names, date formats, and amounts.
    categoriser         Assign spending categories to transactions.
    pipeline            Orchestrate parser → normaliser → categoriser flow.
"""
