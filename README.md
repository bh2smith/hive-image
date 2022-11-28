# hive-image
A sample Containerized Hive Instance

Initial Commit is taken from this excellent [Medium article](https://hshirodkar.medium.com/apache-hive-on-docker-4d7280ac6f8e)

## Installation & Run Locally

```sh
git clone git@github.com:bh2smith/hive-image.git
```

```sh
cd hive-image
docker-compose up
```

### Test out instance

```sh
docker exec -it hive-server /bin/bash

$ cd ../employee
$ hive -f employee_table.hql
$ hadoop fs -put employee.csv
```
