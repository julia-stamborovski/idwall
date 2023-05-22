# Challenge Idwall / 2023 - FIAP

# Setup 
~~~
django-admin startproject scrapingIdwall
pip install -r requirements.txt
~~~

## Manage.py 
~~~
python manage.py runserver
~~~

## Criação do superuser
~~~
python manage.py createsuperuser
~~~

# IDE
Visual Studio Code

# Extensões
SQlite Viewer - [Florian Klampfe](https://qwtel.com/)

# Linguagem de Programação
Python

# Framework Web
Django 4.2

# Banco de Dados
SQLite

# Bibliotecas Principais 
🕵️‍♀️  **Django REST Framework** (djangorestframework==3.14.0): Biblioteca para
construção de APIs REST com o Django.
</br>
🕵️‍♀️  **Selenium** (selenium==4.9.1): Biblioteca para automação de testes web.
</br>
🕵️‍♀️  **Requests** (requests==2.30.0): Biblioteca para realizar requisições HTTP.
</br>
🕵️‍♀️  **Pillow** (Pillow==9.5.0): Biblioteca para manipulação de imagens
## Outras bibliotecas
Arquivo --> requirements.py

# Tecnologias
🕵️‍♀️ Swagger 
</br>
🕵️‍♀️ Pip 

# Swagger
~~~
pip install drf-yasg
~~~


# Definições Funcionais
Identificar os requisitos funcionais e não funcionais da solução

## Requisitos Funcionais
1. Registro de perfis de pessoas procuradas, incluindo informações como: nome, foto, crimes cometidos, status da investigação e tipo de crime.
2. Pesquisa e filtragem avançada para localizar pessoas procuradas com base em critérios específicos, como: nome.
3. Visualização detalhada do perfil de uma pessoa procurada, com acesso a todas as informações relevantes.
4. Integraçado com sistemas do FBI para **sincronizar** e **atualizar** automaticamente os dados sobre pessoas procuradas.
5. Monitoramento diário das atualizações das listas de pessoas procuradas para manter as informações sempre atualizadas.
6. Recursos de segurança, como autenticação de usuários, controle de acesso baseado em funções, criptografia de dados e registro de auditoria.
7. Capacidade de adiciconar comentários, notas e atualizações sobre casos de pessoas procuradas para compartilhar informações importantes entre os usuários autorizados.
8. Geração de relatórios e exportação de dados para facilitar a análise e compartilhamento de informações.

## Requisitos <u>Não</u> Funcionais

1. Segurança robusta para proteger as informações sensíveis e garantir o acesso autorizado **************apenas************** para usuários apropriados.
2. Desempenho e escalabilidade para lidar com grandes volumes de dados e múltiplos usuários acessando o sistema simultaneamente.
3. Interface de usuário intuitiva e amigável para facilitar a navegação e o uso eficiente do sistema.
4. Alta disponibilidade para garantir que o sistema esteja sempre acessível quando necessário.
5.**Conformidade com as leis e regulamentos de privacidade de dados relevantes** 
6. Resposta rápida do sistema para consultas de pesquisa e recuperação de dados.
7. Facilidade de integração com outros sistemas e tecnologias existentes nas agências
8. Manutenção e suporte contínuos para garantir a correção de bugs, atualizações de segurança e aprimoramentos futuros do sistema.
