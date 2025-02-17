import redis
import mysqlDump

redis_client = redis.Redis(host='localhost', port=6379, db=0)
 
data = mysqlDump.getAllPlayers()

for x in data:
    n,h,w = x
    redis_client.lpush(n,h)
    redis_client.lpush(n,w)
