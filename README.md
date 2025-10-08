# ⚽ Camp-Reserve: Sistema de Aluguel de Campos de Futebol

Projeto acadêmico desenvolvido como exercicio, consiste em uma aplicação web completa para a busca e reserva de campos de futebol. A plataforma foi construída com Django e PostgreSQL, com todo o ambiente de desenvolvimento e produção gerenciado por contêineres Docker.

---

## ✨ Funcionalidades Principais

-   ✅ **Autenticação Completa:** Fluxo de Cadastro (`Sign Up`), Login e Logout para usuários.
-   ✅ **Busca Inteligente:** Pesquisa de campos disponíveis filtrando por nome da cidade.
-   ✅ **Sistema de Reservas:**
    -   Formulário para agendamento por dia e horário.
    -   Cálculo do valor total em **tempo real** com JavaScript.
    -   Validação de backend que **impede a sobreposição** de reservas.
-   ✅ **Gerenciamento de Reservas:**
    -   Página "Minhas Reservas" para o usuário visualizar seus agendamentos.
    -   Funcionalidade para **cancelar** uma reserva existente.
-   ✅ **Feedback ao Usuário:** Mensagens de sucesso e erro para ações como reserva e cancelamento.
-   ✅ **Interface Profissional:** Layout responsivo e limpo construído com Bootstrap e CSS customizado.

---

## 🚀 Tecnologias Utilizadas

-   **Backend:** Python 3.9, Django 4.2
-   **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
-   **Banco de Dados:** PostgreSQL 13
-   **Ambiente e DevOps:** Docker, Docker Compose
-   **Versionamento:** Git e GitHub, com fluxo de trabalho baseado em *Feature Branches* e *Pull Requests*.

---

## 🏁 Como Executar o Projeto

Para rodar este projeto, você precisará ter o **Git** e o **Docker Desktop** instalados em sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/lfslDEV/Aluguel-de-Campos
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd Aluguel-de-Campos
    ```

3.  **Inicie os contêineres com Docker Compose:**
    Este comando irá construir a imagem, baixar o PostgreSQL e iniciar a aplicação.
    ```bash
    docker-compose up --build
    ```
    *Deixe este terminal aberto para ver os logs do servidor.*

4.  **Execute as migrações do banco de dados:**
    *Abra um **novo terminal** na mesma pasta* e execute o comando abaixo.
    ```bash
    docker-compose exec web python manage.py migrate
    ```

5.  **Crie um superusuário (administrador):**
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```
    *Siga as instruções para criar seu usuário de acesso.*

6.  **Acesse a aplicação:**
    Abra seu navegador e acesse: `http://localhost:8000/`

---

## 📁 Estrutura do Projeto

O projeto segue a arquitetura padrão do Django, com uma clara separação de responsabilidades:

-   `locacao_campos/`: Contém as configurações globais do projeto (`settings.py`, `urls.py` principal).
-   `core/`: A aplicação principal do Django, contendo a lógica de negócio (`models.py`, `views.py`, `forms.py`).
-   `templates/`: Contém os arquivos HTML, organizados por aplicação e com um `base.html` para herança.
-   `static/`: Contém os arquivos estáticos (CSS, JS, imagens).

---

## 🌿 Fluxo de Trabalho Git

Este projeto utiliza um fluxo de trabalho profissional para garantir a qualidade e a organização do código:

1.  A branch `main` é protegida e não permite commits diretos.
2.  Toda nova funcionalidade ou correção é desenvolvida em uma **branch separada** (ex: `feature/nome-da-feature`).
3.  Após a conclusão, um **Pull Request (PR)** é aberto para revisar as alterações.
4.  Com o PR aprovado, as mudanças são integradas à branch `main` através de um *merge*.