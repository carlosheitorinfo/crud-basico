# Passos para configurar este arquivo settings.py:
# 1. Definir o SECRET_KEY e o modo de depuração (DEBUG):
#    SECRET_KEY = 'sua-chave-secreta-aqui'
#    DEBUG = True  # Defina como False em produção
#
# 2. Configurar os hosts permitidos (ALLOWED_HOSTS):
#    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
#
# 3. Registrar os aplicativos instalados (INSTALLED_APPS):
#    Inclua os aplicativos padrão do Django e o aplicativo `projetos`.
#
# 4. Configurar os middlewares (MIDDLEWARE):
#    Certifique-se de que os middlewares padrão do Django estão configurados.
#
# 5. Definir o arquivo de URLs raiz (ROOT_URLCONF):
#    ROOT_URLCONF = 'crudproj.urls'
#
# 6. Configurar os templates (TEMPLATES):
#    Certifique-se de que os templates estão configurados para buscar arquivos na pasta `templates`.
#
# 7. Configurar o banco de dados (DATABASES):
#    Configure o banco de dados SQLite ou outro banco de dados de sua escolha.
#
# 8. Definir as validações de senha (AUTH_PASSWORD_VALIDATORS):
#    Inclua as validações padrão para senhas seguras.
#
# 9. Configurar o idioma e o fuso horário:
#    LANGUAGE_CODE = 'pt-br'
#    TIME_ZONE = 'America/Sao_Paulo'
#
# 10. Configurar os arquivos estáticos (STATIC_URL):
#     STATIC_URL = 'static/'
#
# 11. Definir a configuração de login (LOGIN_URL):
#     LOGIN_URL = '/admin/login/'

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-educacional-crud-exemplo'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projetos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crudproj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crudproj.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configura a URL de login para usar a página de login do admin
LOGIN_URL = '/admin/login/'
