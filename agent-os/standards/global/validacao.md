## Melhores práticas de validação

- **Valide no Lado do Servidor**: Sempre valide no servidor; nunca confie apenas na validação do lado do cliente para segurança ou integridade de dados
- **Lado do Cliente para UX**: Use validação no cliente para feedback imediato, mas duplique as verificações no servidor
- **Falhe Cedo**: Valide entradas o mais cedo possível e rejeite dados inválidos antes do processamento
- **Mensagens de Erro Específicas**: Forneça mensagens de erro claras e específicas por campo que ajudem os usuários a corrigir sua entrada
- **Listas de Permissão (Allowlists) sobre Listas de Bloqueio**: Quando possível, defina o que é permitido em vez de tentar bloquear tudo o que não é
- **Validação de Tipo e Formato**: Verifique tipos de dados, formatos, intervalos e campos obrigatórios sistematicamente
- **Sanitização de Entrada**: Sanitize a entrada do usuário para prevenir ataques de injeção (SQL, XSS, injeção de comando)
- **Validação de Regras de Negócio**: Valide regras de negócio (ex: saldo suficiente, datas válidas) na camada de aplicação apropriada
- **Validação Consistente**: Aplique validação consistentemente em todos os pontos de entrada (formulários web, endpoints de API, jobs em background)
