from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import conexaoMongo as conexaoMongo

def acharVendedores():
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.vendedor

  document = collection.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def acharPeloID(request):
  vendedor = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.vendedor

  document = collection.find({"_id": ObjectId(vendedor["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def inserir(request):
  vendedor = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.vendedor
  collection.insert_one(vendedor)
  
  return json.dumps({
    "status": "O vendedor foi inserido com sucesso!",
    "vendedor":json.loads(json_util.dumps(vendedor))
  })
  
def deleta(request):
  vendedor = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.vendedor

  try:
    collection.delete_one({"_id": ObjectId(vendedor["id"])})
    return json.dumps({"status": "O vendedor foi deletado com sucesso!"})
  except:
    return json.dumps({"message": "Ops! Alguma coisa deu errado :("})


def insereVendedor():
  bd_MercadoLivre = conexaoMongo.connect()
  bd_MercadoLivre.vendedor.insert_many({
    "nome":"Jéssica Castro",
    "cnpj":"12.345.678/0001-91",
    "email":"castrojessica@outlook.com",
    "endereco":{
      "rua":"Vilaça",
      "numero":"20",
      "estado":"SP",
      "cidade":"São José dos Campos"
    },
    "telefone":"12981105174"
  })
  return jsonify(message="success")