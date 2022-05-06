import redis, uuid
from typing import Dict, List

sacola1 = {'usuario_id':1,'atividade_id':2,'pessoa':4,'nome':'banana','preco':2000,'data':'03 maio, 2022','imagem':'dwq.png','hora':'14:00'}
sacola2 = {'usuario_id':1,'atividade_id':3,'pessoa':2,'nome':'parasailing','preco':3000,'data':'02 maio, 2022','imagem':'asd.png','hora':'16:00'}

#conexão com o servidor do redis
r = redis.Redis(host='localhost', port=6379, db=0)

class Sacola:
    _EXPIRED_TIME = 900 # 15 minute
    
    @classmethod
    def salvarSacola(cls,**kwargs) -> Dict[str,str]:
        usuario_id = kwargs['usuario_id']
        # check if cart already exists
        for usuario_sacolas in r.scan_iter(f"sacola:{usuario_id}:*"):
            data = {index.decode('utf-8'):value.decode('utf-8') for index,value in r.hgetall(usuario_sacola).items()}
            if int(data['usuario_id']) == kwargs['usuario_id'] and int(data['atividade_id']) == kwargs['atividade_id']:
                return {'mensagem':'Item já está na sacola'}

        kwargs['rowId'] = uuid.uuid4().hex
        key = f"sacolas:{usuario_id}:{kwargs['rowId']}"
        #colocando a sacola no redis
        [r.hset(key,index,value) for index,value in kwargs.items()]
        #colocando expiração na sacola do redis
        r.expire(key,cls._EXPIRED_TIME)
        resultado = {key.decode('utf-8'):value.decode('utf-8') for key,value in r.hgetall(key).items()}
        return resultado

    @classmethod
    def sacolas(cls,usuario_id: int) -> List[Dict[str,str]]:
        resultado = []
        for usuario_sacolas in r.scan_iter(f"sacolas:{usuario_id}:*"):
            data = {index.decode('utf-8'):value.decode('utf-8') for index,value in r.hgetall(usuario_carts).items()}
            resultado.append(data)
        return resultado
    
    @classmethod
    def atualizarPessoa(cls,usuario_id: int,rowId: str, pessoa: int) -> None:
        key = f"sacolas:{usuario_id}:{rowId}"
        r.hset(key,'pessoa',pessoa)
        #resetar a expiração se o usuário estiver no redis
        r.expire(key,cls._EXPIRED_TIME)

    @classmethod
    def deletarSacola(cls,usuario_id: int, rowId: str) -> int:
        #se retornar 1 é verdadeiro e se retornar 0 é falso, o que significa que o dado não existe
        return r.delete(f"sacolas:{usuario_id}:{rowId}")
    
    @classmethod
    def deletarTodasSacolas(cls,usuario_id: int) -> None:
        [r.delete(x) for x in r.scan_iter(f"sacolas:{usuario_id}:*")]
