# Descrição do projeto de PJI "Gestão Escolar"

Este projeto está usando como base os exemplos do tutorial disponível [neste repositório](https://github.com/vijaythapa333/django-student-management-system).

Especificaçõoes e documentos estão sendo compartilhados em (diretório do google docs)[https://drive.google.com/drive/u/3/folders/0AK3SLmuocjrCUk9PVA?ths=true].

# Execução do projeto

Como terminal aberto no diretório do projeto, basta executar o comando a seguir:

```bash
python manage.py runserver
```

# Execução das migrations

Para criarmos o banco a partir do Model especificado dentro do app `escolar`, precisamos criar as migrations e depois executa-las. Os comandos a seguir, em sequência, realizam essa tarefa:

> python manage.py makemigrations

Isso irá criar os arquivos de migration dentro da pasta *escolar/migrations*. Agora executando 

> python manage.py migrate

