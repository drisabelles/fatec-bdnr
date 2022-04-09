from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import src.connectDb as connectDb

def find_vendedores():
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivree.vendedores

  document = collection.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def find_por_id(request):
  vendedores = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.vendedores

  document = collection.find({"_id": ObjectId(vendedores["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def inserir(request):
  vendedores = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.vendedores
  collection.insert_one(vendedores)
  
  return json.dumps({
    "status": "Vendedor inserido",
    "vendedor":json.loads(json_util.dumps(vendedores))
  })
  
def delete(request):
  vendedores = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.vendedores

  try:
    collection.delete_one({"_id": ObjectId(vendedores["id"])})
    return json.dumps({"status": "Vendedor deletado"})
  except:
    return json.dumps({"message": "Erro"})


def inserir_amostra():
  bd_MercadoLivre = connectDb.connect()
  bd_MercadoLivre.vendedores.insert_many({
    "nome":"João Ferreira",
    "cnpj":"11.111.111/0001-11",
    "endereco":[{
      "cep":12257000,
      "rua":"Av.Perseu",
      "numero":70,
      "bairro":"Satélite",
      "cidade":"São José dos Campos",
      "estado":"SP"
    }],
    "contato": {
      "email":"milena.carvalho@gmail.com",
      "telefone":"",
      "celular":12978453269
    }
  })
  return jsonify(message="success")