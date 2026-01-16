## Melhores práticas de cobertura de testes

- **Escreva Testes Mínimos Durante o Desenvolvimento**: NÃO escreva testes para cada mudança ou passo intermediário. Foque em completar a implementação da funcionalidade primeiro, depois adicione testes estratégicos apenas em pontos de conclusão lógica
- **Teste Apenas Fluxos de Usuário Principais**: Escreva testes exclusivamente para caminhos críticos e fluxos de trabalho primários do usuário. Pule a escrita de testes para utilitários não críticos e fluxos secundários até se/quando for instruído a fazê-lo.
- **Adie Testes de Casos de Borda**: NÃO teste casos de borda, estados de erro ou lógica de validação a menos que sejam críticos para o negócio. Estes podem ser endereçados em fases de teste dedicadas, não durante o desenvolvimento de funcionalidades.
- **Teste Comportamento, Não Implementação**: Foque testes no que o código faz, não como ele faz, para reduzir fragilidade
- **Nomes de Teste Claros**: Use nomes descritivos que expliquem o que está sendo testado e o resultado esperado
- **Mock de Dependências Externas**: Isole unidades fazendo mock de bancos de dados, APIs, sistemas de arquivos e outros serviços externos
- **Execução Rápida**: Mantenha testes unitários rápidos (milissegundos) para que desenvolvedores os executem frequentemente durante o desenvolvimento
