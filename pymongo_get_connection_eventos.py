import os 
from pymongo import MongoClient
# LACUNA 1: Importe a classe MongoClient da biblioteca pymongo


# a classe ConnectionFailure da biblioteca pymongo.errors para tratamento de exceções
from pymongo.errors import ConnectionFailure

def get_database():
    """
    Função para estabelecer a conexão com o banco de dados MongoDB.
    Utiliza variáveis de ambiente para a string de conexão por segurança (boas práticas),
    mas possui um valor padrão para uso local (Compass).
    """
    # LACUNA 2: String de conexão. Em um ambiente real, prefira usar variáveis de ambiente (os.environ.get)


    CONNECTION_STRING = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
    
    try:
        # LACUNA 3: Crie a conexão com o cliente do MongoDB utilizando a CONNECTION_STRING
        cliente = MongoClient(CONNECTION_STRING)
        
        # Testa se a conexão foi bem sucedida (força uma requisição ao servidor)
        cliente.admin.command('ping')
        print("Conexão com o MongoDB estabelecida com sucesso!")
        
        # LACUNA 4: Retorne o banco de dados 'eventos_db' (ele será criado se não existir)
        return cliente['eventos_db']
        
    except ConnectionFailure as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None

# Bloco executado apenas se este arquivo for rodado diretamente
if __name__ == "__main__":
    dbname = get_database()
    if dbname is not None:
        print(f"Banco de dados atual: {dbname.name}")
