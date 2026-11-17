# Inventário de URLs e evidências — 2026-11-17

**Método:** leitura pública com Exa, solicitando coleta ao vivo, e leitura somente de consulta pela API do GitHub. **Data das tentativas listadas:** 2026-11-17.

Os estados descrevem a consulta, não uma promessa de disponibilidade. Erro do coletor não equivale necessariamente a resposta HTTP do servidor de origem. Não foram medidos redirecionamentos completos, desempenho, cobertura de índice, todas as funcionalidades ou conteúdo autenticado. Resultados de busca são candidatos, não confirmação de acesso.

## 1. Domínio principal e repositórios

| URL | Estado observado | Última checagem | Decisão editorial |
| --- | --- | --- | --- |
| [asf.surf](https://asf.surf/) | Conteúdo público recuperado. | 2026-11-17 | Identidade principal recomendada para referências ao site oficial; nenhuma nova rota é implantada nesta coleção. |
| [Origem GitHub Pages](https://acarolmourad-commits.github.io/asf-app/) | Conteúdo público equivalente ao da raiz asf.surf recuperado. | 2026-11-17 | Não chamar a equivalência de prova de duplicação no índice; comportamento HTTP final requer verificação própria. |
| [Fonte da homepage no upstream observado](https://github.com/acarolmourad-commits/asf-app/blob/96f9f2ea8e4eab7d38a285bf4dccd84bfb461d4e/index.html) | API recuperou source com canonical `https://asf.surf/`. | 2026-11-17 | Evidência do source daquele snapshot; não comprova escolha de canonical por buscadores nem canonical das páginas internas. |
| [CNAME no upstream observado](https://github.com/acarolmourad-commits/asf-app/blob/96f9f2ea8e4eab7d38a285bf4dccd84bfb461d4e/CNAME) | API recuperou `asf.surf`. | 2026-11-17 | Evidência de configuração armazenada; não é auditoria de DNS. |
| [robots.txt no upstream observado](https://github.com/acarolmourad-commits/asf-app/blob/96f9f2ea8e4eab7d38a285bf4dccd84bfb461d4e/robots.txt) | Source permite raiz, desautoriza rastreio de `/docs/`, `/scripts/` e `/meta-integration/`, e referencia sitemap em asf.surf. | 2026-11-17 | Bloqueio de rastreio não equivale a noindex. Não alterar nem alegar desindexação comprovada. |
| [README do fork no commit-base](https://github.com/saipradikmallakuntla-tech/asf-app/blob/dd22ce1cbba4bfd02f09a37a3730d39220aa2131/README.md) | Conteúdo conferido pela API; descreve publicação em Pages por `main`. | 2026-11-17 | A configuração efetiva do fork foi checada separadamente: Pages e Actions desabilitados. |

## 2. Hubs e satélites públicos

| URL | Estado observado | Última checagem | Encaminhamento |
| --- | --- | --- | --- |
| [Aprender](https://asf.surf/aprender/index.html) | Conteúdo do índice recuperado. | 2026-11-17 | Evitar duplicar guias introdutórios apresentados. As páginas filhas não foram todas abertas individualmente nesta rodada. |
| [Sessões Interativas](https://asf.surf/sessoes-interativas.html) | Interface pública de validação recuperada. | 2026-11-17 | Separar descoberta pública de experiência autenticada. Nenhum login ou sala foi verificado. |
| [Sobre](https://asf.surf/sobre.html) | Texto institucional recuperado. | 2026-11-17 | Referência de identidade; não comprova agenda ou representante de um convite específico. |
| [ASF Previsão](https://acarolmourad-commits.github.io/asf-previsao/) | Texto explicativo recuperado; declara previsão de modelo. | 2026-11-17 | Destino temático observado para condições; mapas e dados não exercitados. |
| [ASF Segurança](https://acarolmourad-commits.github.io/asf-seguranca/) | Texto público recuperado. | 2026-11-17 | Acessibilidade da página não é revisão profissional de todas as instruções; não reproduzir procedimentos de resgate sem validação. |
| [ASF Leitura](https://acarolmourad-commits.github.io/asf-leitura/) | Texto público recuperado. | 2026-11-17 | Não tratar expressões de dados ao vivo como medição local sem verificação da fonte. |
| [ASF Maré](https://acarolmourad-commits.github.io/asf-mare/) | Exa: CRAWL_NOT_FOUND, com 404 reportado. | 2026-11-17 | Não acrescentar novas recomendações. Destino temático proposto: ASF Previsão; não há redirect comprovado nesta entrega. |
| [ASF Vento](https://acarolmourad-commits.github.io/asf-vento/) | Exa: CRAWL_NOT_FOUND, com 404 reportado. | 2026-11-17 | Mesma fila de higiene; confirmar comportamento no navegador antes de uma correção técnica. |
| [ASF Swell](https://acarolmourad-commits.github.io/asf-swell/) | Exa: CRAWL_NOT_FOUND, com 404 reportado. | 2026-11-17 | Não criar substituto editorial redundante nem declarar uma migração técnica já executada. |
| [ASF Eventos](https://acarolmourad-commits.github.io/asf-eventos/) | Texto declara descontinuação da página independente e orienta procurar o app ASF. | 2026-11-17 | Marcar aposentado informado, não agenda ativa. Nenhum calendário específico confirmado. |
| [ASF Comunidade](https://acarolmourad-commits.github.io/asf-comunidade/) | Conteúdo público recuperado. | 2026-11-17 | Mentorias e agenda mencionadas não foram confirmadas como ofertas atuais; revisar mensagens de continuidade. |
| [ASF Galeria](https://acarolmourad-commits.github.io/asf-galeria/) | Texto informa unificação com o app ASF. | 2026-11-17 | Não afirmar funcionamento independente de upload ou de moderação. |

## 3. Referências externas dos seis diretórios

| URL | Estado observado | Última checagem | Uso ou pendência |
| --- | --- | --- | --- |
| [CETESB — Praias Litorâneas](https://www.cetesb.sp.gov.br/cetesb/qualidade_ambiental/agua/praias_litoraneas) | Texto pertinente recuperado. | 2026-11-17 | Referência institucional principal sobre monitoramento paulista. |
| [CETESB — boletim PDF 2026](https://sistemasinter.cetesb.sp.gov.br/praias/boletim-semanal-balneabilidade-praias-2026.pdf) | PDF recuperado; documento observado de 12/11/2026. | 2026-11-17 | Conferir data a cada uso; revisar URL anual. Não transcrever classificações para recomendações permanentes. |
| [CETESB — antiga página semanal](https://cetesb.sp.gov.br/praias/boletim-semanal/) | Conteúdo genérico, não o boletim esperado. | 2026-11-17 | Destino inadequado para recomendação direta de boletim; cadeia HTTP não comprovada. |
| [CETESB — mapa de classificação semanal](https://arcgis.cetesb.sp.gov.br/portal/apps/experiencebuilder/experience?id=5caf462c81a04896baf8f3916121b8ff&page=Classifica%C3%A7%C3%A3o-Semanal) | Extração vazia no Exa. | 2026-11-17 | Não confirmado; conferir manualmente a interface. Não inferir erro do servidor de origem. |
| [CETESB — planilha legada](https://sistemasinter.cetesb.sp.gov.br/praias/excel/boletim.php) | Extração vazia no Exa. | 2026-11-17 | Não confirmado; não recomendar como única fonte. |
| [ANPD — direitos dos titulares](https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados/direito-dos-titulares) | Texto pertinente recuperado. | 2026-11-17 | Informação educativa, não parecer sobre caso concreto. |
| [ANPD — dados de crianças e adolescentes](https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-divulga-enunciado-sobre-o-tratamento-de-dados-pessoais-de-criancas-e-adolescentes) | Texto pertinente recuperado; notícia de 24/05/2023. | 2026-11-17 | Preservar data original e reconhecer possibilidade de orientações posteriores. |
| [ISA — Para Surfing](https://isasurf.org/learning/para-surfing/) | Texto pertinente recuperado. | 2026-11-17 | Separar recursos competitivos de participação recreativa; não endossar documentos vinculados sem revisão própria. |
| [ISA — Adaptive Surfing Instructor Program](https://isasurf.org/learning/para-surfing/isa-adaptive-surfing-instructor-program/) | Texto pertinente recuperado. | 2026-11-17 | Não confirma certificação de pessoa, vagas ou condições de escola. |
| [Marinha — TábuaMares](https://pam.marinha.mil.br/tabuamares/tabuamares.html) | Interface com seleção de estação e data recuperada. | 2026-11-17 | Operação e dados por estação não verificados. |
| [CHM — Tábuas de Maré 2026](https://www.marinha.mil.br/chm/tabuas-de-mare-6) | CRAWL_LIVECRAWL_TIMEOUT no Exa. | 2026-11-17 | Não confirmado, não classificado como quebrado; conferir ano e conteúdo no navegador. |
| [CHM — Avisos de Mau Tempo](https://www.marinha.mil.br/chm/dados-do-smm-avisos-de-mau-tempo/avisos-de-mau-tempo) | Texto pertinente recuperado; página indicava atualização em 17/11/2026. | 2026-11-17 | Consultar novamente antes de decidir; não congelar os avisos desta edição. |
| [CHM — Previsão 48 Horas](https://www.marinha.mil.br/chm/dados-do-smm-meteoromarinha/previsao-48-horas) | CRAWL_LIVECRAWL_TIMEOUT no Exa. | 2026-11-17 | Não confirmado. Não usar resultado de busca como prova de funcionamento atual. |

## 4. Descoberta não é indexação comprovada

A leitura pública confirma que o coletor recuperou conteúdo, quando assim indicado. Não mostra a URL indexada, a canonical escolhida pelo Google, impressões, cliques, posições ou cobertura completa da rede ASF. Nenhum número de Search Console foi consultado ou inventado. A documentação antiga foi tratada como evidência histórica, não como laudo atual de todos os satélites.

Este inventário é delimitado às URLs explicitamente listadas; não é um rastreamento exaustivo da internet ou de todos os links do repositório. Os 18 arquivos novos são ligados entre si pelo [mapa de links](MAPA-DE-LINKS.md), sem prometer implantação ou indexação automática.

[Plano](PLANO.md) · [Critérios de revisão](CRITERIOS-DE-REVISAO.md) · [Changelog](CHANGELOG.md) · [Coleção](../../../publicacoes/README.md)
