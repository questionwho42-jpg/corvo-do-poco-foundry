# Foundry VTT Module Structure

## Diretrizes de Estrutura de Arquivos

Para garantir compatibilidade e organização no módulo "Corvo do Poço", siga esta estrutura rigorosamente:

### 1. Raiz do Módulo

- `module.json`: O manifesto do módulo. Deve ser mantido atualizado com `version` e `compatibility`.
- `README.md`: Documentação básica para o usuário final.
- `LICENSE`: Arquivo de licença.

### 2. Scripts (`scripts/`)

- Módulos Javascript (ESM) devem residir aqui.
- `scripts/main.js`: Ponto de entrada principal (definido em `esmodules`).
- Use subpastas para organizar componentes: `scripts/apps/`, `scripts/models/`, `scripts/hooks/`.

### 3. Estilos (`styles/`)

- Arquivos CSS/SCSS.
- `styles/main.css`: Arquivo principal (definido em `styles`).

### 4. Compêndios (`packs/`)

- Dados de Atores, Itens, Cenas, etc.
- Devem ser definidos no `module.json`.
- Organize por tipo: `packs/actors`, `packs/items`.

### 5. Assets (`assets/`)

- Imagens, sons e outros recursos de mídia.
- Estrutura sugerida:
  - `assets/art/`: Arte de itens, atores.
  - `assets/tokens/`: Tokens de personagens.
  - `assets/ui/`: Elementos de interface.

## Regras de `module.json`

- Mantenha `minimum` e `verified` atualizados com a versão alvo do Foundry (atualmente v13).
- Sempre incremente `version` (Semantic Versioning) ao fazer releases.
