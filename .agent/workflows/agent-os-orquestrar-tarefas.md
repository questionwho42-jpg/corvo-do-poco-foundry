---
description: Agent OS workflow for Orquestrar Tarefas
---

# Processo para Orquestrar a Implementação de uma Especificação

Agora que temos uma especificação e uma lista de tarefas prontas para implementação, prosseguiremos com a orquestração da implementação de cada grupo de tarefas por um agente dedicado usando o seguinte processo MULTI-FASE.

Siga cada uma dessas fases e seus workflows individuais EM SEQUÊNCIA:

## Processo Multi-Fase

### PRIMEIRO: Obter tasks.md para esta especificação

SE você já sabe em qual especificação estamos trabalhando e SE essa pasta de especificação tem um arquivo `tasks.md`, então use-o e pule para a PRÓXIMA fase.

SE você não sabe em qual especificação estamos trabalhando e SE essa pasta de especificação ainda não tem um `tasks.md`, ENTÃO exiba a seguinte solicitação ao usuário:

```
Por favor, aponte-me para o `tasks.md` de uma especificação para a qual você deseja orquestrar a implementação.

Se você ainda não tem um, então execute qualquer um destes comandos primeiro:
/shape-spec
/escrever-spec
/criar-tarefas
```

### PRÓXIMO: Criar orchestration.yml para servir como um roadmap para orquestração de grupos de tarefas

Na pasta desta especificação, crie este arquivo: `agent-os/specs/[esta-spec]/orchestration.yml`.

Preencha este arquivo com os nomes de cada grupo de tarefas encontrado no `tasks.md` desta especificação e use esta estrutura EXATA para o conteúdo de `orchestration.yml`:

```yaml
task_groups:
  - name: [nome-grupo-tarefa]
  - name: [nome-grupo-tarefa]
  - name: [nome-grupo-tarefa]
  # Repita para cada grupo de tarefas encontrado em tasks.md
```


### PRÓXIMO: Pedir ao usuário para atribuir subagentes a cada grupo de tarefas

A seguir, devemos determinar quais subagentes devem ser atribuídos a quais grupos de tarefas. Peça ao usuário para fornecer esta informação usando a seguinte solicitação ao usuário e AGUARDE a resposta do usuário:

```
Por favor, especifique o nome de cada subagente a ser atribuído a cada grupo de tarefas:

1. [nome-grupo-tarefa]
2. [nome-grupo-tarefa]
3. [nome-grupo-tarefa]
[repita para cada grupo-tarefa que você adicionou ao orchestration.yml]

Simplesmente responda com os nomes dos subagentes e o número do grupo de tarefas correspondente e eu atualizarei o orchestration.yml de acordo.
```

Usando as respostas do usuário, atualize `orchestration.yml` para especificar esses nomes de subagentes. `orchestration.yml` deve acabar ficando assim:

```yaml
task_groups:
  - name: [nome-grupo-tarefa]
    claude_code_subagent: [nome-subagente]
  - name: [nome-grupo-tarefa]
    claude_code_subagent: [nome-subagente]
  - name: [nome-grupo-tarefa]
    claude_code_subagent: [nome-subagente]
  # Repita para cada grupo de tarefas encontrado em tasks.md
```

Por exemplo, após este passo, o arquivo `orchestration.yml` pode parecer com isso (nomes exatos variarão):

```yaml
task_groups:
  - name: sistema-autenticacao
    claude_code_subagent: especialista-backend
  - name: dashboard-usuario
    claude_code_subagent: especialista-frontend
  - name: endpoints-api
    claude_code_subagent: especialista-backend
```



### PRÓXIMO: Pedir ao usuário para atribuir padrões a cada grupo de tarefas

A seguir, devemos determinar quais padrões devem guiar a implementação de cada grupo de tarefas. Peça ao usuário para fornecer esta informação usando a seguinte solicitação ao usuário e AGUARDE a resposta do usuário:

```
Por favor, especifique o(s) padrão(ões) que deve(m) ser usado(s) para guiar a implementação de cada grupo de tarefas:

1. [nome-grupo-tarefa]
2. [nome-grupo-tarefa]
3. [nome-grupo-tarefa]
[repita para cada grupo-tarefa que você adicionou ao orchestration.yml]

Para cada número de grupo de tarefas, você pode especificar qualquer combinação do seguinte:

"all" para incluir todos os seus padrões
"global/*" para incluir todos os arquivos dentro de standards/global
"frontend/css.md" para incluir o arquivo de padrão css.md
"none" para não incluir nenhum padrão para este grupo de tarefas.
```

Usando as respostas do usuário, atualize `orchestration.yml` para especificar esses padrões para cada grupo de tarefas. `orchestration.yml` deve acabar tendo PELO MENOS a seguinte informação adicionada a ele:

```yaml
task_groups:
  - name: [nome-grupo-tarefa]
    standards:
      - [1ª resposta do usuário para este grupo de tarefas]
      - [2ª resposta do usuário para este grupo de tarefas]
      - [3ª resposta do usuário para este grupo de tarefas]
      # Repita para todos os padrões que o usuário especificou para este grupo de tarefas
  - name: [nome-grupo-tarefa]
    standards:
      - [1ª resposta do usuário para este grupo de tarefas]
      - [2ª resposta do usuário para este grupo de tarefas]
      # Repita para todos os padrões que o usuário especificou para este grupo de tarefas
  # Repita para cada grupo de tarefas encontrado em tasks.md
```

Por exemplo, após este passo, o arquivo `orchestration.yml` pode parecer com isso (nomes exatos variarão):

```yaml
task_groups:
  - name: sistema-autenticacao
    standards:
      - all
  - name: dashboard-usuario
    standards:
      - global/*
      - frontend/components.md
      - frontend/css.md
  - name: grupo-tarefa-sem-padroes
  - name: endpoints-api
    standards:
      - backend/*
      - global/error-handling.md
```

Nota: Se a flag `use_claude_code_subagents` estiver habilitada, o `orchestration.yml` final incluirá AMBOS atribuições `claude_code_subagent` E `standards` para cada grupo de tarefas.


### PRÓXIMO: Delegar implementações de grupos de tarefas para subagentes atribuídos

Percorra (loop) cada grupo de tarefas em `agent-os/specs/[esta-spec]/tasks.md` e delegue sua implementação para o subagente atribuído especificado em `orchestration.yml`.

Para cada delegação, forneça ao subagente:

- O grupo de tarefas (incluindo a tarefa pai e todas as sub-tarefas)
- O arquivo de especificação: `agent-os/specs/[esta-spec]/spec.md`
- Instrua o subagente a:
  - Realizar sua implementação
  - Marcar a tarefa e sub-tarefa(s) em `agent-os/specs/[esta-spec]/tasks.md`

Além dos itens acima, também instrua o subagente a aderir estritamente aos padrões e preferências do usuário conforme especificado nos seguintes arquivos. Para construir a lista de referências de arquivo para dar ao subagente, siga estas instruções:

⚠️ Workflow not found: implementacao/compile-implementation-standards

Forneça tudo acima ao subagente ao delegar tarefas para ele implementar.
