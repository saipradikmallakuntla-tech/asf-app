# Plano de descoberta editorial e educação — novembro de 2026

**Edição:** 2026-11-17 · **Responsabilidade institucional e revisão especializada:** a designar pela ASF.

## 1. Mandato e fronteira de publicação

Publicar uma coleção educativa original, em português do Brasil, sem anúncios ou afiliação comercial, exclusivamente no fork `saipradikmallakuntla-tech/asf-app`, branch `editorial/discoverability-education-2026-11-17`, baseada em `dd22ce1cbba4bfd02f09a37a3730d39220aa2131`.

São exatamente 18 novos arquivos Markdown: um índice, seis artigos, seis diretórios e cinco registros de governança. Nenhum arquivo existente é alterado. Não estão autorizados nesta entrega: mudanças em HTML, XML, CSS, JavaScript, outros arquivos de código ou configuração; execução de testes; abertura de PR; merge; mudança no upstream; alteração de workflows ou configurações; envio ao Search Console; implantação do site.

Publicação no GitHub não é implantação em asf.surf. Não há promessa de indexação, posicionamento, tráfego ou disponibilidade de novas rotas públicas no domínio oficial. O conteúdo foi preparado com assistência de IA e não declara revisão profissional ou aprovação institucional já realizada.

## 2. Base observada e qualidade da evidência

Foram lidas documentação, estrutura e definições de automação do repositório, além de páginas públicas com o Exa em consultas forçadas ao vivo em 2026-11-17. Firecrawl não foi utilizado. Busca encontrou candidatos; confirmação exigiu leitura de conteúdo pertinente quando possível. Não se realizaram login, inscrição, envio de dados, exploração de área privada ou execução dos scripts do projeto.

A checagem do fork encontrou Actions desabilitado, Pages desabilitado e nenhum webhook de repositório. As 76 definições de workflow do snapshot foram examinadas quanto a gatilhos. O workflow principal restringe push a `main`; os demais gatilhos de push não correspondem aos 18 caminhos novos. Não foi necessário alterar qualquer configuração para esta publicação. Isso descreve o estado observado, não uma garantia sobre futuras mudanças de configuração ou integrações externas não expostas na inspeção.

O upstream foi apenas lido. Seu snapshot observado foi `96f9f2ea8e4eab7d38a285bf4dccd84bfb461d4e`; a branch editorial não o incorpora nem sincroniza código com ele.

## 3. Prioridades de higiene e descoberta

| Prioridade | Evidência | Ação editorial concreta | Dependência e critério de conclusão |
| --- | --- | --- | --- |
| P0 | Maré, Vento e Swell: CRAWL_NOT_FOUND, com 404 reportado pelo Exa. | Não acrescentar novas recomendações dessas URLs; registrar entradas conhecidas e destino temático proposto ASF Previsão. | Uma pessoa responsável confirma o estado no navegador e aprova qualquer correção técnica futura. Não declarar redirect instalado. |
| P0 | ASF Eventos informa descontinuação; Galeria informa unificação com o app. | Distinguir aviso de migração de serviço ativo; não inventar agenda, upload ou rota profunda. | Confirmar destino de navegação e atualizar a mensagem de cada referência em trabalho separado. |
| P0 | URL antiga de boletim CETESB devolve conteúdo genérico. | Usar página institucional atual e PDF pertinente, com data e limites; manter o legado no registro de cautelas. | Última checagem e data da edição do PDF ficam visíveis; não tratar abertura genérica como boletim válido. |
| P1 | Duas entradas do site raiz recuperaram conteúdo equivalente; source atual declara canonical em asf.surf. | Padronizar a identidade editorial principal como asf.surf, mantendo a origem GitHub Pages identificada como alternativa técnica. | Não confundir conteúdo equivalente com prova de duplicação no índice. Cadeias HTTP e canonical das páginas internas exigem verificação própria. |
| P1 | Hub Aprender apresenta guias introdutórios; comunidade inclui acesso autenticado. | Acrescentar intenções complementares e um índice público de arquivos, sem copiar guias ou expor conteúdo de membros. | Cada pacote tem pergunta exclusiva, fontes e links de continuidade. Uma futura navegação no site depende de aprovação fora deste escopo. |
| P1 | Algumas fontes oficiais têm timeout ou interface dinâmica. | Publicar estados de verificação graduados, com finalidade e data, em vez de “todos os links funcionando”. | Uma entrada não confirmada permanece assim até nova evidência. |
| P2 | Não há acesso a dados de Search Console nesta entrega. | Definir indicadores e solicitar revisão humana futura, sem alegar números ou diagnóstico de indexação. | Responsável e janela de comparação são registrados antes de divulgar resultados. |

## 4. Seis pacotes e diferenciação editorial

