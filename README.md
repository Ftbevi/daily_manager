# Daily Manager - Backend

## Objetivo
Projeto de Controle de Finanças Pessoais.

## Ferramentas do Ambiente de Desenvolvimento.
. Cointaneirazação: Docker e Docker-Compose.
. Control Settings: [Python-decouple](https://github.com/henriquebastos/python-decouple) e arquivo .env.
. Dependency Manager: [Poetry](https://python-poetry.org/).

## Executar o Projeto.
1. Realizar clone da aplicação através do link. O comando também irá renomear a pasta para server.
~~~bash
git clone https://github.com/Ftbevi/daily_manager.git server
~~~
2. Entrar na pasta server e se certificar que esta na branch master.
~~~bash
cd server && git status
~~~
3. Dentro da pasta server executar o docker-compose para que ele crie e execute a aplicação.
~~~bash
docker-compose -f ".docker/docker-compose.yml" up -d --build
~~~
4. Execute as migrações.
~~~bash
docker-compose exec dailymanager python manage.py makemigrations
docker-compose exec dailymanager python manage.py migrate
~~~
4. Execute a criação de usuário.
~~~bash
docker-compose exec dailymanager python manage.py createsuperuser
~~~
5. Irá necessitar adicionar o usuário, email e senha. Após isso esta disponivel o acesso via seu endereço local **127.0.0.1:8000** ou **localhost:8000**.