from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import conexaoMongo as conexaoMongo

def acharUsuarios():
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.usuario

  document = collection.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def achaPeloID(request):
  usuario = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.usuario

  document = collection.find({"_id": ObjectId(usuario["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)
  

def inserir(request):
  usuario = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.usuario
  collection.insert_one(usuario)
  
  return json.dumps({
    "status": "O usuário foi inserido com sucesso!",
    "usuario":json.loads(json_util.dumps(usuario))
  })
  
def deleta(request):
  usuario = request.get_json()
  bd_MercadoLivre = conexaoMongo.connect()
  collection = bd_MercadoLivre.usuario
  print(usuario)

  try:
    collection.delete_one({"_id": ObjectId(usuario["id"])})
    return json.dumps({"status": "O usuário foi deletado com sucesso!"})
  except:
    return json.dumps({"message": "Ops! Alguma coisa deu errado :("})


def insereUsuario():
  bd_MercadoLivre = conexaoMongo.connect()
  bd_MercadoLivre.usuario.insert_many([{
    "nome":"Isabelle Dias Ribeiro Silva",
    "cpf":"123.456.789-10",
    "endereco":{
      "rua":"Benedicto Rezende de Souza",
      "numero":750,
      "estado":"SP",
      "cidade":"São José dos Campos"
    },
    "carrinho":[{
      "produto1":{
        "nome":"Shampoo Truss",
        "desc":"shampoo para cabelos com raizes oleosas e pontas secas",
        "preco":89.99,
        "a-vista":69,
        "prazo":94.60,
        "uuid-vendedor":"6229d65857dd0e593464069b"
      },
      "produto2":{
        "nome":"Condicionador Truss",
        "desc":"condicionador para cabelos com raizes oleosas e pontas secas",
        "preco":87.99,
        "a-vista":67,
        "prazo":92.60,
        "uuid-vendedor":"6229d65857dd0e593464069b"
      }}],
      "email":"drisabelles@outlook.com",
      "telefone":"12982629247"
    }])
  return jsonify(message="success")