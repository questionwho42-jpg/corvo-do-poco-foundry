# Foundry VTT Data Mapping

Esta regra define como converter o conteúdo de World Building (`jogo/mundo`) em dados do Foundry VTT (`packs`).

## Mapeamento Geral

| Origem (`jogo/mundo`) | Destino Foundry (`packs`) | Tipo de Documento | Detalhes PF2e                                                                       |
| :-------------------- | :------------------------ | :---------------- | :---------------------------------------------------------------------------------- |
| `/bestiario/*.md`     | `corvo-do-poco-actors`    | **Actor**         | Type: `npc`. Use o Bloco de Estatísticas para preencher attributes/skills.          |
| `/populacao/*.md`     | `corvo-do-poco-actors`    | **Actor**         | Type: `npc`. Preencher `biography` com Lore e Motivação. Influência vai para Notes. |
| `/missoes/*.md`       | `corvo-do-poco-journals`  | **JournalEntry**  | Cada arquivo é uma Entry. Seções (Objetivo, Gatilho) viram Pages ou Headers.        |
| `/lore/*.md`          | `corvo-do-poco-journals`  | **JournalEntry**  | Text Pages. Mantenha formatação Markdown/HTML.                                      |
| `/mecanicas/*.md`     | `corvo-do-poco-journals`  | **JournalEntry**  | Rules Pages.                                                                        |

## Conversão de Campos

### Bestiário -> NPC

- **Nome**: Título do MD.
- **Lore**: Aba "Biography" do NPC.
- **Mecânica**: Traduzir para valores numéricos na aba "Attributes" e "Inventory" (criar Itens do tipo `action` ou `spell`).
- **Imagem**: Gerar com base no Prompt e salvar em `assets/tokens/` ou `assets/art/`.

### População -> NPC

- **Nome**: Título do MD (ex: `[Nome] ([Raça], [Idade])`).
- **Lore/Personalidade**: Aba "Biography" (seção `Public`).
- **Segredos**: Aba "Biography" (seção `GM Only`).

### Missões -> Journal

- **Título**: Nome da Missão.
- **Corpo**: Converter Markdown para HTML.
- **Links**: Inserir links de entidade `@UUID[Actor.ID]{Nome}` quando mencionar NPCs já criados.

## Assets

- Use o prompt definido no Markdown (`/design` ou no próprio arquivo) para gerar a arte.
- Salve em `assets/` e linke no `img` (Actor) ou `src` (Journal Image).
