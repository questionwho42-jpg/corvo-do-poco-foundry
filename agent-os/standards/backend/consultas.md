## Melhores práticas de consultas de banco de dados

- **Previna Injeção de SQL**: Sempre use consultas parametrizadas ou métodos ORM; nunca interpole entrada do usuário em strings SQL
- **Evite Consultas N+1**: Use eager loading ou joins para buscar dados relacionados em uma única consulta em vez de múltiplas consultas
- **Selecione Apenas Dados Necessários**: Solicite apenas as colunas que você precisa em vez de usar SELECT \* para melhor desempenho
- **Indexe Colunas Estratégicas**: Indexe colunas usadas em cláusulas WHERE, JOIN e ORDER BY para otimização de consultas
- **Use Transações para Mudanças Relacionadas**: Envolva operações de banco de dados relacionadas em transações para manter a consistência dos dados
- **Defina Timeouts de Consulta**: Implemente timeouts para prevenir que consultas descontroladas impactem o desempenho do sistema
- **Cache de Consultas Caras**: Faça cache de resultados de consultas complexas ou executadas frequentemente quando apropriado
