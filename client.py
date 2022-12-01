import time

from pyhive import hive


def connect():
    return hive.Connection(
        host="localhost",
        # port=9083,
        # username="hive",
        # password="hive",
    )
    # return hive.connect("localhost")


if __name__ == "__main__":
    time.sleep(60)
    cur = connect()
    print(cur)
