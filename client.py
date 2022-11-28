from pyhive import hive


def connect():
    return hive.Connection(
        host="jdbc:postgresql://hive-metastore/metastore",
        port=10000,
        username="hive",
        # password="hive",
    )


if __name__ == "__main__":
    connect()
