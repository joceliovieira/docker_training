# Treinamento Docker
Autor: Jocélio Vieira

## Objetivo
O objetivo do treinamento é demonstrar uma visão prática da tecnologia de conteinrização disponibilizada através da ferramenta Docker. Este treinamento tem como base, em grande parte, a documentação oficial do Docker.

Fonte: [_Docker Documentation - Overview_](https://docs.docker.com/get-started/overview/)


## Descrição Oficial 

"_Docker is an open platform for developing, shipping, and running applications._" \
"_Docker enables you to separate your applications from your infrastructure so you can deliver software quickly._" \
"_With Docker, you can manage your infrastructure in the same ways you manage your applications._" \
"_By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production._"


"_Docker provides the ability to package and run an application in a loosely isolated environment called a container._" \
"_Containers are lightweight and contain everything needed to run the application, so you do not need to rely on what is currently installed on the host._" \
"_You can easily share containers while you work, and be sure that everyone you share with gets the same container that works in the same way._"


## Arquitetura - Componentes básicos

<div style="text-align: center;">

![](/img/docker-architecture.svg "Arquitetura Docker")
<figcaption>
Figura 1:  Arquitetura Docker

Fonte: [_Docker Documentation - Overview_](https://docs.docker.com/get-started/overview/)
</figcaption>

</div>

### Docker 

#### Process
Def.: "_A program or command that is actually running on the computer is referred to as a process._"\
Fonte: [IBM](https://www.ibm.com/docs/en/aix/7.2?topic=processes-)

#### Daemon Process
Def.: _Daemons are processes that run unattended. __They are constantly in the background and are available at all times__. Daemons are usually started when the system starts, and they run until the system stops. A daemon process typically performs system services and is available at all times to more than one task or user. For example, the qdaemon process provides access to system resources such as printers. Another common daemon is the sendmail daemon._\
[Fonte: IBM](https://www.ibm.com/docs/en/aix/7.2?topic=processes-)

#### Docker Daemon
_The Docker daemon listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes._


### Docker Client

#### Client-Server Model
_A __client__ is a program that uses services that other programs provide. The programs that provide the services are called __servers__. The client makes a request for a service, and a server performs that service. Client programs typically handle user interactions and often request data or initiate some data modification on behalf of a user._\
Fonte: [IBM](https://www.ibm.com/docs/en/txseries/8.1.0?topic=computing-clientserver-model)

_The main role of server is to provide services and main role of client is to consume services._\
Fonte: [Medium - Simple Introduction to Client-Server Architecture Concept](https://nimesha-dilini.medium.com/simple-introduction-to-client-server-architecture-concept-7d2979bed31d)


<div style="text-align: center;">

![](/img/client-server-model.jpeg "Arquitetura Docker")
<figcaption>
Figura 1:  Arquitetura Docker

Fonte: [Medium - Simple Introduction to Client-Server Architecture Concept](https://nimesha-dilini.medium.com/simple-introduction-to-client-server-architecture-concept-7d2979bed31d)
</figcaption>

</div>

#### Docker Client

_The Docker client is the primary way that many Docker users interact with Docker._\
_When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon._

### Docker Registries

_A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default. You can even run your own private registry._\
_When you use the docker pull or docker run commands, the required images are pulled from your configured registry. When you use the docker push command, your image is pushed to your configured registry._

### Docker objects

_When you use Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects. This section is a brief overview of some of those objects._

#### Images
_An image is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization. For example, you may build an image which is based on the ubuntu image, but installs the Apache web server and your application, as well as the configuration details needed to make your application run._

_You might create your own images or you might only use those created by others and published in a registry. To build your own image, you create a Dockerfile with a simple syntax for defining the steps needed to create the image and run it. Each instruction in a Dockerfile creates a layer in the image. When you change the Dockerfile and rebuild the image, only those layers which have changed are rebuilt. This is part of what makes images so lightweight, small, and fast, when compared to other virtualization technologies._

#### Containers

_A container is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI. You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state._

_By default, a container is relatively well isolated from other containers and its host machine. You can control how isolated a container’s network, storage, or other underlying subsystems are from other containers or from the host machine._

_A container is defined by its image as well as any configuration options you provide to it when you create or start it. When a container is removed, any changes to its state that are not stored in persistent storage disappear._

Algumas características dos contêineres:

- Is a runnable instance of an image. You can create, start, stop, move, or delete a container using the DockerAPI or CLI.
- Can be run on local machines, virtual machines or deployed to the cloud.
- Is portable (can be run on any OS)
- Containers are isolated from each other and run their own software, binaries, and configurations.


### Recapitulando - Arquitetura ecossistema Docker

<div style="text-align: center;">

![](/img/docker-architecture.svg "Arquitetura Docker")
<figcaption>
Figura 2:  Arquitetura Docker

Fonte: [_Docker Documentation - Overview_](https://docs.docker.com/get-started/overview/)
</figcaption>

</div>

#### Exemplo - Fluxo de processos

The following command runs an ubuntu container, attaches interactively to your local command-line session, and runs /bin/bash.

    docker run -i -t ubuntu /bin/bash

When you run this command, the following happens (assuming you are using the default registry configuration):

1. If you do not have the ubuntu image locally, Docker pulls it from your configured registry, as though you had run docker pull ubuntu manually.
2. Docker creates a new container, as though you had run a docker container create command manually.
3. Docker allocates a read-write filesystem to the container, as its final layer. This allows a running container to create or modify files and directories in its local filesystem.
4. Docker creates a network interface to connect the container to the default network, since you did not specify any networking options. This includes assigning an IP address to the container. By default, containers can connect to external networks using the host machine’s network connection.
5. Docker starts the container and executes /bin/bash. Because the container is running interactively and attached to your terminal (due to the -i and -t flags), you can provide input using your keyboard while the output is logged to your terminal.
6. When you type exit to terminate the /bin/bash command, the container stops but is not removed. You can start it again or remove it.

## Docker Desktop
_Docker Desktop is an easy-to-install application for your Mac or Windows environment that enables you to build and share containerized applications and microservices. Docker Desktop includes Docker Engine, Docker CLI client, Docker Compose..._

[Docker Desktop Dashboard](https://docs.docker.com/desktop/dashboard/)

### Instalação
Passo a passo disponível em [Get Docker](https://docs.docker.com/get-docker/).

## Iniciando uma aplicação
Tendo em vista que as aplicações podem ser compostas por um único container ou múltiplos containers, essa seção será dividida em 2 partes.

No caso da aplicação ser composta por 2 ou mais containers, será utilizada a ferramenta Docker Compose para realizar a configuração e implementação dos diversos serviços (containers) que irão compor a aplicação final.

### Aplicação single-container
Para implementar uma aplicação simples, pode-se utilizar o próprio Docker Client, como exposto na seção anterior.

#### Comando: ___docker run___

    docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
Referência: [Documentação Oficial - docker run](https://docs.docker.com/engine/reference/commandline/run/)

The docker run command first creates a writeable container layer over the specified image, and then starts it using the specified command. That is, docker run is equivalent to the API /containers/create then /containers/(id)/start.\
A stopped container can be restarted with all its previous changes intact using docker start. See docker ps -a to view a list of all containers.

Mais um exemplo de utilização do Docker Client para 'subir' um container.

    docker run -d -p 80:80 docker/getting-started

#### Flags

    -d - run the container in detached mode (in the background)

    -p 80:80 - map port 80 of the host to port 80 in the container
    docker/getting-started - the image to use



### Aplicação multi-container
Como já fora exposto, para implementação de uma aplicação multi-container, será utilizada a ferramenta Docker Dompose.
Por sua vez, para configurar o ambiente em que esta aplicação irá ser hospedada, deve-se definir o dockerfile contendo tais informações.

Exemplo com passo a passo: [Get started with Docker Compose](https://docs.docker.com/compose/gettingstarted/)

#### Dockerfile
Ref.: [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)\
Ref.: [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)\
Def.: Docker can build images automatically by reading the instructions from a Dockerfile. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.

Docker builds images automatically by reading the instructions from a Dockerfile -- a text file that contains all commands, in order, needed to build a given image. A Dockerfile adheres to a specific format and set of instructions which you can find at Dockerfile reference.

Exemplo de um dockerfile:

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

This tells Docker to:

- Build an image starting with the Python 3.7 image.
- Set the working directory to /code.
- Set environment variables used by the flask command.
- Install gcc and other dependencies
- Copy requirements.txt and install the Python dependencies.
- Add metadata to the image to describe that the container is - listening on port 5000
- Copy the current directory . in the project to the workdir . in the - image.
- Set the default command for the container to flask run.


#### Docker Compose
Ref.: [Docker Compose Overview](https://docs.docker.com/compose/)\
Def.: Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

Etapas da utilização do Docker Compose para criação e implementação de uma aplicação multi-container:
1. Define your app’s environment with a Dockerfile so it can be reproduced anywhere.
2. Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.
3. Run docker compose up and the Docker compose command starts and runs your entire app. You can alternatively run docker-compose up using the docker-compose binary.

Exemplo de um arquivo docker-compose.yml:

```yml
version: "3" # opcional

services:
  influxdb:
    image: influxdb:latest
    container_name: influxdb
    ports: 
      - "8086:8086"
    volumes:
      - influxdb:/var/lib/influxdb
      - ./influxdb.conf:/etc/influxdb/influxdb.conf:ro
    restart: always

  grafana:
    image: grafana/grafana
    container_name: grafana
    volumes:
      - grafana-data:/var/lib/grafana
      - grafana-conf:/etc/grafana
      - grafana-logs:/var/log/grafana
    ports: 
      - "3000:3000"
    restart: always

volumes:
  influxdb:
  grafana-data:
  grafana-conf:
  grafana-logs:
```

PS.: o docker-compose.yml acima não tem relação com o dockerfile apresentado na seção anterior.

Para o exemplo do dockerfile acima (python + flask/redis), o docker-compose seria o seguinte.

```yml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:5000"
  redis:
    image: "redis:alpine"
```


Após definição do dockerfile e do docker-compose.yaml, pode-se executar o comando a seguir, responsável por criar a infraestrutura e subir os containers envolvidos.

    docker-compose up

Para parar a aplicação, utiliza-se o seguinte comando.
    
    docker-compose down