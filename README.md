<h1 align="center">Doggis - Sistema de Petshop</h1>
<p>Projeto executado como trabalho de conclusão de curso, que tem como objetivo gerenciar  as  atividades  do  pet  shop  “Doggis”.</p>

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/downloads/). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/);

### Abrir e rodar o projeto
Clone o repositório:
```bash
git clone git@github.com:nicoleCopetti/Doggis.git
```
Acesse o projeto:
```bash
cd/Doggis
```
Crie um ambiente virtual:
```bash
python -m venv <nome_da_virtualenv>
```
Ative o ambiente virtual que você acabou de criar:
```bash
python -m venv <nome_da_virtualenv>
```
Instale os pacotes de desenvolvimento local:
```bash
pip install -r requirements.txt
```
Execute as migrações:
```bash
python manage.py migrate
```
Popule a base com dados pré definidos:
```bash
python manage.py  dumpdata > databasedump.json
```
Rode o servidor de desenvolvimento:
```bash
python manage.py runserver
```
