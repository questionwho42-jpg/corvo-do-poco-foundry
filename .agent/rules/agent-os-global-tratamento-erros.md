## Melhores práticas de tratamento de erros

- **Mensagens Amigáveis ao Usuário**: Forneça mensagens de erro claras e acionáveis aos usuários, sem expor detalhes técnicos ou informações de segurança
- **Falhe Rápido e Explicitamente**: Valide entradas e pré-condições cedo; falhe com mensagens claras em vez de permitir estados inválidos
- **Tipos de Exceção Específicos**: Use tipos de exceção/erro específicos em vez de genéricos para permitir tratamento direcionado
- **Tratamento de Erros Centralizado**: Trate erros nas fronteiras apropriadas (controllers, camadas de API) em vez de espalhar blocos try-catch por todo lugar
- **Degradação Graciosa**: Projete sistemas para degradar graciosamente quando serviços não críticos falham, em vez de quebrar completamente
- **Estratégias de Tentativa (Retry)**: Implemente recuo exponencial (exponential backoff) para falhas transitórias em chamadas de serviços externos
- **Limpeza de Recursos**: Sempre limpe recursos (arquivos abertos, conexões) em blocos `finally` ou mecanismos equivalentes
