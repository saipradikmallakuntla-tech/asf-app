# Critérios de revisão editorial, referências e descoberta

**Edição:** 2026-11-17 · **Aplicação:** coleção em Markdown no fork; nenhuma mudança técnica de site é autorizada por este documento.

## 1. Integridade de escopo

- Exatamente 18 novos caminhos, todos terminados em `.md`, sob `publicacoes/` e `docs/editorial/descoberta-2026-11/`.
- Nenhum arquivo preexistente editado, excluído, renomeado ou sobrescrito.
- Branch `editorial/discoverability-education-2026-11-17`, criada em `dd22ce1cbba4bfd02f09a37a3730d39220aa2131`, somente no fork `saipradikmallakuntla-tech/asf-app`.
- Sem alterações no upstream, em `main`, código, configurações, workflows, HTML, XML, CSS ou JavaScript.
- Sem PR, merge, testes, execução de scripts do projeto, implantação, envio ao Search Console ou alteração de domínio.

A inspeção de arquivos de código ou de workflows é somente leitura para compreender a publicação. Ler uma definição não significa executá-la. As configurações atuais observadas do fork não devem ser alteradas como parte deste trabalho.

## 2. Originalidade e intenção

Antes de futura adoção, comparar título, propósito e abertura com guias existentes. Classificar a peça como complementar, equivalente, obsoleta ou conflitante. Equivalência exige revisar o conteúdo existente em vez de criar uma nova página concorrente. Esta coleção declara o limite da comparação feita: índice público, documentação e estrutura observada não equivalem a leitura exaustiva de todo o acervo.

Cada artigo precisa ter uma pergunta específica, uma resposta útil na abertura, seções próprias, limites claros e referências pertinentes. Não usar paráfrase extensa de fontes, estatística sem comprovação, data falsa de atualização, depoimento inventado ou otimização por repetição de palavras-chave. Os seis diretórios devem acompanhar o respectivo artigo, sem virar um segundo artigo sobre o mesmo assunto.

## 3. Segurança e precisão temática

- **Água:** distinguir balneabilidade de condições do mar; identificar ponto e data; não criar lista de praias seguras ou prazo universal pós-chuva.
- **Previsão:** distinguir modelo, observação, aviso e tábua; conferir vigência e fuso; não dar autorização individual de entrada.
- **Dados e imagem:** não tratar consentimento como hipótese única para qualquer caso; distinguir direitos de imagem, proteção de dados e autoria; respeitar melhor interesse de menores e condições legais de pedidos.
- **Acessibilidade:** priorizar autonomia, descrição de barreiras e capacidade real de apoio; não prescrever transferências, equipamentos ou terapia; não confundir competição com participação recreativa.
- **Eventos:** não inventar vagas, datas, preços, organizadoras ou links de inscrição; identificar descontinuação e informação não confirmada.

Instruções de salvamento, recomendação clínica, interpretação jurídica específica e certificação profissional exigem revisão especializada antes de eventual inclusão. Uma ressalva genérica não corrige um conselho perigoso. Não transferir para esta coleção afirmações não revisadas só porque existem em um satélite.

## 4. Vocabulário de verificação de URLs

| Estado editorial | Evidência mínima | O que não permite afirmar |
| --- | --- | --- |
| Conteúdo conferido | Coleta ao vivo retorna texto pertinente à finalidade da entrada. | Operação completa, correção de todas as afirmações, acesso futuro, certificação ou segurança. |
| Interface conferida; operação não verificada | Página de interface recuperada, sem exercer o fluxo. | Funcionamento de login, mapas, seleção de estação, upload ou envio de e-mail. |
| Destino inadequado | Conteúdo recuperado difere da finalidade esperada. | Código HTTP, descontinuação definitiva ou cadeia de redirects sem evidência própria. |
| Não confirmado | Timeout, extração vazia ou informação insuficiente. | Site quebrado, erro HTTP original, encerramento ou resultado favorável. |
| Aposentado informado | A própria página declara descontinuação ou unificação. | Que um redirect 301 esteja instalado ou que todas as funcionalidades migraram. |
| CRAWL_NOT_FOUND reportado | O Exa informa essa condição e um código de referência. | Verificação independente de DNS, configuração ou toda a cadeia HTTP. |

Toda entrada externa de diretório deve conter responsável ou contexto, finalidade, estado, última checagem e limite relevante. Distinguir data de consulta, data de publicação e data de atualização da fonte. Uma notícia antiga recuperada hoje continua sendo uma notícia antiga. Conteúdo dinâmico deve ser reaberto no momento de uso.

Não se repetem coletas idênticas sem necessidade; uma alternativa oficial pode ser procurada quando falha a principal. Uma pendência honesta é melhor que um estado positivo inventado. Fontes oficiais também podem ter conteúdo histórico ou interfaces que o coletor não extrai.

## 5. Privacidade e independência comercial

Não publicar dados de membros, listas de presença, documentos, credenciais, conversas privadas ou autorizações assinadas. Não solicitar dados pessoais por issue ou comentário público. Não prometer anonimização apenas com desfoque de rosto ou sigilo absoluto em um grupo.

Não incluir anúncios, cupons, links afiliados, códigos promocionais, obrigação de compra, endosso de fornecedor ou promessa de retorno. Uma página externa pode ter seus próprios links comerciais; sua presença como referência de contexto não é recomendação de compra desta coleção.

## 6. Navegação e inspeção pela API

O índice deve levar a todos os artigos, diretórios e registros. Cada artigo retorna ao índice e ao próprio diretório e oferece leituras relacionadas; cada diretório retorna ao artigo, ao índice e aos critérios. Os arquivos de governança devem manter uma rota até a coleção.

Após o commit, ler explicitamente cada caminho pela API Contents com `ref` da branch editorial, decodificar a resposta e conferir o texto. Relacionar os SHAs de blob retornados com o diff ou a árvore do commit. Resolver todos os links relativos para arquivos presentes, sem tratar texto entre crases como link. Não basta verificar só a existência ou a resposta do commit de escrita.

Conferir também o commit: pai igual ao base aprovado, exatamente 18 arquivos adicionados, nenhuma exclusão ou modificação. O SHA do blob é diferente do SHA do commit. O recibo final deve apresentar URLs diretas e o commit de publicação para os 18 caminhos, além do resultado da conferência de navegação.

Essa conferência é análise de respostas e de documentos, não execução de testes ou scripts do projeto. Não se adiciona arquivo de teste nem um registro extra ao repositório.

## 7. Revisão futura e tratamento de pendências

Propor revisão mensal dos diretórios, revisão na mudança de ano para URLs anuais e revisão imediata após alerta de falha ou mudança institucional. Não atualizar a data sem refazer a consulta. Não remover uma ressalva até existir evidência suficiente.

A pessoa responsável registra: caminho, trecho, fonte, data, mudança proposta e motivo. Correções de segurança ou privacidade têm prioridade. Questões individuais seguem por canal adequado e restrito; não abrir uma discussão pública contendo o dado que se deseja proteger.

Para medição de busca futura, pedir acesso adequado e registrar método e período. `robots.txt` restringindo rastreio não é uma diretiva noindex. Canonical no source não prova a canonical escolhida pelo buscador. Publicar um arquivo em uma branch não cria automaticamente uma URL de produção ou uma página indexada.

[Plano](PLANO.md) · [Inventário](INVENTARIO-URLS.md) · [Mapa de links](MAPA-DE-LINKS.md) · [Changelog](CHANGELOG.md) · [Coleção](../../../publicacoes/README.md)
