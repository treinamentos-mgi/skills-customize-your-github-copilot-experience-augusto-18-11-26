
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa o clássico jogo de adivinhar palavras em Python. Os jogadores adivinham letras para revelar uma palavra oculta antes de esgotar as tentativas.

**Habilidades praticadas:** manipulação de strings, loops, condicionais, seleção aleatória e entrada de dados do usuário.

## 📝 Tarefas

### 🛠️ Seleção da Palavra e Exibição do Progresso

#### Descrição
Crie a base do jogo: escolha uma palavra aleatória e mostre ao jogador o progresso atual, com as letras ainda não descobertas representadas por `_`.

#### Requisitos
O programa concluído deve:

- Selecionar palavras aleatoriamente de uma lista predefinida.
- Exibir o progresso atual no formato `_ _ _`, mostrando as letras já adivinhadas.

### 🛠️ Palpites e Controle de Tentativas

#### Descrição
Implemente o laço principal do jogo, em que o jogador informa letras e o programa controla as tentativas restantes.

#### Requisitos
O programa concluído deve:

- Aceitar palpites de letras usando `input()`.
- Atualizar o progresso sempre que a letra estiver na palavra.
- Rastrear o número de tentativas incorretas restantes.

### 🛠️ Fim de Jogo e Mensagens

#### Descrição
Defina quando o jogo termina e informe o resultado ao jogador.

#### Requisitos
O programa concluído deve:

- Encerrar quando a palavra for adivinhada ou quando as tentativas se esgotarem.
- Exibir mensagens de vitória ou derrota ao final da partida.