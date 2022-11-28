from pyhive import hive
import pyhs2


def connect():
    return hive.Connection(
        host="localhost",
        port=9083,
        username="hive",
        # password="hive",
    )


def alt_connect():
    with pyhs2.connect(
        host="localhost",
        port=10000,
        authMechanism="PLAIN",
        user="hive",
        password="hive",
        database="default",
    ) as conn:
        with conn.cursor() as cur:
            # Show databases
            print(cur.getDatabases())

            # Execute query
            cur.execute("select * from table")

            # Return column info from query
            print(cur.getSchema())

            # Fetch table results
            for i in cur.fetch():
                print(i)


if __name__ == "__main__":
    try:
        connect()
    except Exception:
        alt_connect()
