from pymongo import MongoClient

def conecta():
  client = MongoClient("mongodb+srv://isabelle:1tfmVTT7AmeWtt0A@cluster0.brhj9.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-kgm265-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
  db_MercadoLivre = client['MercadoLivre']

  return db_MercadoLivre
