include .env
export $(shell sed 's/=.*//' .env)

# text/colors
BOLD:=$(shell tput bold)
RESET:=$(shell tput sgr0)
GREEN:=$(shell tput setaf 2)

# messages
SUCCESS:=$(GREEN)OK$(RESET)

.PHONY: help

help:
	@echo ""
	@echo "  $(BOLD)$(GREEN)Comandos disponíveis$(RESET)"
	@echo ""
	@echo "    $(BOLD)clear$(RESET): limpa arquivos temporários "
	@echo "    $(BOLD)env-create$(RESET): cria o ambiente virtual "
	@echo "    $(BOLD)env-destroy$(RESET): destrói o ambiente virtual "
	@echo "    $(BOLD)env-use-dev$(RESET): altera para ambiente de desenvolvimento "
	@echo "    $(BOLD)env-use-prod$(RESET): altera para ambiente de produção "
	@echo "    $(BOLD)start$(RESET): executa o projeto para o ambiente atual "
	@echo "    $(BOLD)test$(RESET): executa os testes do projeto "
	@echo "    $(BOLD)flake8$(RESET): executa o utilitário flake8 "
	@echo "    $(BOLD)isort$(RESET): executa o utilitário isort "
	@echo ""

clear:
	@printf "Limpando arquivos temporários... "
	@rm -rfd *.egg-info
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.log' -delete
	@echo "$(SUCCESS)"

env-destroy: clear
	@printf "Destruindo o ambiente ... "
	@rm -rfd venv
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.log' -delete
	@echo "$(SUCCESS)"

env-create:
	@printf "Criando o ambiente ... "
	@echo ""
	@pyenv local 3.9.0
	@python -m venv venv
	@printf "Atualizando o pip... "
	@pip install -q -U pip
	@echo ""
	@printf "Instalando as dependências... "
	@venv/bin/pip install -q --no-cache-dir -r requirements/dev.txt
	@echo ""
	@echo "============================================"
	@echo "Tudo pronto para o desenvolvimento"
	@echo ""
	@echo "Digite para ativar o ambiente: "
	@echo ""
	@echo "source venv/bin/activate"
	@echo "============================================"
	@printf "$(SUCCESS)"
	@echo ""

env-use-dev:
	@echo "switching to DEV..."
	@cp .env.dev .env

env-use-prod:
	@echo "switching to Prod..."
	@cp .env.prod .env

start:
	@venv/bin/scrapy runspider ./project/spiders/fundsexplorer.py

test:
	@venv/bin/pytest --cache-clear --cov=project

flake8:
	@venv/bin/flake8 --exclude=./project/settings.py --show-source ./project

isort:
	@venv/bin/isort ./project
