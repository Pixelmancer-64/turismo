# Controle de Turismo
Gerador de senhas para controle de transporte turístico.

## 1 - Instalação

Para instalar as dependencias do projeto basta usar o comando: __pip install -r requeriments.txt__

## 2 - Configurando as Variáveis de Ambiente

Para criar as variáveis de ambiente crie um arquivo com o nome **'.envars.yaml'** na raiz do seu projeto ou no diretrio **acima da pasta do seu projeto** contendo as seguintes informações conforme o modelo abaixo:
```
db_name: turismo # Este projeto foi pensando para suportar MySql ou MariaDB
db_user: usuariodobanco # Usuário do banco com todas as permissões para a base de dados
db_pw: senhadobanco # A senha do respectivo usuário do banco
django_secret_key: secretkey123456 # Insira sua django secret key
debug_mode: True # Use True para DEBUG or False para PRODUCTION
email_sistema: seu@email.com # E-mail utilizado para recuperação de senha
email_pw: su@senha123 # Senha do email acima
hCAPTCHA_Public_Key: 6484-dsadad4994ds949494d2314 # Inscreva-se https://www.hcaptcha.com/
hCAPTCHA_Secret_Key: 6484-dsadad4994ds949494d2314dsd4900c0952 # Cadastre seu site após se inscrever
GOOGLE_OAUTH2_PUBLIC_KEY: 74526484-dsadad4994ds949494d2314.apps.googleusercontent.com # Inscreva-se https://console.cloud.google.com/ e gere as chames para seu site
GOOGLE_OAUTH2_SECRET_KEY: GOCSPX-dsadad4994ds949494d2314
FACEBOOK_DEVELOPER_PUBLIC_KEY: 4994ds949494d2314 # Inscreva-se https://developers.facebook.com/ e gere as chaves para seu site
FACEBOOK_DEVELOPER_SECRET_KEY: 494d231479ff65cb6307b3
```
