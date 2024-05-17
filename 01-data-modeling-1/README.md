# Building a Data Model with PostgreSQL

Step 1 install psycopg2, using to connect with PostgreSQL
```
pip install psycopg2
```

Step 2 run docker-compose with this command
```
docker compose up
```

Step 3 run create_table.py to create tables in PostgreSQL
```
python create_tables.py
```

Step 4 run etl.py to insert data into DB
```
python etl.py
```