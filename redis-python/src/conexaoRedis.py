import redis

def conecta():
  redisConexao = redis.Redis(
    host='localhost',
    port='18380',
    password='123456'
  )

  return redisConexao