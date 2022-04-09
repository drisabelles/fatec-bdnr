from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import src.connectDb as connectDb

def find_usuarios():
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.usuarios

  document = col.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def find_por_id(request):
  usuarios = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.usuarios

  document = collection.find({"_id": ObjectId(usuarios["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)
  

def inserir(request):
  usuarios = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.usuarios
  collection.insert_one(usuarios)
  
  return json.dumps({
    "status": "Usuario inserido",
    "usuario":json.loads(json_util.dumps(usuarios))
  })
  
def delete(request):
  usuarios = request.get_json()
  bd_MercadoLivre = connectDb.connect()
  collection = bd_MercadoLivre.usuarios
  print(usuarios)

  try:
    collection.delete_one({"_id": ObjectId(usuarios["id"])})
    return json.dumps({"status": "Usuario deletado"})
  except:
    return json.dumps({"message": "Erro"})


def inserir_amostra():
  bd_MercadoLivre = connectDb.connect()
  bd_MercadoLivre.usuarios.insert_many([{
    "nome":"Luciana Ribeiro",
    "cpf":"987.654.321-00",
    "endereco":[{
      "cep":12230000,
      "rua":"Belmiro Andrade",
      "numero":200,
      "bairro":"Jd Oriental",
      "cidade":"São José dos Campos",
      "uf":"SP"
    }],
    "contato": {
      "email":"luciana.ribeiro@gmail.com",
      "telefone":"",
      "celular":12981107154
    },
    "carrinho":[{
      "produto1":{
        "nome":"Tinta para carros",
        "desc":"pinta carros",
        "preco":59.99,
        "a-vista":50,
        "prazo":65.99,
        "uuid-vendedor":"6229d65857dd0e593464069b"
      }}],
    }])
  return jsonify(message="success")