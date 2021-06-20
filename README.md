# Web Scraping para dados de Fundos Imobiliários

Projeto criado para obter dados de Fundos Imobiliários em sites especializados e salvar no MongoDB. O projeto foi criado para compor um sistema de gerenciamento de portifólios de investimentos junto com uma [API](https://github.com/jnetocurti/patrimony-management-api) e uma aplicação [Web](https://github.com/jnetocurti/patrimony-management-web).

![pyenv](https://img.shields.io/badge/pyenv-2.0.1-blue)
![python](https://img.shields.io/badge/python-3.9.0-blue)
![scrapy](https://img.shields.io/badge/scrapy-2.5.0-blue)
![pymongo](https://img.shields.io/badge/pymongo-3.11.4-blue)
![github](https://img.shields.io/github/forks/jnetocurti/patrimony-management-web-scraping)
![github](https://img.shields.io/github/stars/jnetocurti/patrimony-management-web-scraping)
![github](https://img.shields.io/github/issues/jnetocurti/patrimony-management-web-scraping)
![github](https://img.shields.io/github/license/jnetocurti/patrimony-management-web-scraping)
[![Python application](https://github.com/jnetocurti/patrimony-management-web-scraping/actions/workflows/python-app.yml/badge.svg)](https://github.com/jnetocurti/patrimony-management-web-scraping/actions/workflows/python-app.yml)
![Codecov](https://img.shields.io/codecov/c/github/jnetocurti/patrimony-management-web-scraping)

### Tecnologias

- [Python](https://www.python.org)
- [Scrapy](https://scrapy.org/)
- [mongoDB](https://www.mongodb.com/)

### Pré-requisitos e como executar

Poderá ser utilizado o comando `make` que já possui as tarefas pré-definidas (vide: `make help`).

### Instalando o ambiente

```sh
make env-create
```

### Alterar para ambiente de desenvolvimento

```sh
make env-use-dev
```

### Alterar para ambiente de produção

```sh
make env-use-prod
```

### Executa o projeto para o atual ambiente

```sh
make start
```

### Executa os testes do projeto

```
make test
```
