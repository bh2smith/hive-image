from pyhive import hive


def connect():
    return hive.Connection(
        host="jdbc:postgresql://hive-metastore-postgresql/metastore",
        port=9083,
        username="hive",
        # password="hive",
    )


if __name__ == "__main__":
    connect()
