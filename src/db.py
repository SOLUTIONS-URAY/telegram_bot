import psycopg2
import os
import logging

from handlers import start
from dotenv import load_dotenv
from psycopg2.extras import LoggingConnection

load_dotenv()

def query(sql, paramas):
    connection = psycopg2.connect(connection_factory=LoggingConnection,
        database=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        host=os.getenv("PGHOST"),
        port=os.getenv("PGPORT")
    )
    print("dev124")
    logger = logging.getLogger(__name__)
    print("dev125")
    connection.initialize(logger)
    print("dev1264")
    cursor = connection.cursor()
    try:
        print("dev1242",sql, paramas)
        cursor.execute(sql, paramas)
        print("dev123234")

        if "SELECT" in sql:
            print("de34v124")
            return cursor.fetchall()
        else:
            connection.commit()
            return None

    except psycopg2.Error as e:
        print(f"Database error: {e}, query: {sql}, params: {paramas}")
        return None

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    main()