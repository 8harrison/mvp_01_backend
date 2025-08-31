# API de Gestão Financeira

## Descrição do Projeto

A API de Gestão Financeira é uma aplicação backend desenvolvida em Flask que permite gerenciar movimentações financeiras e usuários. A API oferece endpoints para adicionar, visualizar, atualizar e excluir movimentações, além de funcionalidades de autenticação e registro de usuários.

## Funcionalidades Principais

- **Gestão de Movimentações**: CRUD completo para movimentações financeiras
- **Autenticação de Usuários**: Sistema de registro e login de usuários
- **Documentação Interativa**: Documentação automática com Swagger, Redoc e RaptDoc
- **Validação de Dados**: Schemas Pydantic para validação de entrada e saída de dados

## Tecnologias Utilizadas

- Python 3.12
- Flask
- SQLAlchemy (ORM)
- Pydantic (validação de dados)
- OpenAPI (documentação)

## Instalação e Configuração

### Pré-requisitos

- Python 3.12 ou superior
- pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)

### Configuração do Ambiente

1. **Clone o repositório** (se aplicável):
```bash
git clone <url-do-repositorio>
cd mvp_api_gestao_financeira
```

2. **Crie um ambiente virtual**:
```bash
# Linux/Mac
python3 -m venv env

# Windows
python -m venv env
```

3. **Ative o ambiente virtual**:
```bash
# Linux/Mac
source env/bin/activate

# Windows
env\Scripts\activate
```

4. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

### Scripts de Automação

O projeto inclui scripts para facilitar a configuração e execução:

**Setup (configuração inicial)**:
```bash
source setup.sh
```
*Este script cria o ambiente virtual, ativa-o e instala as dependências.*

**Inicialização da aplicação**:
```bash
source start.sh
```
*Este script ativa o ambiente virtual e inicia o servidor Flask.*

### Execução Manual

Caso prefira executar manualmente:

1. **Ative o ambiente virtual**:
```bash
source env/bin/activate
```

2. **Execute a aplicação**:
```bash
flask run --host 0.0.0.0 --port 5000 --reload
```

## Estrutura da API

### Endpoints Principais

#### Documentação
- **GET** `/` - Redireciona para a página de seleção de documentação (Swagger, Redoc ou RaptDoc)

#### Movimentações
- **POST** `/adicionar_movimentacao` - Adiciona uma nova movimentação
- **PUT** `/atualizar_movimentacao` - Atualiza uma movimentação existente
- **DELETE** `/excluir_movimentacao` - Remove uma movimentação
- **GET** `/listar_movimentacoes` - Lista todas as movimentações

#### Usuários
- **POST** `/autenticar_usuario` - Autentica um usuário
- **POST** `/registrar_usuario` - Registra um novo usuário

## Modelos de Dados

### Movimentação
- `id`: Identificador único (Integer)
- `valor`: Valor da movimentação (Float)
- `tipo`: Tipo da movimentação (Enum: ENTRADA/SAIDA)
- `data_movimentacao`: Data e hora da movimentação (DateTime)
- `categoria`: Categoria da movimentação (String)
- `descricao`: Descrição adicional (String, opcional)
- `contraparte`: Contraparte da movimentação (String, opcional)
- `usuario_id`: ID do usuário associado (Integer)

### Usuário
- `usuario_id`: Identificador único (Integer)
- `username`: Nome de usuário (String)
- `senha`: Senha criptografada (String)
- `saldo`: Saldo atual do usuário (Float)
- `ultimo_calculo`: Data do último cálculo de saldo (DateTime)
- `created_at`: Data de criação do usuário (DateTime)

## Exemplos de Uso

### Adicionar uma movimentação
```bash
curl -X POST http://localhost:5000/adicionar_movimentacao \
  -H "Content-Type: application/json" \
  -d '{
    "valor": 150.00,
    "tipo": "SAIDA",
    "data_movimentacao": "18/08/2025 22:30",
    "categoria": "Alimentação",
    "descricao": "Lanche com a familia",
    "contraparte": "BurgerKing",
    "usuario_id": 1
  }'
```

### Autenticar um usuário
```bash
curl -X POST http://localhost:5000/autenticar_usuario \
  -H "Content-Type: application/json" \
  -d '{
    "username": "Teste",
    "senha": "123456"
  }'
```

## Documentação da API

A API inclui documentação interativa automaticamente gerada. Após iniciar o servidor, acesse:

- **Swagger UI**: http://localhost:5000/openapi/swagger
- **Redoc**: http://localhost:5000/openapi/redoc
- **RaptDoc**: http://localhost:5000/openapi/rapidoc

## Estrutura do Projeto

```
mvp_api_gestao_financeira/
├── env/                 # Ambiente virtual (gerado)
├── models/              # Modelos de dados
├── schemas/             # Schemas Pydantic
├── services/            # Lógica de negócio
├── app.py               # Aplicação principal
├── requirements.txt     # Dependências do projeto
├── setup.sh            # Script de configuração
├── start.sh            # Script de inicialização
└── README.md           # Este arquivo
```

## Troubleshooting

### Problemas Comuns

1. **Erro de porta em uso**: 
   - Verifique se a porta 5000 está livre ou altere a porta no comando de execução

2. **Erro de dependências**:
   - Certifique-se de que todas as dependências foram instaladas corretamente
   - Execute `pip install -r requirements.txt` novamente

3. **Problemas com o ambiente virtual**:
   - Delete a pasta `env/` e recrie o ambiente virtual

## Contribuição

1. Faça o fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato através do email.
