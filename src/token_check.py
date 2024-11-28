import psycopg2
import os

from handlers import start

from dotenv import load_dotenv

def main(referral_code):

    load_dotenv()

    try:
        connection = psycopg2.connect(
            database=os.getenv("PGDATABASE"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            host="localhost",
            port=os.getenv("PGPORT")
        )

        cursor = connection.cursor()

        query = "SELECT * FROM secret_token WHERE secret_token = %s;"
        cursor.execute(query, (referral_code,))

        record = cursor.fetchall()

        if record:
            print(f"Data retrieved for referral code {referral_code}:")
            api_user_id = [row[0] for row in record]
            api_user_id = api_user_id[0]
        else:
            print(f"No data found for referral code {referral_code}.")
            return None

        return api_user_id

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    main()