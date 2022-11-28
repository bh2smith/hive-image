from pyhive import hive


def connect():
    return hive.Connection(
        host="localhost",
        port=9083,
        username="hive",
        # password="hive",
    )


if __name__ == "__main__":
    connect()
