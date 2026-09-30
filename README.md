# Sistema de Controle de Peças


---

## Sobre o projeto

Sistema desenvolvido em Python para automatizar o controle de qualidade de peças fabricadas em uma linha de montagem industrial. O sistema avalia automaticamente cada peça com base em critérios de qualidade, armazena as aprovadas em caixas e gera relatórios consolidados.

---

## Funcionalidades

| Opção | Descrição |
|---|---|
| 1. Cadastrar nova peça | Registra id, peso, cor e comprimento e avalia automaticamente |
| 2. Listar peças | Exibe todas as peças aprovadas e reprovadas com motivos |
| 3. Remover peça | Remove uma peça cadastrada pelo ID |
| 4. Listar caixas | Exibe as caixas fechadas e a caixa atual |
| 5. Relatório final | Gera relatório consolidado com totais e status das caixas |

---

## Critérios de qualidade

| Critério | Valor aceito |
|---|---|
| Peso | Entre 95g e 105g |
| Cor | Azul ou Verde |
| Comprimento | Entre 10cm e 20cm |

Peças que não atendem a um ou mais critérios são **reprovadas** com o motivo registrado.

---

## Como rodar o programa

### Pré-requisitos
- Python 3.x instalado

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/sistema-controle-pecas.git
```

**2. Entre na pasta:**
```bash
cd sistema-controle-pecas
```

**3. Execute o programa:**
```bash
python sistema_pecas.py
```

---

## Exemplos de entrada e saída

### Cadastrando uma peça aprovada:
```
Digite o ID da peca: P001
Digite o peso da peca (g): 100
Digite a cor da peca: azul
Digite o comprimento da peca (cm): 15

-> Peça P001 APROVADA
```

### Cadastrando uma peça reprovada:
```
Digite o ID da peca: P002
Digite o peso da peca (g): 80
Digite a cor da peca: vermelho
Digite o comprimento da peca (cm): 25

-> Peça P002 REPROVADA: peso fora do intervalo de 95g a 105g; cor diferente de azul ou verde; comprimento fora do intervalo de 10cm a 20cm
```

### Relatório final:
```
========================================
           RELATÓRIO FINAL
========================================
Total de peças aprovadas : 10
Total de peças reprovadas: 3

Motivos das reprovações:
  - Peça P002: peso fora do intervalo de 95g a 105g; cor diferente de azul ou verde
  - Peça P005: comprimento fora do intervalo de 10cm a 20cm
  - Peça P009: cor diferente de azul ou verde

Quantidade de caixas utilizadas: 1
  Caixa 1: 10 peça(s) [Cheia]
========================================
```

---

## Estrutura do código

```
sistema_pecas.py
│
├── ler_float()          — Leitura segura de números decimais
├── avaliar_peca()       — Verifica os critérios de qualidade
├── cadastrar_peca()     — Cadastra e avalia uma nova peça
├── listar_pecas()       — Lista aprovadas e reprovadas
├── remover_peca()       — Remove uma peça pelo ID
├── listar_caixas()      — Lista caixas fechadas e caixa atual
├── gerar_relatorio()    — Gera relatório consolidado
├── menu()               — Exibe o menu interativo
└── main()               — Loop principal do programa
```

---


