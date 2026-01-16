---
description: Workflow para criar uma nova funcionalidade no módulo Foundry VTT
---

# Workflow: Criar Funcionalidade Foundry VTT

Este workflow guia o processo de implementação de uma nova funcionalidade no módulo "Corvo do Poço".

## FASE 1: Planejamento (.agent/rules/agent-os-foundry-module-structure.md)

1.  **Definir Escopo**: O que a funcionalidade faz? (Ex: um novo botão na ficha de ator, uma automação de combate, uma nova janela de configuração).
2.  **Identificar Arquivos**:
    - Precisa de um novo arquivo em `scripts/`?
    - Precisa de templates `.hbs`?
    - Precisa de estilos CSS em `styles/`?
3.  **Verificar Hooks**: Que hooks do Foundry ou do PF2e serão necessários? (`renderActorSheet`, `preUpdateItem`, etc.)

## FASE 2: Implementação (.agent/skills/agent-os-foundry-dev)

1.  **Criar Estrutura**: Crie os arquivos definidos no planejamento.
2.  **Registrar (se necessário)**: Importe o novo script em `main.js` ou registre a classe/função no hook `init` ou `ready`.
3.  **Codificar**: Implemente a lógica usando as melhores práticas (`agent-os-foundry-api-best-practices.md`).
    - Use `console.log` com prefixo para debug.
    - Localize strings de texto.

## FASE 3: Verificação

1.  **Lint/Check**: Verifique se não há erros de sintaxe.
2.  **Teste Manual (Instruções)**: Instrua o usuário a abrir o Foundry VTT e testar:
    - O módulo carrega sem erros no console (F12)?
    - A funcionalidade aparece/funciona como esperado?
    - Não há conflitos óbvios com o sistema PF2e?

## Exemplo de Comando

Para iniciar este workflow para uma feature "Botão de Descanso Personalizado":
`/run workflow agent-os-foundry-create-feature --input "Botão de Descanso Personalizado"`
