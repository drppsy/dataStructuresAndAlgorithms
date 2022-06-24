import redis
import random

# 新建一个连接池
pool = redis.ConnectionPool(host='r-uf697ainqzydpprbeypd.redis.rds.aliyuncs.com', password='ESsSjAztJr9guph4')
r = redis.Redis(connection_pool=pool)


alist = [{"uid":51232302, "isSignUp": 1}, {"uid":51232403, "isSignUp": 1}]


for i in range(5):
    rand_num = random.randint(1,5)
    i_json={"uid":51232300+i, "isSignUp": rand_num}
    alist.append(i_json)

for item in alist:
    r.hset('2021-08-26-4', item.get("uid"), item.get("isSignUp"))

# r.hgetall('2021-08-26-0')
