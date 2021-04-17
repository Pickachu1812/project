import psycopg2

def main():
    connect_string = "user='postgres' password='postgrespassword' host='postgres' port='5432' dbname='postgres'"
    with psycopg2.connect(connect_string) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM test")
            row = cursor.fetchone()[0]
            result = {"response":row}
            return result

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns,row))
        for row in
        cursor.fetchall()
        ]

if __name__ == "__main__":
    main()

