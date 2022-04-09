from pymongo import MongoClient

def connect():
  client = MongoClient("mongodb+srv://isabelle:1tfmVTT7AmeWtt0A@cluster0.brhj9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
  db_MercadoLivre = client['MercadoLivre']

  return db_MercadoLivre