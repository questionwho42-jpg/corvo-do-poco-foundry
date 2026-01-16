# Foundry VTT API & Best Practices

## Diretrizes de Desenvolvimento (Foundry VTT)

### 1. Hooks

- Use `Hooks.on('hookName', callback)` ou `Hooks.once(...)` para reagir a eventos.
- Centralize registros de hooks em `scripts/hooks/`.
- Exemplos comuns: `init`, `ready`, `renderActorSheet`.

### 2. Applications (Interface)

- Prefira a API de Aplicações V2 (`foundry.applications.api.ApplicationV2`) se disponível e estável para a versão alvo.
- Se usar V1 (`FormApplication`), garanta que o `getData` retorne objetos serializáveis.

### 3. Localização

- Use `game.i18n.localize("KEY")` ou `game.i18n.format("KEY", {data})`.
- Arquivos de tradução devem estar em `languages/`.

### 4. Depuração

- Use `console.log`, `console.warn`, `console.error` com um prefixo do módulo: `console.log("Corvo do Poço | Mensagem")`.
- Utilize `foundry.utils.mergeObject` para manipular configurações e dados.

### 5. Integração com PF2e

- Ao trabalhar com o sistema PF2e, verifique as classes e tipos de dados mais recentes em `game.pf2e`.
- Respeite as regras de automação do sistema.
