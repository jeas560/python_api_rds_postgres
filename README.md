# Projeto de prática em Eng. de Dados

Projeto simples como prática de engenharia de dados

## Objetivos da implementação

- [x] Extração de dados da API da `Coinmarketcap`
- [x] Utilização de variáveis de ambiente para segurança de dados sensíveis
- [x] Conversão dos dados em Dataframe Pandas
- [x] Tratamento de possíveis erros básicos ao gerar o Dataframe
- [x] Utilização de `docker compose` para containerização do banco de dados local
- [x] Testar a possibilidade de utilizar AWS RDS como banco de dados na nuvem mudando apenas o `.env`
- [x] Criação de scripts para automatização de algumas tarefas de infra (e.g. subir o docker)
- [ ] Finalizar a implementação para ser de forma recorrente
- [ ] Implementação de testes automatizados mais robustos e com cobertura adequada
- [ ] Implementação de uso de Linter
- [ ] Implementar Precommit para uma melhor manutenção
- [ ] Escrever uma documentação com cobertura adequada

## 📦 Package manager

Foi utilizado `poetry` como gerenciador de pacotes. Você pode instalar `poetry` seguindo as instruções [aqui](https://python-poetry.org/docs/#installation).

Favor **Não** utilizar `pip` ou `conda` para instalar as dependencias. Para isso, utilize o seguinte comando:

```bash
poetry install
```

### Formatação de código com `black`

Foi utilizado `black` para reformatar o código executando o seguinte comando:

```bash
black python_api_rds_postgres 
```

## 🤖 Scripts de automação

Em construção

## 🧪 Testes

Utilizaremos `pytest` para testar nosso código. Você pode executar os testes executando o seguinte comando:

```bash
poetry run pytest
```
