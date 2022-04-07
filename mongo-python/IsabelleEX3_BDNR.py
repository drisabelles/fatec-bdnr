import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb+srv://isabelle:1tfmVTT7AmeWtt0A@cluster0.brhj9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

global mydb
mydb = client.MercadoLivre

def findSort():
    #Sort
    global mydb
    mycol = mydb.usuarios
    print("\n####SORT####")
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)

def findQuery():
    #Query
    global mydb
    mycol = mydb.usuarios
    print("\n####QUERY####")
    myquery = { "nome": "Isabelle" }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def insert():
    #Insert
    global mydb
    mycol = mydb.usuarios
    print("\n####INSERT####")
    mydict = { "nome": "Diego Silva", "email":"diego.silva@gmail.com", "endereco":"jd america", "carrinho":"mouse"}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insert():
    #Insert
    global mydb
    mycol = mydb.vendedores
    print("\n####INSERT####")
    mydict = { "nome": "Rodrigo Castro", "email":"rodrigocastro@gmail.com", "endereco":"santana, são paulo"}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insert():
    #Insert
    global mydb
    mycol = mydb.produtos
    print("\n####INSERT####")
    mydict = { "nome": "Mouse", "descricao":"mouse preto logitec m535", "preco":110, "aVista":100, "aPrazo":130, "vendedor":({"nome":"Rodrigo","endereco":"santana, são paulo"})}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insert():
    #Insert
    global mydb
    mycol = mydb.compras
    print("\n####INSERT####")
    mydict = { "usuario": ({"nome":"Diego", "email":"diego.silva@gmail.com", "endereco":"jd america"}), "produto":({"nome":"mouse", "descricao":"mouse preto logitec m535", "aPrazo":130}), "vendedor":({"nome":"Rodrigo", "email":"rodrigocastro@gmail.com", "endereco":"santana, são paulo"}), "perguntas":({})}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

#main
findSort()
findQuery()
insert()