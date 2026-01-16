## Padrões e convenções de endpoints de API

- **Design RESTful**: Siga princípios REST com URLs claras baseadas em recursos e métodos HTTP apropriados (GET, POST, PUT, PATCH, DELETE)
- **Nomeação Consistente**: Use convenções de nomenclatura consistentes, em minúsculas, com hífens ou sublinhados para endpoints em toda a API
- **Versionamento**: Implemente uma estratégia de versionamento de API (caminho da URL ou headers) para gerenciar mudanças que quebram a compatibilidade sem impactar clientes existentes
- **Substantivos no Plural**: Use substantivos no plural para endpoints de recursos (ex: `/usuarios`, `/produtos`) para consistência
- **Recursos Aninhados**: Limite a profundidade de aninhamento a 2-3 níveis no máximo para manter URLs legíveis e sustentáveis
- **Parâmetros de Consulta**: Use query parameters para filtragem, ordenação, paginação e busca em vez de criar endpoints separados
- **Códigos de Status HTTP**: Retorne códigos de status HTTP apropriados e consistentes que reflitam com precisão a resposta (200, 201, 400, 404, 500, etc.)
- **Headers de Rate Limiting**: Inclua informações de limite de taxa nos headers de resposta para ajudar clientes a gerenciar seu uso
