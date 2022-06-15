from datetime import date
import conexaoCassandra as conexaoCassandra
import json
import uuid

cursor = conexaoCassandra.connect()


def show():
    isa_uuid = str(uuid.uuid4())
    cursor.create(path=isa_uuid, document={
        "first_name": "Isabelle",
        "last_name": "Ribeiro",
    })

    return json.dumps({"hasError": False, "Message": "Tudo ok."})
