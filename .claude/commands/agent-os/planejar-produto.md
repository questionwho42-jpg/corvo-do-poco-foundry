## Processo de Planejamento de Produto

Você está ajudando a planejar e documentar a missão, roadmap e tech stack para o produto atual. Isso incluirá:

- **Coleta de Informações**: A visão do produto do usuário, personas de usuário, problemas e funcionalidades principais
- **Documento de Missão**: Pegue o que você coletou e crie um documento de missão conciso
- **Roadmap**: Crie um plano de desenvolvimento em fases com funcionalidades priorizadas
- **Tech stack**: Estabeleça a stack técnica usada para todos os aspectos da base de código deste produto

Este processo criará esses arquivos no diretório `agent-os/product/`.

### FASE 1: Coletar Requisitos do Produto

Use o subagente **planejador-produto** para criar documentação abrangente do produto.

SE o usuário forneceu quaisquer detalhes em relação à ideia do produto, seu propósito, lista de funcionalidades, usuários-alvo e quaisquer outros detalhes, então forneça-os ao subagente **planejador-produto**.

O planejador-produto irá:

- Confirmar (ou coletar) ideia do produto, funcionalidades, usuários-alvo, confirmar a tech stack e coletar outros detalhes
- Criar `agent-os/product/mission.md` com visão e estratégia do produto
- Criar `agent-os/product/roadmap.md` com plano de desenvolvimento em fases
- Criar `agent-os/product/tech-stack.md` documentando todas as escolhas de tech stack deste produto

### FASE 2: Informar o usuário

Após todos os passos estarem completos, exiba o seguinte para informar o usuário:

```
Seu planejamento de produto está pronto!

✅ Missão do produto: `agent-os/product/mission.md`
✅ Roadmap do produto: `agent-os/product/roadmap.md`
✅ Tech stack do produto: `agent-os/product/tech-stack.md`

PRÓXIMO PASSO 👉 Execute `/shape-spec` ou `/escrever-spec` para começar a trabalhar em uma funcionalidade!
```