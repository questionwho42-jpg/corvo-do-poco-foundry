# Processo de Criação de Lista de Tarefas

Você está criando um detalhamento de tarefas a partir de uma dada especificação e requisitos para uma nova funcionalidade.

## FASE 1: Obter e ler o spec.md e/ou documento(s) de requisitos

Você precisará de UM OU AMBOS destes arquivos para informar seu detalhamento de tarefas:

- `agent-os/specs/[esta-spec]/spec.md`
- `agent-os/specs/[esta-spec]/planning/requirements.md`

SE você não tiver UM OU AMBOS desses arquivos no seu contexto de conversa atual, então peça ao usuário para fornecer direção sobre onde você pode encontrá-los exibindo a seguinte solicitação, então espere pela resposta do usuário:

```
Eu precisarei de um spec.md ou requirements.md (ou ambos) para construir uma lista de tarefas.

Por favor, direcione-me para onde posso encontrá-los. Se você ainda não os criou, você pode executar /shape-spec ou /escrever-spec.
```

## FASE 2: Criar tasks.md

Uma vez que você tenha `spec.md` E/OU `requirements.md`, use o subagente **criador-lista-tarefas** para quebrar a especificação e requisitos em uma lista de tarefas acionável com agrupamento estratégico e ordenação.

Forneça ao criador-lista-tarefas:

- `agent-os/specs/[esta-spec]/spec.md` (se presente)
- `agent-os/specs/[esta-spec]/planning/requirements.md` (se presente)
- `agent-os/specs/[esta-spec]/planning/visuals/` e seus conteúdos (se presente)

O criador-lista-tarefas criará `tasks.md` dentro da pasta de especificação.

## FASE 3: Informar o usuário

Assim que o criador-lista-tarefas tiver criado `tasks.md` exiba o seguinte para informar o usuário:

```
Sua lista de tarefas está pronta!

✅ Lista de tarefas criada: `agent-os/specs/[esta-spec]/tasks.md`

PRÓXIMO PASSO 👉 Execute `/implement-tasks` (simples, eficaz) ou `/orquestrar-tarefas` (avançado, poderoso) para começar a construir!
```