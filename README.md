# nutrition-report-backend

### Setup and Run
- `pip install -r requirements.txt`
- Create file `.env` with entry:
    ```
    DB_HOST=<localhost_or_remote>
    DB_PORT=5432
    DATABASE=<name_of_database>
    DB_USER=<user>
    DB_PASSWORD=<password>
    ```
- `export $(cat .env | xargs) && python app.py`