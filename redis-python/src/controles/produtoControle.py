from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import conexaoMongo as conexaoMongo

def acharProdutos():
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.produto

  document = collection.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def acharPeloID(request):
  produto = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.produto

  document = collection.find({"_id": ObjectId(produto["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))
  
  return json.dumps(retorno)

def inserir(request):
  produto = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.produto
  collection.insert_one(produto)
  
  return json.dumps({
    "status": "O produto foi inserido com sucesso! :)",
    "produto":json.loads(json_util.dumps(produto))
  })
  
def deleta(request):
  produto = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.produto

  try:
    collection.delete_one({"_id": ObjectId(produto["id"])})
    return json.dumps({"status": "O produto foi deletado!"})
  except:
    return json.dumps({"message": "Ops! Ocorreu um erro :("})


def insereCompra():
  bd_MercadoLivre = conexaoMongo.connect()
  bd_MercadoLivre.produto.insert_many({
    "nome": "Shampoo Truss",
    "descricao":"shampoo para cabelos com raizes oleosas e pontas secas",
    "preco":89.99,
    "a-vista":69,
    "prazo":94.60,
    "uuid-vendedor":"6229d65857dd0e593464069b",
    "pagamento":"a-vista",
    "status":"pago"
  },
  {
    "nome": "Condicionador Truss",
    "descricao":"condicionador para cabelos com raizes oleosas e pontas secas",
    "preco":87.99,
    "a-vista":67,
    "prazo":92.60,
    "uuid-vendedor":"6229d65857dd0e593464069b",
    "pagamento":"a-vista",
    "status":"pago"
  })
  return jsonify(message="sucess")