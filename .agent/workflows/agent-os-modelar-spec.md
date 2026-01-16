---
description: Agent OS workflow for Modelar Spec
---

# Processo de Modelagem de Especificação (Spec Shaping)

Você está me ajudando a modelar e planejar o escopo para uma nova funcionalidade. O processo a seguir visa documentar nossas decisões-chave em relação ao escopo, design e abordagem de arquitetura. Usaremos nossas descobertas deste processo mais tarde quando escrevermos o documento formal de especificação (mas NÃO estamos escrevendo a especificação formal ainda).

Este processo seguirá 3 fases principais, cada uma com seus próprios passos de fluxo de trabalho:

Visão geral do processo (detalhes a seguir)

FASE 1. Inicializar especificação
FASE 2. Pesquisar requisitos para esta especificação
FASE 3. Informar o usuário que a especificação foi inicializada

Siga cada uma dessas fases e seus fluxos de trabalho individuais EM SEQUÊNCIA:

## Processo Multi-Fase:

### FASE 1: Inicializar Especificação

Use o subagente **inicializador-spec** para inicializar uma nova especificação.

SE o usuário forneceu uma descrição, forneça-a ao inicializador-spec.

O inicializador-spec fornecerá o caminho para a pasta de especificação datada (YYYY-MM-DD-nome-spec) que ele criou.

### FASE 2: Pesquisar Requisitos

Após o inicializador-spec completar, use imediatamente o subagente **modelador-spec**:

Forneça ao modelador-spec:

- O caminho da pasta de especificação do inicializador-spec

O modelador-spec lhe dará várias respostas separadas que você DEVE mostrar ao usuário. Estas incluem:

1. Perguntas de esclarecimento numeradas junto com uma solicitação de ativos visuais (mostre estas ao usuário, espere pela resposta do usuário)
2. Perguntas de acompanhamento se necessário (com base nas respostas do usuário e visuais fornecidos)

**IMPORTANTE**:

- Exiba estas perguntas ao usuário e espere pela resposta dele
- O modelador-spec pode pedir para você retransmitir perguntas de acompanhamento que você deve apresentar ao usuário

### FASE 3: Informar o usuário

Após todos os passos completos, informe o usuário:

```
Modelagem de especificação completa!

✅ Pasta de especificação criada: `[caminho-spec]`
✅ Requisitos coletados
✅ Ativos visuais: [Encontrados X arquivos / Nenhum arquivo fornecido]

PRÓXIMO PASSO 👉 Execute `/escrever-spec` para gerar o documento de especificação detalhado.
```