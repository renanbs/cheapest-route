# Cheapest Route

Este projeto consiste em uma implementação simples do algoritmo Dijkstra.
Que pode ser acessada tanto pela linha de comando como por API REST.

O algoritmo de Dijkstra foi escolhido ao invés do Bellman–Ford por ser mais rápido e por que os pesos não são negativos.

A estrututa de diretórios do projeto foi desenhada dessa forma seguindo, de forma bem básica, o Domain Driven Design (ainda necessita de melhorias).

Foram adicionados apenas testes unitários básicos.

 - Este projeto foi testado apenas em Linux.

#### API Endpoints
- POST /routes/cheapest - para buscar a rota mais barata

```json
{
    "start": "GRU",
    "end": "CDG"
}
```

- POST /routes - para cadastro de novas rotas

```json
{
    "start": "GRU",
    "end": "CDG",
    "cost": 10
}
```

#### Linha de comando

Para usar a linha de comando basta rodar o seguinte comando:

```bash
$ python command_line.py input-file.csv
```
Onde `input-file.csv` é o arquivo no formato CSV com as rotas.


## Requirements

 - Make
 - Python 3.8+
 - pyenv


## Ambiente de Desenvolvimento
 
 
### Ferramenta de Automação

Este projeto usa `Makefile` como ferramenta de automação.

### Configurar o ambiente virtual

Os comandos abaixo irão instalar e configurar a ferramenta `pyenv` (https://github.com/pyenv/pyenv) usada para criar/gerenciar ambientes virtuais:

> Caso o terminal usado seja o zsh, substitua `bashrc` por `zshrc`.

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
$ exec "$SHELL"
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ exec "$SHELL"
```

Após executados os comando acima, acesse o diretório raiz e execute `make create-venv` para criar e recriar o ambiente virtual:

```bash
➜ make create-venv
```

> O ambiente vai ser criado no diretório do usuário:

> `$PROJECT_NAME` e `$PYTHON_VERSION` são variáveis definidas no Makefile

```bash
$HOME/.pyenv/versions/$PROJECT_NAME-$PYTHON_VERSION/bin/python

/home/renan/.pyenv/versions/cheapest_route-3.8.5/bin/python
```


### Rodar os testes unitários

Running unit tests
```bash
➜ make test
```

ou 
```bash
➜ pytest
```

## Como rodar:

### API REST
Existem 2 formas:

```bash
➜ flask run
```
ou

```bash
➜ python wsgi.py
```

O servidor irá ser executado no localhost na porta 5000 e fica acessível no link abaixo, apesar de não haver o endpoint raiz:

> http://127.0.0.1:5000/

Os únicos endpoints disponíveis são:
- POST http://127.0.0.1:5000/routes/cheapest
- POST http://127.0.0.1:5000/routes

---
## Exemplos de uso

### cURL


Buscar rota mais barata

```bash
➜ curl -X POST http://127.0.0.1:5000/routes/cheapest -d '{"start": "GRU", "end": "CDG"}' -H 'Content-Type: application/json'
```

Cadatro de novas rotas
```bash
➜ curl -X POST http://127.0.0.1:5000/routes -d '{"start": "GRU", "end": "GCC", "cost": "10"}' -H 'Content-Type: application/json'                                      
```

### Linha de comando

A linha abaixo, como descrita anteriormente realiza a busca da rota mais barata após a entrada destes dados no formato `START-END`

```bash
$ python command_line.py input-file.csv
please enter the route: GRU-CDG
best route: GRU - BRC - SCL - ORL - CDG > $40
```