---
description: Workflow para converter conteúdo de jogo/mundo para Foundry VTT
---

# Workflow: Migrar Conteúdo para Foundry

Use este workflow para transformar arquivos Markdown de World Building em dados utilizáveis no Foundry VTT.

## FASE 1: Análise (.agent/rules/agent-os-foundry-data-mapping.md)

1.  **Ler Arquivo**: Leia o arquivo Markdown de origem em `c:\Users\Pichau\Desktop\jogo\mundo`.
2.  **Identificar Tipo**: É um Monstro? NPC? Missão? Lore?
3.  **Checar Mapeamento**: Consulte a regra `data-mapping` para saber qual Pack e Tipo de Documento usar.

## FASE 2: Geração de Dados (Foundry)

1.  **Criar Entidade**: Use a skill `foundry-dev` para criar o documento via script ou instrução de macro.
    - Ex: `Actor.create({name: "Goblin", type: "npc"})`
2.  **Preencher Dados**:
    - Copie o texto de Lore para `system.details.biography.value` (NPC) ou `content` (Journal).
    - Converta estatísticas para campos do sistema PF2e (se aplicável).
3.  **Links**: Identifique referências a outros NPCs/Locais e crie links de UUID se eles já existirem no Foundry.

## FASE 3: Arte (Assets)

1.  **Checar Prompt**: Existe um prompt de imagem no arquivo?
2.  **Gerar/Localizar**: Se a imagem já existe em `assets/`, use-a. Se não, marque para geração.
3.  **Vincular**: Atualize o caminho da imagem (`img`) no documento criado.

## Exemplo de Comando

Para migrar um monstro específico:
`/run workflow agent-os-foundry-migrate-content --input "bestiario/goblin_rei.md"`
