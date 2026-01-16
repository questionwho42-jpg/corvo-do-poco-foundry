# Processo de Escrita de Especificação

Você está criando uma especificação abrangente para uma nova funcionalidade.

Use o subagente **redator-spec** para criar o documento de especificação para esta spec:

Forneça ao redator-spec:

- O caminho da pasta de especificação (encontre o atual ou o mais recente em `agent-os/specs/*/`)
- Os requisitos de `planning/requirements.md`
- Quaisquer ativos visuais em `planning/visuals/`

O redator-spec criará `spec.md` dentro da pasta de especificação.

Assim que o redator-spec tiver criado `spec.md` exiba o seguinte para informar o usuário:

```
Seu spec.md está pronto!

✅ Documento de especificação criado: `[caminho-spec]`

PRÓXIMO PASSO 👉 Execute `/criar-tarefas` para gerar sua lista de tarefas para esta especificação.
```