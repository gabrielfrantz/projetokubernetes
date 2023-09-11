# versão da imagem do postgresql
FROM postgres:latest

# copia tudo da pasta corrente e executa os scripts SQL na criação do banco de dados no container (create e insert)
COPY . /docker-entrypoint-initdb.d/