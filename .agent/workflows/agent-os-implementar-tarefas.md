---
description: Agent OS workflow for Implementar Tarefas
---

# Processo de Implementação de Especificação

Agora que temos uma especificação e lista de tarefas prontas para implementação, prosseguiremos com a implementação desta especificação seguindo este processo multi-fase:

FASE 1: Determinar qual(is) grupo(s) de tarefas de tasks.md deve(m) ser implementado(s)
FASE 2: Delegar implementação para o subagente implementador
FASE 3: Após TODOS os grupos de tarefas terem sido implementados, delegar para verificador-implementacao para produzir o relatório final de verificação.

Siga cada uma dessas fases e seus fluxos de trabalho individuais EM SEQUÊNCIA:

## Processo Multi-Fase

### FASE 1: Determinar qual(is) grupo(s) de tarefas implementar

Primeiro, verifique se o usuário já forneceu instruções sobre qual(is) grupo(s) de tarefas implementar.

**Se o usuário TIVER fornecido instruções:** Prossiga para a FASE 2 para delegar a implementação desse(s) grupo(s) de tarefas especificado(s) para o subagente **implementador**.

**Se o usuário NÃO tiver fornecido instruções:**

Leia `agent-os/specs/[esta-spec]/tasks.md` para revisar os grupos de tarefas disponíveis, então exiba a seguinte mensagem ao usuário e AGUARDE a resposta deles:

```
Devemos prosseguir com a implementação de todos os grupos de tarefas em tasks.md?

Se não, por favor especifique qual(is) tarefa(s) implementar.
```

### FASE 2: Delegar implementação para o subagente implementador

Delegue para o subagente **implementador** para implementar o(s) grupo(s) de tarefas especificado(s):

Forneça ao subagente:

- O(s) grupo(s) de tarefas específico(s) de `agent-os/specs/[esta-spec]/tasks.md` incluindo a tarefa pai, todas as sub-tarefas e quaisquer sub-pontos
- O caminho para a documentação desta especificação: `agent-os/specs/[esta-spec]/spec.md`
- O caminho para os requisitos desta especificação: `agent-os/specs/[esta-spec]/planning/requirements.md`
- O caminho para os visuais desta especificação (se houver): `agent-os/specs/[esta-spec]/planning/visuals`

Instrua o subagente a:

1. Analisar o spec.md, requirements.md e visuais fornecidos (se houver)
2. Analisar padrões na base de código de acordo com seu fluxo de trabalho embutido
3. Implementar o grupo de tarefas atribuído de acordo com requisitos e padrões
4. Atualizar `agent-os/specs/[esta-spec]/tasks.md` para marcar tarefas completas com `- [x]`

### FASE 3: Produzir o relatório final de verificação

SE TODOS os grupos de tarefas em tasks.md estiverem marcados como completos com `- [x]`, então prossiga com este passo. Caso contrário, retorne à FASE 1.

Assumindo que todas as tarefas estão marcadas como completas, então delegue para o subagente **verificador-implementacao** para fazer sua verificação de implementação e produzir seu relatório final de verificação.

Forneça ao subagente o seguinte:

- O caminho para esta especificação: `agent-os/specs/[esta-spec]`
  Instrua o subagente a fazer o seguinte:
  1. Rodar todas as suas verificações finais de acordo com seu fluxo de trabalho embutido
  2. Produzir o relatório final de verificação em `agent-os/specs/[esta-spec]/verifications/final-verification.md`.