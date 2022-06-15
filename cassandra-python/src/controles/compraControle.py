from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import conexaoMongo as conexaoMongo

def acharCompras():
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.Compra

  document = collection.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def acharPeloID(request):
  compra = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.compra

  document = collection.find({"_id": ObjectId(compra["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))
  
  return json.dumps(retorno)

def inserir(request):
  compra = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.compra
  collection.insert_one(compra)
  
  return json.dumps({
    "status": "A compra foi inserida com sucesso! :)",
    "Compra":json.loads(json_util.dumps(compra))
  })
  
def deleta(request):
  compra = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.compra

  try:
    collection.delete_one({"_id": ObjectId(compra["id"])})
    return json.dumps({"status": "A compra foi deletada!"})
  except:
    return json.dumps({"message": "Ops! Algo deu errado :("})


def insereCompra():
  bd_MercadoLivre = conexaoMongo.connect()
  bd_MercadoLivre.compra.insert_many({
    "usuario": {
      "nome":"Isabelle Dias",
      "endereco": {
        "rua":"Benedicto Rezende de Souza",
        "numero":750,
        "estado":"SP",
        "cidade":"São José dos Campos"
      },
      "produto":[{
        "nome":"Shampoo Truss",
        "descricao":"shampoo para cabelos com raizes oleosas e pontas secas",
        "preco":89.99,
        "a-vista":69,
        "prazo":94.60,
        "uuid-vendedor":"6229d65857dd0e593464069b"
      }],
      "vendedor": {
        "nome":"Jéssica Castro",
        "endereco": {
          "rua":"Vilaça",
          "numero":20,
          "estado":"SP",
          "cidade":"São José dos Campos"
          }
        },
        "total":69,
        "status":"pago",
        "pagamento":"a vista"
    }
  })
  return jsonify(message="sucess")