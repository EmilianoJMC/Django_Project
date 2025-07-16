# Django Blog

## Descrição

Este projeto é um blog completo desenvolvido com Django, incluindo:
- Sistema de autenticação (login, logout, registro)
- Perfis de usuário editáveis (avatar, bio, data de nascimento)
- Listagem, criação, edição e exclusão de posts (com CKEditor)
- Sistema de mensagens de feedback
- Templates responsivos com Bootstrap
- Navegação dinâmica conforme login/logout

## Funcionalidades

- Cadastro, login e logout de usuários
- Edição de perfil e dados do usuário
- Alteração de senha
- Criação automática de perfil ao registrar
- Listagem e visualização de posts
- Criação, edição e exclusão de posts (restrito a staff)
- Upload de imagens e avatar
- Mensagens de feedback para todas as ações

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd Django_Project
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Colete os arquivos estáticos:**
   ```bash
   python manage.py collectstatic
   ```

7. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

8. **Acesse o sistema:**
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - Blog: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Estrutura de URLs principais

- `/accounts/login/` — Login
- `/accounts/logout/` — Logout (via botão na NavBar)
- `/accounts/register/` — Cadastro
- `/accounts/perfil/` — Perfil do usuário
- `/accounts/perfil/editar/` — Editar perfil
- `/accounts/usuario/editar/` — Editar dados do usuário
- `/accounts/senha/` — Alterar senha
- `/pages/` — Listagem de posts
- `/pages/novo/` — Novo post (staff)

## Requisitos

- Python 3.10+
- Django 5+
- Pillow
- django-ckeditor

## Dicas e Observações

- O logout deve ser feito pelo botão na NavBar (POST), conforme padrão Django.
- O perfil é criado automaticamente ao registrar um novo usuário.
- Para editar posts, o usuário deve ser staff ou superusuário.
- O projeto já está pronto para deploy em servidores WSGI (ex: Heroku, PythonAnywhere, etc).
- Para produção, configure variáveis de ambiente e ajuste o DEBUG/ALLOWED_HOSTS.

## Estrutura de Pastas

- `core/` — Home, sobre, base de templates
- `blog/` — Posts e páginas
- `accounts/` — Autenticação e perfis
- `messenger/` — (futuro) Mensagens privadas
- `static/` e `media/` — Arquivos estáticos e uploads

## Licença

Este projeto é livre para fins acadêmicos e de estudo.

---

Dúvidas ou sugestões? Abra uma issue ou entre em contato! 