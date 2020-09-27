# Relatórios Médicos

## Iniciando o sistema

Para se iniciar o sistema, devem ser executados os seguintes comandos no diretório raiz da aplicação:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runscript autoinsert
python manage.py runserver
```

Esses comandos irão instalar as bibliotecas, criar o banco de dados e iniciar a aplicação que, por padrão será executada na seguinte URL:

```
http://127.0.0.1:8000/
```

OBS.: Iremos considerar essa URL padrão, mas, para alterá-la, pode-se definir outro IP, com o seguinte comando:

```
python manage.py runserver [IP]:[PORTA]
```

## Verificando Relatórios

Para exibir os relatórios médicos, basta acessar a seguinte URL:

```
http://127.0.0.1:8000/
```

E, para acessar a página dos relatórios pelo Heroku, deve-se acessar a seguinte URL:

```
https://relatorios-consultas.herokuapp.com/
```