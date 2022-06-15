import src.controle.usuarioControle as usuarioControle
import src.controle.vendedorControle as vendedorControle
import src.controle.produtoControle as produtoControle
import src.controle.compraControle as compraControle
import src.controle.redisControle as redisControle



from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def test():
  jsonTest = {"status": "API Online"}
  return jsonify(jsonTest)

#--------------------------------------------------------
#Usuarios
@app.route("/usuario/insereUsuario", methods=['POST'])
@cross_origin()
def insereUsuario():
    return usuarioControle.insereUsuario()

@app.route("/usuarios", methods=['GET'])
@cross_origin()
def usuarios():
	return usuarioControle.acharUsuarios()

@app.route("/usuario", methods=['GET'])
@cross_origin()
def usuario():
	return usuarioControle.acharPeloID(request)

@app.route("/usuario/cria", methods=['POST'])
@cross_origin()
def criaUsuario():
	return usuarioControle.inserir(request)

@app.route("/usuario/deleta", methods=['DELETE'])
@cross_origin()
def deletaUsuario():
	return usuarioControle.deleta(request)

#--------------------------------------------------------
#vendedores
@app.route("/vendedores/insereVendedor", methods=['POST'])
@cross_origin()
def insereVendedor():
    return vendedorControle.insereVendedor()

@app.route("/vendedores", methods=['GET'])
@cross_origin()
def vendedores():
	return vendedorControle.acharVendedores()

@app.route("/vendedor", methods=['GET'])
@cross_origin()
def vendedor():
	return vendedorControle.acharPeloID(request)

@app.route("/vendedor/criar", methods=['POST'])
@cross_origin()
def criaVendedor():
	return vendedorControle.inserir(request)

@app.route("/vendedor/deleta", methods=['DELETE'])
@cross_origin()
def deletaVendedor():
	return vendedorControle.deleta(request)

#--------------------------------------------------------
#Produtos
@app.route("/produtos/insereProduto", methods=['POST'])
@cross_origin()
def insereProduto():
    return produtoControle.insereProduto()

@app.route("/produtos", methods=['GET'])
@cross_origin()
def produtos():
	return produtoControle.acharProdutos()

@app.route("/produto", methods=['GET'])
@cross_origin()
def produto():
	return produtoControle.acharPeloID(request)

@app.route("/produto/criar", methods=['POST'])
@cross_origin()
def criarProduto():
	return produtoControle.inserir(request)

@app.route("/produto/deleta", methods=['DELETE'])
@cross_origin()
def produto_deleta():
	return produtoControle.deleta(request)

#--------------------------------------------------------
#Compras
@app.route("/compras/insereCompras", methods=['POST'])
@cross_origin()
def insereCompras():
    return compraControle.insereCompras()

@app.route("/compras", methods=['GET'])
@cross_origin()
def compras():
	return compraControle.acharCompras()

@app.route("/compra", methods=['GET'])
@cross_origin()
def compra():
	return compraControle.achaPeloID(request)

@app.route("/compra/criar", methods=['POST'])
@cross_origin()
def compra_criar():
	return compraControle.inserir(request)

@app.route("/compra/deleta", methods=['DELETE'])
@cross_origin()
def compra_deleta():
	return compraControle.deleta(request)


# Redis
@app.route("/produto/redis/incrementarVisualizacoes", methods=['GET'])
@cross_origin()
def incrementarVisualizacoesProduto():
	return redisControle.incrementarVisualizacoesProduto(request)

@app.route("/website/redis/incrementarVisualizacoes", methods=['GET'])
@cross_origin()
def incrementarVisualizacoesPagina():
	return redisControle.incrementarVisualizacoesPagina()

@app.route("/website/redis/relatorioGeral", methods=['GET'])
@cross_origin()
def relatorioGeral():
	return redisControle.relatorioGeral()

@app.route("/redis/deletaTodasChaves", methods=['DELETE'])
@cross_origin()
def deletaTodasChaves():
	return redisControle.deletaTodasChaves()

@app.route("/redis/salvaRelatorio", methods=['POST'])
@cross_origin()
def salvaRelatorio():
	return redisControle.salvaRelatorio()




if __name__ == '__main__':
	app.run(debug=True)