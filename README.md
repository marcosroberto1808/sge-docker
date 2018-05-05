Docker para aplicações python3.4 com imagem django-nginx-uwsgi-centos7
=================================

Arquivo dockerfile com alguns shellscripts para rodar uma app Django , combinados com Nginx, uWsgi e usando um Centos 7.x container.

Uso
-----

Para criar a imagem `centos7-dpge-python3`, execute o comando a seguir na pasta do projeto:

        docker build -t centos7-dpge-python3 .

        ou com a tag da versao:

        docker build -t centos7-dpge-python3:latest .

        ou com argumentos requeridos:

        docker build -t teste-app --build-arg AMBIENTE=homolog --build-arg APPNAME=sge --build-arg DB_HOST=192.168.0.199 --build-arg DB_NAME=marcos_db --build-arg DB_USER=sge --build-arg DB_PASS=123456 --build-arg ROOT_DOMAIN=defensoria.ce.def.br .

Para carregar a imagem e associar a portas externas:

        docker run -d -p 8080:8080 --name=APP_ALIAS centos7-dpge-python3
        
        ou com múltiplas portas:

        docker run -h APP_ALIAS -d -p 8080:8080 -p 422:22 --name=APP_ALIAS centos7-dpge-python3

Verificar os logs da aplicacao:

        
        docker logs <CONTAINER_ID> ou APP_ALIAS

        ou

        nginx e uWsgi logs:
        docker exec -it APP_ALIAS tail -f /PATH_APP_LOGS/error.log
        docker exec -it APP_ALIAS tail -f /PATH_APP_LOGS/access.log
        docker exec -it APP_ALIAS tail -f /PATH_APP_LOGS/uwsgi.log


Acessar o terminal do container diretamente com o comando abaixo:

        docker exec -it APP_ALIAS bash

Apagar containers:

        containers parados:
        docker rm @(docker ps -aq)

        todas as imagems:
        docker rmi @(docker images -aq)

Comandos mais usados:

        docker build -t centos7-dpge-python3 .
        docker run -d -p 8080:8080 -p 422:22 --name=APP_ALIAS centos7-dpge-python3

        Apagar os containers parados e todas as imagems:
        
        docker rm @(docker ps -aq) ; docker rmi @(docker images -aq)

        Listar containers parados e todas as imagens:

        docker ps -a ; docker images

        Parar o container APP_ALIAS e depois apagar, rebuild da imagem e iniciar novamente o container APP_ALIAS :
        
        docker stop APP_ALIAS ; docker rm APP_ALIAS ; docker build -t centos7-dpge-python3 . ; docker run -h APP_ALIAS -d -p 8080:8080 -p 422:22 --name=APP_ALIAS centos7-dpge-python3

