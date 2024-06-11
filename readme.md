# Gender

## Guia

### "src" -> backend + banco de dados

-   "main" -> Execução do código em si, aonde estão as rotas

-   "services" -> Lugar aonde contém as regras de negócio

-   "repositories" -> Tudo que vá manipular diretamente o banco de dados

-   "config" -> Conexão com o banco de dados

-   "database.sqlite" -> Banco de Dados

## Organização

-   Imports -> Imports builtins separados por enter de imports próprios do projeto

-   Ordem das pastas -> Arquivo main chama a pasta service (onde tem as regras de negócio) que chama a pasta repositories (interação com o banco de dados) que chama a pasta config para conexão com o banco.

- Funções -> snake_case

- Classes -> PascalCase

## Observações

-   Para você que vai dar um clone no projeto, só tem como visualizar o banco de dados se baixar a extensão "SQLite Viwer"

- "uvicorn main:app --reload" comando para rodar o server