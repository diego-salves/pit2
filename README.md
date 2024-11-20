# Projeto Integrador Transdisciplinar em Engenharia de Software II - Cakemania

## Documentação atualizada do PIT I para o Tutor:
[Documentação Atualizada](https://docs.google.com/document/d/13afiliTYM_gqmr_2N397unevMdqkVjIT/edit?usp=sharing&ouid=104057225532776075855&rtpof=true&sd=true)

Cakemania é um projeto de loja online de cupcakes desenvolvido para demonstrar uma aplicação full-stack usando tecnologias modernas. Este projeto inclui um banco de dados PostgreSQL, uma API backend construída com Flask e um frontend criado com React.

## Tecnologias Utilizadas

### Banco de Dados

- **PostgreSQL**: Um poderoso sistema de banco de dados objeto-relacional open source. É usado para armazenar e gerenciar os dados da aplicação.

### Backend

- **Python**: A principal linguagem de programação usada para o backend.
- **Flask**: Um framework leve para aplicações web WSGI em Python. É usado para construir a API RESTful da aplicação.
- **Flask-SQLAlchemy**: Uma extensão para Flask que adiciona suporte para SQLAlchemy, uma biblioteca de mapeamento objeto-relacional (ORM) e kit de ferramentas SQL.
- **Flask-CORS**: Uma extensão para lidar com Cross-Origin Resource Sharing (CORS), tornando possível requisições AJAX entre diferentes origens.

### Frontend

- **React**: Uma biblioteca JavaScript para construção de interfaces de usuário. É usada para criar o frontend interativo da aplicação.
- **Create React App**: Um ambiente confortável para aprender React e a melhor maneira de começar a construir uma nova aplicação de página única em React.

## Configuração do Projeto

### Configuração do Banco de Dados

1. **Instalar PostgreSQL**: Baixe e instale PostgreSQL a partir do [site oficial](https://www.postgresql.org/download/).

2. **Criar um Banco de Dados**:
    ```sh
    psql -U <seu_usuario_postgres>
    CREATE DATABASE cakemania;
    ```

3. **Criar Tabelas**: Use o script SQL fornecido na pasta `DB` para criar as tabelas necessárias. Navegue até a pasta `DB` e execute o script.
    ```sh
    psql -U <seu_usuario_postgres> -d cakemania -f DB/create_tables.sql
    ```

### Configuração do Backend

1. **Instalar Python**: Certifique-se de ter o Python instalado. Você pode baixá-lo do [site oficial](https://www.python.org/downloads/).

2. **Criar um Ambiente Virtual**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instalar Dependências**:
    ```sh
    pip install Flask psycopg2-binary Flask-SQLAlchemy Flask-CORS
    ```

4. **Criar `config.py`**: Crie um arquivo `config.py` com o seu URI do banco de dados e outras configurações.
    ```python
    SQLALCHEMY_DATABASE_URI = 'postgresql://<usuario>:<senha>@localhost/cakemania'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```

5. **Executar o Servidor Backend**:
    ```sh
    python app.py
    ```

### Configuração do Frontend

1. **Instalar Node.js**: Certifique-se de ter o Node.js instalado. Você pode baixá-lo do [site oficial](https://nodejs.org/).

2. **Criar o React App**:
    ```sh
    npx create-react-app cakemania-frontend
    cd cakemania-frontend
    ```

3. **Configurar as Chamadas de API**: Atualize seus componentes React para fazer chamadas à API do servidor backend, substituindo a rota do fetch no `App.js`:
    ```jsx
      useEffect(() => {
        const fetchProducts = async () => {
          try {
            const response = await fetch('sua-rota-aqui');
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            const data = await response.json();
            setProducts(data);
          } catch (error) {
            console.error('Failed to fetch products:', error);
          }
        };

        fetchProducts();
      }, []);
    ```

4. **Executar o Servidor Frontend**:
    ```sh
    npm start
    ```

## Como Executar o Projeto

1. **Iniciar o servidor PostgreSQL** e certificar-se de que o banco de dados `cakemania` está rodando.
2. **Criar as tabelas do banco de dados** executando o script SQL localizado na pasta `DB`.
    ```sh
    cd DB
    psql -U <seu_usuario_postgres> -d cakemania -f create_tables.sql
    ```
3. **Iniciar o servidor backend do Flask**:
    ```sh
    cd path/to/backend
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    python app.py
    ```
4. **Iniciar o servidor frontend do React**:
    ```sh
    cd path/to/cakemania-frontend
    npm start
    ```
5. Abra seu navegador e navegue até `http://localhost:3000` para ver a aplicação em ação.

## Melhorias Futuras

- Implementar autenticação e autorização de usuários.
- Adicionar funcionalidades de gerenciamento de contas de usuário.
- Melhorar a interface do usuário do frontend com mais funcionalidades e melhor design.
- Implementar funcionalidades adicionais no backend como rastreamento de pedidos, integração de pagamentos, etc.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