O hub Aprender consultado apresenta temas como início no surf, primeira prancha, etiqueta, remada e correntes. O plano de conteúdo antigo do snapshot cobre, entre outros, previsão básica, prancha, praias, yoga e nutrição. Esta edição não produz novas versões desses guias genéricos. A classificação é complementar, com limite de comparação pública: não se declara auditoria exaustiva de todo texto histórico ou de conteúdo privado.

| Pacote | Intenção principal | Valor original e limite de não duplicação |
| --- | --- | --- |
| [Balneabilidade](../../../publicacoes/balneabilidade/artigo.md) | Como consultar qualidade da água antes do surf. | Ponto de coleta, datas e limites da classificação; não lista “praias seguras”. |
| [Previsão e avisos oficiais](../../../publicacoes/previsao-e-avisos-oficiais/artigo.md) | Como separar previsão, aviso e tábua. | Proveniência, vigência e fuso; não refaz guia genérico de altura e período. |
| [Encontros e privacidade](../../../publicacoes/encontros-e-privacidade/artigo.md) | Como organizar uma saída sem expor rotina. | Minimização de dados e diferença entre convite público e coordenação restrita. |
| [Imagens e consentimento](../../../publicacoes/imagens-e-consentimento/artigo.md) | Como conversar sobre captação, publicação e retirada. | Contexto, recusa e direitos distintos; não oferece autorização jurídica genérica. |
| [Aula acessível](../../../publicacoes/aula-acessivel/artigo.md) | O que perguntar antes da primeira aula. | Cadeia de acesso, autonomia e capacidade real de apoio; não prescreve adaptação ou terapia. |
| [Verificar eventos](../../../publicacoes/verificar-eventos/artigo.md) | Como confirmar um convite e sua atualidade. | Fonte independente, mudanças e dados; não cria calendário ou inscrição fictícia. |

Cada pacote tem `artigo.md` e `recursos.md`. Os diretórios justificam cada fonte; não são listas de backlinks, recomendações comerciais ou um segundo texto concorrente com o artigo.

## 5. Arquitetura editorial desta edição

O [índice da coleção](../../../publicacoes/README.md) aponta para todos os 12 arquivos de leitura e para os cinco registros de governança. Artigos ligam seu diretório, o índice e leituras relacionadas. Diretórios retornam ao artigo e informam critérios de manutenção. O [mapa de links](MAPA-DE-LINKS.md) define a intenção de cada ligação.

Usar títulos descritivos, um H1 por arquivo, abertura que responda à pergunta e linguagem sem exageros. Não forçar variações de palavra-chave, criar estatísticas, publicar resenhas fictícias ou copiar texto das fontes. Sem imagens nesta edição, para não introduzir direitos ou arquivos adicionais. Descrições para eventual adoção no site são decisões futuras; não há tags ou front matter que finjam implementar metadados técnicos.

## 6. Fila futura, sem execução técnica nesta entrega

1. Responsável editorial da ASF revisa identidade, linguagem e relação com conteúdos existentes.
2. Pessoas habilitadas avaliam afirmações de segurança, proteção de dados, imagem e acessibilidade conforme o tema.
3. Responsável por URLs confirma no navegador destinos de satélites, comportamento HTTP e mensagens de migração; registra a evidência antes de propor correções.
4. Somente com nova autorização, a equipe do site decide se adotará os textos, quais serão suas URLs e quais páginas já existentes devem receber ligações. Canonical, sitemap, redirects, robots e HTML ficam fora desta entrega.
5. Após uma publicação real no site, uma pessoa com acesso ao Search Console pode inspecionar URLs e acompanhar descoberta, indexação e consultas. Solicitação não garante indexação.

## 7. Manutenção e indicadores

Antes de toda saída, participantes precisam consultar novamente dados dinâmicos; a periodicidade editorial não substitui essa consulta. Para os diretórios, propor revisão mensal, revisão na virada do ano para URLs anuais e revisão imediata após relato de falha ou mudança institucional. Não alterar a data sem uma nova checagem.

Indicadores de governança: arquivos esperados presentes, links internos resolvíveis, entradas com data e estado, pendências sem falsa confirmação e divergências com responsável definido. Indicadores de busca futuros: descoberta, URL canônica selecionada, páginas indexadas e consultas pertinentes em uma janela documentada. Não há linha de base quantitativa ou resultado de ranqueamento afirmado aqui.

## Documentos relacionados

[Inventário de URLs](INVENTARIO-URLS.md) · [Mapa de links](MAPA-DE-LINKS.md) · [Critérios de revisão](CRITERIOS-DE-REVISAO.md) · [Changelog](CHANGELOG.md) · [Coleção](../../../publicacoes/README.md)
