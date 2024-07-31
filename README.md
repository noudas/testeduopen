# Teste Duopen

## Descrição

Este projeto é uma aplicação full-stack desenvolvida para demonstrar a integração entre uma interface web React e uma API RESTful Flask, utilizando a API Pluggy para operações financeiras. A aplicação permite que os usuários insiram seus dados pessoais e aceitem termos de uso, e então esses dados são enviados para a API Pluggy para processamento.

## Objetivos

- Demonstrar a criação de uma interface web responsiva com React.
- Implementar uma API RESTful com Flask para manipulação de dados.
- Integrar a API Pluggy para realizar operações financeiras baseadas nos dados dos usuários.

## Tecnologias Utilizadas

### Frontend

- **React**: Biblioteca JavaScript para construção de interfaces de usuário.
- **Axios**: Biblioteca para fazer requisições HTTP.

### Backend

- **Flask**: Framework Python para desenvolvimento de APIs web.
- **Psycopg2**: Conector PostgreSQL para Python.
- **Requests**: Biblioteca para fazer requisições HTTP.

### Infraestrutura

- **Docker**: Ferramenta para containerização de aplicações.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional.

### API Externa

- **Pluggy API**: Serviço de fintech utilizado para operações financeiras.

## Como Executar Localmente

### Pré-requisitos

Certifique-se de ter o Node.js, Python e Docker instalados em sua máquina.

### Passo a Passo

#### Clonando o Repositório

Clone este repositório para sua máquina local.
```
git clone https://github.com/noudas/testeduopen.git 
cd testeduopen
```


#### Instalando Dependências

Navegue até o diretório do projeto e instale as dependências necessárias.

```
cd frontend npm install
```

Faça o mesmo para o backend, se necessário.

#### Iniciando o Projeto

Inicie o servidor de desenvolvimento do frontend.

```
npm start
```

No backend, utilize o Docker Compose para iniciar todos os serviços.

```
docker-compose up --build
```


## Uso da API Pluggy

O projeto integra a API Pluggy para realizar operações financeiras. Os usuários inserem seus dados pessoais através da interface web, que são então enviados para a API Pluggy através da API RESTful Flask. Para entender melhor como a API Pluggy funciona e como utilizá-la, consulte a [documentação oficial](https://docs.pluggy.ai/docs/quick-pluggy-introduction).

## Contribuição

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir um pull request com suas melhorias ou dúvidas.

