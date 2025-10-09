# Instruções

Esse trabalho é o primeiro de dois sobre testes unitários e test driven development. Fazer ele é obrigatório para a segunda parte.

O objetivo é fazer um jogo nos moldes do classico snake, onde uma cobra cresce ao comer frutas ou até que ela coma um segmento do próprio corpo. O jogo deve também deve permitir que a cobra dê a volta na tela e quando a cobra atinge tamanho 10, duas frutas devem aparecer por vez, quando atingir 20, três frutas, e assim por diante. 

Faça uma cópia do arquivo em https://github.com/JoaoVitorSantiagoNogueira/TDD---Exercicio ou um branch do repositório. Lá uma classe io_handler cuida do input e da exibição do jogo. Em outro arquivo, que importa essa classe de io_handler, crie o comportamento do jogo snake usando os padrões de TDD.

- Crie testes mínimos que falhem usando Pytests (red)
- Faça seu código passar em seus testes mínimos (green)
- Refratore seu código (refactor)

Um breve guia do pytest é:
https://youtu.be/SPwcj137e0U?feature=shared

A entrega final deve ser um zip com pastas referentes a cada iteração ou um git com devidamente commitado para acompanhar a evolução do projeto ao longo do tempo - pelo menos um commit pra cada red, green e refactor. 

Etapa 1
    testes.py
    snake.py
    snake_ref.py
Etapa 2 
...
Etapa N

Façam etapas até que o jogo esteja completo e todos os testes estejam verdes.

# Como rodar
## 💻 Pré-requisitos

Antes de rodar o projeto, você precisa ter:
- Python 3.10+
- UV (gerenciador de ambientes virtuais)
- Dependências do projeto (pip)
- Permissões de acesso ao teclado (necessário para o pacote keyboard no Linux)

## ⚙️ Instalação com UV

### Crie e ative o ambiente virtual usando UV:
```bash
uv venv create .venv
uv venv activate .venv
```
Isso cria um ambiente virtual .venv isolado e já o ativa.

### Instale as dependências do projeto com pip:

```bash
uv sync
```

O keyboard requer acesso ao teclado do SO, especialmente no Linux.

## 🧪 Rodando os testes

Dentro do ambiente virtual UV, execute:

```bash
uv run pytest -vv
```

Todos os testes do TDD devem passar antes de rodar o jogo.

## ▶️ Rodando o jogo no Ubuntu/Linux

No Linux, o pacote keyboard precisa de permissões de root para acessar eventos do teclado. Execute:

```bash
sudo .venv/bin/python3 -m src.main
```


Use WASD para mover a cobra.
Pressione ESC para sair do jogo.
O jogo usa a classe io_handler para desenhar o tabuleiro e receber entradas do teclado.