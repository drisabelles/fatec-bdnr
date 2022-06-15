from datetime import date
import simplejson as json
from bson import json_util, ObjectId

import conexaoRedis as conexaoRedis
import conexaoMongo as conexaoMongo
import src.utils.dias_do_mes as dias_do_mes

cursor = conexaoRedis.connect()
bd_MercadoLivre = conexaoMongo.connect()

hoje = date.today()

hojeSTRING = hoje.strftime("%d/%m/%Y")


def incrementarVisualizacoesProdutos(request):
    collection = bd_MercadoLivre.produto

    produto = request.get_json()
    try:
        document = collection.find({"_id": ObjectId(produto["id"])})
        for x in document:
            retorno = json.loads(json_util.dumps(x))

        cursor.incr(f'produto:{produto["id"]}:{hojeSTRING}:views_dia')
        cursor.incr(f'produto:{produto["id"]}:views_total')
        return json.dumps({
            "produto": retorno,
            "visualizacoesHOJE": {
                "data_hoje": hojeSTRING,
                "visualizacoesDIA": int(cursor.get(f'produto:{produto["id"]}:{hojeSTRING}:visualizacoesDIA')),
            },
            "vizualizacoesTOTAL": int(cursor.get(f'produto:{produto["id"]}:vizualizacoesTOTAL'))
        })

    except:
        return json.dumps({
            "message": "Ops! Alguma coisa deu errado :("
        })


def visualizacoesPAGINA():
    cursor.incr(f'pagina:{hojeSTRING}:visualizacoesDIA')
    cursor.incr(f'pagina:visualizacoesTOTAL')
    return json.dumps({
        "visualizacoesTOTAL": int(cursor.get(f'pagina:visualizacoesTOTAL')),
        "visualizacoesHOJE": {
            "data_hoje": hojeSTRING,
            "vizualizacoesQNT": int(cursor.get(f'pagina:{hojeSTRING}:visualizacoesDIA'))
        }
    })


def relatorioGeral():

    listagemVisualizacoesDia = []
    contadorVisualizacoesMensal = 0
    for dia in dias_do_mes.dias_do_mes():
        if (cursor.get(f'pagina:{dia}:visualizacoesDIA')):
            listagemVisualizacoesDia.append({
                "dia": dia,
                "visualizacoesDIA": int(cursor.get(f'pagina:{dia}:visualizacoesDIA'))
            })
            contadorVisualizacoesMensal += int(
                cursor.get(f'pagina:{dia}:visualizacoesDIA'))
        else:
            listagemVisualizacoesDia.append({
                "dia": dia,
                "visualizacoesDIA": 0
            })

    return json.dumps({
        "visualizacoesTOTAL": int(cursor.get(f'pagina:visualizacoesTOTAL')),
        "visualizacoesMENSAL": contadorVisualizacoesMensal,
        "listagemVisualizacoesDia": listagemVisualizacoesDia
    })


def salvaRelatorio():
    try:
        hoje = date.today()
        hojeSTRING = hoje.strftime("%d/%m/%Y")

        relatorio = bd_MercadoLivre.relatorio

        relatorioSalvo = {
            "backup_dia": hojeSTRING,
            "dados": json.loads(relatorioGeral())
        }

        print(relatorioSalvo)

        relatorio.insert_one(relatorioSalvo)

        return json.dumps({"message": "O relatório foi salvo com sucesso! :)"})

    except:
        return json.dumps({"message": "Ops! Algo deu errado :("})


def deletaTodasChaves():
    cursor.flushall()

    return json.dumps({
        "message": "Todas as chaves foram deletadas com sucesso!"
    })
