from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import src.connectDb as connectDb

def find_produtos():
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.produtos

  document = collection.find()

  retorno = []
  for x in doc:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def find_por_id(request):
  produtos = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.produtos

  document = collection.find({"_id": ObjectId(produtos["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))
  
  return json.dumps(retorno)

def inserir(request):
  produto = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.produtos
  collection.insert_one(produtos)
  
  return json.dumps({
    "status": "Produto inserido",
    "produto":json.loads(json_util.dumps(produtos))
  })
  
def delete(request):
  produtos = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.produtos

  try:
    collection.delete_one({"_id": ObjectId(produtos["id"])})
    return json.dumps({"status": "Produto deletado"})
  except:
    return json.dumps({"message": "Erro"})


def inserir_amostra():
  bd_MercadoLivre = connectDb.connect()
  bd_MercadoLivre.produtos.insert_many({
    "titulo": "Mouse Logitec",
    "descricao":"Mouse azul e ciano logitec bluetooth",
    "precoPadrao":110,
    "precoAVista":100,
    "precoAPrazo":130,
    "vendedorID":""
  })
  return jsonify(message="success")