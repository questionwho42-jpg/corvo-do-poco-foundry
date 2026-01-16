## Melhores práticas de migração de banco de dados

- **Migrações Reversíveis**: Sempre implemente métodos de rollback/down para permitir reversões seguras de migração
- **Mudanças Pequenas e Focadas**: Mantenha cada migração focada em uma única mudança lógica para clareza e solução de problemas mais fácil
- **Deploy com Zero Downtime**: Considere a ordem de implantação e compatibilidade retroativa para sistemas de alta disponibilidade
- **Separar Schema e Dados**: Mantenha mudanças de esquema separadas de migrações de dados para melhor segurança de rollback
- **Gerenciamento de Índices**: Crie índices em tabelas grandes com cuidado, usando opções concorrentes quando disponíveis para evitar bloqueios (locks)
- **Convenções de Nomenclatura**: Use nomes claros e descritivos que indiquem o que a migração faz
- **Controle de Versão**: Sempre faça commit de migrações para o controle de versão e nunca modifique migrações existentes após o deploy
