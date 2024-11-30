import psycopg2
import os
import db

from handlers import start

def check(referral_code, id, username):
    record = db.query('SELECT * FROM telegram_token WHERE uuid = %s AND "active" = TRUE;', (referral_code,))

    if record:
        print(f"Data retrieved for referral code {referral_code}:")
        print("debug:", record)
        api_user_id = record[0][1]
        print("debug2:", api_user_id)
        a = (str(id), username, int(record[0][1]),)
        print("debug23:", a)
        db.query('UPDATE "telegram_token" SET "active" = false WHERE "uuid" = %s', (referral_code,))
        print("debug4:")
        db.query('INSERT INTO telegram_match ("telegramId","telegramUsername","userId") VALUES %s;', (a,))
        print("debug3:", (id, username, record[0][1],))
        fullNameRecords = db.query('SELECT * FROM "user" WHERE "id" = %s;', (api_user_id,))
        print("debug5:", fullNameRecords)
        return fullNameRecords[0][1]
    else:
        print(f"No data found for referral code {referral_code}.")
        return None

if __name__ == "__main__":
    main()