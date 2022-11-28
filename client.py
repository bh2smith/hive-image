from pyhive import hive


def connect():
    # return hive.Connection(
    #     host="localhost",
    #     port=9083,
    #     username="hive",
    #     # password="hive",
    # )
    return hive.connect("localhost").cursor()


if __name__ == "__main__":
    cur = connect()
    print(cur)
