# EVENTEX FÊNIX
 
Sistema de eventos desenvolvido em conjunto com a comunidade WTTD via discord com afins
de aprofundar conhecimentos com python e seu framework DJANGO.

## Como desenvolver?
1. Clone o repositório
2. Crie um virtualenv com python 3.5 >
3. Ative o virtualenv
4. Instale as dependencias
5. Configure a instância com o .env
6. Execute os testes

``` console
git clone github.com/zeny-brus/wttd.git
cd wttd
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py test
---
