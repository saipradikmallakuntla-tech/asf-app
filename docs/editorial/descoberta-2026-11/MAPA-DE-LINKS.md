# Mapa de links, intenção e continuidade editorial

**Edição:** 2026-11-17 · **Escopo:** os 18 novos arquivos Markdown desta coleção.

## 1. Regras de ligação

Usar caminhos relativos para navegar dentro da branch. Assim, a revisão permanece no mesmo conjunto de arquivos, sem enviar a leitora para `main` ou para uma página de asf.surf ainda inexistente. Não usar âncoras de fragmento nesta edição: os destinos são arquivos completos, para reduzir dependência de geração de identificadores de títulos.

As ligações externas usam URL completa e rótulo descritivo. Os diretórios documentam a situação observada em cada entrada. Um link para uma fonte é referência, não anúncio, afiliação ou afirmação de segurança. URLs legadas ou não confirmadas ficam em contexto de cautela, nunca como recomendação silenciosa.

## 2. Hub de entrada

O [índice de publicações](../../../publicacoes/README.md) liga os seis artigos e os seis diretórios, além dos cinco registros de governança. Cada artigo e diretório possui retorno ao índice. O índice novo não é ligado a partir do README raiz porque esta entrega não altera arquivos existentes.

Consequência explícita: existe navegação interna completa na coleção, mas não se declara que ela deixou de ser órfã em toda a navegação do repositório ou do site. A ligação a partir de um hub já existente é uma decisão futura, sujeita a autorização e revisão editorial.

## 3. Pares de publicação e suas próximas leituras

| Entrada educativa | Referências companheiras | Próximas leituras no artigo | Motivo editorial |
| --- | --- | --- | --- |
| [Balneabilidade](../../../publicacoes/balneabilidade/artigo.md) | [Diretório](../../../publicacoes/balneabilidade/recursos.md) | Previsão e avisos; encontros e privacidade. | Separar água de condições de mar e permitir planejar sem expor rotina. |
| [Previsão e avisos oficiais](../../../publicacoes/previsao-e-avisos-oficiais/artigo.md) | [Diretório](../../../publicacoes/previsao-e-avisos-oficiais/recursos.md) | Balneabilidade; verificar eventos. | Conectar limites de fontes com decisões de saída, sem transformar previsão em autorização. |
| [Encontros e privacidade](../../../publicacoes/encontros-e-privacidade/artigo.md) | [Diretório](../../../publicacoes/encontros-e-privacidade/recursos.md) | Imagens e consentimento; verificar eventos. | Diferenciar logística, dados e escolha de divulgação. |
| [Imagens e consentimento](../../../publicacoes/imagens-e-consentimento/artigo.md) | [Diretório](../../../publicacoes/imagens-e-consentimento/recursos.md) | Encontros e privacidade; aula acessível. | Relacionar autonomia e contexto de participação sem copiar o guia de dados. |
| [Aula acessível](../../../publicacoes/aula-acessivel/artigo.md) | [Diretório](../../../publicacoes/aula-acessivel/recursos.md) | Imagens e consentimento; encontros e privacidade. | Apoiar escolhas e comunicação sem prescrever procedimentos. |
| [Verificar eventos](../../../publicacoes/verificar-eventos/artigo.md) | [Diretório](../../../publicacoes/verificar-eventos/recursos.md) | Encontros e privacidade; previsão e avisos. | Confirmar origem, atualidade, dados e limites de uma saída. |

Os nomes de próximas leituras nesta tabela descrevem ligações presentes nos respectivos artigos; não são promessa de que todas as relações da coleção sejam simétricas. Cada diretório retorna ao próprio artigo, ao índice e aos critérios de revisão.

## 4. Governança e leitura responsável

| Registro | Função | Ligações estruturais |
| --- | --- | --- |
| [PLANO.md](PLANO.md) | Mandato, prioridades, diferenciação e fila futura. | Coleção, seis artigos, inventário, mapa, critérios e changelog. |
| [INVENTARIO-URLS.md](INVENTARIO-URLS.md) | Evidências datadas e limitações das URLs observadas. | Plano, mapa, critérios, changelog e coleção. |
| [MAPA-DE-LINKS.md](MAPA-DE-LINKS.md) | Este mapa de navegação e intenção. | Todos os 18 arquivos por seus papéis de entrada, conteúdo e governança. |
| [CRITERIOS-DE-REVISAO.md](CRITERIOS-DE-REVISAO.md) | Critérios de aceite e revisão futura. | Plano, inventário, mapa, changelog e coleção. |
| [CHANGELOG.md](CHANGELOG.md) | Histórico e limites da entrega. | Os demais registros e a coleção. |

## 5. Destinos públicos existentes: relações futuras, não alterações feitas

- **Aprender:** possível ponto de apresentação dos novos temas, após comparação de conteúdo e aprovação. Não inserir outra versão de primeira prancha, remada ou correntes.
- **ASF Previsão:** referência de contexto para o artigo de proveniência das fontes. Não substituir avisos oficiais nem criar novos satélites de Maré, Vento ou Swell.
- **Comunidade e Sessões Interativas:** manter separação entre explicação pública de participação e conteúdo restrito. Nunca expor credenciais ou listas de membros para melhorar busca.
- **Galeria:** esclarecer que a interface observada se apresenta como unificada ao app; não prometer upload ou moderação não verificados.
- **Eventos:** manter o aviso de aposentadoria identificado; só adicionar um destino atual após confirmação do canal responsável. Não inventar rota para a agenda.

As evidências e URLs completas desses destinos estão no [inventário](INVENTARIO-URLS.md). As relações acima são backlog editorial; não são mudanças executadas no site.

## 6. Prevenção de canibalização e ligações artificiais

Uma intenção principal por artigo; o diretório responde “onde conferir e com qual limite”, sem republicar o artigo. Não criar páginas por variação mínima de palavra-chave, listas de “melhores” sem critérios ou cadeias de links com finalidade exclusiva de ranqueamento. A escolha de uma futura URL oficial precisa preservar propósito e evitar competir com um guia equivalente já existente.

## 7. Conferência posterior à gravação

A API Contents deve ser chamada para cada um dos 18 caminhos na branch correta. A conferência precisa ler o conteúdo retornado, resolver os destinos relativos e relacionar os arquivos ao commit e ao diff. O campo `sha` de uma resposta de arquivo é o SHA do blob, não o SHA do commit: o recibo de publicação deve distingui-los.

A conferência é análise de documentos retornados pela API, não execução de testes do projeto. Não se executam scripts, workflows, navegador de login ou implantação. O resultado final será registrado no recibo da publicação, sem adicionar um décimo nono arquivo ao repositório.

[Plano](PLANO.md) · [Inventário](INVENTARIO-URLS.md) · [Critérios](CRITERIOS-DE-REVISAO.md) · [Changelog](CHANGELOG.md) · [Coleção](../../../publicacoes/README.md)
