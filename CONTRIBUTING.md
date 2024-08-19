# Contribuindo para o Projeto 8-Puzzle

Obrigado por contribuir para o projeto! Para manter a qualidade e consistência do código, estamos seguindo as diretrizes do **PEP 8**. Este documento descreve o estilo de código, convenções de nomeação e ferramentas recomendadas para garantir que todos os colaboradores estejam alinhados.

## Estilo de Código

### Regras de Indentação

- Utilize **4 espaços** por nível de indentação.
- **Não utilize tabs**. Configure seu editor ou IDE para substituir tabs por espaços automaticamente.
- Revise seu código antes de submetê-lo para garantir que todos os níveis de indentação estejam corretos e consistentes.

### Convenções de Nomeação

Para garantir consistência e legibilidade em todo o projeto, seguimos as convenções de nomeação recomendadas pelo **PEP 8**:

#### Variáveis e Funções
- Use o estilo **snake_case**: todas as letras em minúsculas e palavras separadas por underscores (`_`).
- Exemplos:
  - Variável: `minha_variavel`
  - Função: `minha_funcao()`

#### Classes
- Use o estilo **PascalCase**: cada palavra começa com uma letra maiúscula, sem underscores.
- Exemplo: `MinhaClasse`

Essas convenções seguem as melhores práticas para facilitar a leitura e manutenção do código.

## Ferramentas de Formatação

Para manter o código alinhado com o estilo PEP 8, recomendamos o uso das seguintes ferramentas:

- **Black**: Um formatador automático que aplica o estilo PEP 8 ao código.
- **autopep8**: Uma ferramenta que corrige problemas de estilo de acordo com o PEP 8.

### Automação de Formatação

Você pode configurar um **pre-commit hook** para automatizar a formatação do código antes de cada commit. Isso garantirá que o código submetido ao repositório esteja sempre dentro das regras estabelecidas.

## Exemplo de Indentação Correta

```python
def exemplo_funcao():
    if condicao:
        executar_acao()
    else:
        executar_acao_alternativa()
