from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import src.connectDb as connectDb

def find_compras():
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.compras

  document = collection.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def find_por_id(request):
  compras = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.compras

  document = collection.find({"_id": ObjectId(compras["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))
  
  return json.dumps(retorno)

def inserir(request):
  compras = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.compras
  collection.insert_one(compras)
  
  return json.dumps({
    "status": "Compra inserida",
    "Compras":json.loads(json_util.dumps(compras))
  })
  
def delete(request):
  compras = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.compras

  try:
    collection.delete_one({"_id": ObjectId(compras["id"])})
    return json.dumps({"status": "Compra deletada"})
  except:
    return json.dumps({"message": "Erro"})


def inserir_amostra():
  bd_MercadoLivre = connectDb.connect()
  bd_MercadoLivre.compras.insert_many({
    "usuario": {
      "nome":"Luciana Ribeiro",
      "cpf":"987.654.321-00",
      "endereco": {
        "cep":12230000,
        "rua":"Belmiro Andrade",
        "numero":200,
        "bairro":"Jd Oriental",
        "cidade":"São José dos Campos",
        "uf":"SP"
      },
      "contato": {
          "email":"luciana.ribeiro@gmail.com",
          "telefone":"",
          "celular":12981107154
      },
      "produto":[{
        "nome":"Mouse Logitec",
        "descricao":"Mouse azul e ciano logitec bluetooth",
        "precoPadrao":110,
        "precoAVista":100,
        "precoAPrazo":130,
        "vendedorID":""
      }],
      "vendedor": {
        "nome":"Milena Carvalho",
        "cnpj":"11.111.111/0001-11",
        "endereco": {
          "cep":12257000,
          "rua":"Av.Perseu",
          "numero":70,
          "bairro":"Satélite",
          "cidade":"São José dos Campos",
          "estado":"SP"
        },
        "contato": {
          "email":"milena.carvalho@gmail.com",
          "telefone":"",
          "celular":12978453269
        }
      },
        "total":100,
        "status":"pendente",
        "pagamento":"a vista"
    }
  })
  return jsonify(message="success")