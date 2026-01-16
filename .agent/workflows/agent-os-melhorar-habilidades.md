---
description: Agent OS workflow for Melhorar Habilidades Antigravity
---

Eu quero que você me ajude a melhorar os arquivos que compõem minhas Skills do Antigravity, reescrevendo suas descrições para que possam ser mais facilmente descobertas e usadas pelo Antigravity quando ele trabalha em tarefas de codificação.

Todas as Skills em nosso projeto estão localizadas em `.agent/skills/`. Cada Skill tem sua própria pasta e dentro de cada pasta de Skill há um arquivo chamado `SKILL.md`.

PERCORRA (LOOP) cada arquivo `SKILL.md` e PARA CADA UM use o seguinte processo para revisar seu conteúdo e melhorá-lo:

## Processo de Melhoria de Skill do Antigravity

### Passo 1: Confirmar quais skills melhorar

Primeiro, peça ao usuário para confirmar se ele quer que TODAS as suas skills do Antigravity sejam melhoradas, ou apenas Skills selecionadas. Assuma que a resposta será "todas", mas peça ao usuário para confirmar exibindo a seguinte mensagem, então AGUARDE a resposta do usuário antes de prosseguir para o Passo 2:

```
Antes de eu prosseguir com a melhoria das suas Skills do Antigravity, você pode confirmar se deseja que eu revise e melhore TODAS as Skills na sua pasta .agent/skills/?

Se não, por favor especifique quais Skills eu devo incluir ou excluir.
```

### Passo 2: Analisar o que esta Skill faz

Analise e leia o arquivo da skill para entender o que é, para que deve ser usada e quando deve ser usada. As melhores práticas específicas são descritas e linkadas dentro dele. Olhe nesses lugares para ler e entender cada skill:

- O nome da Skill e o nome do arquivo.
- O SKILL.md pode conter links que apontam para arquivos em `.agent/rules/` — Siga esses links e leia seu conteúdo.

### Passo 3: Reescrever a descrição da Skill

O elemento mais importante de um arquivo SKILL.md que impacta sua descoberta e capacidade de acionamento pelo Antigravity é o conteúdo que escrevemos na `description` no frontmatter do SKILL.md.

Reescreva esta descrição usando as seguintes diretrizes:

- A primeira frase deve descrever claramente o que é esta skill. Por exemplo: "Escrever código Tailwind CSS e estruturar UIs front-end usando classes utilitárias Tailwind CSS."
- A segunda frase e as subsequentes devem descrever clara e diretamente múltiplos exemplos de onde e quando esta skill deve ser usada.
- Os exemplos de caso de uso podem incluir "Ao escrever ou editar [tipos de arquivo]" onde [tipos de arquivo] pode ser uma lista de extensões de arquivo ou tipos de arquivos ou componentes comumente encontrados em projetos de software.
- Os exemplos de caso de uso também podem incluir situações ou áreas ou ferramentas onde o uso desta skill deve entrar em jogo.
- O texto da descrição pode ser longo. Não há limite máximo de caracteres ou palavras.
- Foque em adicionar exemplos onde a skill DEVE ser usada. Não inclua instruções sobre quando NÃO usar uma skill (nosso objetivo é que a Skill seja encontrada prontamente e usada frequentemente).

### Passo 4: Inserir uma seção para 'Quando usar esta skill'

No topo do conteúdo do SKILL.md, abaixo do frontmatter, insira um cabeçalho H2, "Quando usar esta skill" seguido por uma lista de exemplos de casos de uso.

Os exemplos de casos de uso podem repetir o(s) mesmo(s) listado(s) na descrição e/ou expandi-los.

Exemplo:

```markdown
## Quando usar esta skill:

- [Exemplo descritivo A]
- [Exemplo descritivo B]
- [Exemplo descritivo C]
  ...
```

### Passo 5: Aconselhar o usuário sobre como melhorar suas skills ainda mais

Após revisar TODOS os arquivos SKILL.md localizados na pasta `.agent/skills/` do projeto, exiba a seguinte mensagem ao usuário para aconselhá-lo sobre como melhorar ainda mais suas Skills do Antigravity:

```
Todas as Skills do Antigravity foram analisadas e revisadas!

RECOMENDAÇÃO 👉 Revise e refine-as ainda mais usando estas dicas:

- Torne as Skills o mais descritivas possível
- Use o frontmatter 'description' para dizer ao Antigravity quando ele deve usar essa skill proativamente.
- Inclua todas as instruções, detalhes e diretrizes relevantes dentro do conteúdo da Skill.
- Você pode linkar para outros arquivos (como seus arquivos de regras/rules) usando links markdown.
- Você pode consolidar múltiplas skills similares em skills únicas onde fizer sentido para o Antigravity encontrá-las e usá-las juntas.
```
