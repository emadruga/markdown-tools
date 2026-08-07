<!--
Transcrição em Markdown do DOQ-DIMCI-020_jun2026-Final.docx.pdf (465 páginas).
Gerada via pdftotext -layout + reestruturação manual em headings Markdown.
Esta é uma TRANSCRIÇÃO FIEL do PDF na forma em que ele se encontra hoje —
inclui deliberadamente as não conformidades já identificadas (nomes de dimensão
abreviados, uso ambíguo de "Empresa", dimensões sem capacidade), que serão
corrigidas em edições subsequentes, uma por vez, e documentadas em
INCONSISTENCIAS_NOMENCLATURA.md e docs/PLANO_PARA_VERFICACAO_DA_CONFORMIDADE.md.
Exceção: o Sumário do PDF original (que pulava os capítulos 4-8 e omitia a
entrada do ANEXO II) foi substituído por um índice Markdown navegável — essa
correção específica já foi aplicada nesta versão.
Cada seção traz um comentário (pág. original: N/465) apontando a página
real no PDF, confirmada via pdftotext (cabeçalho "PÁGINA n/465").
-->

# ORIENTAÇÃO PARA AVALIAÇÃO DE MATURIDADE DE INDÚSTRIAS 4.0

<!-- pág. original: 1/465 -->

**Diretoria de Metrologia Científica e Industrial**

Documento de caráter orientativo

**DOQ-DIMCI-020**
Revisão 01 – Junho/2026

---

## SUMÁRIO

<!-- Índice navegável gerado a partir dos headings reais deste arquivo .md. Substitui
     a transcrição literal do Sumário impresso no PDF original, que continha lacunas
     (capítulos 4 a 8 e a entrada do ANEXO II ausentes) — não conformidades já
     documentadas em docs/PLANO_PARA_VERFICACAO_DA_CONFORMIDADE.md, seção 6, itens 1-2. -->

- [1 OBJETIVO](#1-objetivo)
- [2 CAMPO DE APLICAÇÃO](#2-campo-de-aplicação)
- [3 RESPONSABILIDADE](#3-responsabilidade)
- [5 DOCUMENTOS DE REFERÊNCIA](#5-documentos-de-referência)
- [6 DOCUMENTOS COMPLEMENTARES](#6-documentos-complementares)
- [7 SIGLAS](#7-siglas)
- [8 TERMOS E DEFINIÇÕES](#8-termos-e-definições)
  - [8.1 Organização Candidata](#81-organização-candidata)
  - [8.2 Responsável Técnico](#82-responsável-técnico)
  - [8.3 Participante](#83-participante)
  - [8.4 Instituição Avaliadora](#84-instituição-avaliadora)
  - [8.5 Avaliador-Líder](#85-avaliador-líder)
  - [8.6 Equipe da Organização](#86-equipe-da-organização)
- [9 GENERALIDADES](#9-generalidades)
- [10 ORIENTAÇÕES DE CONDUTA](#10-orientações-de-conduta)
- [11 DOCUMENTAÇÃO PESSOAL NECESSÁRIA](#11-documentação-pessoal-necessária)
  - [11.1 Avaliações no Brasil](#111-avaliações-no-brasil)
  - [11.2 Avaliações no Exterior](#112-avaliações-no-exterior)
- [12 CONHECIMENTO DOS REQUISITOS DE CERTIFICAÇÃO](#12-conhecimento-dos-requisitos-de-certificação)
- [13 AVALIAÇÃO DE MATURIDADE](#13-avaliação-de-maturidade)
- [9 HISTÓRICO DA REVISÃO](#9-histórico-da-revisão)
- [ANEXO I - QUESTIONÁRIO DE AVALIAÇÃO DA MATURIDADE DA INDÚSTRIA 4.0](#anexo-i-questionário-de-avaliação-da-maturidade-da-indústria-40)
  - [I.1 Dimensão: Integração Vertical](#i1-dimensão-integração-vertical)
    - [I.1.1 Capacidade: Integração vertical entre chão de fábrica e sistemas corporativos](#i11-capacidade-integração-vertical-entre-chão-de-fábrica-e-sistemas-corporativos)
      - [I.1.1.1 Questão: Em que medida os sistemas de controle e operação (como PLC, SCADA e...](#i111-questão-em-que-medida-os-sistemas-de-controle-e-operação-como-plc-scada-e)
      - [I.1.1.2 Questão: Até que ponto os dados de produção, manutenção e suprimentos são...](#i112-questão-até-que-ponto-os-dados-de-produção-manutenção-e-suprimentos-são)
      - [I.1.1.3 Questão: Em que grau a organização dispõe de rastreabilidade e visibilidade...](#i113-questão-em-que-grau-a-organização-dispõe-de-rastreabilidade-e-visibilidade)
      - [I.1.1.4 Questão: Como a organização assegura que os dados trocados entre diferentes...](#i114-questão-como-a-organização-assegura-que-os-dados-trocados-entre-diferentes)
      - [I.1.1.5 Questão: Em que medida a organização utiliza análises preditivas, algoritmos...](#i115-questão-em-que-medida-a-organização-utiliza-análises-preditivas-algoritmos)
  - [I.2 Dimensão: Integração Horizontal](#i2-dimensão-integração-horizontal)
    - [I.2.1 Capacidade: Integração horizontal com parceiros da cadeia de valor](#i21-capacidade-integração-horizontal-com-parceiros-da-cadeia-de-valor)
      - [I.2.1.1 Questão: Em que medida os sistemas internos da organização (ERP, MES, SCM,...](#i211-questão-em-que-medida-os-sistemas-internos-da-organização-erp-mes-scm)
      - [I.2.1.2 Questão: Até que ponto os processos de suprimento, produção, logística e...](#i212-questão-até-que-ponto-os-processos-de-suprimento-produção-logística-e)
      - [I.2.1.3 Questão: Em que grau a organização e seus parceiros mantêm rastreabilidade...](#i213-questão-em-que-grau-a-organização-e-seus-parceiros-mantêm-rastreabilidade)
      - [I.2.1.4 Questão: Em que medida a organização utiliza plataformas digitais ou sistemas...](#i214-questão-em-que-medida-a-organização-utiliza-plataformas-digitais-ou-sistemas)
      - [I.2.1.5 Questão: Até que ponto a empresa aplica análise de dados e algoritmos...](#i215-questão-até-que-ponto-a-empresa-aplica-análise-de-dados-e-algoritmos)
      - [I.2.1.6 Questão: Em que medida a organização e seus parceiros são capazes de reagir de...](#i216-questão-em-que-medida-a-organização-e-seus-parceiros-são-capazes-de-reagir-de)
  - [I.3 Dimensão: Ciclo de Vida de Produto Integrado](#i3-dimensão-ciclo-de-vida-de-produto-integrado)
    - [I.3.1 Capacidade: Foco em benefícios ao cliente](#i31-capacidade-foco-em-benefícios-ao-cliente)
      - [I.3.1.1 Questão: Como a informação do produto é gerenciada e compartilhada entre as...](#i311-questão-como-a-informação-do-produto-é-gerenciada-e-compartilhada-entre-as)
      - [I.3.1.2 Questão: Em que medida a empresa utiliza representações digitais (como modelos...](#i312-questão-em-que-medida-a-empresa-utiliza-representações-digitais-como-modelos)
      - [I.3.1.3 Questão: Como a empresa integra e utiliza dados de diversas fontes (design,...](#i313-questão-como-a-empresa-integra-e-utiliza-dados-de-diversas-fontes-design)
      - [I.3.1.4 Questão: Como a empresa lida com a colaboração e a integração de parceiros...](#i314-questão-como-a-empresa-lida-com-a-colaboração-e-a-integração-de-parceiros)
      - [I.3.1.5 Questão: Como a empresa gerencia e incorpora feedback do uso do produto e...](#i315-questão-como-a-empresa-gerencia-e-incorpora-feedback-do-uso-do-produto-e)
  - [I.4 Dimensão: Automação do Chão de Fábrica](#i4-dimensão-automação-do-chão-de-fábrica)
    - [I.4.1 Capacidade: Design de interfaces orientado à tarefa](#i41-capacidade-design-de-interfaces-orientado-à-tarefa)
      - [I.4.1.1 Questão: A informação digital se adapta dinamicamente (em conteúdo e formato)...](#i411-questão-a-informação-digital-se-adapta-dinamicamente-em-conteúdo-e-formato)
      - [I.4.1.2 Questão: O design de HMI dos sistemas de assistência no Chão de Fábrica...](#i412-questão-o-design-de-hmi-dos-sistemas-de-assistência-no-chão-de-fábrica)
    - [I.4.2 Capacidade: Interface de usuário específica](#i42-capacidade-interface-de-usuário-específica)
      - [I.4.2.1 Questão: Qual o impacto do formato (e.g., AR, tabelas, voz) e tempo de entrega...](#i421-questão-qual-o-impacto-do-formato-eg-ar-tabelas-voz-e-tempo-de-entrega)
  - [I.5 Dimensão: Automação Corporativa](#i5-dimensão-automação-corporativa)
    - [I.5.1 Capacidade: Automação de processos administrativos](#i51-capacidade-automação-de-processos-administrativos)
      - [I.5.1.1 Questão: Em que medida os processos de vendas, marketing e aquisição/compras...](#i511-questão-em-que-medida-os-processos-de-vendas-marketing-e-aquisiçãocompras)
      - [I.5.1.2 Questão: Até que ponto a organização utiliza automação inteligente (RPA, IA)...](#i512-questão-até-que-ponto-a-organização-utiliza-automação-inteligente-rpa-ia)
      - [I.5.1.3 Questão: Em que medida os sistemas de planejamento de demanda e gestão de...](#i513-questão-em-que-medida-os-sistemas-de-planejamento-de-demanda-e-gestão-de)
    - [I.5.2 Capacidade: Automação da gestão de recursos e planejamento corporativo](#i52-capacidade-automação-da-gestão-de-recursos-e-planejamento-corporativo)
      - [I.5.2.1 Questão: Como a organização utiliza sistemas informatizados para planejar e...](#i521-questão-como-a-organização-utiliza-sistemas-informatizados-para-planejar-e)
      - [I.5.2.2 Questão: Em que grau as políticas e regras de negócio administrativas (alçadas...](#i522-questão-em-que-grau-as-políticas-e-regras-de-negócio-administrativas-alçadas)
      - [I.5.2.3 Questão: Até que ponto a organização utiliza análise preditiva para antecipar...](#i523-questão-até-que-ponto-a-organização-utiliza-análise-preditiva-para-antecipar)
  - [I.6 Dimensão: Automação de Instalações](#i6-dimensão-automação-de-instalações)
    - [I.6.1 Capacidade: Automação predial e integração de sistemas de instalações (BMS/HVAC)](#i61-capacidade-automação-predial-e-integração-de-sistemas-de-instalações-bmshvac)
      - [I.6.1.1 Questão: Em que medida os sistemas de HVAC, refrigeração, segurança e...](#i611-questão-em-que-medida-os-sistemas-de-hvac-refrigeração-segurança-e)
      - [I.6.1.2 Questão: Até que ponto o controle de acesso, os sistemas de segurança predial...](#i612-questão-até-que-ponto-o-controle-de-acesso-os-sistemas-de-segurança-predial)
    - [I.6.2 Capacidade: Eficiência energética e manutenção preditiva de instalações](#i62-capacidade-eficiência-energética-e-manutenção-preditiva-de-instalações)
      - [I.6.2.1 Questão: Em que medida a organização utiliza análise de dados para monitorar e...](#i621-questão-em-que-medida-a-organização-utiliza-análise-de-dados-para-monitorar-e)
      - [I.6.2.2 Questão: Até que ponto a organização utiliza manutenção preditiva, apoiada em...](#i622-questão-até-que-ponto-a-organização-utiliza-manutenção-preditiva-apoiada-em)
  - [I.7 Dimensão: Conectividade de Chão de Fábrica](#i7-dimensão-conectividade-de-chão-de-fábrica)
    - [I.7.1 Capacidade: Aquisição de dados por sensores e atuadores](#i71-capacidade-aquisição-de-dados-por-sensores-e-atuadores)
      - [I.7.1.1 Questão: Os equipamentos e máquinas do chão de fábrica foram aprimorados com...](#i711-questão-os-equipamentos-e-máquinas-do-chão-de-fábrica-foram-aprimorados-com)
      - [I.7.1.2 Questão: O pré-processamento dos dados brutos dos sensores diretamente nos...](#i712-questão-o-pré-processamento-dos-dados-brutos-dos-sensores-diretamente-nos)
      - [I.7.1.3 Questão: A aquisição de dados é facilitada pela conectividade dos sistemas de...](#i713-questão-a-aquisição-de-dados-é-facilitada-pela-conectividade-dos-sistemas-de)
      - [I.7.1.4 Questão: Os dados coletados por sensores e atuadores são utilizados de forma...](#i714-questão-os-dados-coletados-por-sensores-e-atuadores-são-utilizados-de-forma)
  - [I.8 Dimensão: Conectividade Corporativa](#i8-dimensão-conectividade-corporativa)
    - [I.8.1 Capacidade: Interface de dados padronizada](#i81-capacidade-interface-de-dados-padronizada)
      - [I.8.1.1 Questão: Os principais sistemas de TI da Empresa (como ERP, PLM e MES) estão...](#i811-questão-os-principais-sistemas-de-ti-da-empresa-como-erp-plm-e-mes-estão)
      - [I.8.1.2 Questão: A empresa utiliza interfaces de dados padronizadas e formatos de...](#i812-questão-a-empresa-utiliza-interfaces-de-dados-padronizadas-e-formatos-de)
      - [I.8.1.3 Questão: A infraestrutura de TI da empresa utiliza metadados estruturados e...](#i813-questão-a-infraestrutura-de-ti-da-empresa-utiliza-metadados-estruturados-e)
  - [I.9 Dimensão: Conectividade de Instalações (Facility)](#i9-dimensão-conectividade-de-instalações-facility)
    - [I.9.1 Capacidade: Infraestrutura de TI resiliente](#i91-capacidade-infraestrutura-de-ti-resiliente)
      - [I.9.1.1 Questão: Quão eficiente é a infraestrutura de rede (cabeada e sem fio) que...](#i911-questão-quão-eficiente-é-a-infraestrutura-de-rede-cabeada-e-sem-fio-que)
      - [I.9.1.2 Questão: Qual é o grau de integração entre equipamentos da infraestrutura de...](#i912-questão-qual-é-o-grau-de-integração-entre-equipamentos-da-infraestrutura-de)
      - [I.9.1.3 Questão: A infraestrutura de rede (cabeada e sem fio) que interliga os...](#i913-questão-a-infraestrutura-de-rede-cabeada-e-sem-fio-que-interliga-os)
      - [I.9.1.4 Questão: O framework de segurança de TI e as políticas de governança cobrem a...](#i914-questão-o-framework-de-segurança-de-ti-e-as-políticas-de-governança-cobrem-a)
    - [I.9.2 Capacidade: Segurança de TI](#i92-capacidade-segurança-de-ti)
      - [I.9.2.1 Questão: A infraestrutura de Segurança de TI garante a identificação e...](#i921-questão-a-infraestrutura-de-segurança-de-ti-garante-a-identificação-e)
      - [I.9.2.2 Questão: Como a infraestrutura de Segurança de TI implementa a validação de...](#i922-questão-como-a-infraestrutura-de-segurança-de-ti-implementa-a-validação-de)
      - [I.9.2.3 Questão: A infraestrutura de Segurança de TI implementa o controle de fluxo de...](#i923-questão-a-infraestrutura-de-segurança-de-ti-implementa-o-controle-de-fluxo-de)
  - [I.10 Dimensão: Inteligência de Chão de Fábrica](#i10-dimensão-inteligência-de-chão-de-fábrica)
    - [I.10.1 Capacidade: Pré-processamento descentralizado de dados de sensores](#i101-capacidade-pré-processamento-descentralizado-de-dados-de-sensores)
      - [I.10.1.1 Questão: Em que medida a sua organização utiliza sistemas embarcados ou...](#i1011-questão-em-que-medida-a-sua-organização-utiliza-sistemas-embarcados-ou)
      - [I.10.1.2 Questão: Em que medida a sua organização utiliza o pré-processamento...](#i1012-questão-em-que-medida-a-sua-organização-utiliza-o-pré-processamento)
      - [I.10.1.3 Questão: Em que medida a sua organização utiliza o processamento...](#i1013-questão-em-que-medida-a-sua-organização-utiliza-o-processamento)
  - [I.11 Dimensão: Inteligência Corporativa](#i11-dimensão-inteligência-corporativa)
    - [I.11.1 Capacidade: Aprendizagem e tomada de decisão baseadas em dados](#i111-capacidade-aprendizagem-e-tomada-de-decisão-baseadas-em-dados)
      - [I.11.1.1 Questão: Em que medida a organização promove uma cultura de aprendizagem em...](#i1111-questão-em-que-medida-a-organização-promove-uma-cultura-de-aprendizagem-em)
      - [I.11.1.2 Questão: Até que ponto os colaboradores possuem habilidades e conhecimentos...](#i1112-questão-até-que-ponto-os-colaboradores-possuem-habilidades-e-conhecimentos)
      - [I.11.1.3 Questão: Em que grau a organização possui mecanismos estruturados para...](#i1113-questão-em-que-grau-a-organização-possui-mecanismos-estruturados-para)
      - [I.11.1.4 Questão: Como a organização assegura a transparência, a ética e a confiança no...](#i1114-questão-como-a-organização-assegura-a-transparência-a-ética-e-a-confiança-no)
      - [I.11.1.5 Questão: Em que medida a organização é capaz de adaptar processos, estratégias...](#i1115-questão-em-que-medida-a-organização-é-capaz-de-adaptar-processos-estratégias)
  - [I.12 Dimensão: Inteligência de Instalações (Facility)](#i12-dimensão-inteligência-de-instalações-facility)
    - [I.12.1 Capacidade: Análise de dados automatizada](#i121-capacidade-análise-de-dados-automatizada)
      - [I.12.1.1 Questão: Como a empresa utiliza a análise automatizada de dados para gerar...](#i1211-questão-como-a-empresa-utiliza-a-análise-automatizada-de-dados-para-gerar)
      - [I.12.1.2 Questão: Qual é a abrangência da análise automatizada de dados?](#i1212-questão-qual-é-a-abrangência-da-análise-automatizada-de-dados)
      - [I.12.1.3 Questão: Qual é a natureza dos sistemas de análise de dados?](#i1213-questão-qual-é-a-natureza-dos-sistemas-de-análise-de-dados)
      - [I.12.1.4 Questão: Com que frequência e velocidade a análise de dados é executada e os...](#i1214-questão-com-que-frequência-e-velocidade-a-análise-de-dados-é-executada-e-os)
    - [I.12.2 Capacidade: Entrega de informação contextualizada](#i122-capacidade-entrega-de-informação-contextualizada)
      - [I.12.2.1 Questão: Os sistemas de informação da organização conseguem disponibilizar...](#i1221-questão-os-sistemas-de-informação-da-organização-conseguem-disponibilizar)
      - [I.12.2.2 Questão: Em que medida os sistemas de informação corporativos (Enterprise) e...](#i1222-questão-em-que-medida-os-sistemas-de-informação-corporativos-enterprise-e)
      - [I.12.2.3 Questão: Até que ponto a organização assegura a qualidade, a rastreabilidade e...](#i1223-questão-até-que-ponto-a-organização-assegura-a-qualidade-a-rastreabilidade-e)
      - [I.12.2.4 Questão: Os sistemas de informação da organização utilizam análises avançadas...](#i1224-questão-os-sistemas-de-informação-da-organização-utilizam-análises-avançadas)
      - [I.12.2.5 Questão: Em que medida as equipes, em diferentes níveis, têm autonomia para...](#i1225-questão-em-que-medida-as-equipes-em-diferentes-níveis-têm-autonomia-para)
  - [I.13 Dimensão: Desenvolvimento e Aprendizado de Força de Trabalho](#i13-dimensão-desenvolvimento-e-aprendizado-de-força-de-trabalho)
    - [I.13.1 Capacidade: Desenvolvimento profissional contínuo](#i131-capacidade-desenvolvimento-profissional-contínuo)
      - [I.13.1.1 Questão: A organização possui um plano estratégico de desenvolvimento...](#i1311-questão-a-organização-possui-um-plano-estratégico-de-desenvolvimento)
      - [I.13.1.2 Questão: O aprendizado é estruturado de forma personalizada e acessível a...](#i1312-questão-o-aprendizado-é-estruturado-de-forma-personalizada-e-acessível-a)
      - [I.13.1.3 Questão: A organização estimula a cultura de aprendizado contínuo,...](#i1313-questão-a-organização-estimula-a-cultura-de-aprendizado-contínuo)
      - [I.13.1.4 Questão: Os sistemas de aprendizado (LMS, LXP, HRIS) estão integrados a outros...](#i1314-questão-os-sistemas-de-aprendizado-lms-lxp-hris-estão-integrados-a-outros)
      - [I.13.1.5 Questão: O progresso e o impacto do aprendizado são medidos sistematicamente...](#i1315-questão-o-progresso-e-o-impacto-do-aprendizado-são-medidos-sistematicamente)
      - [I.13.1.6 Questão: A organização possui programas estruturados de requalificação e...](#i1316-questão-a-organização-possui-programas-estruturados-de-requalificação-e)
      - [I.13.1.7 Questão: Os líderes incentivam, acompanham e servem de modelo no processo de...](#i1317-questão-os-líderes-incentivam-acompanham-e-servem-de-modelo-no-processo-de)
      - [I.13.1.8 Questão: Existem políticas, papéis e processos definidos para governar o...](#i1318-questão-existem-políticas-papéis-e-processos-definidos-para-governar-o)
      - [I.13.1.9 Questão: A organização mantém parcerias com instituições de ensino, centros de...](#i1319-questão-a-organização-mantém-parcerias-com-instituições-de-ensino-centros-de)
      - [I.13.1.10 Questão: A organização utiliza dados e inteligência artificial para...](#i13110-questão-a-organização-utiliza-dados-e-inteligência-artificial-para)
    - [I.13.2 Capacidade: Reconhecer o valor dos erros](#i132-capacidade-reconhecer-o-valor-dos-erros)
      - [I.13.2.1 Questão: Em que medida os erros e falhas são analisados e utilizados como...](#i1321-questão-em-que-medida-os-erros-e-falhas-são-analisados-e-utilizados-como)
      - [I.13.2.2 Questão: Até que ponto os colaboradores se sentem seguros para relatar erros,...](#i1322-questão-até-que-ponto-os-colaboradores-se-sentem-seguros-para-relatar-erros)
      - [I.13.2.3 Questão: Existem processos ou ferramentas digitais que registram, organizam e...](#i1323-questão-existem-processos-ou-ferramentas-digitais-que-registram-organizam-e)
      - [I.13.2.4 Questão: Como os líderes e gestores demonstram, na prática, comportamentos que...](#i1324-questão-como-os-líderes-e-gestores-demonstram-na-prática-comportamentos-que)
      - [I.13.2.5 Questão: De que forma a organização incentiva a experimentação e a inovação,...](#i1325-questão-de-que-forma-a-organização-incentiva-a-experimentação-e-a-inovação)
      - [I.13.2.6 Questão: O feedback sobre erros e resultados inesperados é utilizado...](#i1326-questão-o-feedback-sobre-erros-e-resultados-inesperados-é-utilizado)
      - [I.13.2.7 Questão: A organização utiliza ferramentas digitais e analíticas para...](#i1327-questão-a-organização-utiliza-ferramentas-digitais-e-analíticas-para)
      - [I.13.2.8 Questão: De que forma a organização estimula os colaboradores a experimentar...](#i1328-questão-de-que-forma-a-organização-estimula-os-colaboradores-a-experimentar)
      - [I.13.2.9 Questão: As lições aprendidas com erros ou experimentos são compartilhadas...](#i1329-questão-as-lições-aprendidas-com-erros-ou-experimentos-são-compartilhadas)
      - [I.13.2.10 Questão: Em que medida a organização utiliza o aprendizado proveniente de...](#i13210-questão-em-que-medida-a-organização-utiliza-o-aprendizado-proveniente-de)
    - [I.13.3 Capacidade: Prover competências digitais](#i133-capacidade-prover-competências-digitais)
      - [I.13.3.1 Questão: Em que medida a organização identifica, registra e monitora as...](#i1331-questão-em-que-medida-a-organização-identifica-registra-e-monitora-as)
      - [I.13.3.2 Questão: Até que ponto o planejamento de desenvolvimento da força de trabalho...](#i1332-questão-até-que-ponto-o-planejamento-de-desenvolvimento-da-força-de-trabalho)
      - [I.13.3.3 Questão: Em que grau a organização implementa programas estruturados e...](#i1333-questão-em-que-grau-a-organização-implementa-programas-estruturados-e)
      - [I.13.3.4 Questão: Em que medida a organização utiliza plataformas digitais e...](#i1334-questão-em-que-medida-a-organização-utiliza-plataformas-digitais-e)
      - [I.13.3.5 Questão: Até que ponto a organização promove uma cultura de aprendizado...](#i1335-questão-até-que-ponto-a-organização-promove-uma-cultura-de-aprendizado)
      - [I.13.3.6 Questão: Em que grau a organização mede o impacto dos programas de capacitação...](#i1336-questão-em-que-grau-a-organização-mede-o-impacto-dos-programas-de-capacitação)
      - [I.13.3.7 Questão: Até que ponto as competências digitais desenvolvidas são efetivamente...](#i1337-questão-até-que-ponto-as-competências-digitais-desenvolvidas-são-efetivamente)
      - [I.13.3.8 Questão: Em que medida a organização utiliza dados e análises (learning...](#i1338-questão-em-que-medida-a-organização-utiliza-dados-e-análises-learning)
      - [I.13.3.9 Questão: Até que ponto os colaboradores estão preparados para se adaptar a...](#i1339-questão-até-que-ponto-os-colaboradores-estão-preparados-para-se-adaptar-a)
      - [I.13.3.10 Questão: Em que grau a organização estabelece parcerias com instituições de...](#i13310-questão-em-que-grau-a-organização-estabelece-parcerias-com-instituições-de)
  - [I.14 Dimensão: Competência de Liderança](#i14-dimensão-competência-de-liderança)
    - [I.14.1 Capacidade: Abertura à inovação](#i141-capacidade-abertura-à-inovação)
      - [I.14.1.1 Questão: Como a liderança e a organização demonstram abertura à inovação...](#i1411-questão-como-a-liderança-e-a-organização-demonstram-abertura-à-inovação)
      - [I.14.1.2 Questão: Como a organização lida com erros em iniciativas de inovação e os...](#i1412-questão-como-a-organização-lida-com-erros-em-iniciativas-de-inovação-e-os)
      - [I.14.1.3 Questão: Qual o nível de autonomia e empoderamento que colaboradores possuem...](#i1413-questão-qual-o-nível-de-autonomia-e-empoderamento-que-colaboradores-possuem)
      - [I.14.1.4 Questão: Quanto tempo a organização leva para validar hipóteses e testar novas...](#i1414-questão-quanto-tempo-a-organização-leva-para-validar-hipóteses-e-testar-novas)
    - [I.14.2 Capacidade: Confiança em processos e sistemas de informação](#i142-capacidade-confiança-em-processos-e-sistemas-de-informação)
      - [I.14.2.1 Questão: Como a liderança e as equipes utilizam e confiam em processos...](#i1421-questão-como-a-liderança-e-as-equipes-utilizam-e-confiam-em-processos)
      - [I.14.2.2 Questão: Como a organização desenvolve e mantém a consciência de segurança...](#i1422-questão-como-a-organização-desenvolve-e-mantém-a-consciência-de-segurança)
      - [I.14.2.3 Questão: Qual o grau de integração e interoperabilidade entre os diversos...](#i1423-questão-qual-o-grau-de-integração-e-interoperabilidade-entre-os-diversos)
      - [I.14.2.4 Questão: Qual o nível de disponibilidade, confiabilidade e resiliência dos...](#i1424-questão-qual-o-nível-de-disponibilidade-confiabilidade-e-resiliência-dos)
    - [I.14.3 Capacidade: Estilo de liderança democrático](#i143-capacidade-estilo-de-liderança-democrático)
      - [I.14.3.1 Questão: Quando a sua equipe precisa decidir sobre a adoção de uma nova...](#i1431-questão-quando-a-sua-equipe-precisa-decidir-sobre-a-adoção-de-uma-nova)
      - [I.14.3.2 Questão: Como os dados de produção e operação são utilizados para apoiar as...](#i1432-questão-como-os-dados-de-produção-e-operação-são-utilizados-para-apoiar-as)
      - [I.14.3.3 Questão: Quando surge a necessidade de integração entre diferentes áreas (ex.:...](#i1433-questão-quando-surge-a-necessidade-de-integração-entre-diferentes-áreas-ex)
      - [I.14.3.4 Questão: Como a sua equipe contribui com ideias de inovação ou melhoria...](#i1434-questão-como-a-sua-equipe-contribui-com-ideias-de-inovação-ou-melhoria)
      - [I.14.3.5 Questão: Como é definido o desenvolvimento de novas competências (habilidades...](#i1435-questão-como-é-definido-o-desenvolvimento-de-novas-competências-habilidades)
      - [I.14.3.6 Questão: Quando ocorre um problema inesperado (falha de máquina, atraso de...](#i1436-questão-quando-ocorre-um-problema-inesperado-falha-de-máquina-atraso-de)
      - [I.14.3.7 Questão: Como a organização reage a mudanças externas (novas demandas,...](#i1437-questão-como-a-organização-reage-a-mudanças-externas-novas-demandas)
    - [I.14.4 Capacidade: Gestão ágil](#i144-capacidade-gestão-ágil)
      - [I.14.4.1 Questão: Qual é a prontidão da liderança para alavancar conceitos e técnicas...](#i1441-questão-qual-é-a-prontidão-da-liderança-para-alavancar-conceitos-e-técnicas)
      - [I.14.4.2 Questão: Qual é o nível de patrocínio executivo, investimento de recursos e...](#i1442-questão-qual-é-o-nível-de-patrocínio-executivo-investimento-de-recursos-e)
      - [I.14.4.3 Questão: Qual é a frequência, qualidade e intensidade da participação de...](#i1443-questão-qual-é-a-frequência-qualidade-e-intensidade-da-participação-de)
      - [I.14.4.4 Questão: Qual é o grau de alinhamento entre os valores culturais existentes...](#i1444-questão-qual-é-o-grau-de-alinhamento-entre-os-valores-culturais-existentes)
      - [I.14.4.5 Questão: Qual é a qualidade, abrangência e continuidade dos programas de...](#i1445-questão-qual-é-a-qualidade-abrangência-e-continuidade-dos-programas-de)
      - [I.14.4.6 Questão: Qual é o nível de estruturação do processo de transformação ágil,...](#i1446-questão-qual-é-o-nível-de-estruturação-do-processo-de-transformação-ágil)
    - [I.14.5 Capacidade: Sistemas de metas motivacionais](#i145-capacidade-sistemas-de-metas-motivacionais)
      - [I.14.5.1 Questão: Como a liderança estabelece e gerencia sistemas de metas para motivar...](#i1451-questão-como-a-liderança-estabelece-e-gerencia-sistemas-de-metas-para-motivar)
      - [I.14.5.2 Questão: Como as metas são formuladas em termos de clareza, especificidade e...](#i1452-questão-como-as-metas-são-formuladas-em-termos-de-clareza-especificidade-e)
      - [I.14.5.3 Questão: Qual o nível de transparência e visibilidade das metas individuais,...](#i1453-questão-qual-o-nível-de-transparência-e-visibilidade-das-metas-individuais)
      - [I.14.5.4 Questão: Qual a frequência dos ciclos de definição, revisão e ajuste de metas?](#i1454-questão-qual-a-frequência-dos-ciclos-de-definição-revisão-e-ajuste-de-metas)
      - [I.14.5.5 Questão: Como as metas individuais e de equipe conectam-se ao propósito e...](#i1455-questão-como-as-metas-individuais-e-de-equipe-conectam-se-ao-propósito-e)
      - [I.14.5.6 Questão: Como dados, métricas e analytics são utilizados no processo de...](#i1456-questão-como-dados-métricas-e-analytics-são-utilizados-no-processo-de)
  - [I.15 Dimensão: Colaboração inter e intra-organização](#i15-dimensão-colaboração-inter-e-intra-organização)
    - [I.15.1 Capacidade: Comunicação aberta](#i151-capacidade-comunicação-aberta)
      - [I.15.1.1 Questão: Como a comunicação e o compartilhamento de informações acontecem...](#i1511-questão-como-a-comunicação-e-o-compartilhamento-de-informações-acontecem)
      - [I.15.1.2 Questão: Como a organização compartilha informações estratégicas, decisões e...](#i1512-questão-como-a-organização-compartilha-informações-estratégicas-decisões-e)
      - [I.15.1.3 Questão: Como a organização pratica e incentiva o feedback contínuo entre...](#i1513-questão-como-a-organização-pratica-e-incentiva-o-feedback-contínuo-entre)
      - [I.15.1.4 Questão: Como a organização comunica durante crises, mudanças significativas...](#i1514-questão-como-a-organização-comunica-durante-crises-mudanças-significativas)
      - [I.15.1.5 Questão: Como a organização pratica a escuta ativa, capturando e respondendo...](#i1515-questão-como-a-organização-pratica-a-escuta-ativa-capturando-e-respondendo)
    - [I.15.2 Capacidade: Comunicação eficiente](#i152-capacidade-comunicação-eficiente)
      - [I.15.2.1 Questão: Como a comunicação e a troca de informações são estruturadas e...](#i1521-questão-como-a-comunicação-e-a-troca-de-informações-são-estruturadas-e)
      - [I.15.2.2 Questão: Como se dá a comunicação com Parceiros?](#i1522-questão-como-se-dá-a-comunicação-com-parceiros)
      - [I.15.2.3 Questão: Como se dá normalmente a comunicação entre os funcionários?](#i1523-questão-como-se-dá-normalmente-a-comunicação-entre-os-funcionários)
    - [I.15.3 Capacidade: Comunidades flexíveis](#i153-capacidade-comunidades-flexíveis)
      - [I.15.3.1 Questão: Como a estrutura organizacional da empresa apoia a colaboração e a...](#i1531-questão-como-a-estrutura-organizacional-da-empresa-apoia-a-colaboração-e-a)
      - [I.15.3.2 Questão: De que forma as ferramentas de TI e plataformas de colaboração dão...](#i1532-questão-de-que-forma-as-ferramentas-de-ti-e-plataformas-de-colaboração-dão)
      - [I.15.3.3 Questão: Como a gestão de desempenho e os sistemas de metas estão adaptados...](#i1533-questão-como-a-gestão-de-desempenho-e-os-sistemas-de-metas-estão-adaptados)
      - [I.15.3.4 Questão: Como a gestão ágil e a distribuição de autoridade são aplicadas para...](#i1534-questão-como-a-gestão-ágil-e-a-distribuição-de-autoridade-são-aplicadas-para)
    - [I.15.4 Capacidade: Cooperação dentro da rede](#i154-capacidade-cooperação-dentro-da-rede)
      - [I.15.4.1 Questão: Como acontece a comunicação e o compartilhamento de informações entre...](#i1541-questão-como-acontece-a-comunicação-e-o-compartilhamento-de-informações-entre)
      - [I.15.4.2 Questão: Sua empresa coopera com parceiros na cadeia de valor (fornecedores,...](#i1542-questão-sua-empresa-coopera-com-parceiros-na-cadeia-de-valor-fornecedores)
      - [I.15.4.3 Questão: Sua empresa participa de redes e ecossistemas que colaboram em...](#i1543-questão-sua-empresa-participa-de-redes-e-ecossistemas-que-colaboram-em)
      - [I.15.4.4 Questão: Projetos de novos produtos e serviços requerem inputs/componentes...](#i1544-questão-projetos-de-novos-produtos-e-serviços-requerem-inputscomponentes)
      - [I.15.4.5 Questão: Como as tecnologias digitais são utilizadas para melhorar a...](#i1545-questão-como-as-tecnologias-digitais-são-utilizadas-para-melhorar-a)
      - [I.15.4.6 Questão: Como sua empresa gerencia relacionamentos e confiança com parceiros...](#i1546-questão-como-sua-empresa-gerencia-relacionamentos-e-confiança-com-parceiros)
  - [I.16 Dimensão: Estratégia & Governança](#i16-dimensão-estratégia-governança)
    - [I.16.1 Capacidade: Dar forma à mudança](#i161-capacidade-dar-forma-à-mudança)
      - [I.16.1.1 Questão: Qual é a atitude e o nível de autonomia dos funcionários para iniciar...](#i1611-questão-qual-é-a-atitude-e-o-nível-de-autonomia-dos-funcionários-para-iniciar)
      - [I.16.1.2 Questão: Como a estrutura de gestão reage (apoia, bloqueia, ignora) quando um...](#i1612-questão-como-a-estrutura-de-gestão-reage-apoia-bloqueia-ignora-quando-um)
      - [I.16.1.3 Questão: Qual é a postura do funcionário em relação à sua responsabilidade...](#i1613-questão-qual-é-a-postura-do-funcionário-em-relação-à-sua-responsabilidade)
      - [I.16.1.4 Questão: Qual é a abordagem predominante da organização para implementar...](#i1614-questão-qual-é-a-abordagem-predominante-da-organização-para-implementar)
    - [I.16.2 Capacidade: Gestão de direitos de decisão](#i162-capacidade-gestão-de-direitos-de-decisão)
      - [I.16.2.1 Questão: Como a sua empresa gerencia os direitos de decisão, equilibrando a...](#i1621-questão-como-a-sua-empresa-gerencia-os-direitos-de-decisão-equilibrando-a)
      - [I.16.2.2 Questão: Em que medida a empresa delega a autoridade de decisão de processos...](#i1622-questão-em-que-medida-a-empresa-delega-a-autoridade-de-decisão-de-processos)
      - [I.16.2.3 Questão: Em que medida os tomadores de decisão (em todos os níveis) têm acesso...](#i1623-questão-em-que-medida-os-tomadores-de-decisão-em-todos-os-níveis-têm-acesso)
    - [I.16.3 Capacidade: Governança de dados](#i163-capacidade-governança-de-dados)
      - [I.16.3.1 Questão: Qual o nível atual da 'Governança de Dados' na sua organização?](#i1631-questão-qual-o-nível-atual-da-governança-de-dados-na-sua-organização)
      - [I.16.3.2 Questão: Como se dá a Gestão de Dados Mestres (MDM)?](#i1632-questão-como-se-dá-a-gestão-de-dados-mestres-mdm)
      - [I.16.3.3 Questão: Como se dá a Gestão da Qualidade de Dados (DQM)?](#i1633-questão-como-se-dá-a-gestão-da-qualidade-de-dados-dqm)
      - [I.16.3.4 Questão: Há Padronização de Interfaces de Dados?](#i1634-questão-há-padronização-de-interfaces-de-dados)
- [ANEXO II - GUIA DE AVALIAÇÃO DE MATURIDADE DA INDÚSTRIA 4.0](#anexo-ii-guia-de-avaliação-de-maturidade-da-indústria-40)
  - [II.1 Visão Geral](#ii1-visão-geral)
  - [II.2 Objetivo e Escopo](#ii2-objetivo-e-escopo)
  - [II.3 Termos e Definições](#ii3-termos-e-definições)
  - [II.4 Visão Geral do Processo de Avaliação](#ii4-visão-geral-do-processo-de-avaliação)
  - [II.5 Descrição Detalhada do Processo de Avaliação](#ii5-descrição-detalhada-do-processo-de-avaliação)
  - [II.6 Papéis e Responsabilidades](#ii6-papéis-e-responsabilidades)
  - [II.7 Estrutura do Modelo de Maturidade da Indústria 4.0 (MA-I4.0): Estrutura Completa](#ii7-estrutura-do-modelo-de-maturidade-da-indústria-40-ma-i40-estrutura-completa)
  - [II.8 Método de Cálculo do Índice de Maturidade](#ii8-método-de-cálculo-do-índice-de-maturidade)
  - [APÊNDICE A - Detalhamento das 16 Dimensões](#apêndice-a-detalhamento-das-16-dimensões)
    - [Dimensão 1: Integração Vertical](#dimensão-1-integração-vertical)
    - [Dimensão 2: Integração Horizontal](#dimensão-2-integração-horizontal)
    - [Dimensão 3: Ciclo de Vida de Produto Integrado](#dimensão-3-ciclo-de-vida-de-produto-integrado)
    - [Dimensão 4: Automação do Chão de Fábrica](#dimensão-4-automação-do-chão-de-fábrica)
    - [Dimensão 5: Automação Corporativa](#dimensão-5-automação-corporativa)
    - [Dimensão 6: Automação de Instalações](#dimensão-6-automação-de-instalações)
    - [Dimensão 7: Conectividade de Chão de Fábrica](#dimensão-7-conectividade-de-chão-de-fábrica)
    - [Dimensão 8: Conectividade Corporativa](#dimensão-8-conectividade-corporativa)
    - [Dimensão 9: Conectividade de Instalações](#dimensão-9-conectividade-de-instalações)
    - [Dimensão 10: Inteligência de Chão de Fábrica](#dimensão-10-inteligência-de-chão-de-fábrica)
    - [Dimensão 11: Inteligência Corporativa](#dimensão-11-inteligência-corporativa)
    - [Dimensão 12: Inteligência de Instalações (Facility)](#dimensão-12-inteligência-de-instalações-facility)
    - [Dimensão 13: Desenvolvimento e Aprendizado de Força de Trabalho](#dimensão-13-desenvolvimento-e-aprendizado-de-força-de-trabalho)
    - [Dimensão 14: Competência de Liderança](#dimensão-14-competência-de-liderança)
    - [Dimensão 15: Colaboração inter e intra-organização](#dimensão-15-colaboração-inter-e-intra-organização)
    - [Dimensão 16: Estratégia & Governança](#dimensão-16-estratégia-governança)
  - [APÊNDICE B - Modelo de Relatório de Avaliação](#apêndice-b-modelo-de-relatório-de-avaliação)
  - [APÊNDICE C - Planilha de Cálculo do Índice idx4.0](#apêndice-c-planilha-de-cálculo-do-índice-idx40)
- [Bibliografia](#bibliografia)
- [Controle de Versões](#controle-de-versões)

---

## 1 OBJETIVO

<!-- pág. original: 7/465 -->

Este documento fornece orientações gerais para a realização de uma avaliação de maturidade
de uma indústria 4.0.

## 2 CAMPO DE APLICAÇÃO

Este documento aplica-se à Dmtic ou Organismo de Avaliação da Conformidade acreditada no
escopo da Portaria Inmetro 171 de Mar/26, ou substituta.

## 3 RESPONSABILIDADE

A responsabilidade pela revisão deste documento é da Dmtic.

## 5 DOCUMENTOS DE REFERÊNCIA

| Documento | Descrição |
|---|---|
| Portaria Inmetro nº 171, de 2026, ou substituta | Aprova a Instrução Normativa Inmetro e os Requisitos de Avaliação da Conformidade para Classificação da Maturidade da Indústria 4.0. |

## 6 DOCUMENTOS COMPLEMENTARES

<!-- pág. original: 8/465 -->

| Documento | Descrição |
|---|---|
| ABNT NBR ISO 19011 | Diretrizes para auditoria de sistemas de gestão |
| ABNT NBR ISO 9001 | Sistemas de gestão da qualidade - Requisitos |
| ABNT NBR ISO/IEC 17065 | Avaliação da conformidade - Requisitos para organismos de certificação de produtos, processos e serviços |

## 7 SIGLAS

<!-- pág. original: 9/465 -->

| Sigla | Significado |
|---|---|
| ABNT | Associação Brasileira de Normas Técnicas |
| ASO | Atestado de Saúde Ocupacional |
| Dmtic | Divisão de Metrologia em Tecnologia da Informação e Telecomunicações |
| DOQ | Documento Orientativo da Qualidade |
| EPI | Equipamento de Proteção Individual |
| IEC | International Electrotechnical Committee (Comitê Eletrotécnico Internacional) |
| Inmetro | Instituto Nacional de Metrologia, Qualidade e Tecnologia |
| ISO | International Organization for Standardization (Organização Internacional para Normalização) |
| NBR | Norma Brasileira |
| OAC | Organismo de Avaliação da Conformidade |
| RAC | Regulamento de Avaliação da Conformidade |

## 8 TERMOS E DEFINIÇÕES

### 8.1 Organização Candidata

Organização que está requerendo a avaliação de uma unidade organizacional, candidatando-se a uma certificação de maturidade.

### 8.2 Responsável Técnico

Profissional formalmente indicado e com alguma forma de vínculo com a organização candidata, estando legalmente habilitado e devidamente registrado no respectivo órgão de classe profissional, com formação e/ou experiências compatíveis com a digitalização de processos produtivos, responsável por receber e enviar as informações e evidências requeridas ao longo das etapas da certificação.

### 8.3 Participante

Profissional, com alguma forma de vínculo com a organização candidata, que fornece conhecimento ou experiência específicos para o responsável técnico, incluindo conhecimento ou experiência sobre a organização, processo ou atividade a ser candidata, bem como o idioma.

### 8.4 Instituição Avaliadora

Organização responsável pelo processo de avaliação e certificação de uma indústria 4.0, papel que pode ser desempenhado pela Dmtic ou OAC acreditada pelo Inmetro.

### 8.5 Avaliador-Líder

Auditor indicado pela Instituição Avaliadora como líder da avaliação.

### 8.6 Equipe da Organização

Um ou mais participantes, incluindo o responsável técnico, que compõem a equipe da organização candidata.

## 9 GENERALIDADES

<!-- pág. original: 10/465 -->

**9.1** Para avaliar a organização candidata, a equipe de auditoria deve ser composta por indivíduos que não devem pertencer a um concorrente dos produtos ou serviços fornecidos pela organização. Além disso, os auditores não podem estar trabalhando ou terem trabalhado para a referida organização há menos de três anos, o que seria caracterizado como conflito de interesse.

**9.2** A avaliação deve ser realizada de forma discreta, evitando manifestação verbal ou postural. A equipe de auditoria não deve fazer considerações sobre a avaliação na presença do pessoal da organização, a menos que haja possibilidade de risco. As necessidades de intervenção devem ser, sempre que possível, formalmente comunicadas antecipadamente ao responsável técnico e, em casos excepcionais, à equipe da organização.

**9.3** A equipe de auditores pode coletar informações através de: verificação de equipamentos; observações de atividades, do ambiente e condições de trabalho; documentos pertinentes à organização em processo de certificação ou já certificada como política, objetivos e metas, planos de gestão, procedimentos, normas, instruções, licenças, alvarás, outorgas, notificações e permissões, especificações, desenhos, contratos e registros. Caso continuem com dúvidas relativas ao escopo da avaliação ou atendimento a algum requisito, poderá solicitar esclarecimentos diretamente ao responsável técnico, apoiado ou não pela equipe da organização, desde que haja a anuência do avaliador-líder.

**9.4** Todas as observações devem ser registradas no Relatório de Auditoria da Instituição Avaliadora.

## 10 ORIENTAÇÕES DE CONDUTA

Recomenda-se aos integrantes da equipe avaliadora a seguinte conduta no período em que estiver participando de avaliações:

**10.1** Restrinja-se ao trabalho em execução. Não cite nomes de outras empresas em que trabalha ou trabalhou. Não apresente cartão de visita, nem faça propaganda pessoal.

**10.2** O contato com a organização avaliada é atribuição do auditor-líder. Todas as comunicações do avaliador-líder sobre a avaliação devem ser feitas ao responsável técnico da organização ou a Dmtic. Não entre em contato diretamente com a organização a ser candidata. Caso chegue antes do auditor-líder, aguarde-o na recepção da organização candidata.

**10.3** Qualquer contato comercial com a organização só pode ser realizado após a conclusão da avaliação e efetivo encaminhamento, pela Dmtic, do relatório ao avaliado. Contudo, neste caso para a participação como membro da equipe de auditoria em futuras avaliações na mesma organização, deverá haver um interstício de três anos. Durante o período da avaliação não comente assuntos comerciais.

**10.4** A pontualidade é importante para o cumprimento do programa de avaliação proposto. Não se atrase. Procure chegar ao local marcado com antecedência de 15 minutos.

**10.5** A confidencialidade é um requisito essencial em avaliações. Não se refira a sua participação em auditorias anteriores. Concentre-se nos assuntos relativos à auditoria corrente.

**10.6** Evite brincadeiras e assuntos paralelos. Observe discretamente o avaliado, permitindo-lhe a condução sem constrangimentos da avaliação. Faça intervenções oportunas (intervenções e observações devem ser registradas).

**10.7** Mantenha padrões de comportamento profissionais. Estabeleça uma comunicação amistosa com os envolvidos na avaliação.

**10.8** Não consuma bebida alcoólica em refeições feitas com representantes do auditado.

**10.9** Caso prefira, leve seus EPI pessoais, mas só os utilize quando a organização disponibilizar os EPI para a equipe.

## 11 DOCUMENTAÇÃO PESSOAL NECESSÁRIA

### 11.1 Avaliações no Brasil

O auditor deve portar documento de identidade original ou carteira de conselho regional.

Caso a organização candidata exija ASO para que um auditor adentre às suas instalações, é obrigação da organização candidata arcar com estes custos.

### 11.2 Avaliações no Exterior

O auditor deve portar passaporte, documento de identidade original (carteiras de conselhos regionais só são válidas em território nacional), carteira internacional de vacinação contra a febre amarela e outras vacinações necessárias conforme orientação do país de destino ou escala, e visto para ingresso nos EUA ou se o voo fizer escala nos EUA.

Responda com seriedade às perguntas da alfândega. Brincadeiras nessa etapa da viagem podem ter consequências desagradáveis.

## 12 CONHECIMENTO DOS REQUISITOS DE CERTIFICAÇÃO

<!-- pág. original: 12/465 -->

É requerido que o auditor designado pela Instituição Avaliadora tenha conhecimento (leitura) dos requisitos de certificação listados em 12.1 e esteja em posse dos mesmos.

**12.1** As normas, regulamentos e documentos base da certificação comuns são:

a) Portaria Inmetro nº 171, de 2026, ou substituta, e;
b) ANEXO I - QUESTIONÁRIO DE AVALIAÇÃO DA MATURIDADE DA INDÚSTRIA 4.0.

## 13 AVALIAÇÃO DE MATURIDADE

<!-- pág. original: 13/465 -->

**13.1** A avaliação de maturidade é um processo que deve ser implementado e formalizado pela Instituição Avaliadora para conduzir uma avaliação robusta, repetível e rastreável, baseando-se na Portaria Inmetro nº 171, de 2026, ou substituta, que atua como o instrumento normativo para estabelecer: quais os papéis desempenhados pelas partes interessadas, quais os insumos e resultados obrigatórios, bem como os cálculos devem ser feitos, quais critérios de decisão valem para concessão e manutenção do certificado e quais controles de qualidade e auditoria precisam existir para dar credibilidade ao resultado.

**13.1.1** O ANEXO II (- GUIA DE AVALIAÇÃO DE MATURIDADE DA INDÚSTRIA 4.0) apresenta um guia de avaliação da maturidade, estabelecendo o conjunto mínimo de etapas e atividades que devem ser implementadas pela Instituição Avaliadora. Além disso, o guia explicita o método de medição da maturidade contido na Portaria Inmetro nº 171, de 2026, ou substituta, e como este se encaixa ao longo do processo de avaliação.

**13.2** A Instituição Avaliadora sempre usará a última versão Portaria, ou substituta, e do ANEXO I (QUESTIONÁRIO DE AVALIAÇÃO DA MATURIDADE DA INDÚSTRIA 4.0) durante todo o processo de avaliação. Esse uso deve ser devidamente registrado ao longo do processo de avaliação para garantir rastreabilidade e consistência entre avaliações de diferentes organizações, bem como deixar transparente quais os parâmetros estão sendo utilizados para avaliar a organização candidata.

**13.3** Inicialmente, a organização candidata informa a Instituição Avaliadora, formalizando o escopo da avaliação determinado pela unidade organizacional que será certificada — por exemplo, uma planta, uma linha ou um conjunto de processos — e definem os limites, o período de evidências.

**13.3.1** Todos os insumos e exigências contidas na Portaria, ou substituta, por exemplo, que o período de evidências precisa cobrir um ciclo completo de produção, ou que determinados registros digitais são mandatórios, devem ser incorporados e apresentados em um Relatório de Auto-Avaliação como uma das condições de aceitação antes de prosseguir com o processo de avaliação.

**13.3.2** A instituição candidata deverá sempre basear-se na última versão Portaria, ou substituta, e do ANEXO I (QUESTIONÁRIO DE AVALIAÇÃO DA MATURIDADE DA INDÚSTRIA 4.0) para construção do Relatório de Auto-Avaliação.

**13.3.3** Ao responder o questionário do ANEXO I, a organização candidata deve explicitamente relacionar as evidências às respostas de cada questão. Consequentemente, essas evidências irão relacionar-se aos resultados obtidos nos cálculos referentes às capacidades e respectivas dimensões, para que, então, seja capaz de determinar qual o nível de maturidade pretendido.

**13.4** Se concluir que é possível prosseguir com a avaliação, a Instituição Avaliadora irá produzir um plano de avaliação, onde os insumos exigidos pela certificação são os requisitos para a sua elaboração. O plano de avaliação deve ser apresentado à organização candidata antes da etapa seguinte, que deve formalmente manifestar seu de acordo para o prosseguimento da avaliação.

**13.5** Uma vez apresentado o plano de avaliação, ocorre uma avaliação inicial, que funciona como uma verificação de prontidão e de aderência do escopo. Nessa fase, a Instituição Avaliadora revisa previamente evidências documentais e digitais, valida se o que foi definido no plano é viável e se há disponibilidade de informações suficientes para sustentar um julgamento consistente. O resultado típico é um ajuste fino do escopo, da amostra e do roteiro de entrevistas, reduzindo o risco de que a avaliação final seja contaminada por falta de evidência, acesso limitado a sistemas ou inconsistências de definição. No contexto da Portaria, essa etapa é importante porque reforça a conformidade processual: a certificação não depende apenas de uma nota final, mas da capacidade de demonstrar que a avaliação foi conduzida sob regras claras, com insumos válidos e evidências auditáveis. Se a Portaria, ou substituta, prever critérios de elegibilidade (por exemplo, requisitos mínimos de documentação, governança, rastreabilidade de dados ou condições de segurança e confidencialidade), a avaliação inicial é o ponto natural para confirmar esses critérios antes de avançar.

**13.6** A penúltima etapa é a avaliação final, o núcleo do processo, onde a maturidade é efetivamente mensurada. Nessa etapa, entrevistas confirmatórias, observações (presenciais ou remotas) e demonstrações de processos e sistemas são conduzidas de forma estruturada para coletar e triangular resultados alcançados, medições e evidências. A triangulação é essencial: o julgamento de cada capacidade não deve depender apenas do "discurso" ou apenas de um procedimento de responder o questionário do ANEXO I, mas da convergência entre o que está definido (processos e políticas), o que é executado (prática observável) e o que é registrado (evidência objetiva em sistemas, indicadores, logs, relatórios).

**13.6.1** Como a Portaria, ou substituta, é a referência normativa, nela estarão as regras oficiais de cálculo, e classificação da maturidade, a avaliação final do processo de avaliação deve demonstrar como um resultado certificável foi alcançado, com uma classificação bem fundamentada por capacidade e por dimensão.

**13.7** Depois da mensuração, vem a consolidação e a comunicação de resultados, em que a Instituição Avaliadora deve produzir um conjunto de saídas, tipicamente um Relatório de Auditoria, com um sumário executivo, evidências-chave, notas por dimensão, justificativas, pontos fortes, lacunas e recomendações.

**13.7.1** No contexto de certificação, é necessário que esse conteúdo seja apresentado em formato padronizado e auditável, com rastreabilidade suficiente para permitir verificação independente sem expor segredos industriais. O processo de avaliação descreve o "como documentar" e o "como a rastreabilidade é mantida", enquanto a Portaria, ou substituta especifica o "o que precisa constar" para que um resultado seja aceito no processo de decisão de certificação.

## 9 HISTÓRICO DA REVISÃO

| Revisão | Data | Itens revisados |
|---|---|---|
| | | |

---

## ANEXO I - QUESTIONÁRIO DE AVALIAÇÃO DA MATURIDADE DA INDÚSTRIA 4.0

<!-- pág. original: 15/465 -->

Versão 1.0 - Fevereiro de 2026

<!-- pág. original: 16/465 -->

### I.1 Dimensão: Integração Vertical

#### I.1.1 Capacidade: Integração vertical entre chão de fábrica e sistemas corporativos
#### Bloco/Pilar
- Bloco: Processo

- Pilar: Operações/Cadeia de Suprimentos

- Dimensão: Integração Vertical

#### Resumo Descritivo
A integração vertical de sistemas de informação é um componente central para a maturidade digital industrial, conectando todos os níveis da organização — desde o chão de fábrica (nível de controle e automação) até a gestão corporativa e estratégica. Nos modelos ACATECH e SIRI, esse princípio de integração de sistemas de informação (ACATECH) dentro do bloco Process e do pilar Operations/Supply Chain (SIRI) reflete a capacidade da empresa de garantir fluxo contínuo, coerente e bidirecional de dados entre os diferentes níveis hierárquicos (sensor, máquina, célula, linha, planta e empresa). Essa integração permite sincronizar a execução operacional com o planejamento e o controle de negócios, eliminando silos de informação, reduzindo atrasos e ampliando a eficiência produtiva. À medida que a maturidade evolui, a organização migra de conexões pontuais e manuais para arquiteturas integradas e inteligentes, com e visibilidade em tempo real. Em seu estágio mais avançado, a integração vertical possibilita a tomada de decisão autônoma e adaptativa, na qual os sistemas corporativos (ERP, MES, SCADA e IoT) operam de forma coordenada e preditiva, otimizando a performance de toda a cadeia de valor.
#### Questões
##### I.1.1.1 Questão: Em que medida os sistemas de controle e operação (como PLC, SCADA e...
Em que medida os sistemas de controle e operação (como PLC, SCADA e MES) estão integrados aos sistemas corporativos (como ERP, CRM, ou sistemas de gestão de ativos), permitindo fluxo contínuo de informações entre o nível de produção e o nível de gestão?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há integração entre os sistemas; as trocas de informações são manuais e pontuais. |
| 1 | Existem interfaces simples e manuais entre alguns sistemas, com dependência de arquivos ou planilhas. |
| 2 | A troca de informações é digital, porém limitada a integrações locais e unidirecionais. |
| 3 | Os sistemas MES e ERP trocam dados de forma automatizada, possibilitando visibilidade parcial entre operação e gestão. |
| 4 | Há integração transversal entre sistemas de diferentes níveis, com dashboards consolidados e indicadores unificados. |
| 5 | A integração vertical utiliza análise preditiva e inteligência artificial para antecipar necessidades de planejamento e execução. Os sistemas corporativos e operacionais trocam informações em tempo real, permitindo ajustes automatizados e proativos com base em previsões e cenários futuros. |
| 6 | A integração vertical é totalmente autônoma e adaptativa. Todos os sistemas (desde sensores no chão de fábrica até ERP corporativo) operam de forma coordenada e auto-otimizável, com capacidade de adaptação dinâmica em tempo real. O sistema opera de forma integrada mesmo diante de falhas, garantindo resiliência operacional e decisões autônomas alinhadas aos objetivos estratégicos. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Diagramas de arquitetura de sistemas (ERP, MES, SCADA, PLC).

- Registros de logs de integração e fluxos de dados.

- Relatórios de desempenho de sistemas interligados.

- Documentação técnica de APIs, middleware e protocolos de integração.

##### Métricas/KPIs

- Percentual de processos automatizados entre ERP e MES.

- Tempo médio de sincronização entre eventos de produção e registros no ERP Taxa de consistência de dados entre sistemas.

- Percentual de dados operacionais utilizados em decisões corporativas.

##### Sinais por nível

- Nível 0:


  - Ausência de integração

  - dados isolados

- Nível 1:


  - Integração manual e pontual

- Nível 2:


  - Comunicação digital, mas com baixa automação

- Nível 3:


  - Troca automatizada entre MES e ERP

- Nível 4:


  - Consolidação de indicadores e visibilidade corporativa

- Nível 5:


  - Integração preditiva e ajustes automatizados

- Nível 6:


  - Integração total, adaptativa e autônoma entre todos os níveis

##### Amostragem

- Entrevistas com equipes de TI, automação e planejamento; análise documental de fluxos de integração e logs de sistemas; observação de processos de sincronização e atualização de dados; revisão de painéis de controle e relatórios de integração.

##### I.1.1.2 Questão: Até que ponto os dados de produção, manutenção e suprimentos são...
Até que ponto os dados de produção, manutenção e suprimentos são atualizados em tempo quase real entre o chão de fábrica e o planejamento corporativo, permitindo reações rápidas a mudanças e imprevistos?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A atualização de dados entre operação e planejamento é manual e ocorre de forma esporádica, com alto risco de inconsistência. |
| 1 | Existem rotinas formais de atualização, porém sem integração automática; os dados são enviados por planilhas ou relatórios. |
| 2 | Parte dos dados operacionais é registrada digitalmente, mas as atualizações são periódicas e unidirecionais. |
| 3 | Os sistemas operacionais e corporativos estão conectados, permitindo atualizações automatizadas em intervalos regulares. |
| 4 | A sincronização é quase em tempo real; dashboards corporativos exibem dados atualizados de produção e manutenção. |
| 5 | A sincronização é em tempo real com capacidade preditiva. Os sistemas utilizam análise de dados históricos e em tempo real para prever eventos futuros (ex: paradas, gargalos, falta de materiais) e ajustar automaticamente os planos de produção, manutenção e suprimentos de forma proativa, minimizando impactos antes que problemas ocorram. |
| 6 | A sincronização é autônoma e adaptativa em tempo real. O sistema opera com total autonomia para ajustar planos e processos instantaneamente em resposta a mudanças no ambiente operacional, usando inteligência artificial e aprendizado contínuo. Os sistemas de operação e planejamento funcionam como um organismo integrado, auto-otimizando a cadeia de valor de forma contínua sem necessidade de intervenção humana. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Registros de logs e histórico de atualização de dados.

- Diagramas de integração entre ERP, MES e SCADA.

- Relatórios de sincronização de ordens de produção.

- Dashboards e painéis corporativos com indicadores em tempo real.

##### Métricas/KPIs

- Tempo médio de sincronização entre eventos de chão de fábrica e o ERP.

- Percentual de dados operacionais disponíveis em tempo real.

- Taxa de divergência entre planos e execução.

- Tempo de resposta entre detecção de anomalias e ajuste do plano.

##### Sinais por nível

- Nível 0:


  - Atualização manual e eventual

- Nível 1:


  - Procedimentos formais, mas sem automação

- Nível 2:


  - Dados digitalizados, mas sem sincronização contínua

- Nível 3:


  - Atualizações automáticas regulares

- Nível 4:


  - Dashboards com dados quase em tempo real

- Nível 5:


  - Replanejamento preditivo e automatizado

- Nível 6:


  - Adaptação autônoma e instantânea de planos e processos

##### Amostragem

- Entrevistas com equipes de planejamento, manutenção e produção; observação do fluxo de atualização entre sistemas; revisão de relatórios e logs de integração; avaliação de dashboards e ferramentas de monitoramento.

##### I.1.1.3 Questão: Em que grau a organização dispõe de rastreabilidade e visibilidade...
Em que grau a organização dispõe de rastreabilidade e visibilidade integrada dos fluxos de materiais, informações e processos ao longo de toda a cadeia produtiva?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização não possui rastreabilidade formal; o acompanhamento é manual e sem padronização. |
| 1 | Existem registros básicos de produção e materiais, porém sem integração entre sistemas. |
| 2 | Os dados de produção são registrados digitalmente, mas a visibilidade é local e limitada. |
| 3 | Os sistemas de controle e execução (MES/SCADA) estão interligados, oferecendo visibilidade parcial em painéis de processo. |
| 4 | Há rastreabilidade completa dos processos e produtos; dashboards consolidados permitem diagnóstico e análise de desvios. |
| 5 | A visibilidade inclui análises preditivas, identificando potenciais falhas e gargalos antes que ocorram |
| 6 | O sistema opera de forma autônoma, ajustando processos com base em dados de rastreabilidade em tempo real |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Registros de rastreabilidade (ordens de produção, lotes, séries).

- Logs de sistemas MES, SCADA, ERP e IoT.

- Dashboards e relatórios de desempenho produtivo.

- Documentos de controle de qualidade e manutenção.

##### Métricas/KPIs

- Percentual de processos e produtos rastreáveis digitalmente.

- Tempo médio para rastrear a origem de um produto ou evento.

- Percentual de dados visíveis em tempo real.

- Taxa de detecção de falhas antes da ocorrência.

##### Sinais por nível

- Nível 0:


  - Acompanhamento manual sem registros padronizados

- Nível 1:


  - Registros formais, mas sem integração digital

- Nível 2:


  - Rastreabilidade digital local

- Nível 3:


  - Painéis integrados com dados de processo

- Nível 4:


  - Rastreabilidade completa e visibilidade transversal

- Nível 5:


  - Análise preditiva e alertas automáticos

- Nível 6:


  - Correções autônomas e rastreabilidade em tempo real

##### Amostragem

- Entrevistas com equipes de produção, qualidade e logística; verificação prática de sistemas de rastreabilidade e dashboards; revisão de relatórios de controle e eventos de produção; análise de logs de integração entre sistemas.

##### I.1.1.4 Questão: Como a organização assegura que os dados trocados entre diferentes...
Como a organização assegura que os dados trocados entre diferentes sistemas e níveis hierárquicos sejam padronizados, coerentes e de alta qualidade?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há padronização ou controle de qualidade de dados; cada sistema adota modelos próprios. |
| 1 | Existem padrões básicos de nomenclatura e documentação de dados, mas sem política formal de governança. |
| 2 | A padronização é parcialmente digitalizada e aplicada a alguns sistemas de forma isolada. |
| 3 | Há um modelo de dados corporativo aplicado de forma consistente entre sistemas-chave (ERP, MES, SCADA). |
| 4 | A governança de dados é formalizada, com indicadores de qualidade, catálogos e monitoramento de consistência. |
| 5 | Sistemas utilizam validações automáticas e algoritmos para detectar |
| 6 | A padronização é dinâmica e autoajustável; os sistemas garantem coerência e integridade em tempo real de forma autônoma |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Política de governança de dados e padrões de integração.

- Documentação de modelos de dados e dicionários corporativos.

- Logs de integração e relatórios de consistência de dados.

- Registros de auditorias de dados e validações automáticas.

##### Métricas/KPIs

- Percentual de sistemas aderentes ao modelo de dados corporativo.

- Número de inconsistências de dados detectadas por período.

- Taxa de integridade de dados entre sistemas integrados.

- Tempo médio de correção de erros de sincronização.

##### Sinais por nível

- Nível 0:


  - Ausência de padrões de dados e governança

- Nível 1:


  - Definição informal de convenções e nomes

- Nível 2:


  - Padrões digitais limitados a sistemas locais

- Nível 3:


  - Modelo de dados corporativo implementado parcialmente

- Nível 4:


  - Governança formal e indicadores de qualidade de dados

- Nível 5:


  - Validações automáticas e correção preditiva de erros

- Nível 6:


  - Padronização adaptativa e gestão autônoma da qualidade de dados

##### Amostragem

- Entrevistas com equipes de TI, engenharia de dados e automação; revisão documental de modelos e padrões de integração; observação de rotinas de sincronização e controle de qualidade de dados; avaliação de logs de consistência entre sistemas corporativos e operacionais.

##### I.1.1.5 Questão: Em que medida a organização utiliza análises preditivas, algoritmos...
Em que medida a organização utiliza análises preditivas, algoritmos ou IA para integrar automaticamente os fluxos de informação e ajustar os processos produtivos em tempo real?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização não utiliza análises preditivas; decisões são baseadas em relatórios manuais e históricos. |
| 1 | Existem iniciativas isoladas de análise de dados, realizadas de forma manual ou experimental. |
| 2 | Ferramentas digitais registram dados, mas as análises são reativas e voltadas apenas a eventos passados. |
| 3 | Há uso de relatórios analíticos automatizados e dashboards integrados entre os sistemas de operação e gestão. |
| 4 | A empresa realiza análises de diagnóstico , utilizando dados integrados para tomada de decisão. |
| 5 | Modelos analíticos e algoritmos de IA permitem prever falhas e propor ajustes processos. |
| 6 | A organização opera de forma autônoma e auto, ajustando parâmetros em tempo real com base em análises preditivas contínuas. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios e dashboards analíticos (BI, IoT, MES, ERP).

- Registros de uso de algoritmos preditivos e de IA.

- Logs de simulações e ajustes automáticos de processos.

- Documentação de integração entre sistemas de dados e analytics.

##### Métricas/KPIs

- Percentual de processos com suporte de análise preditiva.

- Redução de falhas ou paradas não planejadas.

- Tempo de resposta entre detecção e correção de desvios.

- Precisão dos modelos preditivos implementados.

##### Sinais por nível

- Nível 0:


  - Decisões baseadas em dados históricos manuais

- Nível 1:


  - Uso isolado de planilhas ou relatórios simples

- Nível 2:


  - Análises digitais descritivas e reativas

- Nível 3:


  - Dashboards integrados com indicadores de desempenho

- Nível 4:


  - Diagnósticos automáticos e análises de correlação

- Nível 5:


  - Modelos preditivos e automação de ajustes

- Nível 6:


  - Operação adaptativa e aprendizado autônomo em tempo real

##### Amostragem

- Amostragem Entrevistas com equipes de TI, engenharia de dados e produção; análise de relatórios de desempenho e logs de IA; verificação de dashboards preditivos e históricos de ajustes automáticos; observação de casos de uso de machine learning na operação.

#### Glossário
[Sem glossário]
### I.2 Dimensão: Integração Horizontal

#### I.2.1 Capacidade: Integração horizontal com parceiros da cadeia de valor
#### Bloco/Pilar
- Bloco: Processo

- Pilar: Operações/Cadeia de Suprimentos

- Dimensão: Integração Horizontal

#### Resumo Descritivo
A integração horizontal de sistemas de informação representa a capacidade de uma organização de conectar e sincronizar processos, dados e fluxos de trabalho entre diferentes unidades e parceiros da cadeia de valor — como fornecedores, produção, logística e clientes. Nos modelos ACATECH e SIRI, essa integração é um eixo essencial da maturidade digital, complementando a integração vertical. Enquanto a integração vertical conecta os níveis hierárquicos internos (do chão de fábrica à gestão corporativa), a integração horizontal conecta funções e organizações distintas, garantindo continuidade e transparência nas operações de ponta a ponta. Essa capacidade permite o compartilhamento automatizado e seguro de informações entre sistemas internos e externos (ERP, SCM, CRM, MES, plataformas de IoT, etc.), possibilitando coordenação ágil da cadeia de suprimentos, rastreabilidade global e resposta rápida a variações de demanda. À medida que a maturidade evolui, a organização avança de trocas manuais e isoladas para ecossistemas digitais colaborativos, baseados em dados padronizados, interoperabilidade e inteligência analítica. Nos níveis mais altos, essa integração torna-se preditiva e adaptativa, permitindo que redes de valor inteiras reajam em tempo real a mudanças no mercado, na produção ou na logística.
#### Questões
##### I.2.1.1 Questão: Em que medida os sistemas internos da organização (ERP, MES, SCM,...
Em que medida os sistemas internos da organização (ERP, MES, SCM, CRM) estão integrados aos sistemas de fornecedores, distribuidores e clientes, permitindo troca automatizada e segura de informações?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há integração entre sistemas internos e externos; trocas de dados são manuais e ocasionais. |
| 1 | Há procedimentos formais de comunicação com parceiros, mas as trocas são feitas por e-mail, planilhas ou portais manuais. |
| 2 | Existem trocas digitais pontuais via arquivos ou interfaces simples, com baixa automação. |
| 3 | Os sistemas corporativos (ERP, MES, SCM) estão conectados a parceiros principais, com atualizações automatizadas e regulares. |
| 4 | A integração cobre a maioria dos parceiros; há monitoramento da qualidade dos dados e dashboards compartilhados. |
| 5 | A conectividade é suportada por análises preditivas e automação inteligente, antecipando falhas e sincronizando processos. |
| 6 | A interoperabilidade é total e autônoma; os sistemas interagem em tempo real com parceiros, ajustando fluxos de forma auto. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Diagramas de arquitetura de integração entre ERP, MES e sistemas externos.

- Logs e registros de comunicação automatizada entre sistemas.

- Documentação técnica de APIs, EDI ou middleware de integração.

- Relatórios de consistência e desempenho de dados trocados.

##### Métricas/KPIs

- Percentual de parceiros integrados digitalmente.

- Volume de transações automatizadas na cadeia de valor.

- Tempo médio de atualização de dados entre empresas.

##### Sinais por nível

- Nível 0:


  - Comunicação manual, sem integração de sistemas

- Nível 1:


  - Trocas formais, mas dependentes de processos manuais

- Nível 2:


  - Integração digital limitada e não padronizada

- Nível 3:


  - Conexões automatizadas com principais parceiros

- Nível 4:


  - Padronização e controle da qualidade de dados integrados

- Nível 5:


  - Automação inteligente e preditiva das comunicações

- Nível 6:


  - Interoperabilidade autônoma e adaptativa em tempo real

##### Amostragem

- Entrevistas com equipes de TI, logística, produção e suprimentos; observação de rotinas de comunicação com fornecedores e clientes; revisão de documentação técnica e logs de integração; análise de indicadores de desempenho da cadeia de valor integrada.

##### I.2.1.2 Questão: Até que ponto os processos de suprimento, produção, logística e...
Até que ponto os processos de suprimento, produção, logística e entrega estão sincronizados digitalmente entre diferentes unidades e parceiros da cadeia?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os processos entre unidades e parceiros não são coordenados; as trocas de informação são manuais e reativas. |
| 1 | Existem procedimentos formais de comunicação e controle, mas sem integração digital entre sistemas. |
| 2 | Alguns processos são digitalizados, porém as trocas entre parceiros ainda dependem de intervenções manuais. |
| 3 | Os principais processos (suprimento, produção, entrega) estão conectados e atualizados digitalmente em intervalos regulares. |
| 4 | A sincronização é quase em tempo real; os fluxos são monitorados por dashboards compartilhados entre parceiros. |
| 5 | O sistema utiliza análises preditivas para antecipar gargalos, ajustar prazos e otimizar a coordenação entre elos da cadeia. |
| 6 | A sincronização é total e autônoma; os processos se ajustam dinamicamente em tempo real, com base em aprendizado contínuo. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Mapas e fluxogramas de processos ponta a ponta.

- Logs e registros de integração entre ERP, SCM e sistemas logísticos.

- Dashboards operacionais compartilhados entre parceiros.

- Relatórios de desempenho e indicadores de sincronização.

##### Métricas/KPIs

- Percentual de processos sincronizados digitalmente.

- Taxa de divergência entre planos e execução.

- Nível de visibilidade entre parceiros (quantos compartilham dados em tempo real).

##### Sinais por nível

- Nível 0:


  - Comunicação manual e reativa

- Nível 1:


  - Processos formais, mas não integrados digitalmente

- Nível 2:


  - Digitalização parcial e isolada

- Nível 3:


  - Integração entre processos principais

- Nível 4:


  - Monitoramento contínuo e dashboards compartilhados

- Nível 5:


  - Sincronização preditiva e ajustes automáticos

- Nível 6:


  - Adaptação autônoma e colaboração em tempo real

##### Amostragem

- Entrevistas com equipes de suprimentos, logística e produção; observação prática de processos interdepartamentais; revisão de logs de atualização de sistemas; avaliação de indicadores de sincronização entre parceiros.

##### I.2.1.3 Questão: Em que grau a organização e seus parceiros mantêm rastreabilidade...
Em que grau a organização e seus parceiros mantêm rastreabilidade digital e visibilidade compartilhada sobre materiais, produtos e fluxos de informação?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há mecanismos formais de rastreabilidade; as informações de fluxo são registradas manualmente e localmente. |
| 1 | Existem registros internos de rastreamento, mas não há compartilhamento estruturado entre parceiros. |
| 2 | A rastreabilidade é digital, porém restrita a etapas internas do processo produtivo. |
| 3 | A rastreabilidade é digital e parcial entre parceiros diretos (ex: fornecedor principal e cliente imediato). |
| 4 | Há rastreabilidade ponta a ponta, com dados compartilhados em painéis comuns e validações automáticas. |
| 5 | A rastreabilidade inclui análises preditivas para detectar anomalias, falhas ou riscos na cadeia. |
| 6 | A rede é totalmente transparente e autônoma; a rastreabilidade é dinâmica, em tempo real e autoajustável. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Registros de lotes, ordens de produção e rastreabilidade.

- Logs de integração entre ERP, SCM, PLM e sistemas de transporte.

- Dashboards de rastreamento e relatórios de conformidade.

- Documentos de controle de qualidade e certificações de origem.

##### Métricas/KPIs

- Percentual de produtos ou processos com rastreabilidade digital completa.

- Tempo médio de identificação de origem e destino de itens.

- Percentual de parceiros que compartilham dados de rastreamento.

- Taxa de inconsistência ou falhas detectadas na cadeia de rastreamento.

##### Sinais por nível

- Nível 0:


  - Registros manuais e fragmentados

- Nível 1:


  - Rastreabilidade formal, mas local

- Nível 2:


  - Dados digitais internos

- Nível 3:


  - Integração parcial entre alguns parceiros

- Nível 4:


  - Rastreabilidade ponta a ponta digital e validada

- Nível 5:


  - Análise preditiva de falhas e anomalias

- Nível 6:


  - Transparência autônoma, integrada e em tempo real

##### Amostragem

- Entrevistas com equipes de produção, logística, qualidade e compliance; revisão documental de relatórios de rastreamento e auditorias; observação prática de sistemas de rastreamento interorganizacional; análise de logs de integração e plataformas colaborativas.

##### I.2.1.4 Questão: Em que medida a organização utiliza plataformas digitais ou sistemas...
Em que medida a organização utiliza plataformas digitais ou sistemas colaborativos para troca de informações, planejamento conjunto e coordenação com fornecedores e clientes?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A colaboração entre parceiros ocorre de forma informal, sem sistemas digitais estruturados. |
| 1 | Existem reuniões e trocas de informações regulares, mas sem integração digital entre plataformas. |
| 2 | A comunicação é realizada por ferramentas digitais isoladas (e-mail, planilhas, portais). |
| 3 | Há uso de plataformas digitais colaborativas para planejamento e execução conjunta de processos. |
| 4 | A colaboração digital inclui compartilhamento de dados em dashboards e mecanismos de validação conjunta de decisões. |
| 5 | O processo de co-decisão é suportado por análises preditivas e automação parcial de fluxos de aprovação. |
| 6 | A colaboração é autônoma e contínua; sistemas e parceiros tomam decisões coordenadas em tempo real com base em dados inteligentes. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Registros de uso de plataformas colaborativas (portais B2B, SCM, CRM).

- Logs de reuniões digitais e processos de aprovação conjunta.

- Documentação de integração de dados compartilhados.

- Relatórios de decisões conjuntas e planos de ação colaborativos.

##### Métricas/KPIs

- Percentual de processos gerenciados por plataformas colaborativas.

- Tempo médio para tomada de decisão conjunta.

- Nível de participação dos parceiros em decisões críticas.

- Grau de automação dos fluxos de aprovação interorganizacionais.

##### Sinais por nível

- Nível 0:


  - Comunicação informal e não registrada

- Nível 1:


  - Processos de decisão formais, mas sem digitalização

- Nível 2:


  - Uso de ferramentas digitais isoladas

- Nível 3:


  - Plataforma colaborativa implementada

- Nível 4:


  - Dashboards compartilhados e decisões monitoradas

- Nível 5:


  - Suporte analítico preditivo a decisões conjuntas

- Nível 6:


  - Co-decisão automatizada e adaptativa em tempo real

##### Amostragem

- Entrevistas com equipes de logística, suprimentos, TI e planejamento; revisão de registros de plataformas colaborativas e logs de comunicação; observação de rotinas de tomada de decisão em rede. Avaliação de indicadores de desempenho colaborativo.

##### I.2.1.5 Questão: Até que ponto a empresa aplica análise de dados e algoritmos...
Até que ponto a empresa aplica análise de dados e algoritmos preditivos para automatizar a coordenação entre unidades internas e parceiros externos, antecipando demandas e riscos?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | As decisões da cadeia de suprimentos são manuais e baseadas em relatórios históricos. |
| 1 | Existem relatórios e análises básicas de dados, sem integração entre áreas ou parceiros. |
| 2 | As análises são realizadas em sistemas digitais, mas os dados permanecem isolados e a automação é limitada. |
| 3 | Os sistemas de planejamento e execução (ERP, SCM, MES) compartilham dados analíticos básicos entre as principais unidades. |
| 4 | A empresa utiliza ferramentas analíticas integradas para diagnóstico e otimização dos processos logísticos e produtivos. |
| 5 | Modelos preditivos e algoritmos de IA antecipam demandas e riscos, ajustando automaticamente processos operacionais. |
| 6 | A cadeia de valor opera de forma autônoma e cognitiva, com aprendizado contínuo e decisões automáticas em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios analíticos e dashboards integrados (BI, SCM, ERP).

- Logs de automação e decisões geradas por IA.

- Modelos preditivos implementados (previsão de demanda, manutenção, logística).

- Documentação técnica de sistemas de análise e aprendizado de máquina.

##### Métricas/KPIs

- Percentual de decisões automatizadas na cadeia de valor.

- Precisão dos modelos preditivos utilizados.

- Redução de falhas e desvios operacionais detectados antecipadamente.

- Tempo médio de resposta a variações de demanda.

##### Sinais por nível

- Nível 0:


  - Decisões reativas e manuais

- Nível 1:


  - Relatórios básicos sem integração

- Nível 2:


  - Dados digitais, mas isolados

- Nível 3:


  - Análises integradas entre áreas principais

- Nível 4:


  - Diagnósticos e otimização digital integrada

- Nível 5:


  - Modelos preditivos e automação de ajustes

- Nível 6:


  - Operação cognitiva e autônoma em tempo real

##### Amostragem

- Entrevistas com áreas de planejamento, TI, logística e suprimentos; verificação dos sistemas de análise de dados e IA utilizados; avaliação de relatórios de desempenho e predição de eventos; análise de logs de automação e respostas em tempo real.

##### I.2.1.6 Questão: Em que medida a organização e seus parceiros são capazes de reagir de...
Em que medida a organização e seus parceiros são capazes de reagir de forma autônoma e coordenada a eventos inesperados?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização reage de forma manual e isolada a eventos imprevistos, sem coordenação com parceiros. |
| 1 | Existem planos de contingência documentados, mas sem suporte digital nem comunicação automatizada. |
| 2 | Há registro digital de eventos e respostas, mas a reação ainda depende de intervenção humana. |
| 3 | Os sistemas internos e de parceiros trocam informações automaticamente, permitindo resposta coordenada básica. |
| 4 | O monitoramento é contínuo; alertas e recomendações automáticas suportam decisões de mitigação colaborativas. |
| 5 | Alertas de eventos (previstos pela Q5 ou inesperados) disparam reconfigurações de fluxo semi-automáticas, com validação humana para mitigar o impacto e coordenar parceiros. |
| 6 | A rede de valor demonstra auto-organização: reage a disrupções em tempo real de forma autônoma, redistribuindo recursos e funções na cadeia de forma colaborativa e aprendendo com o evento. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de incidentes e respostas operacionais.

- Logs de monitoramento em tempo real (SCM, ERP, IoT, sistemas logísticos).

- Modelos de simulação e análise preditiva de riscos.

- Protocolos de contingência automatizados e dashboards de controle.

##### Métricas/KPIs

- Tempo médio de resposta a eventos disruptivos.

- Percentual de processos recuperados automaticamente.

- Taxa de falhas mitigadas antes do impacto.

- Nível de integração de dados em alertas e planos de reação.

##### Sinais por nível

- Nível 0:


  - Reações manuais e locais.

- Nível 1:


  - Planos de contingência formais, sem integração.

- Nível 2:


  - Monitoramento digital, mas reações manuais.

- Nível 3:


  - Coordenação automatizada entre unidades.

- Nível 4:


  - Alertas e recomendações automáticas.

- Nível 5:


  - Previsão de eventos e reconfiguração automática.

- Nível 6:


  - Resposta adaptativa autônoma e colaborativa.

##### Amostragem

- Entrevistas com gestores de cadeia de suprimentos, TI e operações; análise de registros de eventos e respostas operacionais; observação de testes de contingência ou simulações; avaliação de logs e dashboards de sistemas de monitoramento.

#### Glossário
[Sem glossário]
### I.3 Dimensão: Ciclo de Vida de Produto Integrado

#### I.3.1 Capacidade: Foco em benefícios ao cliente
#### Bloco/Pilar
- Bloco: Processo

- Pilar: Ciclo de Vida do Produto

- Dimensão: Ciclo de Vida de Produto Integrado

#### Resumo Descritivo
Esta dimensão avalia a integração de pessoas, processos e sistemas ao longo do ciclo de vida do
produto (desde design até o descarte). O objetivo é encurtar os ciclos de desenvolvimento, usando
Gêmeos Digitais (Digital Twins) e sistemas PLM para criar uma Sombra Digital do produto. Isso
permite agilidade e novos modelos de negócio, como o Product-as-a-Service.
#### Questões
##### I.3.1.1 Questão: Como a informação do produto é gerenciada e compartilhada entre as...
Como a informação do produto é gerenciada e compartilhada entre as diferentes fases do seu ciclo de
vida (design, engenharia, produção, uso e serviço)?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há processos ou sistemas definidos para gerenciar informações do produto. |
| 1 | As informações são gerenciadas informalmente por departamentos isolados. |
| 2 | Existem procedimentos formais para troca de informações, mas ainda manuais. |
| 3 | As informações são digitalizadas, porém a integração entre sistemas é manual. |
| 4 | Sistemas digitais estão integrados, mas o fluxo ainda depende de controle humano. |
| 5 | fluxo de informações é automatizado com mínima intervenção humana. |
| 6 | O sistema aprende e adapta-se com base em dados reais do produto. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Mapas ou diagramas de fluxo de informação entre fases do ciclo de vida.

- Relatórios ou políticas de gestão de dados de produto (PLM/PDM).

- Capturas de tela ou documentação de integração entre sistemas (CAD–ERP–MES).

- Logs de atualização e versionamento de documentos técnicos.

- Evidências de uso de gêmeos digitais ou engenharia baseada em modelos (MBSE).

- Registros de feedback de uso e manutenção incorporados em novas versões de design.

##### Métricas/KPIs

- Índice de integração digital (%): proporção de sistemas conectados ao longo do ciclo de vida.

- Tempo médio de atualização de dados de produto: entre criação e sincronização em todos os
          sistemas.
- Taxa de retrabalho por inconsistência de informação (%).

- Percentual de produtos com feedback de uso incorporado no redesenho.

##### Sinais por nível

- Nível 0:


  - As informações são dispersas e dependem de pessoas específicas.

  - Inexistem registros formais e não há consciência sobre controle, rastreabilidade ou versionamento.


- Nível 1:


<!-- pág. original: 284/465 -->
  - Cada área mantém registros próprios em planilhas ou papel.

  - A troca de informação é manual.

  - Ocorrem erros frequentes e não há padronização nem controle de versões.


- Nível 2:


  - Processos documentados em papel.

  - Repositórios físicos separados.

  - Atualizações manuais e controle de versões limitado, com pouca rastreabilidade interdepartamental.
  - Procedimentos documentados, mas sem repositório centralizado.


- Nível 3:


  - Uso de e-mails e pastas compartilhadas.

  - Integração feita por exportação/importação,

  - Ausência de PLM centralizado e falhas na visibilidade em tempo real


- Nível 4:


  - PLM implantado, integração entre áreas garantida digitalmente.

  - Dados rastreáveis e seguros, mas exigindo validação e supervisão constante por pessoas.
  - Rastreabilidade de versões e controle de acesso.


- Nível 5:


  - Dados fluem entre CAD, ERP e MES automaticamente.

  - Há continuidade digital, sincronização entre engenharia e produção, e redução de inconsistências e retrabalhos.


- Nível 6:


<!-- pág. original: 285/465 -->
  - Gêmeos digitais e MBSE otimizam processos.

  - IA gera insights automáticos.

  - Feedback de uso atualiza projetos e o ciclo de vida é totalmente interconectado.

##### Amostragem

- Selecionar 3–5 artefatos referentes a processos relevantes (evidências de logs de
          sincronização ou dashboards PLM), atualizados dos últimos 90 dias

##### I.3.1.2 Questão: Em que medida a empresa utiliza representações digitais (como modelos...
Em que medida a empresa utiliza representações digitais (como modelos 3D, simulações ou gêmeos
digitais) para o design, engenharia e otimização de produtos e processos?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há uso de ferramentas digitais para modelagem ou simulação. |
| 1 | Representações digitais são inexistentes ou ocasionais. |
| 2 | CAD é utilizado apenas para desenhos ou modelos estáticos. |
| 3 | Modelos digitais são usados em etapas específicas, de forma isolada. |
| 4 | Modelos digitais abrangentes são integrados via PLM. |
| 5 | A empresa usa gêmeos digitais para simulação e otimização. |
| 6 | Gêmeos digitais totalmente integrados reagem e otimizam-se em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Exemplos de modelos CAD/CAE e registros de versões digitais de produtos.

- Relatórios de simulações e resultados de análises virtuais (deformação, fluxo, resistência).


<!-- pág. original: 286/465 -->
- Documentação do sistema PLM integrando design, engenharia e produção.

- Evidências de uso de gêmeos digitais em operação (dashboards, logs, relatórios).

- Modelos MBSE (Model-Based Systems Engineering) ou especificações digitais do produto.

- Integrações demonstradas entre ferramentas de simulação, ERP e MES.

##### Métricas/KPIs

- Percentual de produtos desenvolvidos com modelos digitais completos (%).

- Tempo médio de ciclo de design (comparando desenvolvimento físico vs. digital).

- Taxa de reutilização de modelos e simulações em novos projetos (%).

- Grau de integração entre gêmeos digitais e dados operacionais (%).

##### Sinais por nível

- Nível 0:


  - Desenvolvimento físico e experimental.

  - Ausência de CAD ou PLM.

  - Decisões baseadas apenas em testes empíricos e experiência prática.


- Nível 1:


  - Modelos e desenhos feitos manualmente.

  - Protótipos físicos predominam.

  - Nenhuma padronização no design digital.


- Nível 2:


  - Criação de modelos 2D/3D simples sem integração com outras fases.

  - Ausência de simulações ou análises baseadas em modelos digitais.


- Nível 3:


<!-- pág. original: 287/465 -->
  - Uso de CAD/CAE com simulações pontuais.

  - Dados não conectados entre departamentos.

  - Ausência de uma espinha dorsal de informação.

  - Benefícios diretos observados em tempo e custo de desenvolvimento.


- Nível 4:


  - Representações digitais conectam requisitos, componentes e testes.

  - Integração parcial com outras áreas.

  - Otimização ainda guiada manualmente.


- Nível 5:


  - Dados reais atualizam modelos digitais.

  - Sistemas automatizam melhorias.

  - Integração entre produto e processo com mínima intervenção humana.

  - Retroalimentação de dados de uso em simulações.


- Nível 6:


  - Simulações contínuas, IA para análise preditiva e auto-adaptação.

  - Modelos MBSE conectam todas as fases do ciclo de vida.

  - Adaptação dinâmica de parâmetros de produto para customização do cliente.

##### Amostragem

- Selecionar 3–5 artefatos referentes a processos relevantes, atualizados dos últimos 90 dias


##### I.3.1.3 Questão: Como a empresa integra e utiliza dados de diversas fontes (design,...
Como a empresa integra e utiliza dados de diversas fontes (design, produção, uso do cliente, serviço)
para impulsionar a tomada de decisões e a inovação em produtos e processos?


<!-- pág. original: 288/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Dados não são coletados nem usados de forma sistemática. |
| 1 | Dados são coletados pontualmente, sem integração entre áreas. |
| 2 | Dados são coletados em algumas fases, mas sem consolidação. |
| 3 | Dados digitais são coletados, porém analisados de forma isolada. |
| 4 | Dados de múltiplas fontes são conectados em sistemas integrados. |
| 5 | Integração e análise de dados são amplamente automatizadas. |
| 6 | A empresa usa IA e análise avançada para otimização contínua. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentação de arquitetura de dados e fluxos de integração entre sistemas.

- Dashboards de BI, relatórios de analytics e logs de coleta de dados.

- Modelos de dados ou dicionários de integração entre PLM, ERP e CRM.

- Evidências de uso de algoritmos ou IA para análise preditiva.

- Relatórios de correlação entre dados de campo e decisões de engenharia.

- Políticas internas de governança e qualidade de dados.

##### Métricas/KPIs

- Percentual de fontes de dados integradas ao longo do ciclo de vida.

- Tempo médio entre coleta e uso efetivo de dados para decisão.

- Taxa de decisões baseadas em dados vs. decisões empíricas (%).

- Número de insights preditivos aplicados em produtos/processos por ano.


<!-- pág. original: 289/465 -->
##### Sinais por nível

- Nível 0:


  - Não há estrutura para registro de dados.

  - Decisões são totalmente intuitivas, sem base factual ou indicadores consistentes.


- Nível 1:


  - Informações dispersas em relatórios manuais.

  - Cada setor mantém registros próprios.

  - Decisões guiadas por experiência empírica.


- Nível 2:


  - Processos básicos de coleta.

  - Uso de relatórios de produção ou vendas.

  - Integração limitada e dependente de pessoas.


- Nível 3:


  - Uso de planilhas e bancos de dados simples.

  - Análise manual.

  - Integração inconsistente entre dados de design, produção e cliente.


- Nível 4:


  - PLM ou ERP integrando informações.

  - Coleta estruturada.

  - Dados de uso real alimentam melhorias.

  - Análise ainda predominantemente humana.


<!-- pág. original: 290/465 -->
- Nível 5:


  - Processos automatizados de coleta e correlação.

  - Dados em tempo real e históricos usados para decisão.

  - Mínima intervenção humana, mas ainda sem aprendizado adaptativo.


- Nível 6:


  - Big Data e Machine Learning integram todas as fases.

  - Insights preditivos e prescritivos.

  - Inovação contínua orientada por dados.

  - Integração preditiva e prescritiva de todas as fontes.

##### Amostragem

- Selecionar 3–5 artefatos referentes a processos relevantes, atualizados dos últimos 90 dias


##### I.3.1.4 Questão: Como a empresa lida com a colaboração e a integração de parceiros...
Como a empresa lida com a colaboração e a integração de parceiros externos (fornecedores, clientes,
centros de pesquisa) no design e desenvolvimento de produtos?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A empresa opera isoladamente, sem envolvimento de parceiros externos. |
| 1 | A interação com parceiros é pontual e sem estrutura formal. |
| 2 | A colaboração ocorre de forma reativa, sem integração digital. |
| 3 | Ferramentas digitais são usadas apenas para troca de informações. |
| 4 | Plataformas digitais suportam colaboração em fases específicas do ciclo de vida. |
| 5 | Os sistemas da empresa e dos parceiros estão conectados digitalmente. |
| 6 | A empresa integra um ecossistema digital de inovação com parceiros. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Contratos de cooperação, NDAs e acordos de co-desenvolvimento com parceiros externos.

- Documentação de plataformas digitais de colaboração (portais, PLM compartilhado).

- Registros de projetos colaborativos com clientes, fornecedores e centros de pesquisa.

- Logs ou relatórios de integração de sistemas com parceiros (API, EDI, etc.).

- Evidências de participação em ecossistemas de inovação ou clusters tecnológicos.

- Casos de co-design ou co-engenharia documentados entre parceiros e a empresa.

##### Métricas/KPIs

- Percentual de projetos de produto desenvolvidos com participação externa.

- Tempo médio de resposta na troca de informações com parceiros.

- Número de parceiros integrados digitalmente na cadeia de valor.

- Índice de inovação colaborativa (projetos cocriados / total de projetos).

##### Sinais por nível

- Nível 0:


  - Não há trocas de informação, contratos ou interação formal com fornecedores, clientes ou centros de pesquisa.


- Nível 1:


  - Contato eventual por e-mails ou reuniões.

  - Ausência de processos definidos de cooperação ou compartilhamento de dados.


<!-- pág. original: 292/465 -->
- Nível 2:


  - Feedback pontual de clientes e fornecedores.

  - Troca manual de informações.

  - Decisões centralizadas e comunicação não sistemática.


- Nível 3:


  - Envio de arquivos por e-mail ou plataformas simples.

  - Ausência de workflows integrados.

  - Cooperação restrita a compartilhamento documental.

  - Uso de ferramentas básicas, sem controle de versão nem rastreabilidade.


- Nível 4:


  - Integração com clientes e fornecedores em projetos.

  - Uso de portais colaborativos.

  - Decisões conjuntas ainda exigem supervisão humana.

  - Mecanismos de controle de acesso e versionamento compartilhado.


- Nível 5:


  - Integração horizontal entre sistemas.

  - Troca automática de dados.

  - Personalização conjunta de produtos.

  - Colaboração contínua e estruturada.


- Nível 6:


  - Plataformas de IA otimizam co-criação.


<!-- pág. original: 293/465 -->
  - Dados de uso atualizam projetos.

  - Redes colaborativas geram novos modelos de negócio (Product as a Service).

  - Gestão de propriedade intelectual e compliance digital colaborativo.

##### Amostragem

- Selecionar 3–5 artefatos referentes a processos relevantes, atualizados dos últimos 90 dias


##### I.3.1.5 Questão: Como a empresa gerencia e incorpora feedback do uso do produto e...
Como a empresa gerencia e incorpora feedback do uso do produto e requisitos do cliente para refinar
o design e otimizar o desempenho ao longo do ciclo de vida?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A empresa não coleta nem utiliza feedback ou dados de uso. |
| 1 | Feedback é coletado esporadicamente e usado de forma não sistemática. |
| 2 | Feedback é obtido por meios simples e usado ocasionalmente. |
| 3 | Ferramentas digitais coletam dados e feedback, mas sem integração. |
| 4 | Sistemas conectados integram dados de uso e feedback de clientes. |
| 5 | Feedback e dados de uso são analisados automaticamente. |
| 6 | Feedback e uso do produto são analisados por IA em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de feedback de clientes e históricos de tickets de suporte.

- Registros de integração entre CRM, PLM e sistemas de pós-venda.

- Logs de coleta automática de dados de uso (IoT, sensores, telemetria).

- Evidências de atualizações de produto baseadas em feedback de campo.


<!-- pág. original: 294/465 -->
- Planos de melhoria contínua derivados de análises de feedback.

- Casos documentados de personalização ou atualização via software.

##### Métricas/KPIs

- Percentual de feedbacks processados e incorporados em novos produtos.

- Tempo médio entre coleta de feedback e ação corretiva ou melhoria.

- Taxa de automação da análise de feedback (%).

- Número de produtos com telemetria e coleta ativa de dados de uso.

##### Sinais por nível

- Nível 0:


  - Melhoria de produtos baseada em intuição.

  - Inexistência de mecanismos formais de coleta ou canais de comunicação estruturados.


- Nível 1:


  - Reclamações e sugestões recebidas informalmente.

  - Melhorias ad-hoc sem registro ou análise sistemática.


- Nível 2:


  - Pesquisas manuais (sem integração com engenharia) ou canais básicos.

  - Dados analisados pontualmente.

  - Inexistência de monitoramento do uso do produto.


- Nível 3:


  - Uso de CRM básico ou formulários online.

  - Análise em planilhas.

  - Integração restrita entre pós-venda e engenharia.


<!-- pág. original: 295/465 -->
- Nível 4:


  - PLM/CRM integrados.

  - Dados de uso capturados por sensores.

  - Atualizações via software.

  - Análises e decisões ainda humanas.

  - Fechamento de ciclo entre cliente e desenvolvimento.


- Nível 5:


  - Sistemas identificam tendências.

  - Sugestões automáticas de otimização.

  - Integração direta com processos de design e engenharia.

  - Automatização parcial do processo de melhoria do design.


- Nível 6:


  - Machine Learning gera insights preditivos.

  - Design ajustado dinamicamente (product-as-a-service).

  - Novos modelos de negócio e serviços personalizados emergem.

##### Amostragem

- Selecionar 3–5 artefatos referentes a processos relevantes, atualizados dos últimos 90 dias

#### Glossário
[Sem glossário]
### I.4 Dimensão: Automação do Chão de Fábrica

#### I.4.1 Capacidade: Design de interfaces orientado à tarefa


<!-- pág. original: 297/465 -->
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Automação

- Dimensão: Automação do Chão de Fábrica

#### Resumo Descritivo
Esta dimensão avalia o grau e a flexibilidade da automação e sua integração em múltiplos sistemas no
local onde a produção e gestão de bens são realizadas. O foco é otimizar os níveis gerais de
automação dos processos de produção e, em estágios mais altos, permitir a reconfiguração flexível de
máquinas para fabricar maior variedade de produtos com prazos curtos.
#### Questões
##### I.4.1.1 Questão: A informação digital se adapta dinamicamente (em conteúdo e formato)...
A informação digital se adapta dinamicamente (em conteúdo e formato) à necessidade específica do
operador para a tarefa em questão?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A informação para execução de tarefas é exclusivamente analógica (e.g., impressa em papel ou transmitida verbalmente). |
| 1 | A informação é digital (e.g., em PDFs ou planilhas estáticas), mas é genérica, não filtrada e não se adapta à tarefa. |
| 2 | As interfaces são digitais e conseguem filtrar dados (usando apps ou sistemas de TI/OT), mostrando informações relevantes para a área de trabalho ou a máquina, mas não se ajustam dinamicamente à progressão da tarefa. |
| 3 | O conteúdo da interface é continuamente ajustado à tarefa que está sendo realizada, assegurando que apenas a informação relevante seja entregue no momento oportuno (princípio push). |
| 4 | O conteúdo e a apresentação da interface são adaptados não só à tarefa, mas também ao nível de habilidade e competência do funcionário que está utilizando o sistema. |
| 5 | O sistema de assistência é capaz de diagnosticar e prever desvios (erros potenciais) antes que ocorram, ajustando proativamente a interface para guiar o operador à otimização da tarefa em tempo real. |
| 6 | O sistema de informação é auto-aprendiz e entrega conhecimento continuamente contextualizado, permitindo que os operadores participem ativamente no desenho e aprimoramento da interface, focando em autocontrole e melhoria contínua. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Interfaces Homem-Máquina (HMI) e Dashboards.

- Documentação de Integração Vertical de Sistemas (TI/OT).

- Registros de Captura de Dados Operacionais e Sensores Inteligentes.

- Uso de Identificadores (Auto-ID) e Rastreamento (M20).

- Instruções de Trabalho Digitais ou Aplicações (Apps) de Chão de Fábrica.

- Sistemas de Software Avançados (ERP, MES, PLM).

##### Métricas/KPIs

- Taxa de Redução de Erros de Procedimento (TREP)

- Tempo Médio de Reação a Desvios Operacionais (TMRDO)

- Proporção de Tarefas Críticas Guiadas por Sistemas de Assistência Digital (PTCGSAD)

- Índice de Utilização de Dados Contextuais (IUDC).

##### Sinais por nível

- Nível 0:


  - Os processos verticais não estão definidos explicitamente e são gerenciados por métodos informais ou ad-hoc.
  - Não há uso de dispositivos eletrônicos ou digitais no local.


<!-- pág. original: 299/465 -->
  - As instruções de trabalho são baseadas em papel ou comunicação verbal, sem qualquer automação de processos repetitivos.


- Nível 1:


  - A informação é definida e executada por humanos, com o suporte de ferramentas analógicas (como sistemas de rastreamento baseados em papel).
  - Sistemas de OT (Tecnologia Operacional) e TI (Tecnologia da Informação) são utilizados para executar tarefas pré-programadas baseadas em lógica estática, mas a informação gerada é estática (e.g., PDFs, planilhas).
  - Há introdução de TI no chão de fábrica e em outros lugares, mas os sistemas de TI e OT operam isoladamente (silos).


- Nível 2:


  - Os processos verticais digitalizados são concluídos por humanos, com o suporte de ferramentas digitais.
  - Sistemas de TI e OT gerenciam processos, mas ainda em silos.

  - Os sistemas são capazes de identificar desvios dos parâmetros predefinidos, notificando os operadores.
  - A empresa já trabalha com dados e documentos digitais que são amplamente acessíveis.


- Nível 3:


  - Agregação e visualização de dados em tempo quase real de diferentes sistemas de origem (MES, ERP) são alcançadas.
  - A informação é entregue aos funcionários de forma contextualizada.

  - É criado um "sombra digital" (digital shadow) da situação atual da empresa, permitindo que as decisões sejam baseadas em dados reais.
  - O sistema OT/IT consegue diagnosticar desvios e identificar causas potenciais.

  - Dispositivos móveis e wearables são utilizados para integrar os funcionários à plataforma digital.


<!-- pág. original: 300/465 -->
- Nível 4:


  - O sistema não apenas identifica desvios, mas também prevê estados futuros de ativos e sistemas.
  - O conhecimento adquirido é entregue aos funcionários de forma contextualizada e adaptada para apoiar a tomada de decisões de forma complexa e rápida.
  - Os funcionários aprimoram ativamente o sistema com seu próprio conhecimento no interesse da melhoria contínua.


- Nível 5:


  - A interface fornece informações que permitem simular possíveis cenários futuros para habilitar o suporte à decisão.
  - Sistemas OT e IT integrados de ponta a ponta estão analisando ativamente e reagindo aos dados.
  - O sistema notifica o pessoal relevante de desvios potenciais e fornece informações sobre as causas prováveis.
  - Esta etapa representa o estado de "Estar preparado" e entender "O que acontecerá?"


- Nível 6:


  - O sistema atinge a capacidade de resposta autônoma.

  - O processamento da informação é auto-aprendizagem, o que significa que os sistemas de informação se adaptam continuamente às circunstâncias em mudança.
  - Os sistemas podem executar decisões de forma autônoma para otimizar o desempenho e a eficiência de recursos.
  - A cultura da empresa demonstra um estilo de liderança democrático e confiança nos sistemas, e os funcionários participam ativamente na moldagem das mudanças e na documentação do conhecimento adquirido.
  - O loop de aprendizado de interface é centrado no operador.

##### Amostragem

- Selecionar 5–10 processos relevantes que envolvem a interação homem/máquina em Chão de
       Fábrica (gravações de tela e logs de interação HMI)


<!-- pág. original: 301/465 -->
##### I.4.1.2 Questão: O design de HMI dos sistemas de assistência no Chão de Fábrica...
O design de HMI dos sistemas de assistência no Chão de Fábrica utiliza tecnologias de visualização e
informação sensível ao contexto para orientar o operador na execução de tarefas?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | As interfaces são inexistentes ou predominantemente manuais/analógicas. |
| 1 | As interfaces HMI digitais executam tarefas pré-programadas e são genéricas. |
| 2 | Existem interfaces digitais HMI conectadas que fornecem informações básicas, mas não são totalmente orientadas à tarefa. |
| 3 | O design das interfaces é orientado à tarefa e fornece informação contexto-sensível em tempo real. |
| 4 | As interfaces integram sistemas de assistência que não só identificam desvios, mas também diagnosticam as potenciais causas. |
| 5 | As interfaces e sistemas de assistência integram análise preditiva para prever futuros estados de ativos e sistemas (manutenção preditiva, qualidade). |
| 6 | As interfaces facilitam a operação reconfigurável e autônoma, minimizando a intervenção humana. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Interfaces Homem-Máquina (HMI) e Dashboards.

- Documentação de Integração Vertical de Sistemas (TI/OT).

- Registros de Captura de Dados Operacionais e Sensores Inteligentes.

- Uso de Identificadores (Auto-ID) e Rastreamento (M20).

- Instruções de Trabalho Digitais ou Aplicações (Apps) de Chão de Fábrica

- Sistemas de Software Avançados (ERP, MES, PLM).


<!-- pág. original: 302/465 -->
##### Métricas/KPIs

- Tempo médio de resposta do operador a desvios.

- Redução de erros operacionais induzidos pelo operador.

- Adoção (%) de sistemas de assistência HMI por trabalhadores.

- Aumento da Eficácia Geral do Equipamento (OEE) por intervenção assistida.

##### Sinais por nível

- Nível 0:


  - O trabalho repetitivo é executado por humanos, sem automação.

  - A gestão dos processos é baseada em métodos informais ou ad-hoc.


- Nível 1:


  - As interfaces existem, mas o design não é adaptado à tarefa específica ou ao contexto do operador.
  - A intervenção humana é significativa, e a informação é fornecida primariamente através de ferramentas analógicas, como rastreamento baseado em papel.


- Nível 2:


  - As tecnologias de identificação e visualização são introduzidas, mas a informação fornecida ainda é estática ou requer intervenção humana para interpretação.
  - As máquinas e sistemas conseguem interagir ou trocar informação de forma limitada.


- Nível 3:


  - Sistemas de assistência fornecem informações contextuais usando tecnologias de Auto-ID (reconhecimento direto de objetos e seus atributos).
  - O feedback é baseado em dados reais do ambiente de processo, em vez de apenas planos ou previsões.
  - Feedback multimodal (visual, auditivo, tátil) - característica moderna de HMIs sensíveis ao contexto.


<!-- pág. original: 303/465 -->
  - O sistema pode notificar os operadores sobre desvios de parâmetros pré-definidos.


- Nível 4:


  - O design das interfaces incorpora a visualização da análise de dados para ajudar o operador a "entender" o que está acontecendo.
  - Há um foco na usabilidade e em aspectos ergonômicos na integração de processos.


- Nível 5:


  - As informações nas interfaces ajudam o operador a prever potenciais desvios e fornecem informações sobre as possíveis causas.
  - As interfaces permitem que a tomada de decisões seja baseada em cenários futuros simulados.
  - Assistência proativa (interfaces que sugerem ação).


- Nível 6:


  - Os sistemas de assistência realizam a execução autônoma de decisões para otimizar o desempenho e a eficiência.
  - O sistema também permite intervenção e customização.

  - As interfaces suportam a automação plug-and-play, permitindo que os processos de produção automatizados sejam reconfiguráveis de forma rápida e fácil.

##### Amostragem

- Selecionar 5–10 processos relevantes que envolvem a interação homem/máquina em Chão de
        Fábrica (vídeos de operação assistida e capturas de dashboards dinâmicos)
#### Glossário
[Sem glossário]
#### I.4.2 Capacidade: Interface de usuário específica


<!-- pág. original: 305/465 -->
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Automação

- Dimensão: Automação do Chão de Fábrica

#### Resumo Descritivo
Esta dimensão avalia o grau e a flexibilidade da automação e sua integração em múltiplos sistemas no
local onde a produção e gestão de bens são realizadas. O foco é otimizar os níveis gerais de
automação dos processos de produção e, em estágios mais altos, permitir a reconfiguração flexível de
máquinas para fabricar maior variedade de produtos com prazos curtos.
#### Questões
##### I.4.2.1 Questão: Qual o impacto do formato (e.g., AR, tabelas, voz) e tempo de entrega...
Qual o impacto do formato (e.g., AR, tabelas, voz) e tempo de entrega das interfaces no Chão de
Fábrica na otimização das atividades do operador?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | As interfaces específicas de usuário são inexistentes ou não digitais, não é possível avaliar seu impacto em termos de otimização de atividades. |
| 1 | As interfaces HMI são genéricas e não contextuais, os níveis de otimização são mínimos. |
| 2 | Há interfaces digitais conectadas, mas o fornecimento de informação é baseado no princípio pull (o operador busca a informação); logo, os níveis de otimização dependem exclusivamente do agente humano. |
| 3 | As interfaces fornecem informação sensível ao contexto, em tempo real, e o conteúdo é ajustado à tarefa em execução, habilitando processos automáticos de otimização. |
| 4 | As interfaces integram sistemas de assistência que, além de mostrar o estado atual, diagnosticam as causas prováveis dos desvios, ajudando o operador a "entender" (understanding) por que algo está acontecendo. |
| 5 | As interfaces exibem informação preditiva, permitindo que o operador "esteja preparado" (being prepared) para cenários futuros (e.g., manutenção preditiva) e tome decisões baseadas em simulações. |
| 6 | As interfaces suportam a operação reconfigurável e autônoma (plug-and-play), reduzindo latências de reação e minimizando erros induzidos por informação. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- HMI e SCADA (visualização contexto-sensível).

- Registros de erros operacionais ou de qualidade.

- Sistemas de assistência digital (AR/VR e wearables).

- Relatórios de execução de tarefas (MES/PLM/SCM).

- Logs de dados de sensores e IoT em tempo real.

- Documentação de usabilidade (ergonomia e task-flow).

##### Métricas/KPIs

- Redução de erros operacionais (induzidos por informação).

- Tempo Médio de Resposta a Alertas Críticos.

- Aumento da Produtividade por Tarefa Assistida.

- Score de Usabilidade e Adaptação da Interface.

- Latência de reação.

##### Sinais por nível

- Nível 0:


  - Os sistemas de TI/OT não estão em uso no Chão de Fábrica.

  - Os processos são executados por humanos sem automação.


<!-- pág. original: 307/465 -->
- Nível 1:


  - Os sistemas executam tarefas pré-programadas, e a informação exibida é estática ou não filtrada pelas necessidades do operador.
  - O operador precisa interpretar, buscar e classificar a informação por si próprio.

  - Baixo impacto observado na eficiência do operador.


- Nível 2:


  - As interfaces trocam informação, mas o design não é adaptado ao contexto da tarefa e não há agregação de dados em tempo real ou visualização abrangente.


- Nível 3:


  - O sistema permite que o operador "veja" (seeing) o que está acontecendo (e.g., status de produção, desvios) e tome decisões baseadas em dados reais (sombra digital)
  - Ocorre o monitoramento de indicadores de desempenho humano e de sistema.


- Nível 4:


  - A informação é entregue ativamente (princípio push), otimizada e com acesso controlado (e.g., apps para tarefas específicas).
  - O impacto é mensurado (por exemplo, aumento de OEE, redução de erros).


- Nível 5:


  - O sistema começa a fornecer instruções para prevenir desvios, não apenas reagir a eles.
  - Feedback contínuo de desempenho.


- Nível 6:


<!-- pág. original: 308/465 -->
  - O sistema de assistência adapta-se continuamente e executa decisões de forma autônoma, minimizando a necessidade de intervenção humana e garantindo a otimização contínua do desempenho e eficiência dos recursos.
  - Otimização baseada em IA e personalização dinâmica das interfaces, conforme perfil de operador.

##### Amostragem

- Selecionar 5–10 decisões relevantes (investimentos, padrões, fornecedores) dos últimos 90
        dias
- Selecionar 5-10 operações recentes com uso intensivo de interfaces de produção (ex

- : manutenção, setup, inspeção), observando logs de desempenho e reações do operador

#### Glossário
[Sem glossário]
### I.5 Dimensão: Automação Corporativa

#### I.5.1 Capacidade: Automação de processos administrativos
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Automação

- Dimensão: Automação Corporativa

#### Resumo Descritivo
A automação de processos administrativos refere-se à aplicação de tecnologia para executar, sem intervenção manual, as rotinas de vendas, marketing e aquisição/compras que sustentam a operação comercial da organização. Nos modelos ACATECH e SIRI, essa capacidade reflete o eixo Automação dentro do bloco Tecnologia, avaliando o quanto os fluxos de trabalho administrativos deixam de depender de execução humana repetitiva e passam a ser suportados por sistemas informatizados, workflows digitais e, nos estágios mais avançados, por automação inteligente capaz de ajustar prioridades e alçadas de forma autônoma. À medida que a maturidade evolui, a organização migra de controles manuais e planilhas paralelas para sistemas corporativos integrados (ERP, CRM, plataformas de compras), com visibilidade em tempo quase real do andamento dos processos.
#### Questões
##### I.5.1.1 Questão: Em que medida os processos de vendas, marketing e aquisição/compras...
Em que medida os processos de vendas, marketing e aquisição/compras da organização são executados por sistemas automatizados, em vez de controles manuais ou planilhas?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os processos são predominantemente manuais ou baseados em documentos físicos, com uso limitado de sistemas informatizados. |
| 1 | Sistemas computadorizados básicos (ERP, CRM) substituem registros em papel, mas com grande uso de planilhas paralelas. |
| 2 | Integrações entre sistemas corporativos (ERP, CRM, plataformas de compras) permitem troca de dados entre áreas, reduzindo retrabalho na alimentação de informações. |
| 3 | Fluxos de vendas, marketing e compras são suportados por workflows e painéis que dão visibilidade ao andamento de processos, prazos e responsabilidades. |
| 4 | É transparente como os processos administrativos impactam custos, níveis de serviço, prazos e desempenho comercial, permitindo revisão de políticas e regras de negócio. |
| 5 | Modelos analíticos são utilizados para prever demanda comercial, volume de pedidos e riscos de fornecimento, apoiando o planejamento de compras e campanhas. |
| 6 | A automação comercial suporta processos adaptativos, ajustando automaticamente fluxos, alçadas, prioridades e alocação de recursos em função de eventos e previsões de negócio. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Diagramas de arquitetura de sistemas comerciais e de compras (ERP, CRM, plataformas de e-procurement).

- Registros de workflows de aprovação e logs de automação de processos administrativos.

- Relatórios de desempenho de vendas, marketing e compras gerados por sistemas integrados.

- Documentação de regras de negócio e políticas comerciais parametrizadas em sistema.

##### Métricas/KPIs

- Percentual de processos de vendas/compras executados sem intervenção manual.

- Tempo médio de ciclo de um processo administrativo (do início à conclusão).

- Percentual de dados comerciais consistentes entre sistemas integrados.

##### Sinais por nível

- Nível 0:


  - Processos manuais e documentos físicos

  - ausência de sistemas informatizados

- Nível 1:


  - Uso de ERP/CRM básicos

  - dependência de planilhas paralelas

- Nível 2:


  - Integração entre sistemas comerciais e de compras

  - redução de retrabalho

- Nível 3:


  - Workflows digitais com painéis de acompanhamento

  - visibilidade de prazos e responsabilidades

- Nível 4:


  - Transparência de custos e desempenho comercial

  - revisão orientada a dados de políticas comerciais

- Nível 5:


  - Previsão de demanda e de necessidades de compra

  - planejamento apoiado por modelos analíticos

- Nível 6:


  - Ajuste automático de fluxos e alçadas

  - alocação adaptativa de recursos administrativos

##### Amostragem

- Entrevistas com equipes de vendas, marketing e suprimentos; análise documental de workflows e regras de aprovação; observação de rotinas de processamento de pedidos e compras; revisão de relatórios de desempenho comercial.

##### I.5.1.2 Questão: Até que ponto a organização utiliza automação inteligente (RPA, IA)...
Até que ponto a organização utiliza automação inteligente (RPA, IA) para reduzir o esforço manual em tarefas administrativas repetitivas de vendas, marketing e compras?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há uso de automação; tarefas repetitivas (emissão de pedidos, atualização de cadastros, geração de relatórios) são feitas manualmente. |
| 1 | Existem macros ou scripts pontuais para tarefas isoladas, sem padronização nem governança. |
| 2 | Ferramentas de automação digital registram e executam tarefas simples e estruturadas em sistemas locais. |
| 3 | Robôs de automação de processos (RPA) executam rotinas administrativas-chave de forma regular e monitorada. |
| 4 | A automação cobre a maioria das tarefas repetitivas do ciclo comercial, com indicadores de qualidade e exceções tratadas por workflow. |
| 5 | Algoritmos de IA classificam exceções e sugerem ações corretivas, reduzindo a necessidade de intervenção humana em casos não padronizados. |
| 6 | A automação inteligente opera de forma autônoma e adaptativa, ajustando regras de processamento com base em padrões aprendidos e eventos de negócio. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Inventário de robôs de automação (RPA) e scripts em produção.

- Logs de execução e taxas de exceção das automações administrativas.

- Documentação de governança de automação (donos de processo, controles de mudança).

##### Métricas/KPIs

- Percentual de tarefas administrativas cobertas por automação.

- Taxa de exceções tratadas automaticamente vs. manualmente.

- Redução de horas-homem em tarefas administrativas repetitivas.

##### Sinais por nível

- Nível 0:


  - Execução manual de tarefas repetitivas

- Nível 1:


  - Macros e scripts isolados sem governança

- Nível 2:


  - Automação digital local de tarefas simples

- Nível 3:


  - RPA cobrindo rotinas administrativas-chave

- Nível 4:


  - Automação abrangente com tratamento de exceções

- Nível 5:


  - IA classificando exceções e sugerindo ações

- Nível 6:


  - Automação autônoma e adaptativa de regras de processamento

##### Amostragem

- Entrevistas com equipes de TI, operações comerciais e automação de processos; inspeção do inventário de robôs/scripts em produção; análise de logs de exceção e relatórios de governança de automação.

##### I.5.1.3 Questão: Em que medida os sistemas de planejamento de demanda e gestão de...
Em que medida os sistemas de planejamento de demanda e gestão de recursos humanos estão informatizados e integrados aos demais sistemas corporativos de automação administrativa?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O planejamento de demanda e a gestão de RH são feitos de forma manual ou com apoio limitado de planilhas isoladas. |
| 1 | Sistemas computadorizados básicos de RH e planejamento existem, mas operam de forma isolada, sem integração com ERP/CRM. |
| 2 | Sistemas de RH e de planejamento de demanda trocam dados estruturados com os demais sistemas corporativos. |
| 3 | Painéis consolidados oferecem visibilidade quase em tempo real do quadro de pessoal, capacidade e previsão de demanda. |
| 4 | É transparente como decisões de dimensionamento de equipe e de planejamento de demanda impactam custo e nível de serviço. |
| 5 | Modelos preditivos antecipam necessidades de contratação, sazonalidade de demanda e riscos de capacidade. |
| 6 | O planejamento de recursos humanos e de demanda ajusta-se automaticamente com base em previsões, otimizando alocação de pessoal e recursos. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentação de sistemas de RH e de planejamento de demanda (HRIS, S&OP).

- Relatórios de dimensionamento de equipe e de previsão de demanda.

- Registros de integração entre sistemas de RH/planejamento e ERP corporativo.

##### Métricas/KPIs

- Percentual de processos de RH e planejamento de demanda integrados digitalmente.

- Precisão das previsões de demanda e de necessidade de pessoal.

- Tempo médio de resposta a variações de demanda por ajuste de quadro/recursos.

##### Sinais por nível

- Nível 0:


  - Planejamento manual de demanda e RH

- Nível 1:


  - Sistemas de RH/planejamento isolados

- Nível 2:


  - Integração de dados entre RH, planejamento e ERP

- Nível 3:


  - Painéis consolidados de quadro de pessoal e demanda

- Nível 4:


  - Transparência de custo e impacto de decisões de dimensionamento

- Nível 5:


  - Modelos preditivos de contratação e sazonalidade

- Nível 6:


  - Ajuste automático de alocação de pessoal e recursos

##### Amostragem

- Entrevistas com RH, planejamento e controladoria; revisão de sistemas HRIS e de S&OP; análise de relatórios de previsão de demanda e dimensionamento de equipe.

#### Glossário
[Sem glossário]
#### I.5.2 Capacidade: Automação da gestão de recursos e planejamento corporativo
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Automação

- Dimensão: Automação Corporativa

#### Resumo Descritivo
A automação da gestão de recursos e do planejamento corporativo diz respeito ao uso de tecnologia para apoiar a alocação, o controle e a otimização dos recursos administrativos da organização — orçamento, ativos, capacidade e políticas de negócio — em complemento à automação dos processos operacionais de vendas, marketing e compras. Nos modelos ACATECH e SIRI, essa capacidade avalia o grau em que decisões de planejamento e governança administrativa deixam de depender de análises manuais e pontuais para se apoiarem em dados integrados, indicadores consolidados e, nos estágios mais avançados, em modelos preditivos que antecipam riscos e oportunidades de gestão. A evolução da maturidade caminha de controles orçamentários manuais para sistemas de planejamento integrado capazes de ajustar automaticamente políticas, prioridades e alocação de recursos administrativos.
#### Questões
##### I.5.2.1 Questão: Como a organização utiliza sistemas informatizados para planejar e...
Como a organização utiliza sistemas informatizados para planejar e controlar orçamento, ativos e recursos administrativos?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O controle orçamentário e de ativos é manual ou baseado em planilhas isoladas, sem sistema corporativo dedicado. |
| 1 | Sistemas computadorizados básicos (ERP financeiro) registram orçamento e ativos, mas com forte dependência de planilhas paralelas para consolidação. |
| 2 | O sistema financeiro/orçamentário está conectado a outros sistemas corporativos, permitindo troca de dados e redução de retrabalho na consolidação. |
| 3 | Painéis consolidados dão visibilidade em tempo quase real da execução orçamentária e da utilização de ativos e recursos administrativos. |
| 4 | É transparente como decisões de alocação orçamentária impactam custos, prazos e desempenho de áreas administrativas. |
| 5 | Modelos analíticos preveem desvios orçamentários e necessidades futuras de recursos, apoiando decisões de investimento administrativo. |
| 6 | O planejamento orçamentário e de recursos ajusta-se automaticamente com base em previsões e regras de negócio, tornando a gestão administrativa mais ágil. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de execução orçamentária e de controle de ativos administrativos.

- Documentação do sistema financeiro/ERP e de suas integrações.

- Dashboards de acompanhamento orçamentário.

##### Métricas/KPIs

- Percentual de execução orçamentária monitorado digitalmente em tempo quase real.

- Taxa de desvio orçamentário identificada preditivamente antes do fechamento do período.

- Tempo médio de consolidação de relatórios financeiros/administrativos.

##### Sinais por nível

- Nível 0:


  - Controle orçamentário manual

  - ausência de sistema dedicado

- Nível 1:


  - ERP financeiro básico com planilhas paralelas

- Nível 2:


  - Integração do sistema financeiro com outros sistemas corporativos

- Nível 3:


  - Painéis de execução orçamentária em tempo quase real

- Nível 4:


  - Transparência do impacto de decisões orçamentárias

- Nível 5:


  - Previsão analítica de desvios orçamentários

- Nível 6:


  - Ajuste automático do planejamento orçamentário

##### Amostragem

- Entrevistas com controladoria, finanças e gestão de ativos; revisão de relatórios de execução orçamentária; observação de rotinas de consolidação financeira; análise de dashboards de acompanhamento.

##### I.5.2.2 Questão: Em que grau as políticas e regras de negócio administrativas (alçadas...
Em que grau as políticas e regras de negócio administrativas (alçadas de aprovação, prioridades de atendimento, critérios de alocação de recursos) estão parametrizadas em sistema, em vez de dependerem de decisão manual caso a caso?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Políticas e regras de negócio não são formalizadas em sistema; decisões são tomadas caso a caso, de forma manual. |
| 1 | Regras básicas de alçada e aprovação existem, mas aplicadas de forma manual ou parcialmente digital. |
| 2 | Regras de negócio administrativas são parametrizadas em sistemas locais, com aplicação digital estruturada. |
| 3 | As regras parametrizadas cobrem os principais processos administrativos, com painéis que dão visibilidade ao cumprimento das políticas. |
| 4 | É transparente como as regras de negócio impactam prazos, custos e conformidade administrativa, permitindo revisão orientada por dados. |
| 5 | Modelos analíticos identificam oportunidades de revisão de regras e políticas com base no desempenho histórico dos processos administrativos. |
| 6 | As regras de negócio se ajustam automaticamente com base em previsões e eventos, otimizando alçadas, prioridades e alocação de recursos administrativos. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentação de políticas administrativas e matrizes de alçada.

- Configurações de regras de negócio nos sistemas corporativos (ERP, workflow).

- Relatórios de conformidade e de exceções às políticas administrativas.

##### Métricas/KPIs

- Percentual de regras de negócio administrativas parametrizadas em sistema.

- Taxa de exceções às políticas administrativas identificadas automaticamente.

- Tempo médio de revisão e atualização de políticas administrativas.

##### Sinais por nível

- Nível 0:


  - Decisões administrativas caso a caso, sem parametrização

- Nível 1:


  - Regras de alçada aplicadas manualmente

- Nível 2:


  - Regras de negócio parametrizadas em sistemas locais

- Nível 3:


  - Cobertura ampla de regras parametrizadas com painéis de conformidade

- Nível 4:


  - Transparência do impacto das regras de negócio

- Nível 5:


  - Revisão de políticas orientada por análise de desempenho histórico

- Nível 6:


  - Ajuste automático de alçadas, prioridades e alocação de recursos

##### Amostragem

- Entrevistas com gestores administrativos e de governança corporativa; revisão de matrizes de alçada e de configurações de regras de negócio; análise de relatórios de conformidade e exceções.

##### I.5.2.3 Questão: Até que ponto a organização utiliza análise preditiva para antecipar...
Até que ponto a organização utiliza análise preditiva para antecipar riscos e oportunidades na gestão de recursos administrativos (orçamento, capacidade de equipe, ativos)?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há uso de análise preditiva; decisões de gestão de recursos baseiam-se em relatórios históricos manuais. |
| 1 | Existem iniciativas pontuais de análise de dados administrativos, realizadas manualmente. |
| 2 | Ferramentas digitais produzem relatórios descritivos sobre recursos administrativos, mas as análises são reativas. |
| 3 | Sistemas consolidados realizam análises automáticas e relatórios integrados sobre a gestão de recursos em tempo quase real. |
| 4 | Modelos analíticos correlacionam variáveis administrativas (orçamento, capacidade, ativos) e fornecem diagnósticos de desempenho. |
| 5 | Modelos preditivos antecipam riscos administrativos (estouro orçamentário, subdimensionamento de equipe, obsolescência de ativos). |
| 6 | A gestão de recursos administrativos ajusta-se de forma autônoma com base em previsões contínuas, otimizando custo, capacidade e disponibilidade de recursos. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios e dashboards analíticos de gestão de recursos administrativos.

- Documentação de modelos preditivos aplicados a orçamento, capacidade ou ativos.

- Registros de decisões administrativas apoiadas por análises preditivas.

##### Métricas/KPIs

- Percentual de decisões de gestão de recursos apoiadas por análise preditiva.

- Redução de estouros orçamentários ou de capacidade detectados tardiamente.

- Precisão dos modelos preditivos aplicados à gestão administrativa.

##### Sinais por nível

- Nível 0:


  - Decisões baseadas em relatórios históricos manuais

- Nível 1:


  - Análises pontuais e manuais de dados administrativos

- Nível 2:


  - Relatórios digitais descritivos e reativos

- Nível 3:


  - Análises automáticas integradas em tempo quase real

- Nível 4:


  - Diagnósticos correlacionais de desempenho administrativo

- Nível 5:


  - Modelos preditivos de riscos administrativos

- Nível 6:


  - Otimização autônoma e contínua de recursos administrativos

##### Amostragem

- Entrevistas com controladoria, RH e gestão de ativos; verificação de modelos preditivos em uso; avaliação de relatórios de gestão de recursos e de seu histórico de acurácia.

#### Glossário
[Sem glossário]
### I.6 Dimensão: Automação de Instalações

#### I.6.1 Capacidade: Automação predial e integração de sistemas de instalações (BMS/HVAC)
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Automação

- Dimensão: Automação de Instalações

#### Resumo Descritivo
A automação predial refere-se à aplicação de tecnologia para monitorar, controlar e executar processos dentro do edifício físico e das instalações onde a área de produção está localizada, incluindo sistemas de HVAC (aquecimento, ventilação e ar condicionado), refrigeração, segurança predial e iluminação. Nos modelos ACATECH e SIRI, essa capacidade reflete o eixo Automação dentro do bloco Tecnologia, avaliando o grau em que subsistemas prediais deixam de operar de forma manual e isolada e passam a ser controlados por sistemas supervisórios centralizados (BMS — Building Management System), com visibilidade unificada sobre o status de equipamentos, consumo de recursos e alarmes de infraestrutura. À medida que a maturidade evolui, a coordenação entre subsistemas prediais deixa de depender de dispositivos locais isolados e passa a ser orquestrada de forma integrada e, nos estágios mais avançados, adaptativa.
#### Questões
##### I.6.1.1 Questão: Em que medida os sistemas de HVAC, refrigeração, segurança e...
Em que medida os sistemas de HVAC, refrigeração, segurança e iluminação da instalação são controlados por dispositivos automatizados, em vez de operação manual?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Sistemas de instalações (energia, HVAC, ar comprimido, segurança, iluminação) são operados predominantemente de forma manual ou por dispositivos simples não integrados. |
| 1 | Sistemas de instalações utilizam controladores locais e dispositivos eletrônicos básicos, substituindo controles puramente manuais, mas com pouca coordenação entre subsistemas. |
| 2 | Controle de instalações passa a ser centralizado em sistemas BMS ou supervisórios simples, conectando diferentes subsistemas em um mesmo ambiente de operação. |
| 3 | Operadores têm visibilidade em tempo quase real do status de equipamentos, consumos de energia e alarmes de infraestrutura, com painéis que consolidam informações por área ou planta. |
| 4 | As relações entre condições de operação das instalações, consumo de recursos, conforto e impacto na produção tornam-se transparentes, permitindo ajustes de políticas e parâmetros. |
| 5 | Modelos preditivos são usados para antecipar falhas em equipamentos de utilidades e identificar oportunidades de economia de energia. |
| 6 | Sistemas de instalações ajustam automaticamente setpoints, modos de operação e prioridades com base em previsões de demanda, clima e produção, otimizando custo, conforto e disponibilidade. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Diagramas de arquitetura do BMS e dos subsistemas prediais (HVAC, energia, segurança, iluminação).

- Registros de logs e alarmes de sistemas supervisórios de instalações.

- Relatórios de consumo de energia e de utilização de utilidades.

- Documentação técnica de controladores e protocolos de integração predial (BACnet, Modbus etc.).

##### Métricas/KPIs

- Percentual de subsistemas prediais integrados ao BMS.

- Tempo médio de resposta a alarmes de infraestrutura.

- Percentual de consumo de energia monitorado digitalmente em tempo quase real.

##### Sinais por nível

- Nível 0:


  - Operação manual de sistemas prediais

  - dispositivos simples não integrados

- Nível 1:


  - Controladores locais básicos

  - pouca coordenação entre subsistemas

- Nível 2:


  - Controle centralizado via BMS/supervisório

- Nível 3:


  - Painéis com visibilidade de status e alarmes em tempo quase real

- Nível 4:


  - Transparência entre operação predial, consumo e impacto na produção

- Nível 5:


  - Modelos preditivos de falhas e de economia de energia

- Nível 6:


  - Ajuste automático de setpoints e prioridades de operação

##### Amostragem

- Entrevistas com equipes de facilities, manutenção predial e engenharia; observação da sala de controle/BMS; revisão de relatórios de consumo e de alarmes; análise de documentação técnica dos subsistemas prediais.

##### I.6.1.2 Questão: Até que ponto o controle de acesso, os sistemas de segurança predial...
Até que ponto o controle de acesso, os sistemas de segurança predial e a iluminação estão integrados ao sistema de automação da instalação, permitindo operação coordenada?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Controle de acesso, segurança e iluminação operam de forma isolada, sem qualquer integração ou automação. |
| 1 | Existem dispositivos eletrônicos básicos de controle de acesso e iluminação, mas operados de forma independente entre si. |
| 2 | Os sistemas de segurança e iluminação são conectados a um supervisório comum, permitindo troca básica de eventos entre subsistemas. |
| 3 | Painéis consolidados dão visibilidade em tempo quase real de eventos de segurança, ocupação e status de iluminação por área. |
| 4 | É transparente como padrões de ocupação e eventos de segurança impactam consumo de energia e conforto, permitindo ajustes de política. |
| 5 | Modelos analíticos correlacionam dados de ocupação, segurança e consumo para prever necessidades de iluminação e reforço de segurança. |
| 6 | Segurança, controle de acesso e iluminação operam de forma coordenada e autônoma, ajustando-se automaticamente a padrões de ocupação e eventos previstos. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentação de sistemas de controle de acesso e CFTV integrados ao BMS.

- Registros de eventos de segurança e de ocupação por área.

- Relatórios de consumo de iluminação correlacionados a padrões de ocupação.

##### Métricas/KPIs

- Percentual de sistemas de segurança e iluminação integrados ao supervisório predial.

- Tempo médio de resposta a eventos de segurança predial.

- Redução de consumo de iluminação por automação baseada em ocupação.

##### Sinais por nível

- Nível 0:


  - Sistemas isolados sem integração

- Nível 1:


  - Dispositivos básicos operando independentemente

- Nível 2:


  - Conexão a supervisório comum com troca básica de eventos

- Nível 3:


  - Painéis de visibilidade de segurança, ocupação e iluminação

- Nível 4:


  - Transparência do impacto de ocupação/segurança no consumo

- Nível 5:


  - Modelos preditivos de ocupação e necessidade de segurança/iluminação

- Nível 6:


  - Operação coordenada e autônoma de segurança, acesso e iluminação

##### Amostragem

- Entrevistas com equipes de segurança patrimonial e facilities; observação de painéis de controle de acesso e iluminação; análise de relatórios de eventos e de consumo por área.

#### Glossário
[Sem glossário]
#### I.6.2 Capacidade: Eficiência energética e manutenção preditiva de instalações
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Automação

- Dimensão: Automação de Instalações

#### Resumo Descritivo
Esta capacidade avalia o uso de dados e análises preditivas para otimizar o consumo de energia e antecipar falhas em equipamentos de utilidades (HVAC, refrigeração, ar comprimido, energia) das instalações, complementando a automação e integração de subsistemas prediais tratada na primeira capacidade desta dimensão. Nos modelos ACATECH e SIRI, essa capacidade corresponde aos estágios mais avançados de maturidade do eixo Automação — capacidade preditiva e adaptabilidade — nos quais modelos analíticos deixam de apenas registrar o consumo e o estado dos equipamentos para prever estados futuros, antecipar falhas e apoiar decisões de investimento em infraestrutura. Em seu estágio mais avançado, a instalação ajusta automaticamente parâmetros operacionais com base em previsões de demanda, clima e produção, otimizando simultaneamente custo, conforto e disponibilidade.
#### Questões
##### I.6.2.1 Questão: Em que medida a organização utiliza análise de dados para monitorar e...
Em que medida a organização utiliza análise de dados para monitorar e otimizar o consumo de energia e utilidades (HVAC, ar comprimido, refrigeração) das instalações?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há monitoramento estruturado de consumo de energia e utilidades; o acompanhamento é manual e esporádico. |
| 1 | Existem registros básicos de consumo, coletados manualmente ou por medidores isolados, sem análise sistemática. |
| 2 | Medidores digitais registram consumo de energia e utilidades, com relatórios periódicos básicos. |
| 3 | Painéis consolidados apresentam consumo de energia e utilidades por área/planta em tempo quase real, permitindo identificar desvios. |
| 4 | É transparente como o consumo de energia e utilidades se relaciona a níveis de produção, ocupação e condições climáticas, orientando políticas de eficiência. |
| 5 | Modelos preditivos identificam oportunidades de economia de energia e antecipam picos de consumo antes que ocorram. |
| 6 | O consumo de energia e utilidades é otimizado de forma autônoma e contínua, com ajustes automáticos baseados em previsões de demanda, produção e clima. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de consumo de energia, água, ar comprimido e outras utilidades.

- Dashboards de eficiência energética por área ou planta.

- Documentação de metas e políticas de eficiência energética.

- Registros de medidores inteligentes e sistemas de submedição.

##### Métricas/KPIs

- Consumo de energia por unidade produzida (intensidade energética).

- Percentual de utilidades monitoradas digitalmente em tempo quase real.

- Economia de energia obtida por iniciativas orientadas por dados.

##### Sinais por nível

- Nível 0:


  - Ausência de monitoramento estruturado de consumo

- Nível 1:


  - Registros manuais ou por medidores isolados

- Nível 2:


  - Medição digital com relatórios periódicos

- Nível 3:


  - Painéis de consumo em tempo quase real com detecção de desvios

- Nível 4:


  - Transparência da relação entre consumo, produção e ocupação

- Nível 5:


  - Modelos preditivos de economia de energia e picos de consumo

- Nível 6:


  - Otimização autônoma e contínua do consumo de energia/utilidades

##### Amostragem

- Entrevistas com equipes de facilities, engenharia e sustentabilidade; revisão de relatórios de consumo e metas de eficiência; observação de dashboards de submedição; análise de séries históricas de consumo.

##### I.6.2.2 Questão: Até que ponto a organização utiliza manutenção preditiva, apoiada em...
Até que ponto a organização utiliza manutenção preditiva, apoiada em dados, para antecipar falhas em equipamentos de utilidades e infraestrutura predial?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A manutenção de equipamentos de utilidades é corretiva, realizada apenas após a ocorrência de falhas. |
| 1 | Existem planos básicos de manutenção preventiva por calendário, sem uso de dados de condição do equipamento. |
| 2 | Sensores digitais registram parâmetros de operação de equipamentos críticos (temperatura, vibração, pressão), com inspeção periódica dos dados. |
| 3 | Dados de condição dos equipamentos são consolidados em painéis, permitindo priorizar intervenções com base em indicadores de desgaste. |
| 4 | É transparente como o estado de conservação dos equipamentos de utilidades impacta a disponibilidade das instalações e os custos de manutenção. |
| 5 | Modelos preditivos antecipam falhas em equipamentos de utilidades com base em padrões históricos e dados de condição, orientando a manutenção antes da quebra. |
| 6 | A manutenção de instalações é autônoma e adaptativa: o sistema aciona automaticamente ordens de manutenção e ajusta prioridades com base em previsões contínuas de falha. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Planos de manutenção preventiva e preditiva de equipamentos de utilidades.

- Registros de sensores de condição (vibração, temperatura, pressão) de equipamentos críticos.

- Ordens de manutenção geradas por sistemas de gestão de manutenção (CMMS).

- Relatórios de disponibilidade e de falhas de equipamentos de instalações.

##### Métricas/KPIs

- Percentual de equipamentos de utilidades cobertos por manutenção preditiva.

- Redução de falhas não planejadas em equipamentos de instalações.

- Tempo médio entre detecção de anomalia e intervenção de manutenção.

##### Sinais por nível

- Nível 0:


  - Manutenção corretiva reativa

- Nível 1:


  - Manutenção preventiva por calendário sem dados de condição

- Nível 2:


  - Sensoriamento de parâmetros de operação com inspeção periódica

- Nível 3:


  - Painéis de condição orientando priorização de intervenções

- Nível 4:


  - Transparência do impacto da condição dos equipamentos em disponibilidade e custo

- Nível 5:


  - Modelos preditivos de falha em equipamentos de utilidades

- Nível 6:


  - Manutenção autônoma com ordens acionadas automaticamente

##### Amostragem

- Entrevistas com equipes de manutenção predial e confiabilidade; revisão de planos de manutenção e do CMMS; análise de registros de sensores de condição; avaliação de indicadores de disponibilidade das instalações.

#### Glossário
[Sem glossário]
### I.7 Dimensão: Conectividade de Chão de Fábrica

#### I.7.1 Capacidade: Aquisição de dados por sensores e atuadores
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Conectividade

- Dimensão: Conectividade de Chão de Fábrica

#### Resumo Descritivo
Esta dimensão avalia a interconexão de equipamentos, máquinas e sistemas de produção de modo a
permitir a comunicação e a troca de dados entre ativos. O objetivo principal é a digitalização do chão
de fábrica, usando protocolos padronizados e redes IoT para alcançar interoperabilidade, segurança e
comunicação em tempo real e, assim, otimizar as atividades de manufatura.
#### Questões
##### I.7.1.1 Questão: Os equipamentos e máquinas do chão de fábrica foram aprimorados com...
Os equipamentos e máquinas do chão de fábrica foram aprimorados com sistemas embarcados,
sensores e atuadores para criar Sistemas Ciberfísicos (CPS) e estabelecem uma interface entre o
mundo físico e digital?


<!-- pág. original: 310/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Processos não são definidos e são executados com métodos informais ou ad-hoc. |
| 1 | Equipamentos, máquinas e sistemas baseados em computador podem interagir e trocar informações de forma básica. |
| 2 | Componentes mecatrônicos foram aprimorados para criar Sistemas Ciberfísicos (CPS). |
| 3 | Sensores inteligentes são usados para capturar dados de máquinas e equipamentos. |
| 4 | Os dados reais do chão de fábrica são capturados por diferentes redes de sensores e utilizados para tomar decisões. |
| 5 | Os dados são integrados em sistemas inteligentes para a criação de uma Sombra Digital (Digital Shadow) dos processos. |
| 6 | Os sistemas de informação são dotados de mecanismos de auto-aprendizado baseados em dados do CPS e operam de forma autônoma. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Inventário de Sistemas Ciberfísicos (CPS) no chão de fábrica.

- Especificações técnicas de sensores inteligentes.

- Diagramas de arquitetura de rede IoT no chão de fábrica.

- Listas de Ativos com sistemas embarcados atualizados.

- Documentação de retrofit de ativos legados com sensores.

- Planos de investimento em tecnologias de sensores/robótica.

##### Métricas/KPIs

- Porcentagem de máquinas equipadas com sensores inteligentes.

- Número de Sistemas Ciberfísicos (CPS) implementados.


<!-- pág. original: 311/465 -->
- Frequência de coleta de dados brutos dos ativos.

- Conformidade da infraestrutura com padrões industriais (e.g., RAMI 4.0).

- Taxa de dados válidos versus corrompidos

##### Sinais por nível

- Nível 0:


  - Ativos e sistemas da fábrica não estão conectados.

  - A produção é executada por humanos sem automação.


- Nível 1:


  - Existem links formais de rede que permitem a comunicação entre ativos.

  - Ativos operam com a assistência de sistemas baseados em computador.


- Nível 2:


  - Os ativos são interoperáveis.

  - Sistemas embarcados com sensores, atuadores e unidades de processamento são incorporados nos processos de interação e troca de dados.


- Nível 3:


  - Foi estabelecida uma infraestrutura de rede segura (por exemplo, baseada em Ethernet Industrial) para conectar os sistemas de controle e sensores.
  - Dados são coletados e processados rapidamente, de forma contínua.


- Nível 4:


  - Ativos são capazes de comunicação em tempo real, trocando informação no momento em que é gerada.
  - Essa informação está amplamente disponível para processos de otimização.


<!-- pág. original: 312/465 -->
- Nível 5:


  - Existem processos para definição dos requisitos de dados relevantes e a seleção dos sensores recomendados.
  - As redes existentes são escaláveis para acomodar modificações na composição dos equipamentos (e.g., adição de novos sensores).
  - Os sistemas executam tarefas preditivas para diagnóstico e prevenção de falhas.


- Nível 6:


  - Os sistemas utilizam os dados dos CPS para implementar automaticamente as ações correspondentes sem necessidade de intervenção humana.

##### Amostragem

- Selecionar 5–10 artefatos referentes a processos relevantes (registros de calibração de
         sensores), atualizados nos últimos 90 dias

##### I.7.1.2 Questão: O pré-processamento dos dados brutos dos sensores diretamente nos...
O pré-processamento dos dados brutos dos sensores diretamente nos sistemas embarcados e ativos
do chão de fábrica é eficiente e descentralizado?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há pré-processamento de dados digitais ou o fluxo de dados é inexistente. |
| 1 | O processamento de dados é centralizado e os ativos de produção funcionam com lógica pré-programada. |
| 2 | Os dados dos sensores são coletados, mas o pré-processamento é limitado e ainda dependente de processos centralizados. |
| 3 | O pré-processamento dos dados dos sensores é descentralizado, no ponto de geração de dados, com baixa latência. |
| 4 | O pré-processamento descentralizado é otimizado (com uso de balanceamento de carga e confiabilidade). |
| 5 | Os sistemas de informação utilizam análise de dados avançada e desempenho para prever falhas e vulnerabilidades que possam gerar interrupções no processamento de dados. |
| 6 | O processamento e a análise de dados envolvem mecanismos de auto-aprendizado e operam de forma autônoma. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentação de pré-processamento de dados descentralizado.

- Especificações de Edge Server para coleta e análise local.

- Diagramas de arquitetura de Edge/Cloud Computing.

- Logs de latência e tempo de propagação do sinal.

- Relatórios de validação de cálculos críticos on-site.

- Documentação sobre protocolos de comunicação utilizados (e.g., OPC-UA).

##### Métricas/KPIs

- Porcentagem de dados pré-processados de forma descentralizada.

- Latência média da comunicação em chão de fábrica.

- Tempo de Recuperação de Falhas na infraestrutura de edge.

- Taxa de agregação dos dados brutos.

##### Sinais por nível

- Nível 0:


  - Não existem processos definidos referentes ao pré-processamento dos dados.


- Nível 1:


<!-- pág. original: 314/465 -->
  - Processos envolvendo pré-processamento dos dados são ad-hoc e restritos.

  - O foco está nas funcionalidades básicas do sistema.


- Nível 2:


  - Embora exista uma infraestrutura de conectividade disponível para a coleta de dados, o processamento ocorre em unidades centralizadas.
  - É comum a identificação de pontos únicos de falha (do inglês, single point of failures ou SPOFs).


- Nível 3:


  - O processamento é realizado diretamente nos sistemas embarcados ligados aos recursos técnicos de chão de fábrica.
  - SPOFs são eliminados.


- Nível 4:


  - As soluções de processamento distribuído são implementadas para reduzir atrasos na propagação do sinal e entrega de pacotes de rede.
  - Os sistemas embarcados conseguem efetuar cálculos críticos em termos de tempo, otimizando a comunicação.


- Nível 5:


  - Os sistemas de informação implementam mecanismos de detecção e predição de falhas no processamento descentralizado de dados, provendo informações para tomada de decisão.


- Nível 6:


  - Os sistemas de informação executam decisões automaticamente para otimizar o desempenho do processamento sem intervenção humana.


<!-- pág. original: 315/465 -->
##### Amostragem

- Selecionar 5–10 artefatos referentes a processos relevantes (logs de falha e registros de
          latência), atualizados nos últimos 90 dias

##### I.7.1.3 Questão: A aquisição de dados é facilitada pela conectividade dos sistemas de...
A aquisição de dados é facilitada pela conectividade dos sistemas de controle e sensores, incluindo
interfaces abertas e soluções para ativos legados?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os ativos e sistemas são gerenciados de forma independente, sem comunicação formal. |
| 1 | Existem sistemas isolados ou proprietários em chão de fábrica, com capacidades limitadas de integração de dados. |
| 2 | Os ativos são interoperáveis com múltiplas tecnologias e protocolos de comunicação. |
| 3 | Ativos legados (e.g., máquinas antigas) são conectados através de novas tecnologias de sensores para fornecer dados de produção. |
| 4 | Os sistemas de controle e sensoriamento são integrados, e a infraestrutura utiliza interfaces abertas e comunicação em tempo real. |
| 5 | Os sistemas de controle e sensoriamento utilizam os dados integrados em modelos preditivos para otimização das interfaces. |
| 6 | A infraestrutura é capaz de reorganização dinâmica e adaptação automática à integração de novos ativos, e utiliza modelos preditivos para otimizar rotas de dados e cargas de comunicação. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Plano de integração vertical e horizontal.

- Inventário de ativos legados adaptados com sensores.


<!-- pág. original: 316/465 -->
- Documentação de uso de protocolos padrões (e.g., IP).

- Registros de localização e rastreamento de materiais.

- Padrões de comunicação entre máquinas.

- Documentação de interfaces abertas.

##### Métricas/KPIs

- Porcentagem de ativos legados fornecendo dados digitais.

- Taxa de uso de interfaces abertas para comunicação.

- Percentual de protocolos de comunicação interoperáveis utilizados.

- Porcentagem de produtos com identificação rastreável.

- Porcentagem de dados legados integrados sem perdas.

- Número de interfaces interoperáveis ativas.

##### Sinais por nível

- Nível 0:


  - Não existem processos definidos para integração e interoperabilidade entre os ativos.

  - Não há intenção estratégica para integrar máquinas existentes.


- Nível 1:


  - Embora existam links formais de rede para ativos de produção, poucos ativos implementam funcionalidades de integração de dados.
  - A maioria dos equipamentos não é interoperável.


- Nível 2:


  - Os ativos podem trocar informações sem restrições significativas.

  - Protocolos padronizados (como o Internet Protocol IP, por exemplo) são utilizados no chão de fábrica.


- Nível 3:


<!-- pág. original: 317/465 -->
  - Existem iniciativas implementadas de integração com equipamentos e sistemas legados.
  - A conectividade suporta a Integração Vertical (troca de dados em toda a cadeia de valor).


- Nível 4:


  - Existem interfaces abertas e funcionais para troca de dados.

  - A integração de dados entre ativos ocorre em tempo real.

  - O controle de fluxo de dados está implementado para garantir a integridade da informação trocada.


- Nível 5:


  - Existem análises preditivas implementadas, que permitem avaliar cenários de integração de dados e determinar otimizações.
  - As redes existentes são escaláveis, sendo facilmente configuradas para acomodar modificações na composição de equipamentos e sistemas.


- Nível 6:


  - As interfaces são abertas e altamente flexíveis, se adaptando a novos requisitos do sistema de forma contínua.

##### Amostragem

- Selecionar 5–10 artefatos referentes a processos relevantes (registros de integração de ativos
        legados e logs de comunicação via protocolo padrão), atualizados nos últimos 90 dias

##### I.7.1.4 Questão: Os dados coletados por sensores e atuadores são utilizados de forma...
Os dados coletados por sensores e atuadores são utilizados de forma contínua para manter uma
Sombra Digital (Digital Shadow) precisa do chão de fábrica e apoiar a tomada de decisão em tempo
real?


<!-- pág. original: 318/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há dados digitais capturados ou utilizados. |
| 1 | Dados básicos de produção são usados para relatórios elementares, sem integração da cadeia de valor. |
| 2 | Os dados dos sensores são processados e convertidos em informação útil para tomada de decisão. |
| 3 | Existe uma Sombra Digital criada a partir dos dados de sensores e demais ativos de chão de fábrica. O modelo digital é atualizado dinamicamente. |
| 4 | O sistema utiliza os dados da Sombra Digital para executar análises de dados, entender os efeitos e otimizar processos. |
| 5 | Os dados da Sombra Digital são usados para simular possíveis cenários futuros e permitir o suporte à decisão. |
| 6 | O sistema utiliza os dados da Sombra Digital para tomar decisões de forma autônoma. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Modelo de Sombra Digital (Digital Shadow) de chão de fábrica.

- Relatórios de diagnóstico de causas potenciais de desvios.

- Algoritmos de análise preditiva de falhas.

- Dashboards de monitoramento de processos em tempo real.

- Documentação de integração de dados com ERP/MES.

- Registros de localização e rastreamento de materiais.

##### Métricas/KPIs

- Acurácia (%) da previsão de falhas de máquina.

- Tempo para diagnóstico de desvios críticos.


<!-- pág. original: 319/465 -->
- Porcentagem de decisões operacionais baseadas em dados reais.

- Produtividade do chão de fábrica (OEE).

- Tempo de atualização da sombra digital.

- Grau de acurácia (%) entre modelo e estádo físico.

##### Sinais por nível

- Nível 0:


  - Não há processos definidos para utilização de dados de chão de fábrica com objetivos estratégicos.
  - A tomada de decisão é baseada em métodos informais ou ad-hoc.

  - A transformação digital não é foco estratégico.


- Nível 1:


  - Relatórios existentes baseiam-se em dados dos ativos digitais obtidos por funcionalidades pré-programadas.
  - Não há análises baseadas em cruzamento de dados de diferentes ativos.


- Nível 2:


  - Relatórios apresentam informações obtidas a partir de dados de múltiplas fontes.

  - Existem requisitos de negócio determinando quais dados devem ser coletados e analisados.
  - Sistemas de informação podem ser usados para identificar desvios dos parâmetros predefinidos.


- Nível 3:


  - A indústria empreende iniciativas para coletar dados e implementar um modelo digital atualizado dos ativos de chão de fábrica.
  - As decisões gerenciais são baseadas em dados reais.


<!-- pág. original: 320/465 -->
- Nível 4:


  - A informação obtida a partir de sensores e ativos de chão de fábrica é usada para detectar ineficiências e sugerir áreas de melhoria, como por exemplo na redução de resíduos.


- Nível 5:


  - Os sistemas empregam cada vez mais mecanismos de detecção e predição.

  - São capazes de prever desvios e executar decisões de forma independente para otimizar o desempenho.


- Nível 6:


  - Decisões referentes à correção de desvios e otimização da produção são implementadas de forma autônoma pelo sistema.
  - O sistema é dotado de mecanismos de auto-aprendizado e auto-otimização.

##### Amostragem

- Selecionar 5–10 artefatos referentes a processos relevantes (sincronização entre Digital Shadow e processos físicos), atualizados nos últimos 90 dias
#### Glossário
[Sem glossário]
### I.8 Dimensão: Conectividade Corporativa

#### I.8.1 Capacidade: Interface de dados padronizada
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Conectividade

- Dimensão: Conectividade Corporativa

#### Resumo Descritivo
Esta dimensão avalia a interconexão dos sistemas de TI onde o trabalho administrativo é realizado. O
principal objetivo é permitir a comunicação e a troca contínua de dados entre sistemas, visando a


<!-- pág. original: 322/465 -->
interoperabilidade, segurança, velocidade e agilidade da rede para que os sistemas interajam sem
restrições significativas.
#### Questões
##### I.8.1.1 Questão: Os principais sistemas de TI da Empresa (como ERP, PLM e MES) estão...
Os principais sistemas de TI da Empresa (como ERP, PLM e MES) estão formalmente conectados e
são interoperáveis em múltiplos protocolos e tecnologias de comunicação?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os sistemas de TI administrativos não estão conectados. |
| 1 | Existem links formais de rede que permitem que os sistemas interajam e troquem informações. |
| 2 | Os sistemas de TI da empresa são interoperáveis em múltiplos protocolos e tecnologias de comunicação. |
| 3 | A Integração Vertical (ligação produção-gestão) e Horizontal (ligação processos/stakeholders) é formalizada. |
| 4 | Os sistemas de TI interoperáveis são capazes de comunicação em tempo real. |
| 5 | A arquitetura de sistemas suporta uma plataforma central que conecta e fornece informações. |
| 6 | A infraestrutura digital e as interfaces suportam mecanismos de auto-aprendizado. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Diagramas de arquitetura de sistemas corporativos (ERP, MES, PLM).

- Mapa integrado de software.

- Documentação de protocolos de comunicação bidirecional.

- Plano de integração horizontal com parceiros/clientes.

- Registro de rastreabilidade de materiais/produtos.


<!-- pág. original: 323/465 -->
- Relatório de avaliação da Qualidade dos Dados.

##### Métricas/KPIs

- Porcentagem de sistemas de TI empresariais interconectados.

- Taxa de uso de metadados estruturados no sistema.

- Porcentagem de processos com Integração Horizontal na cadeia de valor.

- Porcentagem de decisões operacionais baseadas em dados em tempo real.

- Percentual de integrações realizadas por APIs padronizadas.

##### Sinais por nível

- Nível 0:


  - Sistemas baseados em computador não conseguem interagir ou trocar informações.

  - Os processos são executados em silos, baseados em métodos informais.


- Nível 1:


  - Os sistemas operam com o suporte de ferramentas analógicas.


- Nível 2:


  - A troca parcial de informações ocorre sem restrições significativas.


- Nível 3:


  - Sistemas críticos como ERP, PLM e MES estão integrados.


- Nível 4:


  - A informação é trocada no momento em que é gerada, sem atraso.


- Nível 5:


<!-- pág. original: 324/465 -->
  - Os sistemas de TI podem simular possíveis cenários futuros para suporte à decisão.

  - A arquitetura digital corporativa integra dados operacionais e administrativos de uma camada única de informação, permitindo análise preditiva.


- Nível 6:


  - As informações são utilizadas para implementar automaticamente as medidas correspondentes sem necessidade de intervenção humana, através do uso de IA ou orquestradores para decisão automática.

##### Amostragem

- Selecionar 3-5 artefatos relevantes para evidência dos sinais (logs de integração e relatórios de
          interoperabilidade ERP-MES), atualizados nos últimos 90 dias

##### I.8.1.2 Questão: A empresa utiliza interfaces de dados padronizadas e formatos de...
A empresa utiliza interfaces de dados padronizadas e formatos de troca de dados universais para
interconectar seus sistemas de TI?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A infraestrutura de rede não é definida. |
| 1 | Existe uma infraestrutura de rede, mas as interfaces disponíveis são proprietárias, com baixo grau de customização e interoperabilidade. |
| 2 | Há um esforço para padronizar ou usar tecnologias e protocolos de comunicação complementares. |
| 3 | As interfaces de dados são padronizadas e os formatos de troca de dados são implementados para conectar os sistemas de TI. |
| 4 | A arquitetura de TI é planejada para evitar que diferentes departamentos utilizem sistemas de TI que não sejam interoperáveis. |
| 5 | As interfaces existentes podem ser configuradas de forma rápida e fácil para acomodar quaisquer modificações na composição dos sistemas. |
| 6 | O sistema executa reorganização dinâmica e se adapta automaticamente à integração de novos ativos e sistemas. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Plano de Capacidade de TI (DTC).

- Documentação de uso de interfaces abertas (e.g., APIs).

- Inventário de sistemas de TI não supervisionados (shadow IT).

- Diretrizes de uso de protocolos padronizados na rede corporativa.

- Plano de implementação de Cloud Computing.

- Relatórios de auditoria de aderência a formatos de troca de dados.

##### Métricas/KPIs

- Tempo médio de reconfiguração de interfaces.

- Número de sistemas de TI paralelos (shadow IT) detectados.

- Disponibilidade (%) da infraestrutura digital da empresa.

- Porcentagem de sistemas operando em tempo real.

- Percentual de interfaces documentadas e auditadas.

- Tempo médio de integração de um novo sistema (indicador de agilidade).

##### Sinais por nível

- Nível 0:


  - Não existem processos definidos envolvendo padronização de interfaces.

  - Não há planos estratégicos para a transformação digital da indústria.


- Nível 1:


  - Há links formais de rede instalados.


<!-- pág. original: 326/465 -->
  - O uso generalizado de protocolos de rede padronizados (como o IP, por exemplo) no chão de fábrica é um requisito chave.


- Nível 2:


  - Existem evidências e artefatos documentando a padronização de interfaces e definição de templates de dados.
  - Os sistemas de informação começam a ser usados para identificar desvios.


- Nível 3:


  - Todos os sistemas implementados são especificados para atenderem padrões específicos de interface e troca de dados.
  - A aquisição de novos ativos inclui requisitos de interoperabilidade que garantem a manutenção desses padrões.


- Nível 4:


  - Existem padrões estabelecidos de interface e troca de dados documentados e auditáveis que estão vigentes para todos os departamentos que necessitam de integração com os ativos industriais.


- Nível 5:


  - A infraestrutura de rede e interfaces é escalável.

  - A Capacidade Técnica Digital (DTC) inclui planejamento de necessidades e capacidade da infraestrutura de TI em planos de médio a longo prazo.
  - Os sistemas utilizam dados padronizados para simular possíveis cenários futuros.


- Nível 6:


  - A infraestrutura é capaz de reorganização dinâmica e adaptação automática contínua à integração de novos ativos e sistemas.
  - O sistema executa decisões de auto-otimização (por exemplo, em desempenho).


<!-- pág. original: 327/465 -->
##### Amostragem

- Selecionar 3-5 artefatos relevantes (inventário de APIs e integrações com sistemas legados)
          para evidência dos sinais, atualizados nos últimos 90 dias

##### I.8.1.3 Questão: A infraestrutura de TI da empresa utiliza metadados estruturados e...
A infraestrutura de TI da empresa utiliza metadados estruturados e unificados e políticas de
governança de dados formalizadas?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há metadados estruturados ou unificados. Não existem políticas de governança de dados nem foco em segurança. |
| 1 | A empresa reconhece a necessidade de formalizar sua política de governança de dados, mas possui ainda poucas iniciativas. |
| 2 | A empresa tem iniciativas para coletar e aproveitar os fluxos de dados estruturados e não estruturados. |
| 3 | Políticas de governança de dados são sistematicamente desenvolvidas e mantidas. |
| 4 | A empresa utiliza metadados estruturados e unificados. |
| 5 | Dados de alta qualidade são armazenados centralmente e analisados automaticamente. |
| 6 | A governança de dados inclui mecanismos de auto-aprendizado que ajustam os formatos de dados de forma autônoma para otimizar os sistemas. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Políticas de Governança de Dados formalizadas.

- Framework de Segurança Cibernética.

- Inventário de metadados estruturados e unificados.

- Plano de proteção de dados de stakeholders.


<!-- pág. original: 328/465 -->
- Relatórios de auditoria de conformidade (e.g., ISO27001).

- Relatório de avaliação de riscos de segurança.

##### Métricas/KPIs

- Taxa de incidentes de segurança cibernética.

- Índice de Qualidade dos Dados (acurácia, coerência).

- Tempo de Recuperação de Desastres (TDR).

- Porcentagem de sistemas operando sob governança de dados.

- Taxa de atualização de metadados.

##### Sinais por nível

- Nível 0:


  - Os sistemas de TI administrativos não estão conectados.

  - A governança de dados é tratada de forma inexistente ou totalmente ad-hoc.


- Nível 1:


  - Existem links formais de rede para interconexão dos sistemas, entretanto não existem especificações estruturadas para a troca de dados.


- Nível 2:


  - Os sistemas são interoperáveis, podendo interagir e trocar informações sem restrições significativas.
  - Há esforços básicos para gerenciar o risco de ameaças cibernéticas.

  - Catálogo de dados estruturados e não estruturados em consolidação.


- Nível 3:


  - Um framework com políticas de segurança está em vigor para proteger a rede interoperável contra acesso indesejado e/ou disrupção.


<!-- pág. original: 329/465 -->
  - Políticas de governança de dados são sistematicamente desenvolvidas e mantidas para orientar o processamento, armazenamento e gerenciamento de dados.


- Nível 4:


  - Há iniciativas para melhorar a qualidade dos dados e oferecer suporte à comunicação em tempo real.
  - Os dados são analisados para produzir conhecimento por meio de análise de causa raiz.


- Nível 5:


  - A governança de dados é priorizada em todos os níveis e a empresa busca conformidade com padrões internacionais para proteção de dados.
  - Monitoramento contínuo de integridade e conformidade com base em normas (e.g., ISO 27001, LGPD)


- Nível 6:


  - O processamento e análise de dados incluem mecanismos de auto-aprendizado, adaptando-se continuamente às circunstâncias.
  - Os sistemas de TI são capazes de executar decisões de forma autônoma para otimizar o desempenho e adaptar-se a mudanças.

##### Amostragem

- Selecionar 3-5 artefatos relevantes para evidência dos sinais (relatórios de qualidade de dados,
        logs de auditoria de conformidade, políticas de metadados e fluxos ETL), atualizados nos
        últimos 90 dias
#### Glossário
[Sem glossário]
### I.9 Dimensão: Conectividade de Instalações (Facility)

#### I.9.1 Capacidade: Infraestrutura de TI resiliente
#### Bloco/Pilar
- Bloco: Tecnologia


<!-- pág. original: 331/465 -->
- Pilar: Conectividade

- Dimensão: Conectividade de Instalações (Facility)

#### Resumo Descritivo
Esta dimensão avalia a interconexão de equipamentos e sistemas dentro do ambiente industrial,
incluindo cibersegurança de instalações críticas e controle de condições ambientais (do inglês Heating,
Ventilation, and Air Conditioning, ou HVAC). Visa medir a interoperabilidade e segurança da rede para
permitir a troca contínua de dados e a automação eficiente da instalação, gerando redução de custos e
maior eficiência.
#### Questões
##### I.9.1.1 Questão: Quão eficiente é a infraestrutura de rede (cabeada e sem fio) que...
Quão eficiente é a infraestrutura de rede (cabeada e sem fio) que interliga os sistemas da instalação
de fábrica (inclusive HVAC) para garantir a conectividade?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A infraestrutura de rede digital é inexistente ou não está em uso. |
| 1 | A infraestrutura digital básica foi introduzida mas é limitada. |
| 2 | Os sistemas e ativos da instalação conectados são interoperáveis e conseguem interagir e trocar informações sem restrições significativas. |
| 3 | Os links de rede são capazes de trocar informações assim que geradas. |
| 4 | A infraestrutura suporta a coleta de dados abrangentes em tempo real para criar uma representação digital (sombra digital) do estado da instalação. |
| 5 | A infraestrutura de rede é escalável, permitindo que as redes existentes sejam configuradas de forma rápida e fácil para acomodar modificações na composição dos sistemas da instalação |
| 6 | A infraestrutura suporta a convergência completa das redes e plataformas de automação da instalação com o chão de fábrica e a gerência. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Diagrama de arquitetura de rede (TI/OT) da instalação.

- Relatórios de auditoria ou certificações como ISO 27001.

- Logs de latência e desempenho de rede em tempo real.

- Documentação de arquitetura de Edge/Cloud Computing.

- Dados de sensores (HVAC/chiller) em sistemas de controle.

- Registros de falhas e tempo de recuperação (MTTR).

##### Métricas/KPIs

- Disponibilidade (%) de sistemas críticos da instalação.

- Latência média de dados de sensores da instalação.

- Consumo de energia por unidade produzida.

- Número de incidentes relacionados a falhas na rede.

- Tempo médio de recuperação (MTTR - Mean Time to Repair) de falhas na rede.

##### Sinais por nível

- Nível 0:


  - Os ativos e sistemas da instalação (como HVAC e iluminação) não estão conectados e não são capazes de interagir ou trocar informação.
  - Os processos são gerenciados por métodos informais ou ad-hoc.


- Nível 1:


  - Existem links de rede formais (cabeados e/ou sem fio) que permitem a interação ou troca de informação entre os ativos da instalação.
  - Múltiplas tecnologias e protocolos de comunicação podem estar em uso sem a devida integração.


- Nível 2:


<!-- pág. original: 333/465 -->
  - O Internet Protocol (IP) está se tornando amplamente utilizado (e.g., IPv6), o que é um requisito chave para a Internet of Things (IoT).


- Nível 3:


  - A conectividade provê suporte à análise de dados locais para identificar e diagnosticar as causas potenciais de desvios.


- Nível 4:


  - A troca de dados disponíveis corporativamente em tempo real entre ativos e sistemas da instalação ocorre de forma permanente.
  - Os dados estão disponíveis imediatamente após sua leitura/aquisição.


- Nível 5:


  - A rede suporta a aplicação de análise preditiva e modelos avançados para prever futuros estados de ativos e sistemas (e, falhas no HVAC).


- Nível 6:


  - A rede permite interações dinâmicas e reconfiguráveis entre domínios, suportando a execução autônoma de decisões para otimizar o desempenho da instalação.

##### Amostragem

- Selecionar 3-5 artefatos relevantes para evidência dos sinais (incidentes de rede, logs de
        latência), atualizados nos últimos 90 dias

##### I.9.1.2 Questão: Qual é o grau de integração entre equipamentos da infraestrutura de...
Qual é o grau de integração entre equipamentos da infraestrutura de conectividade com elementos
críticos da instalação e controle do ambiente (e.g., HVAC, iluminação) de fábrica?


<!-- pág. original: 334/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os ativos e sistemas críticos da instalação não estão conectados à infraestrutura de rede, ou a automação é inexistente. |
| 1 | Os sistemas críticos da instalação são introduzidos ou parcialmente automatizados, mas gerenciados por intervenção humana. |
| 2 | A infraestrutura de rede interliga os ativos da instalação, permitindo que os sistemas críticos da instalação sejam interoperáveis. |
| 3 | A infraestrutura permite a comunicação em tempo real para controle dos ativos. |
| 4 | A integração suporta a coleta de dados abrangente em tempo real dos sistemas de controle (e.g., sensores de HVAC), criando uma Sombra Digital precisa do estado da instalação. |
| 5 | A infraestrutura em tempo real é escalável, podendo ser reconfigurada de forma rápida e fácil para acomodar novos ativos de controle. |
| 6 | Os sistemas de controle e a infraestrutura de conectividade estão convergentes com as plataformas de automação do Chão de Fábrica e da Empresa (Enterprise) para formar redes altamente autônomas. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Diagramas de arquitetura de rede TI/OT da instalação, Sistemas de Gerenciamento de
         Edifícios (BMS) ou automação.
- Relatórios de auditoria ou certificações como ISO 27001.

- Logs de latência e desempenho de rede em tempo real.

- Documentação de arquitetura de Edge/Cloud Computing.

- Registros de dados de sensores de HVAC em sistemas MES/ERP.


<!-- pág. original: 335/465 -->
##### Métricas/KPIs

- Consumo energético total da instalação.

- Latência de dados entre sistemas de controle ambiental e o sistema central.

- Disponibilidade (%) dos sistemas.

- Tempo médio de sincronização entre dados OT e TI.

##### Sinais por nível

- Nível 0:


  - O gerenciamento é feito por métodos informais, usualmente de forma manual.


- Nível 1:


  - Existem links de rede formais que permitem a interação ou troca de informação, geralmente através de múltiplas tecnologias e protocolos.
  - A dependência da participação humana é evidente.


- Nível 2:


  - Os ativos conseguem interagir e trocar informação sem restrições significativas.

  - A integração completa entre TI/TO ainda não ocorreu.


- Nível 3:


  - Envio e recebimento de dados e comandos de controle em tempo real.

  - TI/TO estão integrados.

  - Capacidade de sincronização entre TI e OT.


- Nível 4:


  - TI/OT identificam desvios e diagnosticam as causas potenciais (e.g., por que o HVAC está consumindo mais energia).


<!-- pág. original: 336/465 -->
  - A integração vertical e horizontal dos processos e sistemas é estabelecida, resultando em diagnóstico automático de desvios de performance dos sistemas críticos.


- Nível 5:


  - A integração suporta modelos preditivos e análise avançada para prever futuros estados dos sistemas de controle (e.g., manutenção preditiva do chiller ou HVAC).


- Nível 6:


  - O sistema é capaz de executar decisões automaticamente para otimizar o desempenho e a eficiência dos recursos da instalação, sem intervenção humana.

##### Amostragem

- Selecionar 3-5 artefatos relevantes para evidência dos sinais (logs de segurança de rede,
          auditorias e relatórios de incidentes), atualizados nos últimos 90 dias

##### I.9.1.3 Questão: A infraestrutura de rede (cabeada e sem fio) que interliga os...
A infraestrutura de rede (cabeada e sem fio) que interliga os sistemas da instalação (incluindo
controles HVAC, iluminação, etc) permite que as redes existentes sejam facilmente adaptadas para
acomodar novas composições de equipamentos, máquinas e sistemas de computador?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A expansão da infraestrutura é impossível digitalmente. |
| 1 | A adaptação ou adição de novos ativos requer intervenção humana significativa e configuração manual extensa. |
| 2 | Os sistemas conectados são interoperáveis, facilitando a adaptação/adição de novos equipamentos críticos da instalação. |
| 3 | A infraestrutura é totalmente interoperável, e existe um framework definido para inclusão de novos ativos e sistemas de controle. |
| 4 | A infraestrutura é capaz de se adaptar de forma contínua aos requisitos vigentes de configuração e escalabilidade. |
| 5 | A infraestrutura de rede é altamente escalável. |
| 6 | A escalabilidade atinge a autonomia. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentação de soluções Edge ou Cloud Computing.

- Diagramas de arquitetura de rede TI/OT da instalação.

- Protocolos para reconfiguração rápida (Plug-and-play).

- Logs de capacidade e desempenho da infraestrutura.

- Mapa de integração de protocolos (interoperabilidade Facility).

- Planos de integração de novos equipamentos.

##### Métricas/KPIs

- Tempo médio de integração de novo ativo.

- Disponibilidade (%) de sistemas críticos.

- Latência média de dados de rede da instalação.

- Número de incidentes críticos de falhas de disponibilidade.

- Tempo médio de onboarding de novos dispositivos.

##### Sinais por nível

- Nível 0:


  - Os sistemas (e.g., HVAC) não estão conectados e quaisquer modificações ou adições de equipamentos são tratadas de forma isolada, manual ou ad-hoc.


- Nível 1:


  - A infraestrutura de rede básica possui baixo grau de interoperabilidade.


<!-- pág. original: 338/465 -->
  - A integração de novos sistemas de controle ambiental é complexa e lenta devido à incompatibilidade.


- Nível 2:


  - A infraestrutura permite adaptações e novas aquisições de equipamentos sem restrições significativas de protocolo; contudo, a adaptação da rede a grandes mudanças na composição de ativos é lenta e depende de planejamento específico.


- Nível 3:


  - Existem processos definidos e sequenciais para reconfiguração da rede; entretanto, tais processos não são automatizados e ainda dependem de ações específicas.
  - A expansão da coleta de dados em tempo real para novos ativos é uma funcionalidade disponível.


- Nível 4:


  - A rede suporta a adição de novos ativos de controle e a comunicação em tempo real.

  - O sistema ajusta automaticamente a capacidade de rede em função da carga de dados.

  - Os sistemas de assistência diagnosticam o impacto de novos equipamentos na operação.
  - A escalabilidade existe, mas a adaptação não é totalmente autônoma.


- Nível 5:


  - As redes existentes (cabeada e sem fio) podem ser configuradas de forma rápida e fácil para acomodar quaisquer modificações na composição de equipamentos e sistemas da instalação (provisionamento automatizado).
  - A adição de novos ativos suporta a análise preditiva em toda a instalação.


- Nível 6:


  - A rede da instalação está convergente com as plataformas do Chão de Fábrica e Corporativa, permitindo reconfigurações dinâmicas e contínuas (plug-and-play).


<!-- pág. original: 339/465 -->
  - Novos ativos são integrados automaticamente em redes altamente autônomas que otimizam o desempenho da instalação sem intervenção humana (utilizando o aprendizado adaptativo e o balanceamento dinâmico de carga).

##### Amostragem

- Selecionar 3-5 artefatos relevantes para evidência dos sinais, atualizados nos últimos 90 dias


##### I.9.1.4 Questão: O framework de segurança de TI e as políticas de governança cobrem a...
O framework de segurança de TI e as políticas de governança cobrem a administração de ativos,
incluindo equipamentos e sistemas de controle da Instalação?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existe um framework de segurança de TI, e a administração de ativos é feita com base em métodos ad-hoc ou manuais. |
| 1 | A segurança de TI está focada em funcionalidades básicas dos sistemas, sem um foco explícito na administração de ativos digitais ou identificação formal. |
| 2 | A segurança de TI é tratada de forma reativa ou ad-hoc; não há um framework de segurança vigilante e resiliente estabelecido. |
| 3 | Existe um framework de segurança vigilante e resiliente. |
| 4 | A segurança é proativa e adaptada continuamente. |
| 5 | A infraestrutura é altamente escalável e redundante, e o framework de segurança suporta o crescimento contínuo de ativos. |
| 6 | A administração de ativos está integrada em uma arquitetura de segurança ciberfísica segura e resiliente. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Certificação de segurança de rede (e.g., IEC 62443).


<!-- pág. original: 340/465 -->
- Política de segurança cibernética.

- Documentação de identificação e autenticação de ativos.

- Registros de rastreabilidade e localização de ativos.

- Relatórios de auditoria de políticas de segurança dos sistemas da instalação.

- Documentação de políticas de proteção e privacidade de dados.

##### Métricas/KPIs

- Taxa de Incidentes Críticos de Cibersegurança.

- Tempo de Recuperação de Falhas de Ativos.

- Porcentagem de ativos com identificação única, contemplados pelas políticas de segurança.

- Número de Não Conformidades em auditorias da Política de Proteção de Dados.

##### Sinais por nível

- Nível 0:


  - Não há processos definidos de segurança de TI.

  - Em muitos casos, os ativos sequer estão conectados, de modo que a segurança de TI é irrelevante para este domínio.


- Nível 1:


  - Os ativos da instalação (como os controladores do HVAC e iluminação, por exemplo) possuem sistemas de controle próprios e isolados, que executam tarefas pré-programadas.


- Nível 2:


  - A administração de ativos não inclui controle de fluxo de dados formal ou validação contínua.
  - Embora os sistemas estejam conectados e sejam interoperáveis, a segurança de TI é tratada de forma tempestiva, por solicitação de demanda.


- Nível 3:


<!-- pág. original: 341/465 -->
  - Medidas de segurança de TI são formalmente estabelecidas e cobrem questões de administração de ativos, incluindo a proteção de dados da instalação e o controle de acesso de usuários.
  - Existem políticas claras para proteger a rede de ativos interoperáveis da instalação contra acesso ou disrupção indesejada.


- Nível 4:


  - A administração de ativos é suportada por sistemas de informação capazes de realizar o controle do fluxo de dados em tempo real.
  - Os sistemas conseguem identificar desvios relacionados a ativos (e.g., falhas de autenticação de dispositivos) e diagnosticar causas potenciais.


- Nível 5:


  - Os sistemas utilizam análise preditiva e IA/ML para prever vulnerabilidades futuras ou falhas de segurança relacionadas à administração de ativos, como o risco de comprometimento da identidade digital do ativo.


- Nível 6:


  - Os sistemas de informação e segurança são auto-aprendizes e executam decisões automaticamente para otimizar a segurança e a funcionalidade dos ativos, adaptando-se continuamente às circunstâncias, sem intervenção humana.

##### Amostragem

- Selecionar 3-5 artefatos relevantes para evidência dos sinais, atualizados nos últimos 90 dias

#### Glossário
[Sem glossário]
#### I.9.2 Capacidade: Segurança de TI
#### Bloco/Pilar
- Bloco: Tecnologia


<!-- pág. original: 343/465 -->
- Pilar: Conectividade

- Dimensão: Conectividade de Instalações (Facility)

#### Resumo Descritivo
Esta dimensão avalia a interconexão de equipamentos e sistemas dentro do ambiente industrial,
incluindo cibersegurança de instalações críticas e controle de condições ambientais (do inglês Heating,
Ventilation, and Air Conditioning, ou HVAC). Visa medir a interoperabilidade e segurança da rede para
permitir a troca contínua de dados e a automação eficiente da instalação, gerando redução de custos e
maior eficiência.
#### Questões
##### I.9.2.1 Questão: A infraestrutura de Segurança de TI garante a identificação e...
A infraestrutura de Segurança de TI garante a identificação e autenticação de usuários (incluindo
funcionários e colaboradores externos) de forma a controlar o acesso a equipamentos e sistemas
críticos da instalação?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O acesso aos equipamentos e sistemas críticos da instalação é manual ou físico, sem requisitos de identificação ou autenticação de usuários digitais. |
| 1 | O acesso é isolado por sistema, com base em mecanismos simples de identificação e autenticação, sem rastreabilidade centralizada. |
| 2 | Os sistemas estão conectados, e existe alguma forma de identificação/autenticação de usuários. No entanto, a gestão desses mecanismos é frágil ou executada em modo ad-hoc. |
| 3 | Existe um framework de segurança para proteger a rede contra acesso ou disrupção indesejados. |
| 4 | A identificação/autenticação de usuários é realizada em tempo real e de maneira contextualizada para o acesso aos ativos da instalação. |
| 5 | A infraestrutura é escalável e o framework de segurança suporta o crescimento contínuo de usuários. |
| 6 | Os sistemas de controle de acesso são autônomos, adaptativos, e totalmente automatizados. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Certificação de segurança de rede (e.g., IEC 62443).

- Política de segurança cibernética.

- Documentação de identificação e autenticação de usuários.

- Perfis de função e controle de credenciais.

- Registro de uso de assinaturas digitais/aprovações.

- Relatórios de auditoria de políticas de segurança dos sistemas da instalação.

- Documentação de políticas de proteção e privacidade de dados.

##### Métricas/KPIs

- Taxa de Incidentes Críticos de Cibersegurança.

- Tempo médio para restauração de acessos críticos.

- Número (%) de ativos com controle de acesso baseado em função.

- Grau de segurança dos mecanismos de controle de acesso implementados (e.g., senha
          simples é baixo, autenticação de 2 fatores é médio, assinatura digital é alto).
- Número de alertas de acesso indevido tratados automaticamente.

##### Sinais por nível

- Nível 0:


  - Não há processos definidos de identificação/autenticação.

  - Os sistemas de controle não estão conectados ou quando estão, o controle de acesso é inexistente.


- Nível 1:


<!-- pág. original: 345/465 -->
  - Os ativos da instalação estão conectados, mas a identificação e autenticação de usuários são básicas (e.g., senhas simples, muitas vezes compartilhadas entre vários usuários) e geralmente executam tarefas pré-programadas.


- Nível 2:


  - A identificação/autenticação não é baseada em perfis de função (privilégios), e se baseia em mecanismos muito simples (e.g., senhas).
  - A rede é vulnerável a acessos indesejados.


- Nível 3:


  - A infraestrutura implementa a identificação e autenticação de usuários de maneira formal.
  - Os mecanismos utilizados baseiam-se em perfis de função e credenciais únicas (RBAC).
  - O controle de acesso também permite que os funcionários sejam incluídos em processos de comunicação de forma contextualizada.
  - O log é centralizado.


- Nível 4:


  - O sistema de controle de acesso se integra aos demais sistemas da instalação, podendo identificar e diagnosticar desvios ou tentativas de acesso não autorizado, rastreando imediatamente a fonte humana ou digital.


- Nível 5:


  - O sistema de controle de acesso usa análise preditiva para prever vulnerabilidades relacionadas ao acesso de usuários ou identificar proativamente riscos de comprometimento de credenciais, com base na análise comportamental do usuário.


- Nível 6:


  - O sistema de controle de acesso adapta as credenciais e privilégios dos usuários às circunstâncias operacionais de forma automática


<!-- pág. original: 346/465 -->
  - O sistema também se integra com outros domínios para executar decisões de segurança de forma autônoma (e.g., revogação automática de acesso em caso de risco).
  - Existem mecanismos de detecção de intrusão adaptativos e capazes de aprender a partir de padrões comportamentais dos usuários.
  - Há integração com SIEM/SOC para resposta automática.

##### Amostragem

- Selecionar 3-5 artefatos relevantes para evidência dos sinais, atualizados nos últimos 90 dias


##### I.9.2.2 Questão: Como a infraestrutura de Segurança de TI implementa a validação de...
Como a infraestrutura de Segurança de TI implementa a validação de saúde do sistema (do inglês,
system health validation) para os ativos e sistemas de controle da instalação, permitindo a
identificação e registro de desvios, falhas de segurança ou mau funcionamento?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A validação da saúde do sistema não é realizada. |
| 1 | Os sistemas OT e IT da instalação executam tarefas e processos baseados em lógica pré-programada. |
| 2 | Os sistemas OT e IT são capazes de identificar desvios dos parâmetros predefinidos. |
| 3 | Os sistemas OT e IT são capazes de identificar desvios e diagnosticar as causas potenciais. |
| 4 | Os sistemas OT e IT utilizam dados em tempo real para identificar desvios e diagnosticar as causas potenciais. |
| 5 | Os sistemas OT e IT são capazes de prever desvios e executar decisões independentemente, para otimizar o desempenho |
| 6 | A validação da saúde do sistema inclui processos de auto-aprendizagem e o sistema de informação continuamente se adapta às circunstâncias. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Certificação de segurança de rede (e.g., IEC 62443).

- Relatórios de validação da saúde do sistema.

- Logs de detecção e diagnóstico de desvios.

- Dados de sensores em sistemas de informação.

- Documentação de análise preditiva de falhas de ativos.

- Relatórios de auditoria de políticas de segurança dos sistemas da instalação.

##### Métricas/KPIs

- Taxa de Incidentes Críticos de Cibersegurança.

- Tempo médio para diagnóstico de desvios na saúde do sistema.

- Disponibilidade (%) dos sistemas críticos da instalação.

- Acurácia (%) da previsão de falhas de ativos da instalação.

##### Sinais por nível

- Nível 0:


  - Sistemas de TI e OT não estão presentes, ou não há dispositivos eletrônicos ou digitais sendo usados.


- Nível 1:


  - A validação de saúde dos sistemas se limita a funcionalidades estáticas de auto diagnóstico, providas isoladamente pelos próprios equipamentos.
  - Não há capacidade de identificar desvios ou avaliar de forma ativa a saúde do sistema.


- Nível 2:


  - Os sistemas podem notificar o pessoal relevante sobre esses desvios.

  - A validação de saúde do sistema utiliza recursos básicos, focada apenas na detecção.


<!-- pág. original: 348/465 -->
- Nível 3:


  - O framework de segurança contempla a proteção da rede e dos ativos, cobrindo formalmente a validação da saúde do sistema por meio de medidas claras de segurança de TI.


- Nível 4:


  - Os ativos e sistemas da instalação são capazes de comunicação em tempo real.

  - Há medidas proativas para manter a validação de saúde do sistema e adaptá-la em resposta às circunstâncias.


- Nível 5:


  - A validação da saúde do sistema é avançada, utilizando algoritmos e modelos avançados para prever falhas potenciais com antecedência.


- Nível 6:


  - Os sistemas de validação da saúde do sistema funcionam de forma autônoma e podem tomar decisões.
  - Eles são dotados de mecanismos de aprendizado para otimizar o desempenho e a eficiência de recursos.

##### Amostragem

- Selecionar 3-5 artefatos relevantes para evidência dos sinais, atualizados nos últimos 90 dias


##### I.9.2.3 Questão: A infraestrutura de Segurança de TI implementa o controle de fluxo de...
A infraestrutura de Segurança de TI implementa o controle de fluxo de dados para os ativos e sistemas
de controle da instalação?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O fluxo de dados digital é inexistente. |
| 1 | O controle do fluxo de dados é manual e ad-hoc. |
| 2 | Os sistemas e ativos da instalação são capazes de interagir e trocar informação sem restrições significativas, mas não existem políticas de segurança definidas para esses processos. |
| 3 | As políticas de segurança de TI cobrem formalmente o controle de fluxo de dados. |
| 4 | Os sistemas e ativos da instalação são capazes de estabelecer fluxos de dados em tempo real, de forma segura. |
| 5 | O controle do fluxo de dados é suportado por análise avançada e sistemas redundantes. |
| 6 | O controle do fluxo de dados implementa mecanismos de auto-aprendizado e adapta-se continuamente às circunstâncias. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Certificação de segurança de rede (e.g., IEC 62443).

- Diagramas de arquitetura de rede TI/OT da instalação.

- Políticas formais de Controle de Fluxo de Dados.

- Logs de detecção e diagnóstico de desvios.

- Documentação de protocolos de comunicação.

- Relatórios de auditoria de políticas de segurança dos sistemas da instalação.

##### Métricas/KPIs

- Taxa de Incidentes Críticos de Cibersegurança.

- Latência média do fluxo de dados da instalação.

- Disponibilidade (%) dos sistemas críticos da instalação.

- Tempo médio de recuperação de falhas no fluxo de dados.

- Percentual de pacotes retransmitidos (perda de dados).


<!-- pág. original: 350/465 -->
##### Sinais por nível

- Nível 0:


  - Os ativos e sistemas da instalação não estão conectados e não há uso de sistemas de TI/OT.


- Nível 1:


  - Ainda que existam links formais de rede para ativos da instalação, a troca de dados entre os sistemas de controle e os sistemas de TI é predominantemente gerenciada por intervenção humana.


- Nível 2:


  - A segurança na troca de dados entre os ativos é gerida de forma reativa.

  - Não existe um framework de segurança voltado ao controle de fluxo de dados.


- Nível 3:


  - Existe um framework de segurança para proteger a rede e os ativos da instalação contra disrupção.
  - A informação é trocada continuamente entre os sistemas da cadeia de valor (integração vertical).
  - Implementação de firewalls industriais e segmentação lógica.


- Nível 4:


  - O fluxo de dados da instalação é processado sem atraso e está disponível quase imediatamente.
  - O fluxo de dados permite que os sistemas de assistência façam diagnósticos de desvios ou falhas de segurança no fluxo de dados.


- Nível 5:


<!-- pág. original: 351/465 -->
  - Os sistemas utilizam modelos preditivos para prever e prevenir vulnerabilidades ou interrupções no fluxo de dados da instalação antes que ocorram.


- Nível 6:


  - Os sistemas de segurança fazem uso intensivo de dados do próprio fluxo sob controle, estabelecendo padrões seguros de operação.
  - Eles também executam decisões automaticamente para otimizar o fluxo de dados e as funcionalidades do sistema, sem intervenção humana.

##### Amostragem

- Selecionar 3-5 artefatos relevantes para evidência dos sinais, atualizados nos últimos 90 dias

#### Glossário
[Sem glossário]
### I.10 Dimensão: Inteligência de Chão de Fábrica

#### I.10.1 Capacidade: Pré-processamento descentralizado de dados de sensores
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Inteligência

- Dimensão: Inteligência de Chão de Fábrica

#### Resumo Descritivo
A dimensão Shop Floor Intelligence (D10) avalia o processamento e a análise de dados no ambiente
de produção com o objetivo de otimizar processos existentes e, em estágios avançados, criar novas
aplicações, produtos e serviços.
#### Questões
##### I.10.1.1 Questão: Em que medida a sua organização utiliza sistemas embarcados ou...
Em que medida a sua organização utiliza sistemas embarcados ou dispositivos de borda (Edge
Computing) para realizar o pré-processamento e a análise dos dados de sensores, viabilizando
cálculos críticos e ações em tempo real?


<!-- pág. original: 353/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Sistemas de Tecnologia da Operação (OT) e de Tecnologia da Informação (TI) não são utilizados para monitorar ou processar os dados dos sensores. |
| 1 | O processamento de dados de sensores é feito manualmente ou totalmente em sistemas centrais, resultando em significativa latência para a tomada de decisão. |
| 2 | Os sistemas de controle e sensores capturam dados, mas o processamento é isolado, sem o uso de sistemas embarcados avançados para pré-processamento, e a latência de dados é alta. |
| 3 | Sistemas embarcados são utilizados para monitoramento local e loops de controle fechado de processos técnicos, mas esses dados pré-processados não são rotineiramente integrados ou acessíveis à rede corporativa para otimizações amplas. |
| 4 | O pré-processamento descentralizado de dados ocorre em dispositivos de borda, o que garante a redução da latência e permite a entrega de informações contextuais em tempo quase real para apoiar a tomada de decisão humana imediata. |
| 5 | Os sistemas de processamento descentralizado são robustos o suficiente para executar análises complexas (ex. manutenção preditiva, detecção de anomalias) localmente, e as previsões resultantes são integradas ao planejamento para antecipar desvios. |
| 6 | Os sistemas embarcados executam o processamento complexo em tempo real e são capazes de tomar decisões de forma autônoma no nível do recurso (máquina/equipamento) para otimizar o desempenho e adaptar-se às mudanças. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Especificações de Sistemas Embarcados

- Diagramas de Arquitetura de TI

- Configurações de Sistemas de Processamento de Dados

##### Métricas/KPIs

- Latência de Análise: O tempo necessário para que a análise dos dados do evento seja concluída.
- Latência de Decisão: O tempo necessário para que a contramedida ou decisão correspondente seja aprovada
- Latência de Ação: O tempo para que a contramedida entre em vigor.

- Flexibilidade. A capacidade de adaptação às mudanças, frequentemente medida pela capacidade de customização.

##### Sinais por nível

- Nível 0:


  - Ausência de Dispositivos Digitais: Nenhum dispositivo eletrônico ou digital é utilizado

  - Ausência de Conectividade


- Nível 1:


  - Uso de Arquivos Manuais/Planilha

  - Feedback Manual

  - Sistemas de TI e OT Isolados

  - Falta de Informações em Tempo Real no Chão de Fábrica


- Nível 2:


  - Dependência de Transferência Manual para Análise

  - Dados em Silos Descentralizados


<!-- pág. original: 355/465 -->
  - Atraso na Decisão e Ação


- Nível 3:


  - Ação Manual Necessária

  - Falta de Fonte Única de Verdade


- Nível 4:


  - Pré-processamento ocorre em dispositivos de borda

  - Redução de latência

  - Entrega de informação contextual em tempo quase real


- Nível 5:


  - Alertas de Manutenção Preditiva

  - Detecção de Anomalias em Tempo Real

  - Integração com Sistemas de Planejamento


- Nível 6:


  - Ajuste Autônomo de Parâmetros de Processo

  - Autocorreção de Qualidade em Malha Fechada (Closed-Loop)

  - Manutenção Autônoma Preditiva

##### Amostragem

- Amostragem Seleção Estratificada de Processos Críticos

- Processos de Alto Valor Agregado Identifique os equipamentos considerados "cérebros" da operação
- Análise de Lotes Específicos Amostra de Pessoas (Entrevistas): Entreviste o Engenheiro de Automação Converse com o Operador Sênior Entreviste o Analista de Dados ou Cientista de Dados


<!-- pág. original: 356/465 -->
##### I.10.1.2 Questão: Em que medida a sua organização utiliza o pré-processamento...
Em que medida a sua organização utiliza o pré-processamento descentralizado (Edge Computing)
para filtrar, agregar e tratar "ruído" dos dados de sensores diretamente no equipamento, reduzindo o
volume de dados transmitidos para sistemas centrais?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Sistemas de Tecnologia da Operação (OT) e de Tecnologia da Informação (TI) não são utilizados para monitorar ou processar os dados dos sensores. |
| 1 | Todo o fluxo de dados brutos dos sensores é enviado para processamento em sistemas centrais (sem pré-processamento local), resultando em alta latência e alto tráfego de rede. |
| 2 | Os sensores capturam dados, mas o processamento é isolado no equipamento e não há uma estratégia para filtrar ou enviar dados relevantes para outros sistemas; a latência de dados é alta. |
| 3 | Sistemas embarcados são usados para monitoramento local, mas apenas dados de controle de processo (loops fechados) são usados localmente, sem envio de dados pré-processados para a rede corporativa. |
| 4 | O pré-processamento descentralizado (ex em dispositivos de borda) é usado para filtrar e agregar dados brutos, garantindo a redução da latência e enviando apenas informações contextuais em tempo quase real para sistemas centrais (ex: dashboards). |
| 5 | Os sistemas descentralizados executam análises complexas (ex detecção de anomalias, manutenção preditiva) localmente, enviando apenas os insights e previsões para integração com o planejamento, não o fluxo de dados brutos. |
| 6 | Os sistemas embarcados executam o processamento complexo em tempo real, tomando decisões autônomas e enviando aos sistemas centrais apenas os registros das ações tomadas e os resultados de desempenho, otimizando o tráfego de rede. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Configurações de Software de Borda (Edge Software Configuration):
  - Onde buscar: Departamentos de Automação, Engenharia de TI/OT.
  - O que verificar: A lógica de programação nos gateways de IoT ou PCs industriais. Procurar especificamente por funções de agregação (ex: Average(1min)), filtragem (ex: bandas mortas, filtros de média móvel) ou lógica condicional de envio (ex: "enviar dados apenas se a variação for > 5%").
- Logs de Tráfego de Rede e Consumo de Dados:
  - Onde buscar: Departamento de TI (Administradores de rede, Painéis de Provedor de Nuvem).
  - O que verificar: O volume de dados (em MB/GB) transmitido pela rede do chão de fábrica. Comparar o volume de dados brutos que poderia ser gerado (ex: um sensor de vibração de alta frequência gerando 1GB/hora) com o volume realmente transmitido. Uma grande diferença é a evidência do pré-processamento.
- Diagramas de Arquitetura de Fluxo de Dados:
  - Onde buscar: Departamentos de TI, Automação ou Engenharia.
  - O que verificar: Se o diagrama mostra os dados dos sensores sendo enviados primeiro para um dispositivo de borda (ex: IPC, Edge Gateway) e depois para o sistema central (MES, Scada, Nuvem). Verificar se há anotações como "dados agregados" ou "dados filtrados" nesse fluxo.
- Especificações Técnicas dos Dispositivos de Borda:
  - Onde buscar: Departamentos de Automação ou Engenharia.
  - O que verificar: Se os dispositivos no chão de fábrica (além dos CLPs básicos) possuem capacidade de processamento (CPU, RAM) suficiente para executar essa filtragem e agregação localmente.

##### Métricas/KPIs

- Taxa de Redução de Dados (Data Reduction Ratio):

<!-- pág. original: 358/465 -->
  - Descrição: (Volume de dados brutos gerados pelos sensores) / (Volume de dados transmitidos para sistemas centrais).
  - Sinal: Uma taxa alta (ex: 100:1) indica que apenas dados relevantes ou agregados estão sendo enviados.
- Utilização da Largura de Banda da Rede (Network Bandwidth Utilization):
  - Descrição: O percentual da rede OT/TI consumido pelo envio de dados de sensores.
  - Sinal: Baixa utilização apesar da existência de milhares de pontos de dados, indicando processamento eficiente na borda.
- Custo de Transmissão e Armazenamento em Nuvem:
  - Descrição: O custo monetário (ex: R$ por mês) pago a provedores de nuvem para ingestão e armazenamento de dados de IoT.
  - Sinal: Custos controlados ou reduzidos, mesmo com o aumento do número de sensores, devido ao envio apenas de dados valiosos.
- Qualidade dos Dados no Sistema Central (Data Quality):
  - Descrição: Mede a proporção de dados úteis versus "ruído" (dados redundantes, espúrios ou irrelevantes) no banco de dados central.
  - Sinal: Alta qualidade, pois a filtragem de ruído é feita na origem (no equipamento).

##### Sinais por nível

- Nível 0:


  - Ausência de Dispositivos Digitais: Nenhum dado de sensor é coletado digitalmente


- Nível 1:


  - Uso de Arquivos Manuais/Planilha: Os dados são coletados, mas armazenados localmente e movidos manualmente
  - Não há transmissão de dados em tempo real


- Nível 2:


<!-- pág. original: 359/465 -->
  - Dados em Silos Descentralizados: Os dados são registrados em silos locais (ex: cartão SD de um CLP), mas não são enviados para sistemas centrais, ou são enviados com alta latência


- Nível 3:


  - Streaming de Dados Brutos (Sem Filtro): Todo o fluxo de dados brutos de alta frequência dos sensores é enviado diretamente para um sistema central ou nuvem ("data lake")
  - O sinal é o alto tráfego de rede e a necessidade de processamento pesado no sistema central para "limpar" os dados


- Nível 4:


  - Pré-Processamento por Agregação/Filtragem: O dispositivo de borda executa filtragem de ruído e agregação (ex: calcula médias, máximos, mínimos) e envia apenas esses dados agregados em intervalos regulares (ex: a cada 1 minuto) para sistemas centrais
  - O sinal é um tráfego de rede baixo e previsível


- Nível 5:


  - Processamento por Exceção (Envio de Insights): Os dispositivos de borda monitoram os dados brutos, mas só enviam dados para o sistema central quando uma anomalia ou evento de interesse é detectado
  - O sinal é um tráfego de rede muito baixo, quase nulo, com picos apenas durante eventos


- Nível 6:


  - Processamento Autônomo (Envio de Logs): O dispositivo de borda detecta anomalias, toma decisões autônomas e envia aos sistemas centrais apenas um log da ação tomada (ex: "Parâmetro X ajustado às 10:32")
  - É o nível máximo de redução de dados


<!-- pág. original: 360/465 -->
##### Amostragem

- Recomenda-se uma Amostragem Intencional (Propositiva) focada nos sensores que geram maior volume de dados
- Seleção de Processos (Estratificação): Identificar 1-2 processos que utilizam sensores de alta frequência (ex: análise de vibração, acústica, termografia, sistemas de visão de alta velocidade), pois são os maiores geradores de dados e onde o pré-processamento é mais necessário
- Seleção de Sensores: Dentro desses processos, focar a análise em 1-3 sensores específicos de alta frequência
- Seleção de Evidências (Triangulação):
  - Artefatos: Solicitar os diagramas de arquitetura de rede e as especificações do dispositivo (gateway/CLP) conectado a esses sensores específicos
  - Dados (Amostra Comparativa): Solicitar dois conjuntos de dados para o mesmo sensor durante um período de 5 minutos:
    - Um dump dos dados brutos (logados localmente no dispositivo de borda)
    - Um export dos dados que chegaram ao banco de dados central (nuvem/MES)
  - A diferença de volume e formato entre os dois é a prova concreta do pré-processamento
- Entrevistas: Conversar com o Engenheiro de Automação sobre a lógica de filtragem implementada e com o Administrador de Rede sobre o impacto no tráfego de dados

##### I.10.1.3 Questão: Em que medida a sua organização utiliza o processamento...
Em que medida a sua organização utiliza o processamento descentralizado (Edge/embarcado) para
executar cálculos e lógicas de controle em tempo real (ex: loops de controle, intertravamentos de
segurança) que não podem depender da latência da rede central?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Sistemas de Tecnologia da Operação (OT) e de Tecnologia da Informação (TI) não são utilizados para monitorar ou processar os dados dos sensores. |
| 1 | O processamento de dados de sensores é feito manualmente ou totalmente em sistemas centrais, resultando em latência significativa que impede o controle em tempo real. |
| 2 | Os sistemas de controle (CLPs) executam lógicas simples, mas qualquer cálculo complexo ou análise é feito em sistemas centrais, com alta latência, inviabilizando o controle em tempo real. |
| 3 | Sistemas embarcados são utilizados para monitoramento local e loops de controle fechado de processos técnicos (ex controle PID básico em um CLP), mas esses dados não são integrados à rede corporativa. |
| 4 | O pré-processamento descentralizado em dispositivos de borda é usado para executar cálculos mais complexos (ex fusão de múltiplos sensores) para otimizar um processo localmente, garantindo a redução da latência de decisão. |
| 5 | O processamento descentralizado executa cálculos complexos e modelos de otimização (ex Controle de Processo Avançado - APC) em tempo real no dispositivo de borda, ajustando ativamente o processo sem depender da rede central. |
| 6 | Os sistemas embarcados executam processamento complexo em tempo real (ex: modelos de IA, fusão de sensores) para tomar decisões de controle e segurança de forma autônoma (ex: parada de emergência preditiva, otimização de trajetória), garantindo a operação mesmo com falha na rede central. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Lógica de Programação de Controladores (CLP, PAC, IPC):
  - Onde buscar: Departamentos de Automação ou Engenharia de Manutenção.
  - O que verificar: O código-fonte ou os blocos de função nos controladores locais (embarcados na máquina). Procurar por evidências de cálculos complexos (ex: algoritmos de controle preditivo, fusão de sensores, modelos de otimização) que rodam dentro do controlador da máquina, em vez de em um servidor central.
- Diagramas de Arquitetura de Controle e Topologia de Rede:
  - Onde buscar: Departamentos de TI, Automação ou Engenharia.

<!-- pág. original: 362/465 -->
  - O que verificar: Se o "loop de controle" (Sensor -> Processador -> Atuador) está fechado localmente no equipamento. O artefato deve mostrar que as ações críticas de controle não dependem de um "round-trip" (ida e volta) de dados para um sistema SCADA, MES ou nuvem.
- Documentação de Análise de Risco e Intertravamentos de Segurança:
  - Onde buscar: Departamentos de Segurança do Trabalho ou Engenharia.
  - O que verificar: A matriz de segurança e os diagramas de intertravamento. Comprovar que as lógicas de segurança críticas (ex: parada de emergência, cortinas de luz, controle de robôs) são executadas em processadores de segurança dedicados e locais, garantindo resposta em tempo real independente da rede.
- Especificações Técnicas de Processo (ETs):
  - Onde buscar: Departamento de Engenharia de Processo.
  - O que verificar: Requisitos formais que exigem processamento em tempo real. Procurar por especificações como "tempo de resposta do loop de controle < 10ms" ou "taxa de atualização de dados de segurança".

##### Métricas/KPIs

- Latência de Ação (Action Latency): O tempo medido (em milissegundos) entre a detecção de um evento crítico pelo sensor e a resposta física do atuador. Em sistemas descentralizados, esse valor deve ser extremamente baixo e determinístico.
- Tempo de Ciclo do Loop de Controle (Control Loop Cycle Time): O tempo de "scan" do processador local que executa a lógica. Mede a velocidade com que o sistema pode reavaliar e corrigir o processo.
- Disponibilidade da Função de Controle em "Ilhamento": Percentual de tempo que o equipamento continua executando sua lógica de controle complexa e segura após a desconexão da rede central. A meta deve ser 100%.
- Jitter (Variação da Latência): A variação no tempo de resposta. Para controle em tempo real, o jitter (variação) baixo é tão importante quanto a latência baixa. O processamento local elimina o jitter causado pela rede.
- Índice de Capabilidade do Processo (Cp/Cpk): Embora seja uma métrica de qualidade, um Cpk alto e estável é um forte indicador de que o controle em tempo real está efetivamente minimizando desvios do processo.

##### Sinais por nível

- Nível 0:


  - O controle é totalmente manual, baseado na experiência do operador


<!-- pág. original: 363/465 -->
- Nível 1:


  - Uso de Arquivos Manuais/Planilha: O operador lê um sensor analógico, consulta uma planilha e faz um ajuste manual
  - Latência de horas ou minutos


- Nível 2:


  - O sensor envia dados para um sistema SCADA/MES central

  - Um operador (ou o sistema central) analisa e envia um comando de volta para a máquina
  - A latência da rede é alta e impede o controle em tempo real


- Nível 3:


  - O CLP local executa lógicas de intertravamento simples e controle PID básico (loops fechados)
  - Isso é o padrão, mas não inclui cálculos complexos ou preditivos


- Nível 4:


  - O dispositivo de borda (ex: IPC, CLP avançado) executa cálculos complexos (ex: fusão de múltiplos sensores, fórmulas matemáticas) localmente para otimizar um processo em tempo real, garantindo baixa latência


- Nível 5:


  - O dispositivo de borda executa modelos de otimização complexos (ex: Controle de Processo Avançado - APC) em tempo real, ajustando múltiplos parâmetros interdependentes para maximizar a eficiência, sem depender da rede central


- Nível 6:


<!-- pág. original: 364/465 -->
  - Os sistemas embarcados executam processamento complexo (ex: IA, modelos de segurança) em tempo real para tomar decisões autônomas críticas, garantindo a operação segura e otimizada mesmo durante uma falha completa da rede central

##### Amostragem

- Recomenda-se uma Amostragem Intencional (Propositiva), focada em processos onde a latência de controle é intrinsecamente crítica
- Seleção de Processos (Estratificação): Identificar 1-3 processos que sejam:
  - Críticos para Segurança: Onde um atraso de milissegundos pode causar um acidente (ex: prensas, robôs colaborativos, reatores químicos)
  - Críticos para a Qualidade (Alta Precisão): Onde um atraso de milissegundos degrada o produto (ex: usinagem CNC de 5 eixos, soldagem a laser, sistemas de visão em alta velocidade)
  - Críticos para a Velocidade (Alta Cadência): Onde o controle precisa ser local para acompanhar a velocidade física da linha (ex: sistemas "pick-and-place" de eletrônicos, linhas de envase)
- Seleção de Evidências (Triangulação): Artefatos: Solicitar os diagramas de malha de controle avançado (para processos de precisão) ou os diagrama de intertravamento de segurança (para processos de segurança)
- Teste de "Ilhamento" (Se possível): O método de amostragem mais eficaz é um teste prático
  - Desconectar (ou simular a falha) da rede central do equipamento selecionado e observar se a lógica de controle complexa e a segurança continuam operando perfeitamente
- Entrevistas: Conversar com o Engenheiro de Segurança de Máquinas, Engenheiro de Automação ou Engenheiro de Processo Sênior responsável pela operação do equipamento selecionado
#### Glossário
[Sem glossário]
### I.11 Dimensão: Inteligência Corporativa

#### I.11.1 Capacidade: Aprendizagem e tomada de decisão baseadas em dados
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Inteligência

- Dimensão: Inteligência Corporativa


<!-- pág. original: 366/465 -->
#### Resumo Descritivo
A cultura organizacional constitui a base humana e comportamental da transformação digital. No
contexto dos modelos ACATECH e SIRI, a disposição à mudança representa a capacidade da
organização de adaptar-se continuamente a novas tecnologias, processos e formas de trabalho. Essa
abertura cultural é essencial para que a empresa evolua de práticas tradicionais para um modelo
orientado por dados e inteligência digital. A aprendizagem e a tomada de decisão baseada em dados
traduzem o amadurecimento dessa cultura: as decisões deixam de depender apenas da experiência
individual e passam a se fundamentar em evidências extraídas de análises inteligentes. Isso exige
tanto o desenvolvimento de competências digitais quanto a criação de um ambiente que valorize a
experimentação, o aprendizado contínuo e a confiança nos dados. No bloco Tecnologia, pilar
Inteligência, e na dimensão Enterprise (D11) do modelo SIRI, essa capacidade reflete o ponto em que
as pessoas e os sistemas aprendem juntas — promovendo uma cultura organizacional que utiliza
informações analíticas para guiar decisões estratégicas e operacionais. À medida que a maturidade
cresce, a organização passa a incorporar inteligência coletiva e adaptativa, transformando dados em
conhecimento e conhecimento em ação.
#### Questões
##### I.11.1.1 Questão: Em que medida a organização promove uma cultura de aprendizagem em...
Em que medida a organização promove uma cultura de aprendizagem em que decisões e melhorias
são fundamentadas em dados e evidências, e não apenas em experiência ou hierarquia?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Decisões são tomadas com base em intuição ou autoridade; inexistem práticas formais de uso de dados para aprendizado. |
| 1 | Há reconhecimento da importância dos dados, mas a aprendizagem e as decisões ainda dependem de percepções individuais. |
| 2 | Dados são utilizados para registrar resultados, porém sem análise estruturada ou aprendizado coletivo. |
| 3 | As equipes utilizam dados de forma integrada para refletir sobre desempenho e propor melhorias. |
| 4 | A organização adota práticas sistemáticas de análise de dados e aprendizagem, compartilhando lições entre áreas. |
| 5 | O aprendizado é suportado por análises preditivas, permitindo decisões proativas baseadas em padrões de dados. |
| 6 | A organização aprende continuamente com dados em tempo real, ajustando comportamentos e decisões de forma autônoma e colaborativa. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Políticas de gestão do conhecimento e aprendizado.

- Registros de reuniões de análise de desempenho.

- Relatórios e dashboards de indicadores de aprendizado.

- Documentação de planos de ação baseados em dados.

##### Métricas/KPIs

- Percentual de decisões sustentadas por evidências de dados.

- Número de lições aprendidas incorporadas em processos.

- Frequência de análises de desempenho baseadas em dados.

- Índice de maturidade da cultura de dados.

##### Sinais por nível

- Nível 0:


  - Ausência de registro sistemático de dados ou aprendizado estruturado


- Nível 1:


  - Iniciativas pontuais de aprendizado baseadas em resultados individuais


- Nível 2:


<!-- pág. original: 368/465 -->
  - Coleta digital de dados sem uso analítico


- Nível 3:


  - Reflexões locais e revisões de desempenho baseadas em dados


- Nível 4:


  - Troca estruturada de lições aprendidas entre áreas


- Nível 5:


  - Decisões proativas fundamentadas em análises preditivas


- Nível 6:


  - Aprendizado organizacional contínuo, com sistemas e pessoas evoluindo conjuntamente

##### Amostragem

- Entrevistas com gestores e analistas sobre processos de aprendizado; análise documental de
          planos de ação e relatórios de lições aprendidas; observação de reuniões de revisão de
          desempenho; avaliação de plataformas de gestão do conhecimento e BI

##### I.11.1.2 Questão: Até que ponto os colaboradores possuem habilidades e conhecimentos...
Até que ponto os colaboradores possuem habilidades e conhecimentos para interpretar, analisar e
aplicar informações provenientes de dados em suas rotinas de trabalho?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os colaboradores não possuem habilidades para interpretar dados; as decisões são tomadas de forma empírica. |
| 1 | A organização reconhece a importância das competências analíticas, mas o aprendizado ainda é informal e individual. |
| 2 | Ferramentas digitais estão disponíveis, mas poucos colaboradores sabem utilizá-las de forma analítica. |
| 3 | Parte das equipes utiliza dados e ferramentas de BI para apoiar suas decisões locais. |
| 4 | A competência analítica é desenvolvida de forma estruturada e transversal; dados são interpretados e discutidos coletivamente. |
| 5 | As equipes aplicam modelos analíticos e algoritmos preditivos em suas decisões, com suporte de especialistas em dados. |
| 6 | A alfabetização analítica é disseminada em toda a organização; as equipes utilizam e aprimoram modelos de decisão baseados em aprendizado contínuo. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Registros de treinamentos e certificações em análise de dados.

- Relatórios de uso de dashboards e ferramentas de BI.

- Políticas de desenvolvimento de competências digitais.

- Entrevistas com equipes sobre processos de decisão e uso de dados.

##### Métricas/KPIs

- Percentual de colaboradores treinados em análise de dados.

- Número de decisões apoiadas por ferramentas analíticas.

- Frequência de uso de dashboards e relatórios.

- Índice de maturidade de competência analítica (por setor).

##### Sinais por nível

- Nível 0:


  - Decisões baseadas apenas em experiência


<!-- pág. original: 370/465 -->
- Nível 1:


  - Iniciativas isoladas de capacitação


- Nível 2:


  - Uso esporádico de ferramentas digitais sem análise estruturada


- Nível 3:


  - Utilização regular de indicadores locais


- Nível 4:


  - Discussões transversais baseadas em dados


- Nível 5:


  - Aplicação de análises preditivas por equipes técnicas


- Nível 6:


  - Cultura analítica disseminada, com aprendizado contínuo

##### Amostragem

- Entrevistas com gestores e analistas; revisão de relatórios e dashboards utilizados nas áreas;
        observação de reuniões de decisão baseadas em dados; avaliação de materiais de
        capacitação digital

##### I.11.1.3 Questão: Em que grau a organização possui mecanismos estruturados para...
Em que grau a organização possui mecanismos estruturados para aprender com seus próprios dados
e experiências (feedbacks, lições aprendidas, análises pós-ação)?


<!-- pág. original: 371/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização não possui práticas formais de feedback; aprendizado são informa e não documentado. |
| 1 | Há iniciativas pontuais de coleta de feedback, mas sem estrutura de registro ou análise sistemática. |
| 2 | Feedbacks são registrados digitalmente, porém não são utilizados para aprendizado organizacional. |
| 3 | As equipes realizam revisões estruturadas e compartilham feedbacks para ajustes locais de processos. |
| 4 | A organização analisa dados de desempenho e dissemina lições aprendidas entre áreas e níveis. |
| 5 | Os ciclos de feedback são baseados em análises preditivas, permitindo antecipar falhas e oportunidades. |
| 6 | A organização aprende continuamente com feedbacks automatizados e análises em tempo real, promovendo melhoria autônoma e colaborativa. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de lições aprendidas e planos de ação.

- Registros de reuniões de análise crítica e auditorias internas.

- Sistemas digitais de feedback e gestão do conhecimento.

- Indicadores de performance vinculados a melhorias contínuas.

##### Métricas/KPIs

- Percentual de planos de ação derivados de feedbacks concluídos.

- Frequência de revisões de desempenho baseadas em dados.

- Taxa de reincidência de falhas após aplicação de feedback.


<!-- pág. original: 372/465 -->
- Tempo médio entre ocorrência e ação corretiva.

##### Sinais por nível

- Nível 0:


  - Ausência de documentação e análise formal


- Nível 1:


  - Feedback informal e não estruturado


- Nível 2:


  - Registro digital de feedback sem uso analítico


- Nível 3:


  - Revisões locais com base em dados operacionais


- Nível 4:


  - Disseminação transversal de lições aprendidas


- Nível 5:


  - Análises preditivas orientando planos de ação


- Nível 6:


  - Aprendizado organizacional em tempo real e automatizado

##### Amostragem

- Entrevistas com gestores e equipes sobre práticas de feedback; análise de relatórios de
        auditoria e de melhoria contínua; observação de reuniões de análise crítica; avaliação de
        sistemas de gestão do conhecimento


<!-- pág. original: 373/465 -->
##### I.11.1.4 Questão: Como a organização assegura a transparência, a ética e a confiança no...
Como a organização assegura a transparência, a ética e a confiança no uso de dados para apoiar
decisões e orientar comportamentos?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há práticas formais de gestão ética de dados; inexistem políticas de privacidade ou transparência. |
| 1 | Existem políticas básicas de confidencialidade, mas sem mecanismos efetivos de auditoria ou monitoramento. |
| 2 | As políticas de ética e privacidade são documentadas e registradas em sistemas digitais, mas pouco aplicadas. |
| 3 | A conformidade ética e de segurança de dados é integrada aos processos e sistemas organizacionais. |
| 4 | Auditorias regulares e indicadores de conformidade garantem rastreabilidade e confiança no uso dos dados. |
| 5 | Mecanismos de monitoramento automatizado identificam riscos éticos e de privacidade antes que causem impacto. |
| 6 | Sistemas e equipes atuam de forma colaborativa e autônoma para manter a integridade, transparência e confiança contínua no uso de dados. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Políticas de ética e governança de dados.

- Relatórios de auditoria e compliance digital.

- Registros de consentimento e controle de acesso.

- Logs de rastreabilidade de sistemas e decisões automatizadas.


<!-- pág. original: 374/465 -->
##### Métricas/KPIs

- Taxa de conformidade com políticas de privacidade (LGPD/GDPR).

- Número de incidentes de uso indevido de dados.

- Índice de confiança organizacional em sistemas de decisão.

- Percentual de decisões auditáveis e explicáveis.

##### Sinais por nível

- Nível 0:


  - Ausência de políticas de ética e privacidade


- Nível 1:


  - Políticas formais, mas sem aplicação prática


- Nível 2:


  - Documentação digital, sem acompanhamento efetivo


- Nível 3:


  - Integração da ética e segurança nos fluxos de trabalho


- Nível 4:


  - Auditorias e indicadores estruturados de conformidade


- Nível 5:


  - Monitoramento automatizado de riscos


- Nível 6:


<!-- pág. original: 375/465 -->
  - Sistemas e pessoas atuam de forma proativa e autônoma para garantir ética e confiança

##### Amostragem

- Entrevistas com equipes de compliance, TI e gestão de dados; análise de relatórios de
         auditoria e conformidade; verificação de logs e registros de acesso a dados; observação de
         processos de tomada de decisão automatizada

##### I.11.1.5 Questão: Em que medida a organização é capaz de adaptar processos, estratégias...
Em que medida a organização é capaz de adaptar processos, estratégias e decisões com base em
aprendizados gerados por análises e insights de dados?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização reage de forma lenta às mudanças e não utiliza dados para adaptar seus processos. |
| 1 | Existem iniciativas isoladas de análise de dados, mas sem mecanismos estruturados de adaptação. |
| 2 | Sistemas digitais registram dados operacionais, porém a resposta organizacional é predominantemente reativa. |
| 3 | Dados e análises são usados para ajustar processos locais e otimizar a execução de atividades. |
| 4 | A organização utiliza análises e feedbacks para revisar estratégias e implementar melhorias contínuas. |
| 5 | Processos são ajustados de forma proativa com base em previsões e simulações apoiadas por IA. |
| 6 | A empresa opera com inteligência adaptativa, ajustando-se automaticamente a variações internas e externas em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de revisão e melhoria de processos baseados em dados.

- Registros de uso de sistemas de monitoramento em tempo real.

- Planos de ação e indicadores derivados de análises preditivas.

- Documentação de projetos de inovação orientados por dados.

##### Métricas/KPIs

- Tempo médio de resposta a mudanças críticas.

- Percentual de processos revisados com base em análises de dados.

- Taxa de sucesso em decisões adaptativas (ajustes proativos).

- Nível de integração entre sistemas de monitoramento e decisão.

##### Sinais por nível

- Nível 0:


  - Processos estáticos e reativos, sem uso de dados


- Nível 1:


  - Adoção incipiente de análise para ajustes pontuais


- Nível 2:


  - Uso de registros digitais sem ação sistemática


- Nível 3:


  - Ajustes locais sustentados por dashboards e relatórios


- Nível 4:


<!-- pág. original: 377/465 -->
  - Revisão periódica de estratégias com base em feedbacks e diagnósticos


- Nível 5:


  - Ajustes automáticos preditivos orientados por IA


- Nível 6:


  - Adaptação contínua em tempo real com aprendizado digital integrado

##### Amostragem

- Entrevistas com gestores e equipes sobre reações a mudanças; observação de ciclos de
        decisão baseados em dados; avaliação de logs e relatórios de automação adaptativa; revisão
        de planos estratégicos e indicadores de inovação
#### Glossário
[Sem glossário]
### I.12 Dimensão: Inteligência de Instalações (Facility)

#### I.12.1 Capacidade: Análise de dados automatizada
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Inteligência

- Dimensão: Inteligência de Instalações (Facility)

#### Resumo Descritivo
Refere-se à capacidade dos sistemas de informação de agregar dados continuamente para gerar
informações, extrair conhecimento e fornecer suporte às decisões dos usuários. Isso requer a
habilidade de identificar automaticamente relações de causa e efeito a partir de diversas fontes de
dados e prever eventos futuros por meio de simulações e outros métodos. A análise não se limita a
correlações conhecidas, mas também busca identificar novos padrões nos dados para promover um
aprendizado contínuo. Em estágios avançados, algoritmos de otimização integram os impactos de
eventos previstos (como uma falha) para gerar recomendações e ações de forma autônoma.
#### Questões
##### I.12.1.1 Questão: Como a empresa utiliza a análise automatizada de dados para gerar...
Como a empresa utiliza a análise automatizada de dados para gerar insights e dar suporte à tomada
de decisão?


<!-- pág. original: 379/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | As decisões são baseadas puramente na experiência e intuição dos colaboradores, sem qualquer uso de dados de processo ou operacionais para análise. |
| 1 | Os dados são coletados e armazenados em sistemas isolados, sendo utilizados para a criação de relatórios simples e pré-programados, sem capacidade de análise aprofundada. |
| 2 | Os dados de diferentes sistemas de TI e TO são consolidados, mas a análise ainda é realizada manualmente pelos colaboradores para identificar desvios e tendências. |
| 3 | A empresa utiliza painéis e dashboards que monitoram os processos em tempo real, permitindo a visualização do status atual (o que está acontecendo) e a identificação de desvios em relação a parâmetros predefinidos. |
| 4 | São utilizadas ferramentas de análise de dados para realizar diagnósticos e análises de causa raiz, permitindo à empresa compreender por que os eventos ocorrem (por que está acontecendo) e identificar correlações entre diferentes variáveis. |
| 5 | A empresa emprega modelos e algoritmos (ex machine learning) para analisar dados históricos e em tempo real, prevendo eventos futuros como falhas de equipamentos, problemas de qualidade ou variações na demanda (o que vai acontecer). |
| 6 | Os sistemas de TI são capazes não apenas de prever eventos futuros, mas também de executar decisões de forma autônoma ou fornecer recomendações otimizadas para adaptar os processos em tempo real, visando a auto-otimização. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios e Dashboards de BI: Verificar sistemas como ERP, MES, SCADA ou plataformas de
        Business Intelligence para painéis de monitoramento de KPIs em tempo real.
- Documentação de Ferramentas de Análise: Acessar a documentação de plataformas de data
        analytics, modelos de machine learning e algoritmos de simulação utilizados.
- Registros de Análise de Causa Raiz (RCA): Solicitar relatórios de análises de falhas ou
        problemas de qualidade para verificar se a causa foi identificada com base em dados.
- Sistema de Alertas Preditivos: Analisar logs e registros do sistema de manutenção preditiva
        para confirmar a emissão de alertas antes da ocorrência de falhas.
- Configuração de Regras de Decisão Autônoma: Inspecionar as configurações em sistemas
        (MES, sistemas de planejamento) que demonstrem a execução de ações automáticas
        baseadas em análises de dadosA) Artefatos e onde buscar.

##### Métricas/KPIs

- Eficiência Global dos Equipamentos (OEE): Melhorias no OEE podem indicar uma análise de
        dados mais eficaz para reduzir perdas.
- Tempo Médio Entre Falhas (MTBF): Um aumento no MTBF pode ser um indicador do sucesso
        da manutenção preditiva.
- Índice de Rendimento na Primeira Passagem (FPY): Aumento nos índices de qualidade pode
        ser resultado da predição e prevenção de defeitos.
- Redução de Paradas Não Planejadas: Quantificar a diminuição de paradas de máquinas como
        resultado de análises preditivas.
- Acuracidade das Previsões: Medir a precisão dos modelos preditivos (ex: previsão de
        demanda, previsão de falhas).

##### Sinais por nível

- Nível 0:


  - A equipe reage aos problemas (ex: quebra de máquina) apenas depois que eles ocorrem
  - A discussão sobre as causas é baseada em "achismos"


- Nível 1:


<!-- pág. original: 381/465 -->
  - A equipe reage aos problemas (ex: quebra de máquina) apenas depois que eles ocorrem
  - A discussão sobre as causas é baseada em "achismos"


- Nível 2:


  - Existem planilhas ou relatórios básicos que mostram dados de produção passados, mas a equipe leva tempo para cruzar informações e entender o que aconteceu


- Nível 3:


  - Telas e painéis na fábrica mostram em tempo real o status da produção e alertam visualmente quando um indicador (ex: velocidade da linha) sai do padrão


- Nível 4:


  - Diante de um problema de qualidade, a equipe utiliza ferramentas que analisam dados de processo de diversas fontes para apontar as prováveis causas, como a variação de um parâmetro específico


- Nível 5:


  - O sistema de manutenção envia uma ordem de serviço para inspecionar um motor, informando que há 85% de chance de ele falhar nas próximas 48 horas com base na análise de dados de vibração e temperatura


- Nível 6:


  - O sistema de planejamento, ao prever um possível atraso na entrega de um pedido devido a uma redução na eficiência de uma máquina, automaticamente reajusta a sequência de produção para minimizar o impacto, sem intervenção humana

##### Amostragem

- Amostragem Entrevistas: Conversar com gestores de produção, manutenção, qualidade e
       engenheiros de processo
- Perguntar como eles identificam a causa de um problema recorrente


<!-- pág. original: 382/465 -->
- Demonstração Prática: Pedir a um analista ou engenheiro que demonstre, usando as
          ferramentas da empresa, como um conjunto de dados brutos é transformado em uma
          informação acionável (ex: um insight para melhoria de processo)
- Análise de Caso: Selecionar uma parada de máquina ou um desvio de qualidade ocorrido
          recentemente e rastrear como o evento foi detectado, analisado, solucionado e se foram
          tomadas ações para prevenir sua recorrência com base em dados
- Observação: Acompanhar uma reunião de gerenciamento da produção (Shop Floor
          Management) para observar se as discussões e decisões são guiadas por dados apresentados
          em tempo real

##### I.12.1.2 Questão: Qual é a abrangência da análise automatizada de dados?
Qual é a abrangência da análise automatizada de dados?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Nenhuma análise de dados automatizada é realizada na empresa. |
| 1 | A análise automatizada é usada de forma isolada, focada em um único ativo, parâmetro ou processo (ex monitorar a vibração de um motor específico ou a contagem de peças de uma máquina). |
| 2 | A análise é usada para otimizar múltiplos processos ou áreas de forma independente (em silos), sem integração entre eles |
| 3 | A análise integra dados de múltiplos processos e sistemas dentro de um mesmo domínio funcional (ex integração de dados de todas as máquinas do shop floor para otimizar o fluxo de produção e identificar gargalos). |
| 4 | A análise integra dados de forma vertical, conectando o shop floor (TI/TO) com sistemas de gestão corporativa (Enterprise), como ERP ou SCM (ex: analisar como o OEE da produção impacta o custo financeiro do produto no ERP). |
| 5 | A análise integra dados verticalmente (fábrica + gestão) e horizontalmente, incluindo dados de parceiros externos (ex: fornecedores ou clientes) para otimizar processos (ex: prever como um atraso de matéria-prima impactará o OEE). |
| 6 | A análise de dados é holística e dinâmica, abrangendo todo o ecossistema (fornecedores, logística, produção, clientes, dados de mercado) para permitir a otimização e adaptação autônoma da cadeia de valor em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Mapas de Fluxo de Dados (Data Flow Diagrams): Verificar na documentação de TI como os
          dados fluem entre sistemas (ex: MES -> ERP -> SCM).
- Dashboards Gerenciais (BI): Analisar os dashboards de nível estratégico. Verificar se eles
          cruzam dados de produção (ex: OEE, sucata) com dados financeiros (ex: Custo por Unidade,
          margem) ou dados de vendas (ex: On-Time Delivery).
- Documentação de APIs e Integrações: Solicitar à equipe de TI os artefatos que comprovem a
          integração de dados entre sistemas internos (MES, ERP) e externos (portais de fornecedores,
          sistemas de logística).
- Relatórios de Custo do Produto: Verificar se os relatórios de custo utilizam dados de eficiência
          e consumo reais vindos automaticamente do chão de fábrica.

##### Métricas/KPIs

- Custo Total da Qualidade (Total Cost of Quality): Analisar se a métrica é calculada
          automaticamente integrando dados de sucata/retrabalho (MES) com custos de garantia (CRM)
          e custos de material (ERP).
- Giro de Estoque (Inventory Turnover): Um giro de estoque otimizado pode indicar uma boa
          integração entre a previsão de demanda (CRM/SCM) e o ritmo de produção (MES).
- Acuracidade da Previsão de Demanda (Demand Forecast Accuracy): Verificar se a previsão de
          vendas é ajustada automaticamente com base na capacidade de produção real.
- On-Time In-Full (OTIF): Medir o OTIF como um indicador da integração entre planejamento,
          produção e logística.

##### Sinais por nível

- Nível 0:


  - Não há sistemas de análise de dados integrados


<!-- pág. original: 384/465 -->
  - Gerentes não conseguem visualizar dados consolidados de diferentes áreas

  - Decisões são tomadas sem visibilidade integrada do negócio


- Nível 1:


  - O supervisor de uma máquina só consegue ver os dados daquela máquina


- Nível 2:


  - O gerente de produção vê o OEE de todas as linhas em um painel, mas não sabe o custo financeiro de uma parada


- Nível 3:


  - O gerente da fábrica consegue ver em um dashboard qual linha está sendo o gargalo e como isso afeta o plano de produção geral do dia


- Nível 4:


  - O gerente financeiro (Controller) recebe um relatório que mostra como a queda de eficiência de 5% na Linha 3 aumentou o custo real do "Pedido X" em 2%


- Nível 5:


  - O sistema de compras dispara um alerta de risco, informando que a produção está 10% acima do planejado e que, se o fornecedor "Y" não adiantar a entrega, a linha irá parar em 48 horas


- Nível 6:


  - O sistema analisa a previsão de vendas, a capacidade real da fábrica e o custo de energia (variável), e sugere automaticamente um novo mix de produção para o próximo turno para maximizar a margem de lucro


<!-- pág. original: 385/465 -->
##### Amostragem

- Amostragem Entrevistas (Funções Cruzadas): Conversar com o Gerente de TI, Gerente de
          Produção e o Controller (Gerente Financeiro)
- Perguntas-chave: Para o Controller: "Como você sabe o custo real de um produto que acabou
          de ser fabricado? Você usa dados automáticos da fábrica para isso?" Para o Gerente de TI:
          "Me mostre o mapa de integração de dados
- O MES fala com o ERP? E com o SCM?" Para o Gerente de Produção: "Quando um cliente
          liga para Vendas perguntando do pedido dele, o vendedor consegue saber em que pé está a
          produção em tempo real?"

##### I.12.1.3 Questão: Qual é a natureza dos sistemas de análise de dados?
Qual é a natureza dos sistemas de análise de dados?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Nenhuma análise é realizada; os processos são executados com base na intuição e experiência. |
| 1 | A análise é 100% manual. Os dados são exportados (ex: CSV) e analisados manualmente em ferramentas de planilha (ex: Excel). |
| 2 | A análise é automatizada, mas limitada a regras fixas e pré-programadas (ex: scripts SQL, relatórios de BI) para exibir dados históricos ou em tempo real (ex: "mostrar todas as paradas > 5 min"). |
| 3 | Os sistemas aplicam regras de diagnóstico complexas (árvores de decisão, expert systems) que foram definidas manualmente por especialistas para identificar causas conhecidas (ex: "Se Temp > 80 E Vibração > 5, ENTÃO Causa Provável = Falha no Rolamento"). |
| 4 | A empresa utiliza modelos preditivos (ex: regressão, forecasting) que são treinados por especialistas (ex: Cientistas de Dados) e depois implantados no sistema. O modelo é estático até ser manualmente retreinado. |
| 5 | A empresa utiliza ativamente técnicas de Machine Learning (ex: clustering, redes neurais) para descobrir novas correlações, anomalias e padrões nos dados que não eram previamente conhecidos pelos especialistas. |
| 6 | Os sistemas são adaptativos e utilizam autoaprendizado (ex: online learning, reinforcement learning), ajustando seus próprios modelos e algoritmos continuamente à medida que novos dados chegam, sem a necessidade de intervenção humana. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Repositórios de Código/Scripts: Verificar a existência de scripts SQL (Nível 2) vs. scripts de
          Python/R com bibliotecas de ML (ex: Scikit-learn, TensorFlow) (Nível 4/5).
- Documentação de Sistemas (MES/SCADA): Procurar por módulos de "Sistemas Especialistas"
          (Expert Systems) ou "Motores de Regras" (BRMS) (Nível 3).
- Documentação de Projetos de Ciência de Dados: Acessar notebooks (ex: Jupyter) ou relatórios
          de projetos de Data Science que detalhem o processo de "descoberta" (EDA) e modelagem
          (Nível 5).
- Plataformas de MLOps/Auto-ML: Verificar o uso de ferramentas que gerenciam o ciclo de vida
          de modelos, especialmente o retreinamento automático e monitoramento de model drift (Nível
          6).

##### Métricas/KPIs

- Taxa de Descoberta de Insights: Número de novas correlações de processo (causadoras de
          falhas ou melhorias) identificadas pelo sistema vs. por humanos.
- Acuracidade do Modelo (Model Accuracy/Precision/Recall): Verificar se essa métrica é
          monitorada e se há um processo de retreinamento.
- Velocidade de Adaptação do Modelo (Model Drift): Medir quanto tempo um modelo leva para se
          tornar obsoleto e com que frequência ele é atualizado (manual vs. automático).
- Número de Regras de Negócio Manuais vs. Modelos de ML em produção.

##### Sinais por nível

- Nível 0:


  - "Se a máquina quebra, eu chamo o operador mais antigo, ele sabe o que fazer"


<!-- pág. original: 387/465 -->
  - Não existem ferramentas de análise ou BI

  - Todas as decisões baseadas em experiência pessoal sem suporte de dados


- Nível 1:


  - "Se a máquina quebra, eu chamo o operador mais antigo, ele sabe o que fazer


- Nível 2:


  - "Eu tenho um dashboard que me mostra as paradas de ontem, aí eu investigo


- Nível 3:


  - "Nós programamos o sistema para alertar sempre que a pressão X e a temperatura Y saem da faixa que o engenheiro definiu


- Nível 4:


  - "Nossa equipe de dados criou um modelo que prevê o risco de parada

  - Ele é atualizado a cada 3 meses, quando eles rodam o treinamento de novo


- Nível 5:


  - "O sistema de IA analisou 6 meses de dados e descobriu que a maioria das nossas falhas de qualidade acontece 3 horas após a troca de turno, mas apenas quando usamos o material do Fornecedor B
  - Não sabíamos disso"6


- Nível 6:


  - "O algoritmo que otimiza o consumo de energia do forno se ajusta sozinho

  - Ele percebe a variação na umidade da matéria-prima e recalcula os parâmetros de queima em tempo real, sem ninguém pedir


<!-- pág. original: 388/465 -->
##### Amostragem

- Amostragem Entrevistas: Conversar com Engenheiros de Processo, Cientistas de Dados (se
          existirem), Gerentes de TI e Analistas de BI
- Perguntas-chave: "Quando vocês encontram um problema novo, quem define a 'regra' para o
          sistema detectar esse problema no futuro? O sistema aprende sozinho ou um especialista
          precisa programá-lo?" "Me mostre um exemplo de um insight ou correlação que o sistema
          descobriu sozinho, que a equipe de engenharia não conhecia
- " "Com que frequência os modelos preditivos são atualizados (retreinados)? Quem faz isso?"


##### I.12.1.4 Questão: Com que frequência e velocidade a análise de dados é executada e os...
Com que frequência e velocidade a análise de dados é executada e os resultados são disponibilizados
para a tomada de decisão?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A análise de dados não é realizada; as decisões são tomadas com base na percepção imediata do evento. |
| 1 | A análise é puramente manual e ad-hoc (sob demanda). A geração de um relatório ou insight pode levar dias ou semanas após a coleta dos dados. |
| 2 | A análise é automatizada, mas executada em lotes (batch) com baixa frequência (ex: diária, semanal ou mensal). As decisões são sempre baseadas em dados históricos (ex: D-1 ou S-1). |
| 3 | A análise é executada em intervalos frequentes (ex: a cada hora), permitindo uma visão "quase em tempo real" (near real-time) e a tomada de decisões táticas dentro de um mesmo turno ou dia de trabalho. |
| 4 | A análise é executada em tempo real (real-time). Os dados são processados e os insights (diagnósticos, alertas) são gerados em segundos após o evento, permitindo uma resposta humana imediata. |
| 5 | A análise em tempo real é usada para simular cenários futuros imediatos ou fornecer recomendações preditivas, permitindo que a equipe tome decisões proativas antes que um problema se agrave. |
| 6 | A análise em tempo real aciona diretamente ações corretivas ou adaptativas de forma autônoma (ciclo fechado ou closed-loop), muitas vezes sem necessidade de intervenção humana, eliminando a latência de decisão. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Arquitetura de Dados: Verificar se a arquitetura é baseada em data warehouse (geralmente
          batch, Nível 2) ou em plataformas de streaming de dados (ex: Kafka, Spark Streaming) (Nível
          4+).
- Agendadores de Tarefas (Schedulers): Verificar a frequência de execução de jobs de ETL
          (Extração, Transformação e Carga) ou de análise (ex: "rodar todo dia às 02:00" vs. "a cada 5
          minutos").
- Logs de Atualização de Dashboards: Verificar o timestamp da última atualização de dados nos
          painéis de BI e MES.
- Documentação de Arquitetura de Software: Procurar por termos como "processamento de
          eventos complexos" (CEP) ou "arquitetura orientada a eventos" (EDA), que indicam Nível 4+.

##### Métricas/KPIs

- Latência de Insight (Insight Latency): Tempo entre a ocorrência de um evento e a
          disponibilização da informação sobre ele.
- Latência de Análise (Analysis Latency): Tempo necessário para analisar os dados e entender a
          causa raiz do evento.
- Latência de Decisão (Decision Latency): Tempo para aprovar uma (contra)medida com base na
          análise.
- Tempo de Ciclo (Cycle Time) da Análise: O tempo total desde a captura do dado até a geração
          do insight.

##### Sinais por nível

- Nível 0:


  - "Quando a máquina para, eu vejo o problema e decido na hora o que fazer"


<!-- pág. original: 390/465 -->
  - Não há relatórios ou dashboards disponíveis

  - Pode levar semanas para saber o que aconteceu em um evento passado


- Nível 1:


  - "Ao final do mês, rodamos o relatório e vemos o que aconteceu


- Nível 2:


  - "Toda manhã, na reunião das 8h, olhamos o relatório da produção do dia anterior para definir as ações de hoje


- Nível 3:


  - "Eu atualizo o painel a cada hora para ver se estamos dentro da meta do turno


- Nível 4:


  - "O painel ficou vermelho 3 segundos depois que a máquina parou, e o operador já recebeu o alarme no tablet dele


- Nível 5:


  - "O sistema detectou uma vibração anômala e imediatamente simulou o impacto disso na ordem de produção, recomendando ao planejador uma troca de ferramenta na próxima parada programada


- Nível 6:


  - "O sistema detectou a variação na viscosidade do material e ajustou automaticamente a velocidade da linha para manter a qualidade do produto, sem que ninguém precisasse intervir

##### Amostragem

- Amostragem Observação Direta: Ficar ao lado de um operador ou supervisor e perguntar qual
       a data/hora dos dados que ele está vendo em seu painel de controle


<!-- pág. original: 391/465 -->
- Teste Prático: Forçar uma condição de parada (simulada ou real, se seguro) em um
        equipamento e cronometrar quanto tempo leva para o sistema de gerenciamento
        (MES/SCADA) refletir essa mudança
- Entrevistas (TI + Operações): Para TI: "Qual é a frequência de atualização dos nossos
        principais bancos de dados de produção? Os dados são processados em lote ou via
        streaming?" Para Operações: "Se uma meta de produção é perdida, quando você descobre?
        Agora, no final do turno, ou só amanhã?"
#### Glossário
[Sem glossário]
#### I.12.2 Capacidade: Entrega de informação contextualizada
#### Bloco/Pilar
- Bloco: Tecnologia

- Pilar: Inteligência

- Dimensão: Inteligência de Instalações (Facility)

#### Resumo Descritivo
A integração entre sistemas corporativos (Enterprise) e operacionais (Facility) é um elemento
essencial para alcançar inteligência organizacional distribuída. No contexto dos modelos catech e
SIRI, essa integração permite que dados fluam de forma contínua e contextualizada entre níveis
estratégicos e operacionais, viabilizando decisões mais rápidas e alinhadas. Sistemas interoperáveis
garantem coerência entre processos, eliminam redundâncias e possibilitam aprendizado
organizacional. À medida que a maturidade evolui, a comunicação entre plataformas deixa de ser
manual e passa a ocorrer de forma automatizada, inteligente, transformando dados isolados em
conhecimento compartilhado em tempo quase real.
#### Questões
##### I.12.2.1 Questão: Os sistemas de informação da organização conseguem disponibilizar...
Os sistemas de informação da organização conseguem disponibilizar automaticamente informações
relevantes e contextualizadas para apoiar decisões em diferentes níveis (operacional e corporativo)?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existe processo formal para entrega de informação; dados permanecem fragmentados, reativos e implícitos. |
| 1 | Há processos estruturados e formalizados para coleta e registro de dados, mas a contextualização ainda depende de esforço manual. |
| 2 | Dados são registrados em sistemas digitais; relatórios e dashboards fornecem visibilidade básica e transparência operacional. |
| 3 | Sistemas permitem integração local entre áreas; equipes autônomas utilizam métricas contextualizadas para análise e decisão em tempo quasi-real. |
| 4 | Informações são consolidadas e comparadas de forma transversal entre unidades (enterprise e facility), permitindo diagnósticos quantificáveis. |
| 5 | Algoritmos analisam dados e entregam insights preditivos de forma semiautomática, suportando decisões estratégicas. |
| 6 | O sistema opera de forma autodidata, fornecendo informações contextualizadas em tempo real, ajustando recomendações e ações de maneira autônoma. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de BI e dashboards corporativos.

- Logs e registros de sistemas ERP/MES.

- Documentação de integração de dados (APIs, Data Lakes, ETL).

- Relatórios de auditoria sobre governança de dados.

##### Métricas/KPIs

- Tempo médio para disponibilização de informações relevantes.

- Nível de integração entre sistemas (número de interfaces automatizadas vs. manuais).

- Percentual de decisões suportadas por insights de dados.

- Taxa de acurácia dos modelos de previsão.


<!-- pág. original: 394/465 -->
##### Sinais por nível

- Nível 0:


  - Relatórios isolados em planilhas, dependentes de conhecimento tácito


- Nível 1:


  - Procedimentos definidos para coleta de dados, mas sem automação


- Nível 2:


  - Relatórios digitais periódicos (mensais/semanal)


- Nível 3:


  - Dashboards locais em tempo quase real

  - uso de KPIs departamentais


- Nível 4:


  - Consolidação interdepartamental

  - comparações entre unidades


- Nível 5:


  - Modelos preditivos implementados e usados por gestores


- Nível 6:


  - Recomendação adaptativa em tempo real, decisões automatizadas ou semi automatizadas


<!-- pág. original: 395/465 -->
##### Amostragem

- Entrevistas com gestores de TI, analistas de dados e líderes de operação; amostra de
          relatórios históricos e dashboards recentes; demonstração prática de ferramentas de analytics
          utilizadas

##### I.12.2.2 Questão: Em que medida os sistemas de informação corporativos (Enterprise) e...
Em que medida os sistemas de informação corporativos (Enterprise) e operacionais (Facility) estão
integrados, permitindo o fluxo contínuo e contextualizado de dados entre diferentes níveis da
organização?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os sistemas corporativos e operacionais são isolados, sem integração formal; trocas de dados são manuais e pontuais. |
| 1 | Existem interfaces básicas entre alguns sistemas, porém com dependência de processos manuais e falta de padronização. |
| 2 | Fluxos de dados digitalizados, com integração parcial entre alguns sistemas e visibilidade limitada. |
| 3 | Integração local e automatizada entre sistemas operacionais e corporativos; dados consolidados para análise departamental. |
| 4 | Integração transversal entre unidades; dados corporativos e de produção consolidados em bases unificadas e analisáveis. |
| 5 | Integração com inteligência analítica, permitindo previsões baseadas em dados combinados de diferentes níveis. |
| 6 | Interoperabilidade total entre sistemas Enterprise e Facility, com fluxo de dados em tempo real e adaptação automática às mudanças operacionais. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Diagramas de arquitetura de sistemas e fluxos de dados.


<!-- pág. original: 396/465 -->
- Registros de integração (APIs, middleware, gateways IoT).

- Documentação de interoperabilidade (protocolos, padrões de dados).

- Relatórios de sincronização entre ERP, MES e sistemas de automação.

##### Métricas/KPIs

- Percentual de processos automatizados entre Enterprise e Facility.

- Tempo médio de atualização de dados entre sistemas.

- Número de integrações automáticas versus manuais.

- Taxa de consistência de dados entre níveis.

##### Sinais por nível

- Nível 0:


  - Sistemas isolados, sem comunicação direta


- Nível 1:


  - Integração ocasional via planilhas ou exportações manuais


- Nível 2:


  - Integração parcial e digitalizada em processos-chave


- Nível 3:


  - Sincronização automática entre alguns sistemas locais


- Nível 4:


  - Base de dados unificada e visibilidade interdepartamental


- Nível 5:


<!-- pág. original: 397/465 -->
  - Modelos analíticos e preditivos baseados em dados integrados


- Nível 6:


  - Sistema autodidata, capaz de ajustar fluxos de integração em tempo real

##### Amostragem

- Entrevistas com equipes de TI, automação e gestores de operação; análise documental de
          diagramas de sistemas; demonstração de painéis de integração em uso

##### I.12.2.3 Questão: Até que ponto a organização assegura a qualidade, a rastreabilidade e...
Até que ponto a organização assegura a qualidade, a rastreabilidade e a confiabilidade das
informações geradas e distribuídas por seus sistemas inteligentes?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há controle formal da qualidade e rastreabilidade das informações; dados são inconsistentes e não verificados. |
| 1 | Existem procedimentos básicos de verificação manual de dados, mas sem padronização organizacional. |
| 2 | Ferramentas digitais registram dados e logs, porém a validação ainda é parcial e reativa. |
| 3 | Sistemas corporativos e operacionais integram verificações automáticas e alertas locais de inconsistência. |
| 4 | Indicadores de qualidade e rastreabilidade são monitorados transversalmente, permitindo diagnóstico proativo de falhas. |
| 5 | Mecanismos analíticos e preditivos identificam anomalias e antecipam inconsistências de dados. |
| 6 | O sistema corrige automaticamente falhas de qualidade e rastreabilidade em tempo real, assegurando integridade contínua. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Registros de logs e trilhas de auditoria.

- Políticas de governança de dados e documentação de metadados.

- Relatórios de controle de qualidade da informação.

- Dashboards de monitoramento de integridade e consistência de dados.

##### Métricas/KPIs

- Percentual de inconsistências detectadas e corrigidas automaticamente.

- Taxa de integridade de dados entre sistemas.

- Tempo médio de detecção e correção de erros.

- Frequência de falhas de rastreabilidade em auditorias internas.

##### Sinais por nível

- Nível 0:


  - Dados inconsistentes, sem registros ou trilhas de auditoria.


- Nível 1:


  - Verificação manual de amostras de dados.


- Nível 2:


  - Logs digitais e relatórios de controle parcial.


- Nível 3:


  - Validação automatizada e alertas de inconsistência.


- Nível 4:


<!-- pág. original: 399/465 -->
  - Monitoramento contínuo e relatórios transversais de qualidade.


- Nível 5:


  - Previsão de anomalias e falhas de integridade.


- Nível 6:


  - Correção autônoma e aprendizado contínuo do sistema para prevenir reincidência.

##### Amostragem

- Entrevistas com gestores de TI e responsáveis por governança de dados; análise de registros
          de qualidade e relatórios de auditoria; avaliação prática de sistemas de monitoramento e
          alertas

##### I.12.2.4 Questão: Os sistemas de informação da organização utilizam análises avançadas...
Os sistemas de informação da organização utilizam análises avançadas (analytics, machine learning,
IA) para gerar insights preditivos e apoiar decisões antecipadas?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há uso estruturado de análises; decisões baseiam-se em experiência ou relatórios manuais. |
| 1 | Existem iniciativas pontuais de análise de dados, realizadas manualmente e sem padronização. |
| 2 | Ferramentas digitais produzem relatórios descritivos e visibilidade básica de indicadores. |
| 3 | Sistemas consolidados realizam análises automáticas e relatórios integrados em tempo quasi-real. |
| 4 | Modelos analíticos correlacionam variáveis e fornecem diagnósticos de desempenho organizacional. |
| 5 | Aplicação de técnicas de machine learning e IA para prever eventos, tendências e comportamentos. |
| 6 | Sistemas autodidatas ajustam parâmetros e decisões automaticamente em tempo real, baseados em análise contínua de dados. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios e dashboards analíticos.

- Documentação de uso de algoritmos e modelos de IA.

- Registros de scripts e pipelines de dados (ETL, Data Lake).

- Logs de previsão e análises automatizadas.

##### Métricas/KPIs

- Percentual de decisões suportadas por análises de dados.

- Precisão e acurácia dos modelos preditivos.

- Tempo de resposta entre coleta de dados e geração de insights.

- Redução de falhas ou custos baseada em análises preditivas.

##### Sinais por nível

- Nível 0:


  - Decisões empíricas, sem suporte analítico.


- Nível 1:


  - Relatórios manuais e planilhas simples.


- Nível 2:


  - Ferramentas digitais com relatórios descritivos.


- Nível 3:


<!-- pág. original: 401/465 -->
  - Dashboards automatizados com métricas integradas.


- Nível 4:


  - Modelos correlacionais e diagnósticos de causa e efeito.


- Nível 5:


  - Uso de algoritmos preditivos com resultados medidos.


- Nível 6:


  - Sistema autodidata, com predições e ajustes em tempo real.

##### Amostragem

- Entrevistas com analistas de dados, gestores de TI e operação; observação de uso de painéis
          analíticos; verificação de logs de execução de modelos preditivos; revisão de relatórios de
          melhoria baseados em previsões

##### I.12.2.5 Questão: Em que medida as equipes, em diferentes níveis, têm autonomia para...
Em que medida as equipes, em diferentes níveis, têm autonomia para acessar, interpretar e aplicar
informações contextualizadas fornecidas pelos sistemas inteligentes?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O acesso à informação é restrito e centralizado; decisões são tomadas sem base em dados ou suporte digital. |
| 1 | Existem regras formais de acesso à informação, mas o uso permanece limitado e dependente de níveis hierárquicos superiores. |
| 2 | Equipes possuem acesso digital a informações, porém o uso é majoritariamente reativo e individual. |
| 3 | Equipes locais utilizam dados em tempo quasi-real e aplicam análises contextuais em suas decisões cotidianas. |
| 4 | Há compartilhamento transversal de informações; equipes colaboram na análise de causas e soluções baseadas em dados. |
| 5 | Sistemas inteligentes recomendam ações, e equipes atuam proativamente com base em previsões e simulações. |
| 6 | As equipes e os sistemas aprendem mutuamente, operando de forma autônoma, colaborativa e em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Políticas de acesso à informação e perfis de usuário.

- Relatórios de auditoria de uso de dashboards e sistemas analíticos.

- Evidências de treinamentos e programas de capacitação digital.

- Registros de decisões operacionais descentralizadas.

##### Métricas/KPIs

- Percentual de decisões tomadas com base em informações digitais.

- Tempo médio de resposta entre evento e decisão local.

- Autonomia percebida pelos colaboradores.

- Número de usuários ativos em plataformas analíticas.

##### Sinais por nível

- Nível 0:


  - Acesso restrito; decisões baseadas em hierarquia.


- Nível 1:


<!-- pág. original: 403/465 -->
  - Acesso formalizado, porém centralizado.


- Nível 2:


  - Equipes acessam dados, mas sem contextualização ou iniciativa autônoma.


- Nível 3:


  - Uso regular de dados para decisões locais.


- Nível 4:


  - Colaboração transversal e compartilhamento de insights.


- Nível 5:


  - Ações preditivas e autonomia sustentada por IA.


- Nível 6:


  - Aprendizado contínuo entre sistemas e equipes, decisões adaptativas em tempo real.

##### Amostragem

- Entrevistas com líderes e operadores de diferentes áreas; observação de reuniões de decisão
        com base em dados; avaliação de logs de acesso e relatórios de uso de dashboards; análise
        de programas de capacitação digital
#### Glossário
[Sem glossário]
### I.13 Dimensão: Desenvolvimento e Aprendizado de Força de Trabalho

#### I.13.1 Capacidade: Desenvolvimento profissional contínuo
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Prontidão de Talentos

- Dimensão: Desenvolvimento e Aprendizado de Força de Trabalho

#### Resumo Descritivo
O desenvolvimento profissional contínuo representa a capacidade da organização de promover a
aprendizagem permanente e o aprimoramento constante das competências de seus colaboradores,
alinhando o crescimento individual às demandas estratégicas e tecnológicas da empresa. Nos níveis
iniciais de maturidade, o aprendizado ocorre de forma reativa, baseado em treinamentos pontuais ou
obrigatórios. Com o avanço da maturidade, o aprendizado se torna estruturado, digitalizado e
mensurável, apoiado por plataformas tecnológicas, planos de desenvolvimento personalizados e
indicadores de evolução de competências. Nos estágios mais avançados, o desenvolvimento
profissional contínuo é integrado estrategicamente à cultura. Ele é sustentado por sistemas
inteligentes de aprendizado adaptativo, que permitem requalificação em tempo real, mobilidade interna
de talentos e tomada de decisão baseada em dados sobre o desenvolvimento da força de trabalho.
Com isso , o desenvolvimento contínuo se torna um motor de inovação e resiliência organizacional,
fortalecendo tanto o engajamento dos colaboradores quanto a capacidade da empresa de se adaptar
às constantes mudanças tecnológicas e de mercado .
#### Questões
##### I.13.1.1 Questão: A organização possui um plano estratégico de desenvolvimento...
A organização possui um plano estratégico de desenvolvimento profissional alinhado aos objetivos de
negócio e às competências futuras requeridas?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O aprendizado ocorre de forma reativa, sem planejamento estruturado. |
| 1 | Existem planos de treinamento pontuais, sem alinhamento à estratégia organizacional. |
| 2 | O plano de aprendizado é registrado digitalmente, mas sem integração com objetivos estratégicos. |
| 3 | O planejamento do aprendizado é formalizado e alinhado aos objetivos corporativos e tecnológicos. |
| 4 | O desempenho dos programas de aprendizado é medido e ajustado com base em indicadores definidos. |
| 5 | Análises preditivas são utilizadas para antecipar necessidades de capacitação e adequar o plano de desenvolvimento. |
| 6 | O planejamento é dinâmico, automatizado e continuamente ajustado por meio de sistemas inteligentes integrados à estratégia empresarial. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Plano estratégico de aprendizado e desenvolvimento (ex: Plano Diretor de Capacitação, Mapas
          de Competências Estratégicas ).
- Mapas de competências e relatórios de lacunas.

- Registros de revisão e atualização do plano de capacitação.

- Relatórios de performance de programas de aprendizado.

- Ferramentas digitais de gestão de aprendizado (LMS, LXP).

##### Métricas/KPIs

- Percentual de competências críticas com planos de aprendizado associados.

- Taxa de atualização de programas de capacitação.

- ROI (Retorno sobre Investimento) de programas de desenvolvimento profissional.

- Alinhamento entre metas de aprendizado e indicadores de desempenho estratégico.

- Percentual de colaboradores com trilhas de desenvolvimento ativas.

##### Sinais por nível

- Nível 0:


<!-- pág. original: 213/465 -->
  - Ausência de plano ou alinhamento estratégico


- Nível 1:


  - Treinamentos isolados e reativos


- Nível 2:


  - Documentação digital básica sem integração


- Nível 3:


  - Planejamento integrado e formalizado


- Nível 4:


  - Monitoramento com indicadores de desempenho


- Nível 5:


  - Planejamento preditivo baseado em analytics


- Nível 6:


  - Estratégia adaptativa e automatizada de aprendizado contínuo

##### Amostragem

- Entrevistas com gestores de RH e liderança estratégica; revisão do plano de desenvolvimento
        e relatórios de execução; análise de dashboards e KPIs de aprendizado; verificação de
        integração entre sistemas corporativos e plataformas de aprendizado

##### I.13.1.2 Questão: O aprendizado é estruturado de forma personalizada e acessível a...
O aprendizado é estruturado de forma personalizada e acessível a todos os colaboradores ?


<!-- pág. original: 214/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O aprendizado é padronizado e restrito; não há diferenciação por perfil. |
| 1 | Existem programas de treinamento, mas sem adaptação individual. |
| 2 | Há trilhas digitais básicas, mas sem personalização ou acompanhamento. |
| 3 | O aprendizado é acessível e oferece conteúdos personalizados conforme cargo e necessidade. |
| 4 | Dados de desempenho e engajamento são usados para ajustar trilhas de aprendizado. |
| 5 | Modelos analíticos e IA recomendam conteúdos com base em necessidades e desempenho futuros. |
| 6 | O aprendizado é totalmente personalizado e ativamente adaptativo em tempo real, promovendo inclusão e eficiência contínua. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Plataformas de aprendizado digital (LMS/LXP).

- Registros de personalização e relatórios de engajamento.

- Políticas de inclusão e acessibilidade digital.

- Planos de desenvolvimento individual (PDIs).

- Dados de uso e satisfação dos colaboradores.

##### Métricas/KPIs

- Percentual de colaboradores com trilhas personalizadas.

- Índice de acessibilidade e inclusão digital.

- Taxa de engajamento em plataformas de aprendizado.

- Taxa de conclusão de trilhas e certificações.


<!-- pág. original: 215/465 -->
- Satisfação dos usuários com a experiência de aprendizado.

##### Sinais por nível

- Nível 0:


  - Aprendizado uniforme e restrito


- Nível 1:


  - Treinamentos básicos e presenciais


- Nível 2:


  - Uso de plataformas digitais simples


- Nível 3:


  - Trilhas adaptadas por perfil e cargo


- Nível 4:


  - Uso de dados de engajamento para ajustes


- Nível 5:


  - Recomendação preditiva e automatizada


- Nível 6:


  - Aprendizado inclusivo e inteligente em tempo real

##### Amostragem

- Amostragem Entrevistas com colaboradores de diferentes áreas e níveis hierárquicos; revisão
        de relatórios de acessibilidade e engajamento; avaliação técnica de plataformas digitais de
        aprendizado; análise de planos de desenvolvimento individuais (PDIs)


<!-- pág. original: 216/465 -->
##### I.13.1.3 Questão: A organização estimula a cultura de aprendizado contínuo,...
A organização estimula a cultura de aprendizado contínuo, reconhecendo e valorizando colaboradores
que buscam se desenvolver de forma proativa?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há incentivo ou reconhecimento ao aprendizado individual. |
| 1 | A cultura valoriza o aprendizado, mas sem práticas formais de estímulo. |
| 2 | Existem canais digitais de aprendizado, porém com baixa adesão e engajamento. |
| 3 | O aprendizado contínuo é incentivado e apoiado por políticas e programas institucionais. |
| 4 | Há acompanhamento de engajamento e reconhecimento de práticas de autodesenvolvimento. |
| 5 | Dados e analytics são usados para prever níveis de engajamento e ajustar ações de incentivo. |
| 6 | A cultura é auto-sustentada, com aprendizado digital integrado e engajamento contínuo baseado em dados e feedbacks em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Políticas de desenvolvimento de pessoas e cultura organizacional.

- Relatórios de participação em programas voluntários de aprendizado.

- Plataformas digitais de engajamento e gamificação.

- Registros de reconhecimento e recompensas ligadas ao aprendizado.

- Pesquisas de clima e engajamento.

##### Métricas/KPIs

- Taxa de participação e conclusão voluntária em programas de aprendizado.

- Índice de engajamento digital (acessos, horas dedicadas, certificações).


<!-- pág. original: 217/465 -->
- Percentual de colaboradores com PDIs ativos.

- Nível de satisfação com programas de desenvolvimento.

- Taxa de retenção de talentos engajados em aprendizado contínuo.

##### Sinais por nível

- Nível 0:


  - Falta de incentivo ao aprendizado


- Nível 1:


  - Reconhecimento informal e esporádico


- Nível 2:


  - Plataformas digitais pouco utilizadas


- Nível 3:


  - Programas estruturados de incentivo


- Nível 4:


  - Monitoramento ativo do engajamento


- Nível 5:


  - Previsão de padrões de engajamento


- Nível 6:


  - Cultura integrada e auto regulada de aprendizado


<!-- pág. original: 218/465 -->
##### Amostragem

- Amostragem Entrevistas com colaboradores e líderes sobre práticas de incentivo ao
          aprendizado; observação de programas de reconhecimento e campanhas internas; revisão de
          dados de engajamento em plataformas digitais; análise de relatórios de clima e cultura
          organizacional

##### I.13.1.4 Questão: Os sistemas de aprendizado (LMS, LXP, HRIS) estão integrados a outros...
Os sistemas de aprendizado (LMS, LXP, HRIS) estão integrados a outros sistemas corporativos ?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os processos de aprendizado são manuais, sem uso de sistemas digitais. |
| 1 | Existem ferramentas digitais isoladas, sem integração entre si. |
| 2 | O aprendizado é registrado em plataformas digitais, mas sem integração com sistemas corporativos. |
| 3 | Os sistemas de aprendizado e RH estão parcialmente integrados, permitindo acompanhamento básico de competências. |
| 4 | O aprendizado é monitorado digitalmente por indicadores e relatórios integrados. |
| 5 | Análises preditivas e IA são utilizadas para prever lacunas de competências e recomendar ações de capacitação. |
| 6 | O aprendizado é autônomo e em tempo real, com integração vertical (operacional) e horizontal (corporativa) total entre sistemas corporativos e plataformas de aprendizado, suportado por inteligência analítica. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Sistemas de gestão de aprendizado (LMS/LXP) e integração com HRIS, ERPs e sistemas de
          produção (MES).
- Relatórios de analytics e dashboards de competências.


<!-- pág. original: 219/465 -->
- Políticas de integração de dados de RH e aprendizado.

- Registros de atualização automática de trilhas de aprendizado.

- Documentação técnica de interoperabilidade entre plataformas.

##### Métricas/KPIs

- Percentual de integração entre sistemas de aprendizado e gestão.

- Taxa de automação de relatórios de desenvolvimento.

- Frequência de atualização de dados de competência.

- Precisão das recomendações de aprendizado digital.

- Tempo de resposta entre feedback e atualização de trilha.

##### Sinais por nível

- Nível 0:


  - Aprendizado manual e desconectado


- Nível 1:


  - Ferramentas isoladas e não interoperáveis


- Nível 2:


  - Registros digitais sem integração


- Nível 3:


  - Integração funcional básica entre plataformas


- Nível 4:


  - Monitoramento analítico centralizado


- Nível 5:


<!-- pág. original: 220/465 -->
  - Previsão de lacunas e recomendações automáticas


- Nível 6:


  - Integração inteligente e adaptativa em tempo real

##### Amostragem

- Entrevistas com equipes de RH, TI e treinamento; revisão de relatórios e dashboards de
          aprendizado; avaliação técnica de integração entre sistemas digitais; verificação de políticas e
          fluxos de dados de aprendizado

##### I.13.1.5 Questão: O progresso e o impacto do aprendizado são medidos sistematicamente...
O progresso e o impacto do aprendizado são medidos sistematicamente por indicadores, dashboards
e relatórios de desempenho?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há mensuração formal de competências ou resultados de aprendizado. |
| 1 | A avaliação de aprendizado ocorre de forma esporádica e qualitativa. |
| 2 | Alguns dados de desempenho são registrados digitalmente, mas sem integração com planos de aprendizado. |
| 3 | A mensuração de competências é estruturada e conectada aos programas de desenvolvimento. |
| 4 | Indicadores e dashboards são utilizados para monitorar o impacto do aprendizado. |
| 5 | Dados analíticos e IA são aplicados para prever lacunas de competências e otimizar proativamente investimentos em capacitação. |
| 6 | O sistema de mensuração é automatizado, inteligente e em tempo real, permitindo ajustes dinâmicos e aprendizado adaptativo. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de desempenho de aprendizado e avaliação pós-treinamento.

- Dashboards de competências e KPIs de desenvolvimento.

- Políticas de avaliação e feedback contínuo.

- Registros em plataformas LMS/LXP integradas a RH.

- Relatórios de auditorias de aprendizado e performance.

##### Métricas/KPIs

- Percentual de colaboradores com competências avaliadas periodicamente.

- Índice de evolução de competências críticas.

- ROI de programas de aprendizado.

- Taxa de conclusão e retenção de aprendizado.

- Tempo médio de resposta entre lacuna identificada e ação corretiva.

##### Sinais por nível

- Nível 0:


  - Ausência de indicadores ou registros de aprendizado


- Nível 1:


  - Avaliações pontuais e subjetivas


- Nível 2:


  - Registros digitais sem integração


- Nível 3:


  - Sistema estruturado de avaliação por competências


<!-- pág. original: 222/465 -->
- Nível 4:


  - Uso de KPIs e dashboards integrados


- Nível 5:


  - Análises preditivas de lacunas e impacto


- Nível 6:


  - Monitoramento contínuo e aprendizado adaptativo automatizado

##### Amostragem

- Entrevistas com gestores de RH, treinamento e líderes operacionais; revisão de dashboards e
          relatórios analíticos; observação de processos de feedback e avaliação de desempenho;
          análise de planos de ação derivados de lacunas de competência

##### I.13.1.6 Questão: A organização possui programas estruturados de requalificação e...
A organização possui programas estruturados de requalificação e aperfeiçoamento contínuo ?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existem programas formais de requalificação ou atualização profissional. |
| 1 | Existem iniciativas de capacitação pontuais e reativas, sem estrutura definida. |
| 2 | A organização possui registros digitais de treinamentos, mas sem plano de requalificação contínuo. |
| 3 | Há programas estruturados de requalificação e aperfeiçoamento alinhados à estratégia organizacional. |
| 4 | Os programas são acompanhados por indicadores e revisados com base em resultados e demandas de negócio. |
| 5 | Dados e analytics são utilizados para prever lacunas de competências e antecipar ações de requalificação. |
| 6 | A requalificação é dinâmica, personalizada e automatizada, com atualização contínua em tempo real e integração plena à estratégia digital da organização. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Planos de desenvolvimento de competências e relatórios de RH.

- Catálogos e trilhas de aprendizado de requalificação digital.

- Registros de capacitação em plataformas LMS ou LXP.

- Indicadores de reskilling/upskilling nos relatórios de desempenho.

- Políticas corporativas de desenvolvimento de talentos.

##### Métricas/KPIs

- Percentual de colaboradores requalificados em novas tecnologias.

- Taxa de participação em programas de upskilling digital.

- Percentual de lacunas de competências reduzidas.

- ROI de programas de requalificação.

- Tempo médio para requalificação de funções críticas.

##### Sinais por nível

- Nível 0:


  - Ausência de programas de requalificação


- Nível 1:


  - Ações pontuais sem metodologia definida


<!-- pág. original: 224/465 -->
- Nível 2:


  - Registros digitais sem correlação com o desempenho ou avaliação de resultados


- Nível 3:


  - Programas formais e alinhados à estratégia de negócio


- Nível 4:


  - Monitoramento de indicadores e avaliação de impacto


- Nível 5:


  - Uso de analytics e IA para antecipar necessidades


- Nível 6:


  - Requalificação contínua e automatizada com aprendizado adaptativo

##### Amostragem

- Entrevistas com gestores de RH, líderes técnicos e colaboradores; revisão documental de
         programas e políticas de requalificação; análise de dados de participação e resultados em
         plataformas digitais; avaliação de relatórios de impacto e ROI de aprendizado

##### I.13.1.7 Questão: Os líderes incentivam, acompanham e servem de modelo no processo de...
Os líderes incentivam, acompanham e servem de modelo no processo de aprendizado contínuo de
suas equipes?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os líderes não incentivam nem acompanham o aprendizado das equipes. |
| 1 | O incentivo ao aprendizado é eventual e depende da iniciativa individual do líder. |
| 2 | Há registros de atividades de aprendizado, mas a liderança tem envolvimento limitado. |
| 3 | Os líderes são formalmente cobrados por (ex: em suas metas) participar e incentivar ativamente o aprendizado contínuo das equipes. |
| 4 | O comportamento dos líderes é avaliado e monitorado com base em indicadores de aprendizado e engajamento. |
| 5 | Dados de desempenho e aprendizado são utilizados para ajustar práticas de liderança e identificar necessidades de desenvolvimento. |
| 6 | A liderança atua como mentora e catalisadora do aprendizado contínuo, utilizando feedbacks e análises em tempo real para fortalecer a cultura de desenvolvimento. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Programas de desenvolvimento de liderança com módulos específicos sobre mentoria,
         coaching e cultura de aprendizado.
- Relatórios de engajamento e acompanhamento de equipes.

- Indicadores de participação dos líderes em treinamentos e mentorias.

- Feedbacks de colaboradores em pesquisas de clima e cultura.

- Políticas e frameworks de gestão de desempenho e aprendizado.

##### Métricas/KPIs

- Percentual de líderes participantes de programas de aprendizado contínuo.

- Nível de engajamento das equipes em capacitação sob cada liderança.

- Taxa de feedbacks realizados e acompanhamentos de desenvolvimento.

- Índice de satisfação dos colaboradores com o apoio à aprendizagem.

- Avaliação de liderança orientada por aprendizado (learning leadership score).


<!-- pág. original: 226/465 -->
##### Sinais por nível

- Nível 0:


  - Ausência de estímulo ao aprendizado pela liderança


- Nível 1:


  - Incentivo ocasional e sem acompanhamento


- Nível 2:


  - Envolvimento passivo e registro digital básico


- Nível 3:


  - Participação ativa e sistemática dos líderes


- Nível 4:


  - Avaliação contínua da efetividade da liderança no aprendizado


- Nível 5:


  - Uso de dados e IA para fortalecer a atuação dos líderes


- Nível 6:


  - Liderança transformadora e digitalmente integrada ao ecossistema de aprendizado

##### Amostragem

- Amostragem Entrevistas com líderes e equipes sobre práticas de aprendizado; revisão de
        relatórios de engajamento e programas de capacitação; observação de sessões de feedback e
        acompanhamento de desenvolvimento; análise de métricas de liderança e aprendizado
        organizacional


<!-- pág. original: 227/465 -->
##### I.13.1.8 Questão: Existem políticas, papéis e processos definidos para governar o...
Existem políticas, papéis e processos definidos para governar o aprendizado contínuo e o
desenvolvimento de competências na organização?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existem políticas ou estruturas de governança para aprendizado. |
| 1 | Há iniciativas pontuais de aprendizado, mas sem diretrizes formais. |
| 2 | Políticas e papéis estão documentados digitalmente, mas sem integração ou revisão periódica. |
| 3 | A governança de aprendizado é formalizada e integrada à gestão de pessoas. |
| 4 | Indicadores e revisões periódicas avaliam a eficácia das políticas de aprendizado. |
| 5 | Modelos analíticos são utilizados para prever demandas e ajustar a governança. |
| 6 | A governança é adaptativa, inteligente e responsiva, com processos ajustados em tempo real e baseados em dados de aprendizado e desempenho. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Políticas e diretrizes corporativas de aprendizado e desenvolvimento, incluindo orçamento
          definido e papéis.
- Documentos de governança (comitês, papéis, fluxos decisórios).

- Registros de reuniões e atas de revisão de políticas.

- Relatórios de auditoria interna ou externa sobre programas de capacitação.

- Sistemas de gestão de governança (GRC, RH, LMS).

##### Métricas/KPIs

- Frequência de revisão de políticas de aprendizado.


<!-- pág. original: 228/465 -->
- Nível de conformidade com diretrizes e normas internas.

- Percentual de áreas cobertas por planos de desenvolvimento.

- Grau de envolvimento da liderança na governança de aprendizado.

- Tempo médio para atualização de políticas ou papéis.

##### Sinais por nível

- Nível 0:


  - Ausência total de política formal


- Nível 1:


  - Existência de ações isoladas sem controle


- Nível 2:


  - Políticas básicas e digitais, sem integração


- Nível 3:


  - Estrutura formal integrada ao RH


- Nível 4:


  - Indicadores de desempenho revisados periodicamente


- Nível 5:


  - Ajustes proativos com base em dados


- Nível 6:


  - Governança responsiva e automatizada


<!-- pág. original: 229/465 -->
##### Amostragem

- Amostragem Entrevistas com gestores de RH, compliance e desenvolvimento; revisão
          documental de políticas e organogramas de governança; observação de reuniões e processos
          decisórios sobre aprendizado; análise de registros e relatórios de auditoria

##### I.13.1.9 Questão: A organização mantém parcerias com instituições de ensino, centros de...
A organização mantém parcerias com instituições de ensino, centros de pesquisa ou outras empresas
para promover aprendizado colaborativo e inovação?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização não possui parcerias voltadas a aprendizado ou inovação. |
| 1 | Existem contatos informais ou pontuais com instituições externas. |
| 2 | Parcerias estão registradas digitalmente, mas sem integração com o plano estratégico. |
| 3 | Há parcerias formais e estruturadas com foco em capacitação e desenvolvimento conjunto. |
| 4 | Os resultados das parcerias são acompanhados e avaliados por indicadores de impacto. |
| 5 | Dados e analytics são usados para identificar e antecipar novas oportunidades de parceria. |
| 6 | A organização lidera ou participa ativamente de ecossistemas globais de aprendizado, com colaboração digital contínua e inovação em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Acordos de cooperação técnica com universidades e centros de pesquisa.

- Participação em hubs de inovação, clusters setoriais, MOOCs corporativos e programas
          governamentais de capacitação.
- Registros de participação em redes, consórcios ou clusters de inovação.

- Documentação de programas conjuntos de capacitação ou P&D.


<!-- pág. original: 230/465 -->
- Relatórios de resultados e métricas de impacto de parcerias.

- Plataformas de aprendizado e colaboração externas (corporate academies, MOOCs, hubs).

##### Métricas/KPIs

- Número e diversidade de parcerias ativas.

- Percentual de projetos de inovação realizados em parceria.

- Taxa de transferência de conhecimento entre instituições.

- ROI de programas colaborativos de aprendizado.

- Índice de engajamento digital em ecossistemas externos.

##### Sinais por nível

- Nível 0:


  - Isolamento institucional

  - ausência de parcerias


- Nível 1:


  - Colaborações pontuais e informais


- Nível 2:


  - Registros digitais de acordos sem integração estratégica


- Nível 3:


  - Parcerias formalizadas com impacto em capacitação


- Nível 4:


  - Avaliação contínua e mensuração de resultados


- Nível 5:


<!-- pág. original: 231/465 -->
  - Uso de dados para otimizar e prever parcerias futuras


- Nível 6:


  - Atuação em ecossistema global e digital de aprendizado

##### Amostragem

- Amostragem Entrevistas com gestores de RH, inovação e P&D; revisão de acordos e relatórios
          de cooperação; análise de métricas de desempenho de programas colaborativos; avaliação de
          plataformas e repositórios de aprendizado compartilhado

##### I.13.1.10 Questão: A organização utiliza dados e inteligência artificial para...
A organização utiliza dados e inteligência artificial para identificar lacunas de competências,
recomendar trilhas de aprendizado e prever necessidades futuras?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O aprendizado não é orientado por dados ou análises sistemáticas. |
| 1 | São realizadas avaliações pontuais e qualitativas de desempenho e aprendizado. |
| 2 | Dados de aprendizado são registrados digitalmente, mas sem análise automatizada. |
| 3 | Os dados de desempenho e aprendizado são analisados para orientar decisões de capacitação. |
| 4 | Dashboards e relatórios analíticos são usados para medir lacunas e apoiar o planejamento de aprendizado. |
| 5 | IA e algoritmos analíticos são utilizados para prever necessidades futuras e recomendar trilhas personalizadas. |
| 6 | O aprendizado é autônomo e adaptativo, com IA ajustando conteúdos e planos de desenvolvimento em tempo real com base em dados comportamentais e organizacionais. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Dashboards e relatórios de analytics de aprendizado.

- Registros e relatórios de plataformas LMS, LXP e HRIS.

- Políticas e práticas de governança de dados de aprendizado.

- Sistemas de recomendação de trilhas e conteúdos baseados em IA.

- Documentação sobre modelos preditivos e algoritmos aplicados a RH.

##### Métricas/KPIs

- Percentual de decisões de aprendizado baseadas em dados.

- Grau de automação de recomendações de aprendizado.

- Taxa de precisão das previsões de lacunas de competência.

- Percentual de trilhas de aprendizado geradas/ajustadas autonomamente por IA.

- Tempo médio entre identificação de lacuna e ação corretiva.

- Nível de satisfação dos usuários com as recomendações personalizadas.

##### Sinais por nível

- Nível 0:


  - Nenhum uso de dados para aprendizado


- Nível 1:


  - Avaliações manuais e subjetivas


- Nível 2:


  - Registros digitais básicos


- Nível 3:


  - Uso de relatórios analíticos descritivos


<!-- pág. original: 233/465 -->
- Nível 4:


  - Monitoramento quantitativo com dashboards integrados


- Nível 5:


  - Modelagem preditiva e personalização via IA


- Nível 6:


  - Aprendizado autônomo e adaptativo em tempo real

##### Amostragem

- Amostragem Entrevistas com líderes de RH, TI e Analytics; revisão de sistemas e relatórios de
        inteligência de aprendizado; avaliação técnica dos algoritmos e mecanismos de recomendação;
        observação de processos de tomada de decisão baseados em dados
#### Glossário
[Sem glossário]
#### I.13.2 Capacidade: Reconhecer o valor dos erros
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Prontidão de Talentos

- Dimensão: Desenvolvimento e Aprendizado de Força de Trabalho

#### Resumo Descritivo
A capacidade de reconhecer o valor dos erros (Recognise the value of mistakes) reflete o grau de
maturidade cultural e de aprendizado organizacional frente à inovação, experimentação e
transformação digital. Uma cultura que reconhece o valor dos erros não os encara como falhas
individuais, mas como fontes de aprendizado coletivo e oportunidades de inovação. Isso é
especialmente relevante em contextos digitais e industriais complexos, onde a experimentação e a
adaptação são constantes. À medida que a maturidade aumenta, a organização passa de uma postura
punitiva e avessa ao risco para um ambiente seguro psicologicamente, transparente e orientado por
dados, no qual os erros são analisados, documentados e convertidos em conhecimento útil. Nos níveis


<!-- pág. original: 235/465 -->
mais altos, a organização torna-se autodidata , com processos sistematizados de reflexão, análise e
compartilhamento das lições aprendidas, fomentando inovação contínua e resiliência frente à
mudança. Essa capacidade sustenta o princípio da disposição à mudança definido pelo modelo
ACATECH, fortalecendo o alinhamento entre pessoas, processos e tecnologia — e criando as
condições culturais necessárias para a transformação digital sustentável. Este formulário detalhado é
um híbrido que utiliza a dimensão D13 (Workforce Learning & Development) do SIRI como âncora,
mas avalia a capacidade 'Reconhecer o valor dos erros' com a profundidade da área de 'Cultura' do
modelo acatech.
#### Questões
##### I.13.2.1 Questão: Em que medida os erros e falhas são analisados e utilizados como...
Em que medida os erros e falhas são analisados e utilizados como oportunidades de aprendizado
dentro da organização?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os erros são ignorados ou tratados apenas como falhas individuais. |
| 1 | Há reconhecimento informal dos erros, mas sem processos estruturados de análise ou aprendizado. |
| 2 | Alguns registros digitais de erros ou incidentes são mantidos, porém sem aplicação prática sistemática. |
| 3 | Os erros são analisados periodicamente e geram planos de ação ou revisões de processo. |
| 4 | Há mecanismos formais de coleta, análise e disseminação de lições aprendidas a partir de erros. |
| 5 | Dados históricos e análises de erros são utilizados para prever falhas e antecipar melhorias. |
| 6 | O sistema de aprendizado é contínuo e automatizado, com feedback em tempo real e atualização dinâmica de processos a partir dos erros detectados. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Artefatos e onde buscar Relatórios de não conformidades, incidentes e lições aprendidas.
        Registros de reuniões de post-mortem, retrospectivas ou after-action reviews. Planos de
        melhoria contínua e indicadores de eficácia de correções. Repositórios digitais de
        conhecimento organizacional. Documentos de políticas internas sobre gestão de erros e
        aprendizado.

##### Métricas/KPIs

- Métricas/KPIs Percentual de erros analisados versus ocorridos. Tempo médio entre ocorrência
        e ação corretiva. Número de melhorias implementadas a partir de falhas. Engajamento dos
        colaboradores em processos de aprendizado pós-incidente. Taxa de redução de reincidência
        de erros. Redução do Custo da Não-Qualidade (CNQ) melhoria no OEE (Overall Equipment
        Effectiveness) pela redução de paradas não planejadas.

##### Sinais por nível

- Nível 0:


  - Erros tratados com punição, sem aprendizado

  - Inexistência de registros ou discussões estruturadas


- Nível 1:


  - Discussões informais sobre erros, sem registro


- Nível 2:


  - Registros digitais isolados, sem retorno ao processo


- Nível 3:


  - Análises pontuais de causa e impacto com ações corretivas isoladas


- Nível 4:


  - Lições aprendidas documentadas e compartilhadas com indicadores de prevenção


<!-- pág. original: 237/465 -->
- Nível 5:


  - Análises preditivas e integração com dados históricos

  - Aprendizado integrado à gestão de riscos


- Nível 6:


  - Sistema adaptativo e aprendizado em tempo real

##### Amostragem

- Amostragem Selecionar 5–10 incidentes ou falhas relevantes (operacionais, de projeto ou de
          produto) ocorridos nos últimos 6 a 12 meses
- Verificar existência de registros, análises de causa e planos de melhoria

- Avaliar se as lições aprendidas foram compartilhadas entre áreas e se houve monitoramento de
          reincidência

##### I.13.2.2 Questão: Até que ponto os colaboradores se sentem seguros para relatar erros,...
Até que ponto os colaboradores se sentem seguros para relatar erros, propor melhorias e compartilhar
experiências sem receio de punição?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Há medo de punição e pouca abertura para diálogo sobre erros ou melhorias. |
| 1 | A liderança comunica abertura, mas na prática prevalece a aversão a erros e críticas. |
| 2 | Existem canais digitais de comunicação interna, mas pouco utilizados para feedback transparente. |
| 3 | Os colaboradores são encorajados a compartilhar experiências e aprendizados sem retaliação. |
| 4 | A organização mede o nível de segurança psicológica e adota planos de melhoria baseados em dados de clima e engajamento. |
| 5 | Análises de engajamento e clima organizacional são usadas para prever riscos de desconfiança e desmotivação. |
| 6 | A cultura é autorregulada; existe feedback contínuo, confiança mútua e transparência apoiada por sistemas digitais de comunicação e análise de sentimento em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Artefatos e onde buscar Pesquisas de clima e engajamento organizacional. Registros de
          feedbacks, comunicações internas e canais de denúncia. Políticas de cultura, diversidade e
          comportamento ético. Relatórios de gestão de pessoas e de liderança. Entrevistas e grupos
          focais sobre percepção de segurança psicológica.

##### Métricas/KPIs

- Métricas/KPIs Índice de segurança psicológica (em pesquisas internas). Taxa de engajamento
          e confiança em lideranças. Volume de feedbacks registrados por canal oficial. Taxa de retenção
          de talentos e rotatividade voluntária. Número de ideias ou melhorias propostas por
          colaboradores. Redução na taxa de rotatividade (turnover) Aumento no índice de inovação (nº
          de ideias/colaborador) Melhoria na pontuação de E-NPS (Employee Net Promoter Score).

##### Sinais por nível

- Nível 0:


  - Cultura punitiva e hierárquica


- Nível 1:


  - Discurso de abertura sem prática efetiva


- Nível 2:


  - Comunicação digital unidirecional


- Nível 3:


<!-- pág. original: 239/465 -->
  - Feedback e escuta ativa implantados


- Nível 4:


  - Avaliação sistemática de confiança e engajamento


- Nível 5:


  - Uso de analytics para prever rupturas culturais


- Nível 6:


  - Transparência e confiança mantidas de forma autônoma e contínua

##### Amostragem

- Amostragem Avaliar pesquisas de clima, engajamento e feedback 360º

- Realizar entrevistas com amostras representativas de equipes sobre percepções de segurança

- Revisar planos de ação de cultura e liderança baseados em resultados dessas pesquisas


##### I.13.2.3 Questão: Existem processos ou ferramentas digitais que registram, organizam e...
Existem processos ou ferramentas digitais que registram, organizam e disseminam lições aprendidas a
partir de erros ou incidentes?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O aprendizado ocorre de forma informal e não é registrado. |
| 1 | Existem tentativas pontuais de registrar lições aprendidas, sem padronização. |
| 2 | Algumas lições são documentadas em arquivos digitais, mas sem centralização ou controle de qualidade. |
| 3 | Há uma plataforma ou processo padronizado de registro e consulta de aprendizados. |
| 4 | O sistema de aprendizado possui métricas de uso, atualização e relevância. |
| 5 | Dados de aprendizado são analisados para identificar lacunas de conhecimento e direcionar capacitações. |
| 6 | O sistema de aprendizado é automatizado e integrado aos processos corporativos, atualizando-se continuamente com base em dados e feedbacks em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Artefatos e onde buscar Registros de lições aprendidas , knowledge bases e portais de
          aprendizado. Relatórios de atualização e uso de plataformas de conhecimento. Procedimentos
          internos de gestão de aprendizado e melhoria contínua. Logs de sistemas corporativos (LMS,
          LXP, ERP, intranet). Evidências de treinamentos ou workshops derivados de lições aprendidas.

##### Métricas/KPIs

- Métricas/KPIs Número de lições aprendidas registradas e validadas. Taxa de reutilização de
          aprendizados em novos projetos. Frequência de atualização da base de conhecimento.
          Percentual de acessos e consultas a registros de aprendizado. Correlação entre aprendizado
          registrado e redução de erros reincidentes. Redução do tempo de onboarding de novos
          funcionários Redução do tempo médio para resolução de problemas (MTTR) Padronização de
          melhores práticas entre turnos/plantas.

##### Sinais por nível

- Nível 0:


  - Conhecimento disperso e não documentado


- Nível 1:


  - Registros pontuais e desorganizados


- Nível 2:


<!-- pág. original: 241/465 -->
  - Arquivos digitais isolados


- Nível 3:


  - Processo formal de registro e compartilhamento


- Nível 4:


  - Indicadores e análises sobre uso e impacto


- Nível 5:


  - Analytics orientando novas capacitações


- Nível 6:


  - Sistema dinâmico e auto atualizável

##### Amostragem

- Amostragem Revisão de bases de dados de aprendizado

- Entrevistas com gestores de projetos e inovação

- Observação de práticas de documentação e compartilhamento

- Verificação da integração com sistemas de gestão corporativa


##### I.13.2.4 Questão: Como os líderes e gestores demonstram, na prática, comportamentos que...
Como os líderes e gestores demonstram, na prática, comportamentos que valorizam o aprendizado a
partir de erros?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A liderança não reconhece erros nem promove aprendizado aberto nas equipes. |
| 1 | Alguns líderes valorizam o aprendizado, mas sem práticas estruturadas de estímulo. |
| 2 | Existem treinamentos sobre liderança e aprendizado, mas sem integração à rotina de gestão. |
| 3 | Os líderes promovem reuniões de aprendizado e feedback regulares nas equipes. |
| 4 | O comportamento de aprendizado da liderança é monitorado e avaliado por indicadores de engajamento e desenvolvimento. |
| 5 | Dados analíticos e avaliações de clima são usados para prever necessidades de desenvolvimento de líderes. |
| 6 | A liderança é digitalmente empoderada, utiliza ferramentas de feedback contínuo e aprendizado personalizado, e sustenta uma cultura de aprendizado autônoma e colaborativa. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Artefatos e onde buscar Programas de formação e avaliação de líderes. Relatórios de
          desempenho e engajamento de equipes. Resultados de pesquisas de clima e feedback 360°.
          Registros de reuniões de feedback e aprendizado coletivo. Políticas de liderança e cultura
          organizacional.

##### Métricas/KPIs

- Métricas/KPIs Percentual de líderes treinados em cultura de aprendizado. Índice de
          engajamento das equipes por líder. Frequência de feedbacks estruturados. Nível de satisfação
          das equipes com a comunicação e suporte de líderes. Correlação entre liderança de
          aprendizado e desempenho operacional. Aumento na taxa de promoção interna. Correlação
          entre a avaliação do líder e a produtividade da equipe Redução do tempo para atingir metas da
          equipe.

##### Sinais por nível

- Nível 0:


  - Liderança autoritária, foco em controle e punição


- Nível 1:


<!-- pág. original: 243/465 -->
  - Incentivo informal ao aprendizado


- Nível 2:


  - Treinamentos de liderança sem integração prática


- Nível 3:


  - Reuniões e feedbacks regulares


- Nível 4:


  - Avaliação sistemática do papel do líder no aprendizado


- Nível 5:


  - Análise preditiva do desenvolvimento de líderes


- Nível 6:


  - Liderança adaptativa, digital e auto sustentada

##### Amostragem

- Amostragem Entrevistas com líderes e liderados

- Revisão de relatórios de desenvolvimento de liderança

- Observação de reuniões de feedback e retrospectivas

- Análise de dados de engajamento e rotatividade por equipe


##### I.13.2.5 Questão: De que forma a organização incentiva a experimentação e a inovação,...
De que forma a organização incentiva a experimentação e a inovação, ao mesmo tempo em que
gerencia riscos decorrentes de possíveis falhas?


<!-- pág. original: 244/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização evita riscos e desencoraja a experimentação. |
| 1 | Há espaço limitado para inovação, sem mecanismos de controle de risco. |
| 2 | Alguns processos de inovação são documentados digitalmente, mas sem acompanhamento sistemático de riscos. |
| 3 | Existem políticas de inovação e procedimentos básicos de análise de risco. |
| 4 | O gerenciamento de riscos é parte integrante dos processos de inovação e é monitorado com métricas específicas. |
| 5 | Dados analíticos e simulações são usados para prever impactos e orientar decisões de inovação. |
| 6 | O ambiente de inovação é autorregulado, com sistemas de aprendizado e mitigação de risco em tempo real, sustentado por inteligência analítica e governança digital. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Artefatos e onde buscar Políticas de inovação e gestão de riscos. Registros de testes,
          protótipos e pilotos realizados. Relatórios de análise de impacto e mitigação de riscos.
          Ferramentas digitais de gestão de projetos e risk dashboards. Planos de continuidade de
          negócios e aprendizado pós-projeto.

##### Métricas/KPIs

- Métricas/KPIs Número de projetos experimentais concluídos com sucesso. Taxa de inovação
          versus incidentes de risco. Percentual de mitigação de riscos detectados precocemente. Tempo
          médio entre detecção e correção de falhas em experimentos. Retorno sobre investimento em
          projetos de inovação controlada. Melhoria na taxa de sucesso de projetos (projetos entregues
          no prazo/orçamento) ROI de projetos de inovação, redução de custos de mitigação de riscos
          (ex: multas, perdas).

##### Sinais por nível

- Nível 0:


<!-- pág. original: 245/465 -->
  - Cultura avessa ao risco


- Nível 1:


  - Iniciativas isoladas de inovação, sem controle formal


- Nível 2:


  - Documentação parcial e dispersa


- Nível 3:


  - Políticas e processos básicos de risco e inovação


- Nível 4:


  - Monitoramento estruturado com indicadores


- Nível 5:


  - Previsão de riscos via analytics e simulações


- Nível 6:


  - Mitigação adaptativa e aprendizado contínuo em tempo real

##### Amostragem

- Amostragem Entrevistas com equipes de inovação, P&D e gestão de riscos

- Revisão de relatórios de projetos experimentais e testes

- Avaliação de ferramentas digitais de monitoramento de risco

- Observação de práticas de aprendizado pós-projeto


<!-- pág. original: 246/465 -->
##### I.13.2.6 Questão: O feedback sobre erros e resultados inesperados é utilizado...
O feedback sobre erros e resultados inesperados é utilizado sistematicamente para ajustar processos,
produtos e práticas organizacionais?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O feedback é esporádico e não gera ações de melhoria. |
| 1 | O feedback é aplicado informalmente e sem acompanhamento. |
| 2 | Existem registros digitais de feedback, mas sem integração com planos de ação. |
| 3 | O feedback é estruturado e utilizado para aprimorar processos e resultados. |
| 4 | O ciclo de feedback é monitorado por indicadores de desempenho e melhoria contínua. |
| 5 | Análises preditivas são usadas para prever falhas e orientar ações de melhoria. |
| 6 | O feedback é contínuo, automatizado e integrado aos sistemas de gestão, permitindo ajustes em tempo real com base em dados analíticos. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Artefatos e onde buscar Registros de reuniões de feedback e planos de ação. Relatórios de
          auditoria interna e de melhoria contínua. Indicadores de desempenho e dashboards analíticos.
          Ferramentas digitais de gestão de desempenho (OKRs, KPIs, sistemas de RH). Documentação
          de retrospectivas , after-action reviews e post-mortem analysis.

##### Métricas/KPIs

- Métricas/KPIs Percentual de feedbacks convertidos em planos de ação. Tempo médio de
          resposta a incidentes e melhorias. Taxa de reincidência de falhas. Índice de engajamento em
          processos de feedback. Nível de satisfação dos colaboradores com o processo de
          aprendizado. Aumento da produtividade (output/input). Melhoria nos índices de satisfação do
          cliente (CSAT/NPS) Redução do tempo de ciclo de processos.

##### Sinais por nível

- Nível 0:


<!-- pág. original: 247/465 -->
  - Feedback ausente ou punitivo


- Nível 1:


  - Feedback informal, não rastreável


- Nível 2:


  - Registros digitais isolados


- Nível 3:


  - Estrutura formal de ciclos de feedback


- Nível 4:


  - Monitoramento e indicadores ativos


- Nível 5:


  - Análise preditiva e ajustes antecipados


- Nível 6:


  - Feedback em tempo real, com aprendizado adaptativo automatizado

##### Amostragem

- Amostragem Entrevistas com líderes e equipes sobre práticas de feedback

- Revisão de registros de planos de ação e auditorias

- Observação de reuniões de retrospectiva

- Análise de dados de desempenho e dashboards de melhoria


<!-- pág. original: 248/465 -->
##### I.13.2.7 Questão: A organização utiliza ferramentas digitais e analíticas para...
A organização utiliza ferramentas digitais e analíticas para monitorar, registrar e gerar insights sobre
erros, incidentes e melhorias?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O aprendizado e a análise de desempenho não utilizam sistemas digitais. |
| 1 | Algumas ferramentas digitais são usadas isoladamente, sem integração. |
| 2 | Os dados de aprendizado são coletados digitalmente, mas sem análise sistemática. |
| 3 | Sistemas de aprendizado e gestão do conhecimento estão conectados a ferramentas corporativas. |
| 4 | Dados digitais são usados para avaliar desempenho, identificar lacunas e propor melhorias. |
| 5 | Algoritmos e análises preditivas orientam decisões sobre capacitação e desenvolvimento de talentos. |
| 6 | O aprendizado é digitalmente integrado e automatizado, com sistemas que se ajustam em tempo real às necessidades individuais e organizacionais. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Artefatos e onde buscar Plataformas de aprendizado (LMS, LXP, HRIS) e relatórios de uso.
          Dashboards de aprendizado e analytics. Registros de integração entre sistemas de RH,
          operação e treinamento. Políticas de governança de dados e interoperabilidade. Evidências de
          uso de IA e personalização de conteúdo.

##### Métricas/KPIs

- Métricas/KPIs Percentual de integração entre sistemas de aprendizado e gestão. Grau de
          automação dos relatórios de desempenho e capacitação. Tempo médio de atualização das
          trilhas de aprendizado. Precisão dos modelos preditivos de competência. Nível de
          personalização do conteúdo de aprendizado. Aumento da eficiência no uso de sistemas


<!-- pág. original: 249/465 -->
        (menos cliques/tempo por tarefa) ROI sobre investimentos em tecnologia de aprendizado
        (LMS/LXP). Redução de erros operacionais por falta de conhecimento.

##### Sinais por nível

- Nível 0:


  - Ausência de tecnologia no aprendizado


- Nível 1:


  - Ferramentas isoladas e desconectadas


- Nível 2:


  - Coleta digital sem uso analítico


- Nível 3:


  - Integração funcional entre plataformas


- Nível 4:


  - Diagnóstico e melhoria com base em dados


- Nível 5:


  - Decisões preditivas e personalização


- Nível 6:


  - Aprendizado autônomo e adaptativo em tempo real

##### Amostragem

- Amostragem Entrevistas com gestores de RH, TI e inovação

- Análise técnica das integrações entre plataformas digitais


<!-- pág. original: 250/465 -->
- Verificação de relatórios analíticos e dashboards de aprendizado

- Revisão de políticas e práticas de governança de dados


##### I.13.2.8 Questão: De que forma a organização estimula os colaboradores a experimentar...
De que forma a organização estimula os colaboradores a experimentar novas ideias, aceitando erros
como parte do processo de inovação?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização não incentiva a experimentação; erros são penalizados. |
| 1 | Há tolerância informal a erros, mas sem práticas de aprendizado estruturadas. |
| 2 | Algumas iniciativas de inovação e experimentação são registradas digitalmente, mas sem aprendizado sistemático. |
| 3 | A organização estimula a experimentação e reconhece o valor do erro como parte do aprendizado. |
| 4 | Existem processos formais para analisar e compartilhar aprendizados oriundos de erros e experimentos. |
| 5 | Dados e analytics são usados para prever riscos, avaliar hipóteses e ajustar experimentos com base em resultados. |
| 6 | A cultura de inovação é contínua e autodidata , com ciclos ágeis e feedback em tempo real que transformam erros em aprendizado estratégico. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Artefatos e onde buscar Políticas e valores organizacionais sobre inovação e aprendizado.
          Registros de programas de inovação, hackathons ou incubadoras internas. Relatórios de
          experimentação, prototipagem e gestão de ideias. Pesquisas de clima e engajamento sobre
          segurança psicológica. Planos de reconhecimento e comunicação de boas práticas.


<!-- pág. original: 251/465 -->
##### Métricas/KPIs

- Métricas/KPIs Número de experimentos ou projetos piloto realizados anualmente. Taxa de
        aproveitamento de ideias propostas por colaboradores. Percentual de aprendizados
        documentados a partir de falhas. Nível de engajamento em programas de inovação. Indicador
        de segurança psicológica e clima de aprendizado. Aumento da receita vinda de novos
        produtos/serviços Redução do ciclo de P&D (Time-to-Market). Aumento do portfólio de patentes
        ou inovações registradas.

##### Sinais por nível

- Nível 0:


  - Erros punidos

  - medo de propor ideias


- Nível 1:


  - Tolerância ocasional, sem processos de aprendizado


- Nível 2:


  - Iniciativas digitais isoladas de inovação


- Nível 3:


  - Incentivo ativo à experimentação e aprendizado com erros


- Nível 4:


  - Processos estruturados de análise de falhas e lições aprendidas


- Nível 5:


  - Uso de dados para prever resultados e aprimorar testes


- Nível 6:


<!-- pág. original: 252/465 -->
  - Inovação contínua com aprendizado adaptativo e coletivo

##### Amostragem

- Amostragem Selecionar 5 iniciativas de inovação ou protótipos recentes, incluindo projetos com
          falhas
- Verificar se houve registro, avaliação e comunicação dos resultados (positivos e negativos)

- Avaliar reconhecimento e aprendizagem derivada dos experimentos


##### I.13.2.9 Questão: As lições aprendidas com erros ou experimentos são compartilhadas...
As lições aprendidas com erros ou experimentos são compartilhadas entre equipes, áreas e unidades
da organização?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | As lições aprendidas não são documentadas nem compartilhadas. |
| 1 | O compartilhamento de aprendizados ocorre de forma informal e pontual entre colegas ou equipes. |
| 2 | Lições aprendidas são registradas digitalmente, mas o acesso e a disseminação são limitados. |
| 3 | A organização possui processos estruturados para registro e disseminação de lições aprendidas entre áreas. |
| 4 | O compartilhamento é sistemático, acompanhado de métricas e usado para prevenir falhas recorrentes. |
| 5 | Dados de aprendizado e erros alimentam sistemas analíticos que identificam padrões e antecipam riscos. |
| 6 | A disseminação do aprendizado é automatizada e em tempo real, com sistemas inteligentes que atualizam práticas e processos de forma dinâmica. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Artefatos e onde buscar Relatórios de lições aprendidas de projetos ou experimentos.
        Repositórios digitais de conhecimento (intranets, bases de dados de aprendizado). Registros
        de reuniões de pós-projeto e feedback. Planos de comunicação e aprendizado organizacional.
        Plataformas de gestão do conhecimento e colaboração (KM tools, SharePoint, Confluence).

##### Métricas/KPIs

- Métricas/KPIs Percentual de projetos com lições aprendidas documentadas. Número de
        acessos e reutilizações de registros de aprendizado. Índice de prevenção de erros recorrentes.
        Tempo médio entre o registro e a disseminação de uma lição. Nível de engajamento em
        comunidades de prática. Redução da duplicação de esforços/erros entre projetos. Aumento da
        velocidade de implementação de melhorias Melhoria na colaboração interdepartamental
        (medida por pesquisas internas).

##### Sinais por nível

- Nível 0:


  - Nenhum registro ou troca de conhecimento sobre erros

  - Inexistência de canais de comunicação sobre lições aprendidas


- Nível 1:


  - Compartilhamento verbal e informal


- Nível 2:


  - Registros digitais isolados e pouco utilizados


- Nível 3:


  - Processo formal de disseminação de lições aprendidas


- Nível 4:


  - Indicadores de uso e impacto das lições aprendidas


<!-- pág. original: 254/465 -->
- Nível 5:


  - Aprendizado preditivo com base em padrões analíticos


- Nível 6:


  - Disseminação automática e aprendizado organizacional em tempo real

##### Amostragem

- Amostragem Selecionar 5–8 projetos concluídos recentemente com erros ou ajustes
          documentados
- Verificar se as lições foram registradas, disseminadas e reutilizadas

- Observar repositórios, portais ou intranets para confirmar o compartilhamento e a atualização
          periódica

##### I.13.2.10 Questão: Em que medida a organização utiliza o aprendizado proveniente de...
Em que medida a organização utiliza o aprendizado proveniente de erros para antecipar mudanças,
ajustar estratégias e evoluir culturalmente?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | O aprendizado proveniente de erros não é analisado nem utilizado para ajustes organizacionais. |
| 1 | As lições aprendidas são discutidas pontualmente, mas sem impacto em decisões ou estratégias. |
| 2 | Registros de erros e aprendizados são documentados digitalmente, porém sem retroalimentação sistêmica. |
| 3 | O aprendizado é incorporado aos processos e políticas, gerando melhorias pontuais e ajustes de rotina. |
| 4 | Os aprendizados são medidos, avaliados e usados para ajustar estratégias e prevenir recorrências. |
| 5 | Dados de aprendizado e desempenho são analisados por sistemas inteligentes para antecipar mudanças e tendências. |
| 6 | A organização aprende e se ajusta em tempo real, evoluindo continuamente sua cultura, processos e estratégias com base em dados e feedbacks automatizados. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Artefatos e onde buscar Relatórios de lições aprendidas e planos de ação decorrentes de
          falhas. Registros de revisões estratégicas e ajustes baseados em aprendizado. Documentos de
          gestão da mudança organizacional. Dashboards de indicadores de aprendizado e
          desempenho. Evidências de uso de sistemas de análise preditiva e IA em processos de
          melhoria contínua.

##### Métricas/KPIs

- Métricas/KPIs Percentual de ajustes estratégicos resultantes de lições aprendidas. Tempo
          médio de resposta a eventos de erro ou falha. Índice de maturidade da cultura de aprendizado
          organizacional. Número de melhorias implementadas com base em dados de aprendizado.
          Taxa de inovação derivada de experimentação e feedback. Velocidade de adaptação a novas
          demandas de mercado. Aumento da agilidade organizacional (medida por frameworks como
          OKRs) Crescimento da participação de mercado (market share).

##### Sinais por nível

- Nível 0:


  - Erros ignorados ou ocultados


- Nível 1:


  - Discussões isoladas, sem efeito prático


- Nível 2:


<!-- pág. original: 256/465 -->
  - Registros digitais sem retroalimentação


- Nível 3:


  - Melhoria pontual de processos


- Nível 4:


  - Ações corretivas e ajustes estratégicos com base em indicadores


- Nível 5:


  - Uso de analytics para prever riscos e mudanças


- Nível 6:


  - Cultura evolutiva com aprendizado automatizado e contínuo

##### Amostragem

- Amostragem Selecionar 5 decisões ou revisões estratégicas originadas de aprendizados de
        erros
- Avaliar como os dados de desempenho e falhas influenciaram políticas e planos

- Verificar se há revisões periódicas de estratégia baseadas em insights de aprendizado

#### Glossário
[Sem glossário]
#### I.13.3 Capacidade: Prover competências digitais
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Prontidão de Talentos


<!-- pág. original: 258/465 -->
- Dimensão: Desenvolvimento e Aprendizado de Força de Trabalho

#### Resumo Descritivo
A capacidade de prover competências digitais é um elemento essencial para o desenvolvimento da
maturidade organizacional em indústrias e instituições que buscam a transformação digital. Nos
modelos ACATECH e SIRI, essa capacidade faz parte da dimensão organizacional que trata do
preparo da força de trabalho (Talent Readiness) e está relacionada à habilidade de planejar,
desenvolver e sustentar competências técnicas e comportamentais voltadas ao uso e gestão de
tecnologias digitais. O princípio de capacidade digital, na estrutura de recursos do modelo ACATECH,
enfatiza que a transformação digital não depende apenas de infraestrutura tecnológica, mas também
da qualificação contínua das pessoas e da incorporação de uma cultura de aprendizagem adaptativa.
A formação em competências digitais abrange tanto habilidades técnicas (como análise de dados,
automação, segurança cibernética, uso de IA e ferramentas colaborativas) quanto competências
cognitivas e sociais, como resolução de problemas, pensamento crítico e inovação. À medida que a
maturidade aumenta, a organização evolui de ações pontuais de capacitação para um ecossistema de
aprendizagem contínua e personalizada, baseado em plataformas digitais de treinamento, análise de
lacunas de competência e aprendizagem autoguiada. Nos níveis mais elevados, a força de trabalho
torna-se auto aprendente, multidisciplinar e digitalmente fluente, promovendo inovação e agilidade na
adoção de novas tecnologias.
#### Questões
##### I.13.3.1 Questão: Em que medida a organização identifica, registra e monitora as...
Em que medida a organização identifica, registra e monitora as competências digitais necessárias para
cada função ?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização não possui levantamento das competências digitais dos colaboradores. |
| 1 | Existem descrições de cargos e habilidades básicas, mas sem foco em competências digitais. |
| 2 | As competências digitais estão parcialmente registradas em sistemas de RH, sem atualização regular. |
| 3 | Há um processo formal de mapeamento de competências digitais, revisado periodicamente. |
| 4 | O diagnóstico é baseado em dados e métricas que identificam lacunas e orientam ações de capacitação. |
| 5 | Ferramentas analíticas antecipam necessidades futuras de competências e direcionam treinamentos personalizados. |
| 6 | O sistema de mapeamento é adaptativo, autônomo e se atualiza em tempo real com base em dados de desempenho e evolução tecnológica. . |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Banco de dados de competências do RH (sistemas LMS, HR Analytics, People Analytics).

- Relatórios de avaliação de desempenho digital.

- Planos de desenvolvimento individual (PDIs) e mapas de carreira.

- Registros de treinamentos e resultados de avaliações técnicas.

- Matrizes de Habilidades Digitais (Digital Skill Matrix) ou Inventário de Competências Digitais.

##### Métricas/KPIs

- Percentual de funções com competências digitais mapeadas.

- Frequência de atualização dos registros de competência.

- Taxa de fechamento de lacunas identificadas.

- Percentual de colaboradores com trilhas de desenvolvimento digital ativas.

##### Sinais por nível

- Nível 0:


  - Nenhum mapeamento formal de competências


- Nível 1:


  - Inventário de habilidades básicas sem foco digital


- Nível 2:


<!-- pág. original: 260/465 -->
  - Registros digitais parciais e não estruturados


- Nível 3:


  - Processo formal e documentado de diagnóstico


- Nível 4:


  - Lacunas e indicadores de competência são mensurados e usados para decisões


- Nível 5:


  - Diagnóstico automatizado e preditivo com base em dados analíticos


- Nível 6:


  - Atualização contínua e autônoma dos perfis de competência digital

##### Amostragem

- Entrevistas com gestores de RH, líderes de área e colaboradores; análise de registros em
          sistemas de gestão de talentos; observação de práticas de avaliação de desempenho e
          feedback; revisão de relatórios de auditoria interna de competências

##### I.13.3.2 Questão: Até que ponto o planejamento de desenvolvimento da força de trabalho...
Até que ponto o planejamento de desenvolvimento da força de trabalho está alinhado às necessidades
da transformação digital e às mudanças tecnológicas emergentes?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há planejamento estruturado de desenvolvimento de talentos digitais. |
| 1 | Existem planos de capacitação pontuais, sem alinhamento com a estratégia digital. |
| 2 | O planejamento está documentado em sistemas digitais, mas o alinhamento com as metas tecnológicas é reativo ou limitado. |
| 3 | O plano de desenvolvimento de talentos é formalmente alinhado à estratégia digital da organização. |
| 4 | O planejamento baseia-se em métricas de desempenho e learning analytics, permitindo ajustes proativos e direcionados. |
| 5 | Ferramentas analíticas antecipam lacunas de talento e recomendam ações de capacitação. |
| 6 | O planejamento é dinâmico e ajusta automaticamente as iniciativas de capacitação conforme dados em tempo real e evolução tecnológica. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Plano estratégico de transformação digital.

- Documentos de gestão de talentos e relatórios de RH.

- Registros de orçamento e investimento em capacitação digital.

- Planos de sucessão e relatórios de avaliação de competências críticas.

- Relatórios de Projeção de Necessidades de Talentos

##### Métricas/KPIs

- Percentual de funções críticas com plano de desenvolvimento digital definido.

- Grau de alinhamento entre metas de capacitação e estratégia corporativa.

- Taxa de cumprimento dos planos de desenvolvimento.

- Tempo médio de resposta a novas necessidades tecnológicas.

##### Sinais por nível

- Nível 0:


<!-- pág. original: 262/465 -->
  - Ausência de plano formal de talentos


- Nível 1:


  - Planos pontuais, não conectados à estratégia digital


- Nível 2:


  - Registro digital de planos, sem integração estratégica


- Nível 3:


  - Planejamento formal alinhado às metas digitais


- Nível 4:


  - Uso de dados e indicadores para ajuste de planos


- Nível 5:


  - Planejamento preditivo com base em analytics e IA


- Nível 6:


  - Sistema adaptativo de gestão de talentos em tempo real

##### Amostragem

- Entrevistas com RH, liderança de inovação e áreas técnicas; análise de relatórios de revisão de
        competências e sucessão; verificação de integração entre plano de talentos e plano digital;
        observação de comitês de gestão de pessoas e tecnologia

##### I.13.3.3 Questão: Em que grau a organização implementa programas estruturados e...
Em que grau a organização implementa programas estruturados e contínuos de capacitação digital ?


<!-- pág. original: 263/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existem programas estruturados de capacitação digital. |
| 1 | Há treinamentos pontuais e presenciais, sem plano contínuo de capacitação. |
| 2 | Existem programas de treinamento com conteúdos digitais, mas sem acompanhamento sistemático. |
| 3 | Os programas de capacitação digital são contínuos e alinhados aos objetivos estratégicos da organização. |
| 4 | O desempenho e o progresso dos participantes são monitorados e utilizados para melhoria dos programas. |
| 5 | Ferramentas analíticas personalizam o aprendizado com base em dados de desempenho e perfil de cada colaborador. |
| 6 | O sistema de capacitação é autônomo e preditivo, ajustando em tempo real conteúdos e métodos conforme as necessidades individuais e os dados operacionais de desempenho . |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Registros e relatórios de programas de capacitação (RH, Treinamento e Desenvolvimento).

- Cronogramas e conteúdos de trilhas de aprendizado digital.

- Relatórios de desempenho e avaliação dos participantes.

- Sistemas LMS/LXP com indicadores de progresso e conclusão.

- Registros de certificações e feedbacks de aprendizagem.

##### Métricas/KPIs

- Percentual de colaboradores com participação ativa em programas digitais.

- Taxa de conclusão de trilhas de aprendizado.


<!-- pág. original: 264/465 -->
- Frequência de atualização dos conteúdos digitais.

- Índice de satisfação e aplicabilidade dos treinamentos.

- Impacto das capacitações em indicadores de desempenho organizacional.

##### Sinais por nível

- Nível 0:


  - Ausência de treinamentos estruturados


- Nível 1:


  - Treinamentos pontuais e reativos


- Nível 2:


  - Conteúdos digitais básicos, sem acompanhamento


- Nível 3:


  - Programas contínuos e integrados à estratégia


- Nível 4:


  - Monitoramento de desempenho e métricas de evolução


- Nível 5:


  - Aprendizado personalizado, analítico e preditivo


- Nível 6:


  - Aprendizado adaptativo e autônomo, com IA e feedback em tempo real


<!-- pág. original: 265/465 -->
##### Amostragem

- Entrevistas com gestores de RH, inovação e TI; análise de relatórios de plataformas de
          aprendizado (LMS, BI); observação de trilhas de capacitação em execução; verificação de
          políticas e planos de capacitação digital

##### I.13.3.4 Questão: Em que medida a organização utiliza plataformas digitais e...
Em que medida a organização utiliza plataformas digitais e tecnologias educacionais (como LMS, IA,
realidade virtual ou simuladores) ?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há uso de tecnologias digitais em programas de aprendizado. |
| 1 | Ferramentas digitais são utilizadas apenas para registro ou compartilhamento de materiais. |
| 2 | Existe uma plataforma básica de e-learning, com conteúdos disponíveis de forma estática. |
| 3 | O sistema de aprendizado digital é integrado à gestão de talentos e inclui acompanhamento de progresso. |
| 4 | A plataforma gera relatórios e indicadores de desempenho, permitindo análise de eficácia das capacitações. |
| 5 | Tecnologias como IA, Realidade Aumentada (RA) / Realidade Virtual (RV) ou simulações são usadas para personalizar o aprendizado . |
| 6 | O sistema de aprendizado é autônomo e inteligente, ajustando conteúdos e métodos em tempo real conforme o perfil e desempenho do colaborador. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios e dashboards do LMS ou LXP.

- Registros de uso de tecnologias imersivas (RA, RV, simulações).

- Logs de acesso e de conclusão de cursos.


<!-- pág. original: 266/465 -->
- Políticas e planos de adoção tecnológica em aprendizagem.

- Documentação técnica de ferramentas educacionais.

- Especificações técnicas de interoperabilidade entre LMS/LXP e MES/ERP

##### Métricas/KPIs

- Percentual de programas de capacitação suportados digitalmente.

- Taxa de engajamento e conclusão em plataformas digitais.

- Nível de automação de processos de aprendizado (inscrição, avaliação, feedback).

- Índice de personalização de conteúdos por perfil.

- Taxa de adoção de tecnologias emergentes em capacitação.

##### Sinais por nível

- Nível 0:


  - Ausência de tecnologias educacionais


- Nível 1:


  - Uso pontual de ferramentas digitais básicas


- Nível 2:


  - Sistema de e-learning simples, sem acompanhamento


- Nível 3:


  - Integração com RH e monitoramento de progresso


- Nível 4:


  - Relatórios e dashboards analíticos


- Nível 5:


<!-- pág. original: 267/465 -->
  - Personalização preditiva via IA e tecnologias imersivas


- Nível 6:


  - Aprendizado adaptativo em tempo real, com IA autônoma

##### Amostragem

- Entrevistas com RH, equipe de TI e instrutores; verificação direta do uso das plataformas
          digitais; revisão de relatórios de analytics das plataformas; observação de práticas de
          aprendizado imersivo e automatizado

##### I.13.3.5 Questão: Até que ponto a organização promove uma cultura de aprendizado...
Até que ponto a organização promove uma cultura de aprendizado contínuo, incentivando a
autonomia, a curiosidade e a experimentação digital entre os colaboradores?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização não promove iniciativas voltadas à cultura digital ou aprendizado contínuo. |
| 1 | Existem treinamentos obrigatórios, mas sem incentivo à autonomia ou inovação. |
| 2 | A organização oferece cursos e conteúdos digitais, mas o aprendizado é passivo e dirigido. |
| 3 | Há estímulo à aprendizagem contínua, com oportunidades estruturadas de desenvolvimento e feedback. |
| 4 | A cultura digital é ativamente promovida e mensurada por indicadores de engajamento e aprendizado. |
| 5 | A organização utiliza dados e IA para promover recomendações personalizadas de aprendizado e monitorar o engajamento individual. |
| 6 | O aprendizado é autônomo, colaborativo e sustentado por um ecossistema digital que se ajusta em tempo real às necessidades dos colaboradores e da organização. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Políticas e programas de cultura organizacional e transformação digital.

- Campanhas e materiais de comunicação interna sobre inovação e aprendizado.

- Registros de participação em comunidades de prática ou programas de mentoria.

- Dados de engajamento em plataformas digitais de aprendizado.

- Relatórios de feedback, enquetes internas e avaliações de clima organizacional.

- Programas de Reconhecimento e Recompensa por Inovação ou Aprendizado

##### Métricas/KPIs

- Índice de engajamento digital dos colaboradores.

- Percentual de participação voluntária em capacitações.

- Frequência de acesso a plataformas de aprendizado sob demanda.

- Nível de satisfação com a cultura de aprendizado.

- Correlação entre aprendizado autodirigido e desempenho organizacional.

##### Sinais por nível

- Nível 0:


  - Ausência de estímulo à aprendizagem


- Nível 1:


  - Treinamentos formais e obrigatórios, sem protagonismo do colaborador


- Nível 2:


  - Conteúdos digitais disponíveis, mas de uso passivo


- Nível 3:


  - Incentivo à aprendizagem contínua e feedback regular


<!-- pág. original: 269/465 -->
- Nível 4:


  - Mensuração e acompanhamento da cultura digital


- Nível 5:


  - Uso de dados e IA para recomendações personalizadas e integração do conhecimento em bases formais


- Nível 6:


  - Ecossistema autônomo de aprendizado colaborativo e adaptativo

##### Amostragem

- Entrevistas com colaboradores, gestores e RH; análise de relatórios de engajamento e
          indicadores de cultura; verificação do uso de plataformas digitais e fóruns colaborativos;
          observação de práticas de reconhecimento e incentivo ao aprendizado

##### I.13.3.6 Questão: Em que grau a organização mede o impacto dos programas de capacitação...
Em que grau a organização mede o impacto dos programas de capacitação digital, relacionando o
aprendizado ao desempenho, produtividade e resultados da transformação digital?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há avaliação formal das capacitações digitais realizadas. |
| 1 | A avaliação é baseada apenas em feedback de satisfação dos participantes. |
| 2 | Resultados são registrados digitalmente, mas sem análise sistemática de impacto. |
| 3 | Há processos formais para avaliar a eficácia das capacitações e identificar oportunidades de melhoria. |
| 4 | Indicadores e métricas de Learning Analytics são usados para correlacionar o aprendizado com o desempenho operacional e as metas organizacionais. |
| 5 | Ferramentas analíticas e preditivas identificam tendências de impacto e orientam a personalização dos programas. |
| 6 | O sistema de aprendizado fecha o ciclo de feedback e ajusta automaticamente conteúdos e estratégias de capacitação, em tempo real, com base em dados de impacto e desempenho prático. . |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de desempenho de capacitações e dashboards de RH.

- Indicadores de ROI e produtividade relacionados a programas de aprendizado.

- Relatórios de engajamento em plataformas de aprendizagem digital.

- Pesquisas de satisfação e eficácia pós-treinamento.

- Dados de desempenho operacional antes e depois das capacitações.

- Análise de regressão/correlação entre indicadores de L&D e KPIs de Produção/Qualidade.

##### Métricas/KPIs

- Taxa de conclusão de programas de capacitação digital.

- Grau de correlação entre aprendizado e resultados operacionais.

- Retorno sobre investimento (ROI) das capacitações digitais.

- Percentual de programas revisados com base em análise de impacto.

- Tempo médio de melhoria de desempenho pós-treinamento.

##### Sinais por nível

- Nível 0:


  - Ausência de avaliação


<!-- pág. original: 271/465 -->
- Nível 1:


  - Avaliação apenas de satisfação


- Nível 2:


  - Registros digitais sem análise


- Nível 3:


  - Avaliação formal e periódica com relatórios


- Nível 4:


  - Métricas relacionadas a indicadores de desempenho


- Nível 5:


  - Análises preditivas e personalização de programas


- Nível 6:


  - Aprendizado adaptativo com ajustes automáticos

##### Amostragem

- Entrevistas com gestores de RH e líderes de aprendizado; revisão de relatórios de indicadores
        de desempenho pós-capacitação; análise de dados extraídos de plataformas LMS/LXP;
        observação de práticas de feedback e revisão de programas

##### I.13.3.7 Questão: Até que ponto as competências digitais desenvolvidas são efetivamente...
Até que ponto as competências digitais desenvolvidas são efetivamente aplicadas nas rotinas
operacionais, de gestão e inovação da organização?


<!-- pág. original: 272/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | As capacitações digitais não possuem relação direta com as atividades práticas dos colaboradores. |
| 1 | Algumas competências digitais são aplicadas de forma pontual e sem acompanhamento sistemático. |
| 2 | Há registros digitais de aplicação prática, mas sem integração formal com a operação. |
| 3 | O aprendizado digital é planejado e formalmente integrado para apoiar atividades e processos operacionais específicos, sendo um requisito do cargo. |
| 4 | A aplicação prática das competências é monitorada e utilizada como indicador de desempenho e melhoria. |
| 5 | Dados operacionais e analíticos são usados para ajustar e otimizar programas de capacitação de forma contínua. |
| 6 | A integração é completa; o processo de aprendizado está embutido nos sistemas de execução operacional com feedback automático e ajuste contínuo das práticas. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de aplicação prática pós-capacitação.

- Indicadores de desempenho antes e depois da formação digital.

- Dados de integração entre sistemas de aprendizado (LMS) e sistemas operacionais (ERP,
         MES, IoT).
- Planos de desenvolvimento individual vinculados a metas operacionais.

- Registros de feedback de líderes e colaboradores sobre uso das competências em campo.


<!-- pág. original: 273/465 -->
##### Métricas/KPIs

- Percentual de competências aplicadas na rotina operacional.

- Índice de melhoria de produtividade pós-capacitação.

- Tempo médio de incorporação de novas práticas digitais.

- Número de processos otimizados a partir de aprendizado digital.

- Correlação entre aprendizado e redução de erros ou retrabalho.

##### Sinais por nível

- Nível 0:


  - Nenhuma aplicação prática das competências digitais


- Nível 1:


  - Uso pontual e informal de novas habilidades


- Nível 2:


  - Registros digitais isolados de aplicação


- Nível 3:


  - Alinhamento formal entre aprendizado e operação


- Nível 4:


  - Monitoramento sistemático de resultados práticos


- Nível 5:


  - Otimização algorítmica ou baseada em IA de programas de treinamento conforme dados operacionais


<!-- pág. original: 274/465 -->
- Nível 6:


  - Feedback em tempo real entre aprendizado e operação

##### Amostragem

- Entrevistas com gestores operacionais, RH e líderes técnicos; revisão de relatórios de
          integração de sistemas; observação em campo de práticas operacionais digitais; análise de
          métricas de desempenho pós-capacitação

##### I.13.3.8 Questão: Em que medida a organização utiliza dados e análises (learning...
Em que medida a organização utiliza dados e análises (learning analytics) para personalizar
treinamentos, prever lacunas de competência e ajustar seus programas de capacitação?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há coleta ou uso de dados para avaliar o aprendizado. |
| 1 | Dados básicos de participação ou satisfação são coletados, mas não analisados sistematicamente. |
| 2 | Dados de aprendizado são armazenados em sistemas digitais, porém usados apenas para registro. |
| 3 | Há análise regular de dados de aprendizado e desempenho, utilizada para revisão de programas. |
| 4 | Métricas e dashboards analíticos são empregados para identificar lacunas e direcionar capacitações. |
| 5 | Modelos analíticos e algoritmos preveem necessidades futuras de aprendizado e desempenho, suportando decisões proativas. |
| 6 | O sistema de aprendizado utiliza IA e automação para ajustar conteúdos, métodos e recomendações em tempo real, com base em dados individuais e coletivos. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de analytics de plataformas LMS ou LXP.

- Dashboards de desempenho e engajamento em aprendizado.

- Documentação de uso de algoritmos ou modelos preditivos.

- Registros de personalização automática de conteúdos.

- Planos de governança de dados de aprendizado e privacidade.

- Modelo de governança e ética de dados de aprendizado (Learning Data Governance)

##### Métricas/KPIs

- Percentual de decisões de aprendizado baseadas em dados.

- Tempo médio entre coleta de dados e ação corretiva no programa.

- Precisão das previsões de lacunas de competência.

- Grau de personalização dos conteúdos de treinamento.

- Engajamento e desempenho pós-personalização.

##### Sinais por nível

- Nível 0:


  - Ausência de coleta de dados


- Nível 1:


  - Coleta pontual, sem análise


- Nível 2:


  - Dados digitais armazenados, sem uso prático


- Nível 3:


  - Análise periódica e ajustes pontuais


<!-- pág. original: 276/465 -->
- Nível 4:


  - Dashboards e relatórios diagnósticos ativos


- Nível 5:


  - Previsões de aprendizado com base em IA


- Nível 6:


  - Personalização automática e aprendizado adaptativo

##### Amostragem

- Entrevistas com gestores de RH, TI e líderes de capacitação; revisão de relatórios de analytics
          e dashboards de aprendizado; verificação da existência de políticas de governança de dados
          educacionais; observação de recomendações automatizadas em plataformas de aprendizado

##### I.13.3.9 Questão: Até que ponto os colaboradores estão preparados para se adaptar a...
Até que ponto os colaboradores estão preparados para se adaptar a novas tecnologias, processos
digitais e mudanças contínuas no ambiente de trabalho?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os colaboradores resistem às mudanças tecnológicas e não há ações formais de adaptação digital. |
| 1 | Existem treinamentos pontuais para novas ferramentas, mas sem acompanhamento sistemático. |
| 2 | A organização oferece conteúdos digitais sobre novas tecnologias, sem planos estruturados de adaptação. |
| 3 | Há programas formais e contínuos de atualização e requalificação digital (reskilling/upskilling), vinculados a planos de sucessão e mudanças tecnológicas esperadas. |
| 4 | A resiliência digital é monitorada e avaliada por indicadores de engajamento e desempenho em contextos de mudança. |
| 5 | Ferramentas analíticas e dados de desempenho são usados para prever lacunas de adaptação e preparar respostas antecipadas. |
| 6 | A organização possui uma cultura de adaptabilidade intrínseca, em que os colaboradores modelam a mudança e o aprendizado contínuo é apoiado por sistemas inteligentes e processos orgânicos. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Programas de reskilling e upskilling registrados em RH.

- Relatórios de engajamento e desempenho em adoção tecnológica.

- Indicadores de participação em capacitações emergenciais.

- Políticas de mudança organizacional e suporte à inovação.

- Pesquisas internas sobre cultura e adaptação digital.

##### Métricas/KPIs

- Percentual de colaboradores requalificados em novas tecnologias.

- Tempo médio de adaptação a novas ferramentas ou processos.

- Índice de engajamento digital.

- Taxa de sucesso de implementações tecnológicas (adoção efetiva).

- Nível de prontidão digital por área ou função.

##### Sinais por nível

- Nível 0:


  - Resistência generalizada à mudança


<!-- pág. original: 278/465 -->
- Nível 1:


  - Treinamentos pontuais e reativos


- Nível 2:


  - Capacitações digitais básicas


- Nível 3:


  - Programas estruturados e regulares de atualização


- Nível 4:


  - Avaliação e métricas de adaptação


- Nível 5:


  - Ações preditivas com base em dados de engajamento


- Nível 6:


  - Cultura adaptativa e aprendizado contínuo automatizado

##### Amostragem

- Entrevistas com gestores de RH, inovação e líderes de equipe; revisão de relatórios de
        resiliência e readiness digital; análise de indicadores de adoção tecnológica; observação de
        práticas de aprendizado e colaboração digital

##### I.13.3.10 Questão: Em que grau a organização estabelece parcerias com instituições de...
Em que grau a organização estabelece parcerias com instituições de ensino, startups e fornecedores
para desenvolver competências digitais e promover inovação educacional?


<!-- pág. original: 279/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há parcerias ou ações externas relacionadas à capacitação digital. |
| 1 | Existem parcerias pontuais com instituições externas, sem integração formal. |
| 2 | As parcerias são registradas e gerenciadas digitalmente, mas com escopo limitado. |
| 3 | Há programas de capacitação desenvolvidos em colaboração com parceiros externos. |
| 4 | As parcerias são monitoradas por métricas de desempenho e resultados educacionais. |
| 5 | Dados e learning analytics são utilizados para identificar, avaliar e otimizar novas oportunidades de cooperação e a evolução do ecossistema. |
| 6 | A organização integra um ecossistema inteligente e interconectado, com aprendizado colaborativo em tempo real entre múltiplos agentes e troca fluida de dados de desempenho. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Contratos e memorandos de entendimento com universidades, startups e instituições de
         pesquisa.
- Registros de participação em redes de inovação e capacitação.

- Relatórios de resultados de programas desenvolvidos em parceria.

- Documentação de integração de plataformas e dados de aprendizado.

- Registros de eventos, hackathons, certificações e iniciativas conjuntas.

##### Métricas/KPIs

- Número de parcerias ativas voltadas à aprendizagem digital.

- Percentual de programas de capacitação desenvolvidos em parceria.

- Grau de interoperabilidade entre plataformas de parceiros.


<!-- pág. original: 280/465 -->
- Taxa de inovação educacional derivada de colaborações externas.

- Índice de satisfação ou impacto de programas conjuntos.

##### Sinais por nível

- Nível 0:


  - Ausência de parcerias educacionais


- Nível 1:


  - Colaborações isoladas e informais


- Nível 2:


  - Registros digitais de parcerias sem integração operacional


- Nível 3:


  - Programas colaborativos estruturados


- Nível 4:


  - Monitoramento e indicadores de impacto


- Nível 5:


  - Uso de dados para otimizar e expandir o ecossistema


- Nível 6:


  - Rede adaptativa e inteligente de aprendizado colaborativo


<!-- pág. original: 281/465 -->
##### Amostragem

- Entrevistas com gestores de RH, P&D e inovação; análise de relatórios de parcerias e acordos
        de cooperação; verificação de dados de plataformas compartilhadas; avaliação de projetos
        educacionais conjuntos e resultados obtidos
#### Glossário
[Sem glossário]
### I.14 Dimensão: Competência de Liderança

#### I.14.1 Capacidade: Abertura à inovação
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Competência de Liderança

#### Resumo Descritivo
Capacidade de liderança de demonstrar abertura à inovação, envolvendo a disposição para explorar,
testar e adotar novas tecnologias digitais, processos inovadores e modelos de negócio emergentes.
Inclui estabelecer uma cultura organizacional que valoriza experimentação sistemática, tolera erros
como aprendizado, investe em parcerias estratégicas para co-inovação (startups, universidades,
centros de pesquisa), e adapta continuamente a estratégia de inovação em resposta a mudanças
tecnológicas e de mercado.
#### Questões
##### I.14.1.1 Questão: Como a liderança e a organização demonstram abertura à inovação...
Como a liderança e a organização demonstram abertura à inovação através da exploração, teste e
adoção de novas tecnologias digitais e processos inovadores?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização não demonstra abertura para explorar novas tecnologias ou processos inovadores. Não há mecanismos formais para identificar tendências tecnológicas. |
| 1 | A liderança possui alguma consciência sobre tecnologias emergentes através de canais informais (eventos esporádicos, contatos pessoais), mas sem avaliação estruturada ou investimento dedicado. |
| 2 | A organização acompanha sistematicamente tendências tecnológicas através de canais formais (relatórios, benchmarks, associações), mas com limitada aplicação prática e raras experimentações. |
| 3 | A liderança desenvolve iniciativas pontuais de inovação com apoio de parceiros externos (consultores, fornecedores) para aplicações específicas. Há algum investimento em experimentação, mas ainda de forma dependente. |
| 4 | A organização realiza provas de conceito (POCs) e pilotos de forma independente em múltiplas áreas, com parcerias formalizadas (universidades, startups, centros de pesquisa) e orçamento dedicado. Cultura de experimentação estabelecida com processos de captura de aprendizados. |
| 5 | A organização testa continuamente novas tecnologias de forma sistemática, possui ecossistema ativo de co-inovação (corporate venture, aceleração), adapta seu framework de inovação às mudanças tecnológicas, e utiliza análises preditivas para antecipar tendências. Erros são tratados como oportunidades de aprendizado. |
| 6 | A organização possui processo adaptativo e autônomo de experimentação tecnológica com ciclos curtos, portfólio estrategicamente gerenciado de inovações, ecossistema amplo e dinâmico de parcerias, investimento contínuo em P&D digital, e cultura disseminada de “testar rápido, falhar rápido, aprender rápido” em todos os níveis organizacionais. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Radar tecnológico atualizado periodicamente com tendências mapeadas.

- Business cases e relatórios de POCs/pilotos com critérios claros de avaliação e resultados
        documentados.
- Contratos e acordos formalizados de parcerias com universidades, startups, centros de
        pesquisa e institutos de inovação.
- Orçamento anual dedicado a P&D e inovação digital com acompanhamento de execução.

- Relatórios de lições aprendidas (post-mortems) de experimentos bem-sucedidos e falhados.

- Registro de decisões de kill/pivot/scale com justificativas baseadas em dados.

- Programas de corporate venture, aceleração ou innovation hub.

- Políticas e comunicações corporativas sobre cultura de erro e experimentação.

- Canvas de experimentos com hipóteses, métricas e critérios de sucesso definidos.

- Repositório de conhecimento sobre experimentos realizados e aprendizados capturados.

- Mapeamento do ecossistema de inovação (stakeholders, natureza das parcerias, status).

- Registro de participação em eventos, feiras, conferências e comunidades de prática
        tecnológicas.

##### Métricas/KPIs

- Número de tecnologias avaliadas anualmente (scouting tecnológico).

- % do faturamento ou orçamento alocado para experimentação e inovação digital.

- Número de POCs/pilotos executados por período.

- Taxa de conversão do funil de inovação (tecnologias avaliadas → POCs → pilotos →
        implementações).
- Tempo médio de ciclo desde identificação de tecnologia até piloto ou decisão.

- Número de parcerias ativas para co-inovação (universidades, startups, institutos).


<!-- pág. original: 82/465 -->
- Número de experimentos realizados por trimestre/ano.

- Taxa de “kill rate” saudável (idealmente 30-50% dos experimentos descontinuados com base
        em dados).
- Tempo entre identificação de falha e pivô/aprendizado capturado.

- % de experimentos com lições aprendidas formalmente documentadas.

- Número de ideias de inovação derivadas de aprendizados anteriores.

- ROI de investimentos em inovação (quando mensurável).

- Número de patentes, publicações ou inovações geradas em parceria.

- Frequência de revisões da estratégia de inovação.

- Tempo de resposta organizacional a mudanças tecnológicas ou de mercado relevantes.

- % de iniciativas de inovação ajustadas ou canceladas com base em análise de dados.

- Diversidade de fontes de inteligência tecnológica utilizadas (relatórios, eventos, parcerias, etc.).

##### Sinais por nível

- Nível 0:


  - ausência total de mecanismos de scouting tecnológico

  - decisões baseadas apenas em necessidades imediatas ou pressão de fornecedores

  - nenhum investimento em inovação


- Nível 1:


  - consciência informal e esporádica sobre tendências

  - participação ocasional em eventos

  - sem estrutura ou orçamento dedicado

  - sem parcerias formais


- Nível 2:


  - monitoramento formal através de relatórios e benchmarks


<!-- pág. original: 83/465 -->
  - familiaridade conceitual com tecnologias emergentes

  - orçamento limitado e subutilizado

  - parcerias pontuais reativas


- Nível 3:


  - avaliações pontuais de tecnologias com apoio de consultores/parceiros externos

  - aplicação em áreas específicas

  - algum orçamento regular mas ainda dependente de expertise externa


- Nível 4:


  - POCs estruturadas com critérios claros e documentação

  - capacidade interna de desenvolvimento em múltiplas áreas

  - múltiplas parcerias estratégicas formalizadas

  - cultura estabelecida de experimentação

  - processos de captura de aprendizados

  - segurança psicológica para testar e falhar


- Nível 5:


  - experimentação sistemática e contínua

  - framework de inovação adaptável às mudanças

  - portfólio diversificado de experimentos

  - ecossistema ativo de co-inovação com corporate venture/aceleração

  - uso de análises preditivas e cenários

  - aprendizados integrados à estratégia

  - gestão de risco da experimentação


<!-- pág. original: 84/465 -->
- Nível 6:


  - ciclos rápidos e ágeis de teste e aprendizado (“fail fast, learn fast”)

  - portfólio estrategicamente gerenciado e balanceado

  - ecossistema amplo e dinâmico com mensuração de impacto

  - decisões autônomas baseadas em dados

  - cultura disseminada em todos os níveis

  - revisões frequentes da estratégia de inovação

  - integração total com estratégia corporativa

##### Amostragem

- Amostragem Analisar as últimas 5-10 tecnologias ou inovações avaliadas nos últimos 12-24
          meses, rastreando todo o caminho desde identificação inicial até decisão final
          (implementar/descartar/postergar), incluindo participantes, análises realizadas, dados
          utilizados, experimentos conduzidos e aprendizados capturados
- Revisar orçamento de inovação dos últimos 3 anos e mapear as 5-10 principais parcerias
          ativas com seus resultados tangíveis
- Selecionar 3-5 experimentos que falharam nos últimos 12 meses e verificar tratamento (análise
          formal, lições documentadas, consequências para equipe)
- Comparar versões da estratégia de inovação dos últimos 2-3 anos identificando mudanças
          significativas e seus gatilhos
- —


##### I.14.1.2 Questão: Como a organização lida com erros em iniciativas de inovação e os...
Como a organização lida com erros em iniciativas de inovação e os transforma em oportunidades de
aprendizado?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Erros são punidos ou severamente criticados. Não há análise formal ou discussão sobre erros. Clima de medo inibe experimentação. |
| 1 | Erros são tolerados minimamente, mas geram desconforto significativo. Análises informais e superficiais. Foco em culpar indivíduos ao invés de entender causas sistêmicas. |
| 2 | Alguns erros são aceitos como inevitáveis, mas há pouca análise estruturada. Discussões pontuais sem documentação formal ou compartilhamento amplo de lições aprendidas. |
| 3 | A organização reconhece erros como parte do processo de inovação. Análises de causa-raiz são realizadas pela liderança para erros significativos, com algum registro de aprendizados. |
| 4 | Cultura estabelecida de análise colaborativa de erros com métodos estruturados (RCA, post-mortems, retrospectivas). Lições aprendidas são documentadas, compartilhadas entre equipes e utilizadas para melhorar processos. Erros são vistos como oportunidades de aprendizado sem blame individual. |
| 5 | Gestão proativa de erros com comunicação aberta e sistemática. Repositório acessível de lições aprendidas alimenta decisões futuras. Mecanismos de detecção rápida de erros e correção ágil. Celebração de “falhas inteligentes” que geraram aprendizado valioso. Análise preditiva para antecipar potenciais erros. |
| 6 | Cultura de “error management” plenamente estabelecida em todos os níveis. Erros são comunicados imediatamente sem medo de retaliação. Processos automatizados de captura, análise e disseminação de aprendizados. Inovações frequentemente originam-se de insights de erros anteriores. Métricas de aprendizado organizacional acompanhadas regularmente. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de análise de causa-raiz (RCA) utilizando métodos como 5 Porquês, Ishikawa, A3 ou
         equivalentes.


<!-- pág. original: 86/465 -->
- Documentos de post-mortems de projetos e experimentos (bem-sucedidos e falhados).

- Repositório ou base de conhecimento de lições aprendidas acessível à organização.

- Atas de retrospectivas ágeis ou reuniões de lessons learned.

- Políticas formais sobre error management e comunicação de erros.

- Registros de “blameless post-mortems” ou sessões de aprendizado sem atribuição de culpa.

- Comunicações da liderança celebrando falhas que geraram aprendizado.

- Canal formal para reporte de erros (sistema de tickets, plataforma colaborativa).

- Evidências de mudanças em processos/práticas originadas de lições aprendidas.

- Treinamentos sobre cultura de erro e aprendizado organizacional.

##### Métricas/KPIs

- Número de análises formais de erro realizadas por período.

- % de projetos/experimentos com post-mortem documentado.

- Tempo médio entre ocorrência de erro e análise formal.

- % de lições aprendidas que resultaram em mudanças implementadas.

- Taxa de recorrência de erros similares (indica se aprendizado está sendo aplicado).

- Número de acessos ao repositório de lições aprendidas.

- % de colaboradores treinados em error management.

- Net Promoter Score (NPS) interno sobre segurança psicológica para reportar erros.

- Número de inovações originadas de insights de erros anteriores.

- Tempo médio de detecção de erros (MTTD - Mean Time To Detect).

##### Sinais por nível

- Nível 0:


  - punição explícita ou implícita por erros

  - ausência de análises

  - clima de medo

  - alta rotatividade em áreas de inovação


<!-- pág. original: 87/465 -->
- Nível 1:


  - tolerância mínima

  - análises superficiais e informais

  - foco em culpar indivíduos

  - pouca documentação


- Nível 2:


  - aceitação passiva de erros

  - discussões pontuais sem estrutura

  - documentação esporádica

  - compartilhamento limitado


- Nível 3:


  - reconhecimento de erros como parte do processo

  - análises de RCA para casos significativos

  - algum registro e compartilhamento limitado


- Nível 4:


  - análises colaborativas estruturadas

  - documentação sistemática

  - compartilhamento ativo entre equipes

  - ausência de blame culture

  - segurança psicológica estabelecida


- Nível 5:


<!-- pág. original: 88/465 -->
  - gestão proativa com comunicação aberta

  - repositório ativo e utilizado

  - detecção rápida

  - celebração de falhas inteligentes

  - uso de análise preditiva para prevenção


- Nível 6:


  - cultura de error management plena

  - reporte imediato sem medo

  - processos automatizados de captura e disseminação

  - inovações frequentes originadas de erros

  - métricas de aprendizado acompanhadas

##### Amostragem

- Amostragem Selecionar 5-7 erros ou falhas significativas dos últimos 12-18 meses e verificar:
          existência de análise formal, metodologia utilizada, participantes, tempo até análise, lições
          documentadas, ações corretivas implementadas, compartilhamento com outras equipes, e
          evidências de que não houve punição aos envolvidos
- Entrevistar 5-10 colaboradores de diferentes níveis sobre percepção de segurança psicológica
          para reportar erros

##### I.14.1.3 Questão: Qual o nível de autonomia e empoderamento que colaboradores possuem...
Qual o nível de autonomia e empoderamento que colaboradores possuem para propor, testar e
implementar ideias inovadoras sem necessidade de múltiplas aprovações hierárquicas?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Todas as decisões sobre inovação são centralizadas na alta liderança. Colaboradores não têm autonomia para propor ou testar ideias sem aprovação prévia de múltiplos níveis hierárquicos. |
| 1 | Colaboradores podem sugerir ideias, mas todas as decisões e experimentações dependem de aprovação da alta liderança. Processo burocrático e demorado com múltiplas camadas de aprovação. |
| 2 | Autonomia limitada para propor ideias através de canais formais. Experimentações pequenas podem ser autorizadas pela liderança intermediária, mas com processo ainda burocrático e criterioso. |
| 3 | Colaboradores têm autonomia para propor e experimentar ideias de baixo risco ou baixo investimento com aprovação da liderança imediata. Ideias maiores ainda requerem aprovações hierárquicas múltiplas. |
| 4 | Times têm autonomia clara para experimentar e tomar decisões sobre inovações dentro de orçamento e escopo definidos. Processo de aprovação simplificado com critérios transparentes. Colaboradores entendem que são co-responsáveis pela inovação organizacional. |
| 5 | Ampla autonomia para times e indivíduos testarem ideias com recursos pré-alocados (tempo, orçamento). Processo de aprovação mínimo baseado em alinhamento estratégico e viabilidade. Decisões descentralizadas com liderança atuando como facilitadora e removedora de impedimentos. |
| 6 | Autonomia plena com estrutura organizacional adaptada (squads, células, times autônomos). Colaboradores decidem independentemente sobre experimentação e implementação dentro de guardrails estratégicos claros. Orçamento e tempo dedicados à inovação. Decisões rápidas com revisões post-facto ao invés de aprovações prévias. Cultura de “empowered to fail” disseminada. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Organogramas mostrando estrutura hierárquica e níveis de decisão.

- Políticas formais de delegação de autoridade e limites de alçada para inovação.

- Fluxogramas de processos de aprovação para ideias e experimentos.

- Descrições de papéis e responsabilidades (RACI, job descriptions) indicando autonomia.

- Evidências de estruturas descentralizadas (squads, tribes, células autônomas, OKRs em
        cascata).
- Orçamento dedicado por time/squad para experimentação sem aprovações múltiplas.

- Plataformas de ideação mostrando fluxo desde submissão até execução.

- Atas de reuniões mostrando quem toma decisões sobre experimentação.

- Registros de experimentos iniciados por times sem aprovação prévia da alta liderança.

- Comunicações sobre empoderamento e autonomia dos colaboradores.

- Evidências de times multifuncionais autogerenciados.

##### Métricas/KPIs

- Número de níveis hierárquicos que uma ideia precisa atravessar para aprovação.

- Tempo médio desde submissão de ideia até autorização para experimentar.

- % de ideias/experimentos iniciados por colaboradores sem envolvimento da alta liderança.

- Número de experimentos em paralelo conduzidos por times autônomos.

- % de orçamento de inovação alocado diretamente para times vs centralizado. Índice de
        empoderamento percebido (survey interno com escala validada).
- % de decisões sobre inovação tomadas em até 1 semana.

- Taxa de implementação de ideias bottom-up vs top-down.

- Número de times/squads com autonomia formal para experimentar.

- % de colaboradores que reportam sentir-se empoderados para inovar (pesquisa de clima).

##### Sinais por nível

- Nível 0:


<!-- pág. original: 91/465 -->
  - centralização total

  - múltiplas camadas de aprovação

  - processo burocrático longo

  - baixa taxa de ideias bottom-up implementadas


- Nível 1:


  - submissão possível mas decisão centralizada

  - processo demorado

  - baixa autonomia percebida

  - frustração com burocracia


- Nível 2:


  - autonomia muito limitada

  - experimentações pequenas permitidas com aprovação

  - processo ainda burocrático

  - distinção clara entre “quem pensa” e “quem faz”


- Nível 3:


  - alguma autonomia para baixo risco

  - liderança intermediária pode autorizar experimentos pequenos

  - ideias maiores dependem de hierarquia


- Nível 4:


  - autonomia clara dentro de limites

  - processo simplificado e transparente

  - colaboradores entendem co-responsabilidade


<!-- pág. original: 92/465 -->
  - empoderamento documentado em políticas


- Nível 5:


  - ampla autonomia

  - recursos pré-alocados

  - aprovação mínima

  - liderança como facilitadora

  - decisões descentralizadas com alinhamento estratégico


- Nível 6:


  - autonomia plena

  - estrutura organizacional adaptada (squads/células)

  - decisões independentes

  - guardrails claros mas mínimos

  - cultura de empoderamento disseminada

  - revisões post-facto

##### Amostragem

- Amostragem Mapear o fluxo completo de 5-7 ideias recentes desde submissão até
        implementação ou rejeição: quantos níveis de aprovação, tempo em cada etapa, quem tomou
        decisões, nível hierárquico dos proponentes
- Entrevistar 8-12 colaboradores de diferentes níveis sobre percepção de autonomia usando
        escala padronizada
- Analisar % do orçamento de inovação que está alocado centralmente vs descentralizado em
        times
- Verificar quantos experimentos/pilotos foram iniciados no último trimestre sem aprovação
        prévia da C-level

##### I.14.1.4 Questão: Quanto tempo a organização leva para validar hipóteses e testar novas...
Quanto tempo a organização leva para validar hipóteses e testar novas ideias/tecnologias desde a
concepção até obter resultados em condições reais de mercado ou operação?


<!-- pág. original: 93/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A organização não possui processo definido para validação rápida. Ideias levam mais de 12 meses para serem testadas ou nunca são testadas. |
| 1 | Validação é extremamente lenta e burocrática. Leva de 6 a 12 meses para executar um teste piloto simples devido a processos de aprovação, alocação de recursos e priorização. |
| 2 | Há processo definido mas ainda lento. Validações levam de 3 a 6 meses. Dependência de disponibilidade de recursos compartilhados e múltiplas aprovações atrasa experimentação. |
| 3 | Processo de validação moderadamente ágil. Experimentos podem ser executados em 1 a 3 meses. Recursos começam a ser alocados de forma mais dedicada, mas ainda há dependências significativas. |
| 4 | Processo ágil estabelecido. Validações ocorrem em 2-8 semanas com metodologias estruturadas (Design Sprint, Lean Startup, MVPs). Recursos dedicados para experimentação. Ciclos iterativos claros. |
| 5 | Processo altamente ágil. Validações em 1-4 semanas com infraestrutura e ferramentas que permitem prototipagem rápida. Feature flags, A/B testing e ambientes de sandbox disponíveis. Cultura de “build-measure-learn” estabelecida. |
| 6 | Validação ultrarrápida. Experimentos executados em dias (3-10 dias) com infraestrutura de experimentação madura. Continuous delivery, automação de testes, ambientes on-demand. Ciclos múltiplos e paralelos de experimentação. Aprendizado em tempo quase real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Registro temporal de experimentos mostrando data de concepção, início, marcos e conclusão.

- Metodologias de experimentação documentadas (Lean Startup, Design Sprint, MVP, etc.).


<!-- pág. original: 94/465 -->
- Ferramentas e plataformas de prototipagem rápida disponíveis (Figma, InVision, low-code
        platforms).
- Infraestrutura técnica para experimentação (ambientes de sandbox, feature flags, A/B testing).

- Evidências de uso de métodos ágeis (sprints curtos, retrospectivas frequentes).

- Histórico de MVPs (Minimum Viable Products) desenvolvidos e tempo até validação.

- Documentação de pivots rápidos baseados em aprendizado.

- Calendário de Design Sprints ou Innovation Sprints realizados.

- Acesso a ambientes de desenvolvimento e teste isolados.

- Processos de continuous integration/continuous delivery (CI/CD) habilitando deploys rápidos.

##### Métricas/KPIs

- Tempo médio desde concepção de ideia até primeiro teste em ambiente real (lead time de
        experimentação).
- Tempo médio de cada ciclo de build-measure-learn.

- Número de experimentos executados por trimestre.

- Número de iterações/pivots por experimento antes de decisão final.

- % de experimentos que seguem metodologias ágeis estruturadas.

- Tempo médio para provisionar recursos (infraestrutura, equipe) para experimento.

- Número de MVPs lançados por período.

- Frequência de deploys em ambientes de teste.

- % de experimentos concluídos dentro do prazo planejado.

- Número de experimentos em paralelo sendo executados.

##### Sinais por nível

- Nível 0:


  - ausência de processo

  - ideias nunca testadas ou >12 meses

  - sem infraestrutura para experimentação

  - mentalidade de “planejamento perfeito”


<!-- pág. original: 95/465 -->
- Nível 1:


  - processo muito lento (6-12 meses)

  - alta burocracia

  - dependência de recursos compartilhados escassos

  - múltiplas aprovações sequenciais


- Nível 2:


  - processo lento (3-6 meses)

  - alguma estrutura mas com muitas dependências

  - recursos ainda competidos

  - aprovações múltiplas


- Nível 3:


  - moderadamente ágil (1-3 meses)

  - alguma dedicação de recursos

  - ainda há dependências significativas

  - processo definido mas não otimizado


- Nível 4:


  - ágil (2-8 semanas)

  - metodologias estruturadas (Design Sprint, Lean)

  - recursos dedicados

  - ciclos iterativos claros

  - ferramentas adequadas


<!-- pág. original: 96/465 -->
- Nível 5:


  - altamente ágil (1-4 semanas)

  - infraestrutura madura

  - feature flags e A/B testing

  - prototipagem rápida

  - cultura build-measure-learn estabelecida


- Nível 6:


  - ultrarrápido (3-10 dias)

  - continuous delivery

  - automação ampla

  - ambientes on-demand

  - múltiplos experimentos paralelos

  - aprendizado em tempo quase real

##### Amostragem

- habilitando deploys rápidos

- B) Métricas/KPIs Tempo médio desde concepção de ideia até primeiro teste em ambiente real
       (lead time de experimentação)
- Tempo médio de cada ciclo de build-measure-learn

- Número de experimentos executados por trimestre

- Número de iterações/pivots por experimento antes de decisão final

- % de experimentos que seguem metodologias ágeis estruturadas

- Tempo médio para provisionar recursos (infraestrutura, equipe) para experimento

- Número de MVPs lançados por período

- Frequência de deploys em ambientes de teste

- % de experimentos concluídos dentro do prazo planejado


<!-- pág. original: 97/465 -->
- Número de experimentos em paralelo sendo executados

- C) Sinais por nível N0: ausência de processo; ideias nunca testadas ou >12 meses; sem
        infraestrutura para experimentação; mentalidade de “planejamento perfeito”
- N1: processo muito lento (6-12 meses); alta burocracia; dependência de recursos
        compartilhados escassos; múltiplas aprovações sequenciais
- N2: processo lento (3-6 meses); alguma estrutura mas com muitas dependências; recursos
        ainda competidos; aprovações múltiplas
- N3: moderadamente ágil (1-3 meses); alguma dedicação de recursos; ainda há dependências
        significativas; processo definido mas não otimizado
- N4: ágil (2-8 semanas); metodologias estruturadas (Design Sprint, Lean); recursos dedicados;
        ciclos iterativos claros; ferramentas adequadas
- N5: altamente ágil (1-4 semanas); infraestrutura madura; feature flags e A/B testing;
        prototipagem rápida; cultura build-measure-learn estabelecida
- N6: ultrarrápido (3-10 dias); continuous delivery; automação ampla; ambientes on-demand;
        múltiplos experimentos paralelos; aprendizado em tempo quase real
- D) Amostragem Rastrear cronologicamente 5-8 experimentos recentes desde concepção até
        conclusão, documentando: data de cada etapa, tempo total, número de iterações, metodologia
        utilizada, recursos envolvidos, bloqueios encontrados
- Calcular lead time médio de experimentação dos últimos 6-12 meses

- Verificar quantos experimentos foram executados em paralelo no último trimestre

- Entrevistar 3-5 product owners ou líderes de inovação sobre percepção de velocidade e
        obstáculos
#### Glossário
[Sem glossário]
#### I.14.2 Capacidade: Confiança em processos e sistemas de informação
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Competência de Liderança

#### Resumo Descritivo
Capacidade da liderança e das equipes de confiar em processos estruturados e sistemas de
informação digitais para apoiar decisões, monitorar operações e garantir transparência. Inclui a adoção
progressiva de ferramentas digitais, a transição de práticas manuais para automatizadas, o uso de
dados confiáveis e em tempo real, e a cultura de dependência em sistemas integrados para gestão
eficaz da operação e redução de incertezas.
#### Questões
##### I.14.2.1 Questão: Como a liderança e as equipes utilizam e confiam em processos...
Como a liderança e as equipes utilizam e confiam em processos estruturados e sistemas de
informação para apoiar suas decisões e operações diárias?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há processos estruturados nem sistemas de informação digitais; decisões e operações baseiam-se exclusivamente em experiência pessoal e intuição. |
| 1 | Existem processos básicos documentados, mas as informações são gerenciadas manualmente (planilhas locais, registros em papel); há baixa confiança nos dados disponíveis. |
| 2 | Sistemas digitais básicos estão implementados para coleta de dados, mas são subutilizados; equipes ainda dependem parcialmente de métodos manuais e há desconfiança ocasional na precisão dos sistemas. |
| 3 | Processos e sistemas digitais são utilizados regularmente para monitoramento operacional; a maioria das decisões rotineiras é apoiada por dados dos sistemas, com confiança crescente na qualidade das informações. |
| 4 | Processos estão plenamente integrados com sistemas de informação; dados são usados de forma sistemática e confiável para análise de causas, tomada de decisões e identificação de melhorias; há alta transparência e rastreabilidade. |
| 5 | Sistemas de informação são preditivos e integrados; liderança e equipes confiam plenamente em análises avançadas, simulações e alertas automatizados para antecipar problemas e otimizar processos. |
| 6 | Processos e sistemas são totalmente autônomos e adaptativos; decisões operacionais são tomadas automaticamente com base em dados em tempo real; liderança atua como facilitadora e supervisora estratégica. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentação de processos operacionais e de suporte.

- Sistemas de informação implementados (ERP, MES, SCADA, CRM, etc.).

- Registros de decisões baseadas em dados.

- Relatórios de performance e dashboards.

- Políticas de governança de processos e dados.

- Histórico de uso de sistemas (logs de acesso, frequência de uso).

- Pesquisas de satisfação com sistemas.

- Treinamentos sobre processos e sistemas.

- Indicadores de qualidade de dados.

- Políticas de confiabilidade e SLA de sistemas.


<!-- pág. original: 101/465 -->
##### Métricas/KPIs

- Taxa de adesão a processos formalizados.

- % de decisões baseadas em dados vs intuição.

- Frequência de uso de sistemas de informação. Índice de confiança nos dados (survey).

- Taxa de erros em dados.

- % de processos digitalizados.

- Tempo médio para acesso a informações.

- Taxa de utilização de dashboards e relatórios.

- NPS de sistemas de informação.

- % de colaboradores treinados em sistemas e processos.

##### Sinais por nível

- Nível 0:


  - ausência de processos estruturados

  - sem sistemas digitais

  - decisões baseadas em intuição e experiência pessoal

  - operações ad hoc


- Nível 1:


  - processos básicos documentados

  - gestão manual de informações (planilhas, papel)

  - baixa confiança nos dados

  - dados fragmentados em arquivos locais


- Nível 2:


  - sistemas digitais básicos implementados

  - subutilização dos sistemas


<!-- pág. original: 102/465 -->
  - dependência parcial de métodos manuais

  - desconfiança ocasional na precisão


- Nível 3:


  - uso regular de sistemas para monitoramento

  - decisões rotineiras apoiadas por dados

  - confiança crescente na qualidade

  - processos digitalizados


- Nível 4:


  - integração plena de processos e sistemas

  - uso sistemático de dados para decisões

  - análise de causas baseada em dados

  - alta transparência e rastreabilidade


- Nível 5:


  - sistemas preditivos e integrados

  - confiança plena em análises avançadas

  - uso de simulações e alertas automatizados

  - antecipação proativa de problemas


- Nível 6:


  - processos totalmente autônomos

  - decisões automáticas baseadas em dados em tempo real

  - sistemas adaptativos

  - liderança focada em supervisão estratégica


<!-- pág. original: 103/465 -->
##### Amostragem

- Entrevistar 10-15 colaboradores de diferentes níveis sobre confiança em processos e sistemas

- Analisar decisões recentes e identificar base (dados vs intuição)

- Revisar logs de acesso a sistemas

- Analisar pesquisas de satisfação com sistemas

- Avaliar qualidade e completude de dados em sistemas críticos


##### I.14.2.2 Questão: Como a organização desenvolve e mantém a consciência de segurança...
Como a organização desenvolve e mantém a consciência de segurança cibernética e a cultura de
proteção de informações entre todos os colaboradores?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há programa de conscientização sobre segurança; colaboradores desconhecem riscos cibernéticos e políticas de segurança da informação. |
| 1 | Existe programa básico de segurança para atender requisitos mínimos de compliance; treinamento pontual e reativo focado apenas em cumprir auditoria. |
| 2 | Programa de conscientização limitado com treinamento anual básico; colaboradores têm conhecimento superficial sobre segurança mas não aplicam consistentemente na prática. |
| 3 | Programa estruturado de conscientização com treinamentos regulares; equipes compreendem principais riscos e seguem políticas de segurança nas operações rotineiras. |
| 4 | Programa proativo de segurança com múltiplas ações de reforço ao longo do ano; colaboradores demonstram comportamentos seguros consistentes e reportam incidentes; há medição de mudança comportamental. |
| 5 | Cultura de segurança consolidada como parte do dia a dia organizacional; colaboradores são vigilantes, compartilham conhecimento sobre ameaças e participam ativamente da melhoria contínua; programa baseado em métricas e evolução contínua. |
| 6 | Segurança é valor cultural profundamente enraizado; colaboradores são embaixadores da segurança; organização utiliza tecnologias avançadas (IA, machine learning) para detecção e resposta automatizada; melhoria contínua com métricas sofisticadas de impacto. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Programa de conscientização de segurança (conteúdo, frequência, modalidades).

- Políticas e procedimentos de segurança da informação.

- Registros de treinamentos (participação, conclusão, avaliações).

- Métricas de comportamento seguro (phishing simulations, auditorias).

- Incidentes de segurança reportados.

- Canais de comunicação sobre segurança (newsletters, alertas).

- Ferramentas de gestão de segurança (SIEM, EDR, DLP).

- Certificações de segurança (ISO 27001, SOC 2).

- Pesquisas de cultura de segurança.

- Plano de resposta a incidentes.

##### Métricas/KPIs

- % de colaboradores treinados anualmente.

- Taxa de conclusão de treinamentos obrigatórios.

- Taxa de cliques em phishing simulado (phishing test rate).

- Tempo médio para conclusão de treinamentos.

- Número de incidentes de segurança por colaborador.

- Taxa de reporte de incidentes suspeitos.


<!-- pág. original: 105/465 -->
- % de colaboradores que passam em testes de conhecimento.

- Frequência de comunicações sobre segurança. Índice de cultura de segurança (survey).

- Tempo médio de resposta a incidentes.

##### Sinais por nível

- Nível 0:


  - ausência de programa de conscientização

  - colaboradores desconhecem riscos cibernéticos

  - sem políticas de segurança

  - comportamentos inseguros frequentes


- Nível 1:


  - programa básico para compliance

  - treinamento pontual e reativo

  - foco em cumprir auditoria

  - baixa absorção de conhecimento


- Nível 2:


  - treinamento anual básico

  - conhecimento superficial

  - aplicação inconsistente na prática

  - incidentes por descuido


- Nível 3:


  - programa estruturado com treinamentos regulares

  - compreensão dos principais riscos


<!-- pág. original: 106/465 -->
  - seguimento de políticas nas operações

  - redução de incidentes


- Nível 4:


  - programa proativo com ações contínuas

  - comportamentos seguros consistentes

  - reporte proativo de incidentes

  - medição de mudança comportamental


- Nível 5:


  - cultura de segurança consolidada

  - colaboradores vigilantes e proativos

  - compartilhamento de conhecimento sobre ameaças

  - participação ativa em melhoria contínua


- Nível 6:


  - segurança como valor cultural enraizado

  - colaboradores como embaixadores

  - uso de IA e ML para detecção automatizada

  - métricas sofisticadas de impacto

##### Amostragem

- Analisar programa de conscientização dos últimos 12 meses: conteúdo, frequência, formato,
       participação
- Revisar métricas de phishing simulado e incidentes

- Entrevistar 10-15 colaboradores sobre conhecimento e práticas de segurança

- Analisar políticas e procedimentos de segurança


<!-- pág. original: 107/465 -->
- Avaliar ferramentas e capacidades técnicas de segurança


##### I.14.2.3 Questão: Qual o grau de integração e interoperabilidade entre os diversos...
Qual o grau de integração e interoperabilidade entre os diversos sistemas de informação utilizados
pela organização (internos e com parceiros externos)?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Sistemas operam completamente isolados (silos); não há compartilhamento de dados entre sistemas; integração inexistente. |
| 1 | Integração mínima e manual entre sistemas críticos através de transferência manual de arquivos ou reentrada de dados; processos lentos e sujeitos a erros. |
| 2 | Algumas integrações pontuais automatizadas entre sistemas principais; dados fluem parcialmente mas ainda há necessidade de intervenção manual frequente e reconciliação. |
| 3 | Sistemas principais integrados através de interfaces e APIs; dados fluem entre sistemas de forma estruturada mas ainda existem gaps e integrações que requerem desenvolvimento customizado. |
| 4 | Integração abrangente horizontal (entre áreas) e vertical (do chão de fábrica ao ERP); arquitetura de integração bem definida; dados fluem consistentemente com rastreabilidade; integrações com principais parceiros externos. |
| 5 | Plataforma de integração empresarial consolidada; arquitetura orientada a serviços (SOA) ou microserviços; integração em tempo real; ecossistema digital integrado incluindo parceiros, fornecedores e clientes. |
| 6 | Arquitetura totalmente interoperável e adaptativa; integração nativa e automática de novos sistemas; uso de padrões abertos; ecossistema digital dinâmico com IoT, edge computing e cloud integrados; sincronização em tempo real com toda cadeia de valor. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Arquitetura de integração de sistemas (diagramas, documentação técnica).

- Plataformas de integração (ESB, iPaaS, API Gateway).

- Catálogo de APIs e interfaces.

- Registros de integrações implementadas.

- Padrões de dados e protocolos utilizados.

- Logs de transações entre sistemas.

- Documentação de fluxos de dados.

- Contratos de integração com parceiros externos.

- Ferramentas de monitoramento de integrações.

- Roadmap de integrações planejadas.

##### Métricas/KPIs

- % de sistemas integrados vs isolados.

- Número de integrações automatizadas vs manuais.

- Tempo médio para implementar nova integração.

- Taxa de falhas em integrações.

- % de dados replicados vs compartilhados.

- Latência de sincronização de dados.

- % de integrações via APIs vs métodos legados.

- Número de sistemas em silos.

- % de dados disponíveis em tempo real.

- Custo de manutenção de integrações.

##### Sinais por nível

- Nível 0:


  - sistemas operando em silos isolados


<!-- pág. original: 109/465 -->
  - sem compartilhamento de dados

  - integração inexistente

  - reentrada manual de dados


- Nível 1:


  - integração mínima e manual

  - transferência manual de arquivos

  - processos lentos e propensos a erros

  - duplicação de dados


- Nível 2:


  - integrações pontuais automatizadas

  - fluxo parcial de dados

  - intervenção manual frequente

  - necessidade de reconciliação


- Nível 3:


  - sistemas principais integrados via APIs

  - fluxo estruturado de dados

  - gaps de integração existem

  - desenvolvimento customizado necessário


- Nível 4:


  - integração horizontal e vertical abrangente

  - arquitetura de integração definida

  - fluxo consistente com rastreabilidade


<!-- pág. original: 110/465 -->
  - integrações com parceiros externos


- Nível 5:


  - plataforma de integração consolidada

  - arquitetura SOA ou microserviços

  - integração em tempo real

  - ecossistema digital integrado


- Nível 6:


  - arquitetura totalmente interoperável

  - integração automática de novos sistemas

  - uso de padrões abertos

  - ecossistema dinâmico (IoT, edge, cloud)

  - sincronização em tempo real na cadeia de valor

##### Amostragem

- Mapear todos os sistemas de informação e suas integrações (matriz de integração)

- Analisar arquitetura de integração e padrões utilizados

- Entrevistar 5-8 profissionais de TI sobre desafios de integração

- Revisar logs de falhas e incidentes de integração

- Avaliar plataformas e ferramentas de integração disponíveis


##### I.14.2.4 Questão: Qual o nível de disponibilidade, confiabilidade e resiliência dos...
Qual o nível de disponibilidade, confiabilidade e resiliência dos sistemas de informação críticos para as
operações da organização?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Sistemas críticos frequentemente indisponíveis; falhas recorrentes sem planos de contingência; operação severamente impactada por instabilidade tecnológica. |
| 1 | Sistemas apresentam disponibilidade irregular; incidentes frequentes com resolução reativa e demorada; ausência de acordos de nível de serviço (SLAs) ou monitoramento estruturado. |
| 2 | Disponibilidade básica com interrupções ocasionais; existe monitoramento mas resposta ainda é reativa; SLAs definidos mas nem sempre cumpridos; backups básicos implementados. |
| 3 | Sistemas críticos com boa disponibilidade (>95%); monitoramento proativo; SLAs estabelecidos e geralmente cumpridos; planos de recuperação de desastres documentados e testados ocasionalmente. |
| 4 | Alta disponibilidade (>99%); infraestrutura redundante para sistemas críticos; monitoramento em tempo real com alertas automatizados; SLAs rigorosos cumpridos consistentemente; testes regulares de DR. |
| 5 | Disponibilidade muito alta (>99,5%); arquitetura resiliente com failover automático; self-healing capabilities; monitoramento preditivo que antecipa falhas; recuperação rápida (RTO/RPO baixos). |
| 6 | Disponibilidade próxima a 100%; arquitetura distribuída e altamente resiliente; sistemas adaptativos que se auto-otimizam; zero downtime para manutenções; recuperação instantânea; capacidade de operar em modo degradado mantendo funções essenciais. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Políticas de SLA (Service Level Agreement) para sistemas críticos.

- Registros de disponibilidade e uptime.

- Logs de incidentes e interrupções.


<!-- pág. original: 112/465 -->
- Planos de continuidade de negócios (BCP) e recuperação de desastres (DRP).

- Arquitetura de infraestrutura (redundância, failover).

- Ferramentas de monitoramento (APM, SIEM).

- Documentação de testes de DR.

- Cronogramas de manutenção.

- Análises de causa raiz (RCA) de incidentes.

- Métricas de MTBF (Mean Time Between Failures) e MTTR (Mean Time To Repair).

##### Métricas/KPIs

- Disponibilidade percentual (uptime %).

- Número de incidentes por mês.

- Tempo médio de inatividade (MTTR).

- Tempo médio entre falhas (MTBF).

- % de SLAs cumpridos.

- Duração média de incidentes.

- Taxa de sucesso em testes de DR.

- RTO (Recovery Time Objective) e RPO (Recovery Point Objective) alcançados.

- % de sistemas com redundância.

- Impacto de indisponibilidade (horas de produção perdidas, custo).

##### Sinais por nível

- Nível 0:


  - sistemas críticos frequentemente indisponíveis

  - falhas recorrentes

  - sem planos de contingência

  - operação severamente impactada


- Nível 1:


<!-- pág. original: 113/465 -->
  - disponibilidade irregular

  - incidentes frequentes

  - resolução reativa e demorada

  - sem SLAs ou monitoramento estruturado


- Nível 2:


  - disponibilidade básica com interrupções

  - monitoramento com resposta reativa

  - SLAs nem sempre cumpridos

  - backups básicos


- Nível 3:


  - boa disponibilidade (>95%)

  - monitoramento proativo

  - SLAs geralmente cumpridos

  - planos de DR testados ocasionalmente


- Nível 4:


  - alta disponibilidade (>99%)

  - infraestrutura redundante

  - monitoramento em tempo real com alertas

  - SLAs cumpridos consistentemente

  - testes regulares de DR


- Nível 5:


<!-- pág. original: 114/465 -->
  - disponibilidade muito alta (>99,5%)

  - failover automático

  - capacidades de self-healing

  - monitoramento preditivo

  - recuperação rápida (RTO/RPO baixos)


- Nível 6:


  - disponibilidade próxima a 100%

  - arquitetura altamente resiliente

  - sistemas auto-otimizáveis

  - zero downtime para manutenções

  - recuperação instantânea

  - operação em modo degradado

##### Amostragem

- Analisar registros de disponibilidade dos últimos 12 meses para sistemas críticos

- Revisar todos os incidentes significativos: duração, impacto, causa raiz, ações corretivas

- Entrevistar equipes de TI sobre resiliência e preparação

- Avaliar arquitetura de infraestrutura e redundâncias

- Revisar planos de DR e frequência de testes

#### Glossário
[Sem glossário]
#### I.14.3 Capacidade: Estilo de liderança democrático
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Competência de Liderança

#### Resumo Descritivo
Capacidade dos líderes de definir e comunicar uma visão clara para Indústria 4.0, patrocinar a
transformação (recursos, priorização e governança), tomar decisões baseadas em dados, e fomentar
uma cultura de aprendizado contínuo. Inclui incentivar colaboração multifuncional, gerir mudanças
(metas, KPIs e rituais), e garantir planos de capacitação e requalificação alinhados ao roadmap digital.
#### Questões


<!-- pág. original: 117/465 -->
##### I.14.3.1 Questão: Quando a sua equipe precisa decidir sobre a adoção de uma nova...
Quando a sua equipe precisa decidir sobre a adoção de uma nova tecnologia digital (ex.: IoT,
automação, análise de dados), como normalmente ocorre o processo de decisão?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Liderança decide sozinha, baseada em necessidades imediatas de forma reativa. |
| 1 | Existe uma forma estruturada e explícita de avaliar e adotar a adoção de novas tecnologias, sem ou com pouco envolvimento da equipe. |
| 2 | Equipe contribui com sugestões; decisões ainda dependem da liderança. |
| 3 | Decisões são analisadas entre equipe e liderança coletivamente com base em dados históricos e relatórios. |
| 4 | Decisões são discutidas coletivamente com base em estimativas quantitativas do impacto esperado com a adoção da nova tecnologia. |
| 5 | Decisões são tomadas democraticamente com apoio de análises preditivas. |
| 6 | A equipe decide de forma autônoma e adaptativa, usando dados em tempo real; a liderança facilita. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Decision logs com autores, opções consideradas, dados analisados, trade-offs e resultado.

- Business cases/POCs com critérios de sucesso e resultados.

- Atas de comitês técnicos/steering com lista de participantes e votos.

- Roadmap/Portfolio com ligações a análises e pilotos.

- Threads em Slack/Teams com enquetes e síntese da decisão.


<!-- pág. original: 118/465 -->
##### Métricas/KPIs

- % de decisões com documento de decisão e evidência de contribuição de ICs (individual
        contributors).
- Lead time de decisão (proposta → aprovação).

- % de decisões com dados quantitativos (benchmarks, experimentos, TCO, risco).

- Taxa de participação (nº de contribuintes únicos) e diversidade funcional (áreas representadas).

##### Sinais por nível

- Nível 0:


  - decisões unilaterais

  - ausência de POCs/ata

  - racional implícito


- Nível 1:


  - consultas informais

  - atas curtas sem alternativas/dados


- Nível 2:


  - dados e dashboards usados para descrever cenários

  - liderança ainda decide sozinha


- Nível 3:


  - estimativa do impacto esperado na adoção


- Nível 4:


  - alternativas comparadas com dados quantitativos ou análise de causa

  - consenso registrado


<!-- pág. original: 119/465 -->
  - fontes de dados citadas


- Nível 5:


  - decisões amparadas por predições/simulações (risco de falha, demanda, ROI) + critérios preventivos


- Nível 6:


  - feature flags/rollouts e revisões em tempo quase real

  - liderança atua como facilitadora

##### Amostragem

- Amostragem Selecionar 5–10 decisões relevantes (investimentos, padrões, fornecedores) dos
          últimos 90 dias

##### I.14.3.2 Questão: Como os dados de produção e operação são utilizados para apoiar as...
Como os dados de produção e operação são utilizados para apoiar as decisões?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Dados não são coletados. |
| 1 | Coletados manualmente, pouco utilizados. |
| 2 | Coletados digitalmente, mas analisados apenas pela liderança. |
| 3 | Equipe acessa dashboards simples para acompanhar indicadores. |
| 4 | Dados explicam causas dos problemas e são compartilhados para decisões conjuntas. |
| 5 | Dados permitem prever falhas e antecipar demandas, usados de forma colaborativa. |
| 6 | Dados em tempo real orientam decisões autônomas e adaptativas. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Dashboards (KPI owners, dicionário de métricas, data lineage).

- Notebooks/queries anexos às atas/ decision logs.

- Catálogo de dados (glossário, qualidade, SLAs de atualização).

- Playbooks de leitura de KPI e rotinas de revisão (rituais com pauta e prints).

##### Métricas/KPIs

- % de reuniões/decisões com link para dashboard/consulta.

- Freshness (atualização) e completude dos dados usados.

- Taxa de acesso aos dashboards por função/time.

- Nº de Ações registradas que referenciam métricas.

##### Sinais por nível

- Nível 0:


  - ausência de registros


- Nível 1:


  - planilhas locais e dados esparsos

  - raramente citados


- Nível 2:


  - coleta digital centralizada

  - análise restrita a poucos


- Nível 3:


  - dashboards populares com visão descritiva (o que ocorreu)


<!-- pág. original: 121/465 -->
- Nível 4:


  - análises que explicam por que (causas/variáveis)

  - decisões co-criadas


- Nível 5:


  - modelos preditivos e alertas antecipando eventos

  - hipóteses testadas


- Nível 6:


  - decisões autônomas gatilhadas por dados em tempo real (regras/políticas)

##### Amostragem

- Amostragem Explorar 3 intercorrências (ex

- : weekly ops, Planejamento de Vendas e Operações, daily meetings) e mapear como métricas
          sustentam ações nos últimos 90 dias

##### I.14.3.3 Questão: Quando surge a necessidade de integração entre diferentes áreas (ex.:...
Quando surge a necessidade de integração entre diferentes áreas (ex.: produção, manutenção, TI),
como a colaboração acontece?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Cada área atua isoladamente, sem troca de informações. |
| 1 | Existe um procedimento que permite a colaboração quando autorizadas ou solicitadas pela liderança. |
| 2 | As áreas compartilham informações através de instrumentos formais visíveis que permitem a colaboração, com a mediação da liderança. |
| 3 | As áreas envolvidas analisam e discutem problemas em reuniões pontuais, sem a mediação da liderança. |
| 4 | Planejam ações conjuntas antecipando problemas ou demandas futuras com base em informações quantificáveis. |
| 5 | Ações conjuntas são planejadas baseadas em análises preditivas (planos preventivos e prognósticos). |
| 6 | Funcionam em redes multidisciplinares autônomas, ajustando-se dinamicamente. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Calendário de rituais interfuncionais (cadência, pauta e presença).

- RACIs/matrizes de responsabilidade e OKRs compartilhados.

- Arquiteturas de integração (mapas de fluxo de informação).

- Post-mortems/A3s com participantes de múltiplas áreas.

##### Métricas/KPIs

- Taxa de presença por função; nº de itens interáreas concluídos por sprint/mês.

- Tempo de handoff e retrabalho por fronteira (ex.: engenharia→produção).

- Fluxo (lead time, throughput, WIP) em itens que cruzam times.

##### Sinais por nível

- Nível 0:


  - handoffs verbais


- Nível 1:


  - compartilhamento sob demanda/autorização da liderança


<!-- pág. original: 123/465 -->
- Nível 2:


  - procedimento formal suporta a colaboração


- Nível 3:


  - reuniões pontuais de status

  - poucos owners claros


- Nível 4:


  - rotinas formais com análise de causa e plano conjunto

  - responsabilidades documentadas


- Nível 5:


  - planos preventivos interáreas baseados em prognósticos


- Nível 6:


  - células autônomas e rede dinâmica de colaboração

  - decisões distribuídas

##### Amostragem

- Amostragem Selecionar 2–3 iniciativas que exigiram colaboração e seguir o “fio” dos registros
          ponta-a-ponta nos últimos 90 dias

##### I.14.3.4 Questão: Como a sua equipe contribui com ideias de inovação ou melhoria...
Como a sua equipe contribui com ideias de inovação ou melhoria contínua?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existe espaço formal para sugestões. |
| 1 | Existe espaço formal para sugestões. |
| 2 | Sugestões são ouvidas e formalizadas, mas nem todas são avaliadas. |
| 3 | Ideias são formalizadas, avaliadas e aplicadas pela liderança. |
| 4 | Sugestões são discutidas coletivamente e validadas com base em dados. |
| 5 | Ideias são testadas por meio de simulações e predições colaborativas. |
| 6 | Equipe conduz ciclos rápidos de inovação adaptativa e autônoma. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Backlog de ideias (portal/hackathon/kanban) com critérios de priorização.

- Relatos de experimento (Canvas de hipótese, MVT/A-B, resultados e decisão).

- Stage-gate/comitês e atas de kill/scale. Orçamento/tempo reservado a experimentos.

##### Métricas/KPIs

- Funil de inovação: taxa ideia→POC→piloto→escala.

- Tempo até 1º experimento e até decisão.

- % de experimentos com métrica de sucesso definida antes.

- Kill rate saudável (capacidade de dizer “não” com dados).

##### Sinais por nível

- Nível 0:


  - sem canal formal

  - ideias não avaliadas formalmente


- Nível 1:


<!-- pág. original: 125/465 -->
  - com canal formal, ideias não avaliadas formalmente


- Nível 2:


  - ideias avaliadas formalmente, pouco implementadas


- Nível 3:


  - algumas ideias implementadas pela liderança

  - pouca experimentação


- Nível 4:


  - avaliação coletiva com dados

  - lições aprendidas registradas


- Nível 5:


  - simulações e predições suportam priorização e rollout


- Nível 6:


  - ciclos curtos e portfólio adaptativo

  - times decidem e iteram com autonomia

##### Amostragem

- Amostragem Revisar 10 ideias recentes com seu caminho no funil e a base de evidências que
        justificou cada decisão

##### I.14.3.5 Questão: Como é definido o desenvolvimento de novas competências (habilidades...
Como é definido o desenvolvimento de novas competências (habilidades digitais, treinamentos)?


<!-- pág. original: 126/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existe um plano de desenvolvimento de competências. |
| 1 | Definido apenas pela liderança. |
| 2 | Equipe pode sugerir, mas é parcialmente atendida. |
| 3 | Liderança consulta a equipe para definir prioridades conjuntamente. |
| 4 | Plano de capacitação é co-criado, baseado em lacunas identificadas nos dados. |
| 5 | Competências futuras são preditas e planejadas em conjunto. |
| 6 | A equipe identifica autonomamente necessidades e ajusta continuamente o aprendizado. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Matriz de competências e PDI (planos individuais).

- Trilhas/catálogo de cursos; taxa de conclusão e certificações.

- Levantamento de lacunas ligado a dados de desempenho e metas.

- Guildas/chapters e registros de comunidades de prática.

##### Métricas/KPIs

- Horas/colaborador em capacitação e cobertura de skills-chave.

- % de PDIs co-criados e revisados no período.

- Aplicação em campo (ex.: % de projetos que utilizaram técnica recém-treinada).

- Mobilidade interna/mentorias pareadas.

##### Sinais por nível

- Nível 0:


<!-- pág. original: 127/465 -->
  - treinamentos inexistentes ou muito pontuais


- Nível 1:


  - treinamentos impostos top-down


- Nível 2:


  - pedidos pontuais, pouco atendidos


- Nível 3:


  - consultas parciais

  - pouca ligação com lacunas reais


- Nível 4:


  - plano cocriado com base em diagnóstico

  - indicadores de evolução


- Nível 5:


  - predição de skills futuros (analytics, integração, automação) e planejamento preventivo


- Nível 6:


  - aprendizado contínuo/autônomo com feedback do trabalho real

##### Amostragem

- Amostragem Analisar amostras de PDIs e confrontar com projetos que exigiram tais
       habilidades


<!-- pág. original: 128/465 -->
##### I.14.3.6 Questão: Quando ocorre um problema inesperado (falha de máquina, atraso de...
Quando ocorre um problema inesperado (falha de máquina, atraso de produção), como a solução é
construída?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Liderança decide sozinha, de forma reativa, sem procedimento a seguir. |
| 1 | Liderança atua de modo reativo, conforme procedimento estabelecido. |
| 2 | Equipe informa, mas não participa da solução. |
| 3 | Equipe contribui com sugestões; decisão final da liderança. |
| 4 | Equipe participa da análise de causa-raiz para decidir coletivamente. |
| 5 | Equipe utiliza ferramentas preditivas para antecipar e evitar problemas. |
| 6 | A resolução é autônoma, com ajustes dinâmicos em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- RCA (5 Porquês, Ishikawa, A3), post-mortems e runbooks atualizados.

- Playbooks de incidente e evidências de uso durante o evento.

- Logs/tickets com linha do tempo, responsáveis e decisões.

##### Métricas/KPIs

- MTTD/MTTR (detectar e resolver), taxa de recorrência de incidentes.

- % de incidentes com RCA formal e ações preventivas rastreadas.

- Tempo de atualização de runbooks após aprendizado.

##### Sinais por nível

- Nível 0:


<!-- pág. original: 129/465 -->
  - solução imposta

  - sem registro


- Nível 1:


  - solução imposta

  - com registro


- Nível 2:


  - equipe informa, mas não decide

  - pouca documentação


- Nível 3:


  - equipe sugere

  - decisão final centralizada


- Nível 4:


  - Análise colaborativa com causas comprovadas e ações


- Nível 5:


  - deteção preditiva e planos preventivos com thresholds e alertas


- Nível 6:


  - respostas automatizadas (runbooks acionáveis) e ajustes dinâmicos

##### Amostragem

- Amostragem Selecionar 5 incidentes dos último trimestre; verificar do evento à prevenção
       (fechamento do ciclo)


<!-- pág. original: 130/465 -->
##### I.14.3.7 Questão: Como a organização reage a mudanças externas (novas demandas,...
Como a organização reage a mudanças externas (novas demandas, tecnologias, regulações, etc.)?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Mudanças são realizadas, mas tratadas de forma reativa pela liderança. |
| 1 | Liderança responde às mudanças de forma estruturada e limitada, sem equipe envolvida. |
| 2 | Equipe é parcialmente envolvida para discutir impactos. |
| 3 | Mudanças são analisadas coletivamente com base em dados explicativos. |
| 4 | Os desvios são identificados e causas que motivaram as mudanças podem ser diagnosticadas. |
| 5 | Mudanças são preditas com uso de cenários simulados e discutidas em conjunto. |
| 6 | A organização é altamente adaptável, atuando de forma autônoma e colaborativa em tempo real. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Planejamento (de Vendas e Operação) com cenários, impactos e decisões.

- Tech/Market radar, risk register, matriz regulatória.

- Roadmaps com pivôs/realocações e justificativas.

##### Métricas/KPIs

- Lead time de adaptação (mudança → execução).

- % do orçamento/pipe alocado a mudanças emergentes.

- Acurácia de predição (demanda/suprimento) e tempo para compliance.


<!-- pág. original: 131/465 -->
##### Sinais por nível

- Nível 0:


  - reação tardia

  - decisões centralizadas


- Nível 1:


  - respostas limitadas sem envolvimento amplo


- Nível 2:


  - participação parcial

  - análise descritiva do impacto


- Nível 3:


  - existem dados que mensuram o impacto observado


- Nível 4:


  - debate causal e priorização colaborativa com dados


- Nível 5:


  - cenários simulados e decisões preventivas com critérios de risco


- Nível 6:


  - reconfiguração contínua (times/plano) guiada por sinais em tempo quase real

##### Amostragem

- Amostragem Escolher 3 mudanças externas recentes (cliente, tecnologia, regulação) e rastrear
        do sinal à ação


<!-- pág. original: 132/465 -->
#### Glossário
[Sem glossário]
#### I.14.4 Capacidade: Gestão ágil
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Competência de Liderança

#### Resumo Descritivo
Prontidão do núcleo de liderança para alavancar os conceitos e tecnologias mais recentes de gestão
ágil para a relevância e competitividade contínua da organização. A gestão ágil representa uma
técnica moderna de gerenciamento que permite às organizações reagir de forma flexível e rápida a
mercados turbulentos. Sob a Indústria 4.0, as organizações podem adotar estruturas organizacionais
mais horizontais e permitir tomada de decisão descentralizada, tornando-se mais responsivas às
mudanças. Esta capacidade avalia a familiaridade e aplicação da liderança com práticas ágeis
modernas como Scrum, Kanban, SAFe, Lean, e princípios ágeis (iterações curtas, feedback contínuo,
adaptação, autonomia de times). Nos níveis mais baixos, examina-se a familiaridade da equipe de
gestão com os conceitos mais recentes de gestão ágil. À medida que a empresa progride, a dimensão
mede a habilidade da equipe de liderança de desenhar, executar e adaptar estratégias de
transformação ágil de forma independente para garantir a relevância da empresa no longo prazo.
#### Questões
##### I.14.4.1 Questão: Qual é a prontidão da liderança para alavancar conceitos e técnicas...
Qual é a prontidão da liderança para alavancar conceitos e técnicas de gestão ágil (Scrum, Kanban,
Lean, SAFe, etc.) para a transformação organizacional?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não familiarizada: A liderança não está familiarizada com os conceitos e práticas mais recentes de gestão ágil. A gestão desconhece os conceitos mais recentes que podem viabilizar a próxima fase de avanço da organização. |
| 1 | Conhecimento Limitado: A liderança tem alguma consciência, através de canais ad hoc, dos conceitos e práticas mais recentes de gestão ágil. A gestão está parcialmente familiarizada com os conceitos mais recentes que podem viabilizar a próxima fase de avanço. |
| 2 | Informada: A liderança está bem informada, através de canais e vias formais, sobre os conceitos e práticas mais recentes de gestão ágil. A gestão está totalmente familiarizada com os conceitos mais recentes que podem viabilizar a próxima fase de avanço. |
| 3 | Semi-dependente: A liderança depende de parceiros externos para desenvolver iniciativas que alavancam os conceitos mais recentes de gestão ágil para melhorar pelo menos uma área da organização. Com assistência externa, a gestão é capaz de aplicar os conceitos mais recentes para viabilizar melhorias em pelo menos uma área. |
| 4 | Independente: A liderança é capaz, com relativa independência, de desenvolver iniciativas que alavancam os conceitos e técnicas mais recentes de gestão ágil para melhorar mais de uma área da organização. A gestão é capaz de aplicar os conceitos mais recentes para viabilizar melhorias em múltiplas áreas. |
| 5 | Adaptativa: A liderança é capaz de adaptar independentemente seu framework de transformação organizacional baseado em gestão ágil conforme os conceitos e tecnologias mudam. A gestão é capaz de incrementar suas iniciativas de melhoria conforme os conceitos mais recentes de gestão ágil mudam ou evoluem ao longo do tempo. |
| 6 | Transformacional: A liderança se tornou referência em gestão ágil, moldando ativamente o futuro da agilidade organizacional. A gestão não apenas adapta práticas existentes mas inova e cria novos modelos, influenciando o ecossistema externo e estabelecendo padrões de excelência em transformação ágil. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Certificações e treinamentos da liderança em gestão ágil (Scrum Master, SAFe Agilist, Kanban,
        etc.).
- Participação em eventos (conferências ágeis, workshops, comunidades de prática).

- Biblioteca de livros/materiais sobre gestão ágil acessados pela liderança.

- Assinaturas de publicações especializadas (Harvard Business Review, MIT Sloan, revistas
        ágeis).
- Roadmap de transformação ágil desenhado pela liderança.

- Documentação de iniciativas ágeis patrocinadas pela liderança.

- Contratos com consultorias especializadas em transformação ágil.

- Framework ágil adotado (Scrum, Kanban, SAFe, LeSS, etc.) e evidências de customização.

- Rituais de liderança baseados em princípios ágeis (OKRs, retrospectivas de C-level, etc.).

##### Métricas/KPIs

- % da liderança com certificação em gestão ágil.

- Horas de treinamento em gestão ágil por líder/ano.

- Número de iniciativas ágeis patrocinadas pela liderança.

- % de áreas da organização com práticas ágeis implementadas.

- Tempo médio de ciclo para decisões estratégicas (redução ao longo do tempo).

- Taxa de experimentação (pilotos/MVPs lançados por trimestre).

- Frequência de adaptação do roadmap estratégico.

- NPS interno sobre agilidade da liderança.

- Lead time de iniciativas estratégicas (ideia → execução).

##### Sinais por nível

- Nível 0:


  - liderança desconhece Scrum, Kanban, OKRs, sprints

  - gestão tradicional waterfall/hierárquica


<!-- pág. original: 136/465 -->
  - sem interesse em aprender sobre agilidade


- Nível 1:


  - liderança ouviu falar de gestão ágil

  - alguns líderes participaram de palestras ou leram artigos

  - conhecimento superficial e fragmentado

  - sem aplicação prática


- Nível 2:


  - liderança passou por treinamentos formais em gestão ágil

  - compreensão sólida dos conceitos

  - participa de conferências e eventos especializados

  - benchmarking com outras empresas

  - ainda não aplicou na prática


- Nível 3:


  - contratação de consultores especializados para implementar práticas ágeis em uma área piloto (ex: TI)
  - liderança acompanha mas depende fortemente de orientação externa

  - aprendizado pela observação


- Nível 4:


  - liderança lidera a expansão de práticas ágeis para múltiplas áreas sem dependência crítica de consultores
  - customiza frameworks para o contexto da empresa

  - toma decisões informadas sobre onde e como aplicar agilidade

  - coaching interno


<!-- pág. original: 137/465 -->
- Nível 5:


  - liderança adapta continuamente o modelo de gestão ágil conforme aprende

  - experimenta com novos frameworks emergentes

  - contribui para a comunidade ágil (palestras, publicações)

  - framework proprietário evoluído

  - cultura ágil enraizada


- Nível 6:


  - organização é referência em gestão ágil

  - liderança publica livros, artigos e casos de sucesso

  - convida outras organizações para benchmarking

  - desenvolve frameworks proprietários reconhecidos

  - líderes palestram em conferências internacionais

  - contribui para evolução de frameworks ágeis

  - mentoram outras organizações em transformação ágil

##### Amostragem

- Amostragem Entrevistar 3-5 membros da alta liderança para avaliar: (1) familiaridade com
        terminologia ágil (sprints, retrospectivas, MVPs, OKRs, etc
- ); (2) participação em treinamentos/eventos nos últimos 12 meses; (3) capacidade de explicar
        como aplicam princípios ágeis em suas decisões; (4) exemplos concretos de iniciativas ágeis
        que patrocinaram; (5) como adaptaram práticas ágeis ao contexto da empresa
- Analisar últimos 12 meses de iniciativas estratégicas para verificar aplicação de princípios
        ágeis (iterativo, incremental, feedback rápido)

##### I.14.4.2 Questão: Qual é o nível de patrocínio executivo, investimento de recursos e...
Qual é o nível de patrocínio executivo, investimento de recursos e envolvimento ativo da liderança
sênior na transformação ágil?


<!-- pág. original: 138/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A alta gestão não tem conhecimento ou envolvimento com iniciativas de gestão ágil. |
| 1 | A alta gestão tem conhecimento superficial sobre gestão ágil, mas não demonstra apoio ativo ou compromisso. |
| 2 | A alta gestão aprova iniciativas ágeis pontualmente, mas com recursos limitados e baixo envolvimento direto. |
| 3 | A alta gestão patrocina formalmente iniciativas ágeis, aloca recursos específicos, mas o envolvimento é esporádico. |
| 4 | A alta gestão está ativamente envolvida, participa de cerimônias-chave, remove impedimentos e monitora progresso regularmente. |
| 5 | A alta gestão lidera a transformação ágil, investe significativamente, participa de treinamentos e modela comportamentos ágeis. |
| 6 | A alta gestão incorporou completamente mindset ágil, promove cultura de experimentação, e a agilidade é parte da estratégia corporativa. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Atas de reuniões executivas com pautas sobre transformação ágil.

- Orçamento alocado para iniciativas ágeis (treinamentos, ferramentas, consultorias, coaches).

- Comunicados oficiais da liderança sobre compromisso com agilidade.

- Presença de executivos em cerimônias ágeis (sprint reviews, PI planning, town halls).

- Roadmap estratégico incluindo objetivos de transformação ágil.

- Decisões de priorização que favorecem iniciativas ágeis.

- Documentação de impedimentos escalados e resolvidos pela liderança.

- Contratações de roles ágeis (Scrum Masters, Agile Coaches, Product Owners).


<!-- pág. original: 139/465 -->
##### Métricas/KPIs

- % do orçamento de TI/Operações dedicado a transformação ágil.

- Frequência de participação de executivos em eventos ágeis.

- Tempo médio de resolução de impedimentos escalados.

- Número de iniciativas ágeis patrocinadas por executivos.

- Taxa de aprovação rápida de investimentos ágeis vs. tradicionais.

- NPS de times sobre suporte da liderança.

- % de executivos com treinamento/certificação ágil.

##### Sinais por nível

- Nível 0:


  - liderança desconhece práticas ágeis

  - sem menção em estratégia


- Nível 1:


  - liderança ouviu falar mas vê como “coisa de TI”

  - sem apoio tangível


- Nível 2:


  - aprovação reativa de pilotos

  - orçamento mínimo

  - delega totalmente


- Nível 3:


  - sponsor formal designado

  - budget específico

  - revisões trimestrais


<!-- pág. original: 140/465 -->
  - ainda distante do dia-a-dia


- Nível 4:


  - executivos participam de sprint reviews

  - removem blockers

  - questionam métricas ágeis

  - orçamento significativo


- Nível 5:


  - CEO/C-level falam publicamente sobre agilidade

  - fazem treinamentos

  - participam de retrospectivas

  - investimento estratégico


- Nível 6:


  - agilidade é pilar estratégico

  - OKRs corporativos incluem métricas ágeis

  - liderança modela servant leadership

  - experimentação incentivada

##### Amostragem

- Amostragem Analisar últimos 6 meses: (1) atas de comitê executivo (quantas mencionam
        agilidade?); (2) orçamento aprovado para iniciativas ágeis; (3) lista de presença de executivos
        em eventos ágeis; (4) exemplos de impedimentos resolvidos por escalação; (5) comunicações
        oficiais sobre agilidade

##### I.14.4.3 Questão: Qual é a frequência, qualidade e intensidade da participação de...
Qual é a frequência, qualidade e intensidade da participação de clientes/stakeholders no processo de
desenvolvimento e tomada de decisão?


<!-- pág. original: 141/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Clientes/stakeholders não participam do processo; requisitos são coletados uma vez no início. |
| 1 | Contato mínimo com clientes/stakeholders; feedback solicitado apenas em gates formais (trimestral/anual). |
| 2 | Clientes/stakeholders são consultados mensalmente; feedback é coletado mas nem sempre incorporado. |
| 3 | Clientes/stakeholders participam de revisões a cada sprint/iteração; feedback influencia backlog. |
| 4 | Clientes/stakeholders são membros ativos do processo; validam incrementos, participam de refinamentos e priorizam backlog. |
| 5 | Clientes/stakeholders trabalham de forma integrada com o time; disponíveis para esclarecimentos contínuos; co-criam soluções. |
| 6 | Clientes/stakeholders são parte do time estendido; tomam decisões de produto em tempo real; relacionamento de parceria estratégica. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Calendário de cerimônias com lista de presença de clientes/stakeholders (sprint reviews,
         demos).
- Backlog com evidências de input de clientes (user stories com origem, feedback registrado).

- Atas de reuniões de refinamento/priorização com clientes.

- Canais de comunicação dedicados (Slack, Teams) com clientes ativos.

- Contratos/acordos que especificam participação de clientes.

- Feedback logs (pesquisas, entrevistas, testes de usabilidade).

- Artefatos de co-criação (design sprints, workshops, prototipação conjunta).


<!-- pág. original: 142/465 -->
##### Métricas/KPIs

- Taxa de participação de clientes em sprint reviews (% de sprints com cliente presente).

- Tempo médio de resposta de clientes a dúvidas/solicitações.

- % de user stories validadas por clientes antes de desenvolvimento.

- Frequência de interação (média de contatos por semana).

- NPS/CSAT dos clientes sobre o processo colaborativo.

- % de mudanças no backlog originadas de feedback de cliente.

- Lead time de esclarecimento de dúvidas.

##### Sinais por nível

- Nível 0:


  - modelo waterfall

  - requisitos congelados

  - cliente não vê nada até entrega final


- Nível 1:


  - checkpoint único pós-implementação

  - cliente valida apenas no final


- Nível 2:


  - reuniões mensais de status

  - feedback coletado mas pouco acionado


- Nível 3:


  - clientes em todas sprint reviews

  - feedback documentado e priorizado


<!-- pág. original: 143/465 -->
- Nível 4:


  - clientes validam PBIs antes do desenvolvimento

  - participam de refinements

  - acesso a ambiente de homologação


- Nível 5:


  - Product Owner tem acesso direto e contínuo

  - clientes em dailies quando necessário

  - workshops de co-criação regulares


- Nível 6:


  - cliente embedded no time

  - decisões de produto em tempo real

  - mindset de parceria

  - shared ownership de outcomes

##### Amostragem

- Amostragem Analisar últimas 10 sprints: (1) taxa de presença de clientes em reviews; (2)
          número de interações registradas por sprint; (3) % de PBIs que tiveram validação prévia; (4)
          exemplos de mudanças de direção baseadas em feedback; (5) tempo médio entre dúvida e
          resposta do cliente

##### I.14.4.4 Questão: Qual é o grau de alinhamento entre os valores culturais existentes...
Qual é o grau de alinhamento entre os valores culturais existentes (confiança, abertura, tolerância a
erros, colaboração) e os requisitos da cultura ágil?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Cultura organizacional é rigidamente hierárquica, avessa a riscos, com baixa tolerância a erros e comunicação top-down. |
| 1 | Cultura predominantemente tradicional com silos; tentativas de colaboração encontram resistência; erros são punidos. |
| 2 | Cultura em transição; alguns bolsões de colaboração; erros começam a ser vistos como aprendizado, mas inconsistentemente. |
| 3 | Cultura parcialmente alinhada; colaboração é valorizada; erros são tratados de forma mais construtiva; ainda há hierarquia significativa. |
| 4 | Cultura favorável à agilidade; alta confiança entre áreas; erros são oportunidades de aprendizado; transparência é norma. |
| 5 | Cultura fortemente ágil; experimentação é incentivada; feedback aberto é prática comum; autonomia e responsabilidade equilibradas. |
| 6 | Cultura totalmente ágil; segurança psicológica plena; celebração de aprendizado; auto-organização natural; mindset de crescimento. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Assessment de cultura organizacional (ex: Competing Values Framework, Denison, OCAI).

- Pesquisas de clima e engajamento com questões sobre confiança, autonomia, tolerância a
         erros.
- Documentação de valores corporativos e evidências de aplicação prática.

- Registros de retrospectivas e ações de melhoria implementadas.

- Post-mortems de falhas com foco em aprendizado (vs. culpabilização).

- Políticas de gestão de pessoas (avaliação, promoção, recompensas) alinhadas com valores
         ágeis.
- Canais de comunicação abertos (town halls, AMAs, fóruns).


<!-- pág. original: 145/465 -->
##### Métricas/KPIs

- Score de segurança psicológica (survey baseado em Edmondson). Índice de confiança entre
        áreas (survey interno).
- Taxa de “falhas celebradas” (experimentos que falharam mas geraram aprendizado).

- % de decisões tomadas de forma descentralizada.

- Tempo de implementação de ações de retrospectivas.

- Turnover em times ágeis vs. tradicionais. eNPS (employee Net Promoter Score).

- Score de segurança psicológica (survey baseado em Edmondson). Índice de confiança entre
        áreas (survey interno).
- Taxa de “falhas celebradas” (experimentos que falharam mas geraram aprendizado).

- % de decisões tomadas de forma descentralizada.

- Tempo de implementação de ações de retrospectivas.

- Turnover em times ágeis vs. tradicionais. eNPS (employee Net Promoter Score).

- Score de segurança psicológica (survey baseado em Edmondson). Índice de confiança entre
        áreas (survey interno).
- Taxa de “falhas celebradas” (experimentos que falharam mas geraram aprendizado).

- % de decisões tomadas de forma descentralizada.

- Tempo de implementação de ações de retrospectivas.

- Turnover em times ágeis vs. tradicionais. eNPS (employee Net Promoter Score).

- Score de segurança psicológica (survey baseado em Edmondson). Índice de confiança entre
        áreas (survey interno).
- Taxa de “falhas celebradas” (experimentos que falharam mas geraram aprendizado).

- % de decisões tomadas de forma descentralizada.

- Tempo de implementação de ações de retrospectivas.

- Turnover em times ágeis vs. tradicionais. eNPS (employee Net Promoter Score).

- Score de segurança psicológica (survey baseado em Edmondson). Índice de confiança entre
        áreas (survey interno).
- Taxa de “falhas celebradas” (experimentos que falharam mas geraram aprendizado).

- % de decisões tomadas de forma descentralizada.


<!-- pág. original: 146/465 -->
- Tempo de implementação de ações de retrospectivas.

- Turnover em times ágeis vs. tradicionais. eNPS (employee Net Promoter Score).

- Score de segurança psicológica (survey baseado em Edmondson). Índice de confiança entre
        áreas (survey interno).
- Taxa de “falhas celebradas” (experimentos que falharam mas geraram aprendizado).

- % de decisões tomadas de forma descentralizada.

- Tempo de implementação de ações de retrospectivas.

- Turnover em times ágeis vs. tradicionais. eNPS (employee Net Promoter Score).

- Score de segurança psicológica (survey baseado em Edmondson). Índice de confiança entre
        áreas (survey interno).
- Taxa de “falhas celebradas” (experimentos que falharam mas geraram aprendizado).

- % de decisões tomadas de forma descentralizada.

- Tempo de implementação de ações de retrospectivas.

- Turnover em times ágeis vs. tradicionais. eNPS (employee Net Promoter Score).

##### Sinais por nível

- Nível 0:


  - comando-e-controle

  - culpabilização

  - silos rígidos

  - “não temos tempo para experimentar”


- Nível 1:


  - hierarquia rígida

  - colaboração vista como perda de tempo

  - erros = punição

  - “sempre fizemos assim”


<!-- pág. original: 147/465 -->
- Nível 2:


  - discurso sobre colaboração mas estrutura hierárquica permanece

  - alguns experimentos permitidos com muita aprovação


- Nível 3:


  - colaboração cross-funcional acontece

  - erros geram discussão construtiva na maioria das vezes

  - transparência crescente


- Nível 4:


  - confiança alta

  - times se auto-organizam com supervisão leve

  - retrospectivas geram mudanças reais

  - erros = aprendizado


- Nível 5:


  - cultura de experimentação

  - fail fast é norma

  - feedback 360° naturalizado

  - autonomia com accountability


- Nível 6:


  - segurança psicológica máxima

  - celebração pública de falhas instrutivas

  - todos são agentes de mudança


<!-- pág. original: 148/465 -->
  - growth mindset organizacional

##### Amostragem

- Amostragem Realizar survey de cultura ágil com amostra representativa (mín

- 50 pessoas de diferentes níveis/áreas)

- Analisar últimas 5 retrospectivas de 3 times: quantas ações foram implementadas? Houve
          resistência? Revisar 3 post-mortems recentes: foco em aprendizado ou culpa?

##### I.14.4.5 Questão: Qual é a qualidade, abrangência e continuidade dos programas de...
Qual é a qualidade, abrangência e continuidade dos programas de capacitação em práticas ágeis,
incluindo coaching e mentoring?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existe nenhum programa de treinamento ou capacitação em práticas ágeis. |
| 1 | Treinamentos pontuais e esporádicos são oferecidos, sem continuidade ou acompanhamento. |
| 2 | Existe um programa básico de treinamento inicial (ex: Scrum Foundation), mas sem coaching ou follow-up. |
| 3 | Programa de treinamento estruturado com múltiplos níveis; coaching disponível sob demanda; sem plano de desenvolvimento contínuo. |
| 4 | Programa abrangente de capacitação (básico a avançado); coaches/Scrum Masters dedicados; trilhas de desenvolvimento definidas. |
| 5 | Programa maduro e integrado ao plano de carreira; coaching contínuo; comunidades de prática ativas; orçamento dedicado para certificações. |
| 6 | Cultura de aprendizado contínuo institucionalizada; coaching peer-to-peer; times são ambientes de aprendizagem; investimento estratégico em desenvolvimento. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Catálogo de treinamentos ágeis disponíveis (básico, intermediário, avançado, especializado).

- Trilhas de aprendizagem e planos de desenvolvimento individual (PDIs).

- Matriz de competências ágeis e gap analysis.

- Contratos com empresas de treinamento/coaching.

- Relação de coaches/Scrum Masters (dedicados, part-time, ratio coach:time).

- Agenda de coaching e sessões de mentoring.

- Registros de certificações obtidas (CSM, CSPO, SAFe, etc.).

- Comunidades de prática (CoPs, chapters, guilds) com calendário de encontros.

- Materiais de treinamento interno desenvolvidos.

##### Métricas/KPIs

- % da força de trabalho treinada em práticas ágeis (por nível: básico, intermediário, avançado).

- Horas de treinamento per capita em agilidade (anual).

- Número de certificações ágeis por 100 colaboradores.

- Ratio coach:time (ideal: 1:3 a 1:5 times por coach).

- Taxa de conclusão de trilhas de desenvolvimento. $ investido em capacitação ágil / colaborador
        / ano.
- Frequência de coaching (sessões/time/mês).

- Participação em CoPs (% de profissionais ágeis ativos).

##### Sinais por nível

- Nível 0:


  - zero treinamento

  - “aprendam na internet”


- Nível 1:


<!-- pág. original: 150/465 -->
  - 1-2 treinamentos pontuais de 1 dia

  - sem continuidade

  - “já treinamos o pessoal”


- Nível 2:


  - Scrum Foundation para todos

  - materiais básicos disponíveis

  - sem coaching estruturado


- Nível 3:


  - múltiplos cursos disponíveis

  - alguns coaches contratados sob demanda

  - trilhas começando a ser desenhadas


- Nível 4:


  - programa estruturado com certificações patrocinadas

  - coaches dedicados (1:5)

  - PDIs incluem competências ágeis

  - orçamento garantido


- Nível 5:


  - trilhas integradas à carreira

  - coaching embedded

  - CoPs ativas semanalmente

  - budget significativo

  - certificações avançadas incentivadas


<!-- pág. original: 151/465 -->
- Nível 6:


  - learning organization

  - peer coaching natural

  - times ensinam times

  - budget generoso

  - experimentação com novas práticas encorajada

  - contribuições para comunidade externa

##### Amostragem

- Amostragem Analisar: (1) % de pessoas treinadas por nível nos últimos 12 meses; (2) ratio
          atual de coaches:times; (3) budget de capacitação ágil vs
- total de treinamento; (4) amostra de 10 PDIs para verificar inclusão de competências ágeis; (5)
          atividade de CoPs nos últimos 3 meses

##### I.14.4.6 Questão: Qual é o nível de estruturação do processo de transformação ágil,...
Qual é o nível de estruturação do processo de transformação ágil, incluindo assessment de prontidão,
plano de mudança, gestão de resistências e sustentabilidade?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existe processo estruturado; mudanças acontecem de forma ad hoc sem planejamento ou acompanhamento. |
| 1 | Iniciativas isoladas sem coordenação; falta assessment de prontidão; resistências não são gerenciadas sistematicamente. |
| 2 | Existe um plano básico de transformação, mas sem assessment formal de prontidão; gestão de mudança reativa. |
| 3 | Plano de transformação estruturado com fases definidas; assessment de prontidão realizado; gestão de mudança presente mas não integrada. |
| 4 | Programa abrangente de transformação com governance clara; change management integrado; métricas de acompanhamento; gestão ativa de resistências. |
| 5 | Transformação estruturada em múltiplas ondas/fases; assessment contínuo; change management profissional; adaptação baseada em lições aprendidas. |
| 6 | Transformação é contínua e adaptativa; capacidade organizacional de mudança institucionalizada; experimentação e evolução constantes; sustentabilidade garantida. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Plano de transformação ágil (roadmap, fases, milestones).

- Assessment de prontidão organizacional (readiness assessment usando frameworks
         validados).
- Plano de gestão de mudança (stakeholder analysis, plano de comunicação, plano de
         resistências).
- Estrutura de governança (steering committee, transformation office, agile COE).

- Mapa de stakeholders e estratégia de engajamento.

- Plano de comunicação da transformação (canais, frequência, mensagens-chave).

- Registro de riscos e resistências com plano de mitigação.

- Métricas de transformação (leading e lagging indicators).

- Lições aprendidas documentadas e ações corretivas.

- Roadmap de evolução pós-transformação inicial.

##### Métricas/KPIs

- Completion rate de fases do plano de transformação.

- % de times que completaram transição ágil.

- Lead time de transformação por time/área. Índice de resistência (survey ou análise qualitativa).


<!-- pág. original: 153/465 -->
- Engajamento em iniciativas de transformação (participação em eventos, surveys).

- Sustentabilidade (% de times que mantêm práticas após 12 meses).

- ROI da transformação (benefícios vs. investimento).

- Velocidade/throughput antes vs. depois (evidência de melhoria).

##### Sinais por nível

- Nível 0:


  - “vamos fazer ágil”

  - decreto top-down

  - surpresa total

  - resistência massiva não gerenciada


- Nível 1:


  - várias iniciativas desconexas

  - cada área faz do seu jeito

  - sem coordenação

  - “já somos ágeis” sem evidências


- Nível 2:


  - plano existe mas é genérico

  - falta assessment prévio

  - comunicação pobre

  - resistências aparecem como surpresa


- Nível 3:


  - plano detalhado com fases


<!-- pág. original: 154/465 -->
  - assessment feito

  - change manager designado

  - stakeholders mapeados

  - comunicação regular


- Nível 4:


  - programa robusto

  - steering committee ativo

  - change management profissional (Prosci, Kotter)

  - métricas acompanhadas

  - ajustes baseados em feedback


- Nível 5:


  - múltiplas ondas planejadas

  - assessment contínuo (pulse checks)

  - change agents em todas áreas

  - resistências antecipadas e gerenciadas

  - retrospectivas de transformação


- Nível 6:


  - transformação contínua como BAU

  - capacidade de mudança = competência organizacional

  - experimentação incentivada

  - evolução constante

  - práticas ágeis profundamente enraizadas


<!-- pág. original: 155/465 -->
##### Amostragem

- Amostragem Analisar: (1) documentação de plano de transformação e assessment inicial; (2)
        evidências de governance (atas de steering committee dos últimos 6 meses); (3) plano de
        comunicação e exemplos de execução; (4) métricas de progresso; (5) registro de resistências e
        ações de mitigação; (6) survey de sustentabilidade (práticas mantidas após 12+ meses)
#### Glossário
[Sem glossário]
#### I.14.5 Capacidade: Sistemas de metas motivacionais
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Competência de Liderança

#### Resumo Descritivo
Capacidade dos líderes de estabelecer, comunicar e gerenciar sistemas de metas que motivam e
engajam os colaboradores na transformação para Indústria 4.0. Inclui a habilidade de alinhar objetivos
individuais, de equipe e organizacionais; definir metas baseadas em dados; promover autonomia e
ownership; fornecer feedback contínuo; e adaptar metas dinamicamente ao contexto de negócios. Esta
capacidade mede o quanto a liderança é capaz de criar um ambiente onde metas claras, desafiadoras
e motivacionais impulsionam a transformação digital. Estilo de liderança democrático, Gestão ágil,
Estratégia & Governança, Colaboração Inter e Intraempresarial, Workforce Learning & Development,
Abertura à inovação
#### Questões
##### I.14.5.1 Questão: Como a liderança estabelece e gerencia sistemas de metas para motivar...
Como a liderança estabelece e gerencia sistemas de metas para motivar e engajar a equipe na
transformação para Indústria 4.0?


<!-- pág. original: 157/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existem metas formais relacionadas à Indústria 4.0. Liderança não estabelece objetivos claros para a transformação digital. |
| 1 | Liderança define metas de forma unilateral e top-down, comunicadas informalmente. Sem mecanismos de acompanhamento ou feedback. |
| 2 | Liderança define metas formais e as comunica através de canais oficiais, mas sem envolvimento da equipe na definição. Acompanhamento anual ou semestral. |
| 3 | Liderança define metas em consulta com as equipes, com alinhamento parcial entre objetivos individuais e organizacionais. Feedback periódico (trimestral) e sistema básico de reconhecimento. |
| 4 | Liderança co-cria metas com as equipes baseadas em dados, promovendo alinhamento claro entre objetivos individuais, de equipe e organizacionais. Feedback contínuo (mensal) e reconhecimento estruturado. |
| 5 | Liderança estabelece sistema ágil de metas com ciclos curtos, alta autonomia das equipes, dashboards com dados em tempo real, análises preditivas e reconhecimento personalizado. Metas adaptam-se dinamicamente ao contexto. |
| 6 | Liderança atua como facilitadora de sistema totalmente integrado onde equipes autogerenciáveis definem e ajustam metas continuamente com base em dados em tempo real, transparência total, feedback automatizado e celebração de conquistas. Motivação intrínseca sustentável. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentos de definição de metas (OKRs, KPIs, Balanced Scorecard) com evidências de
         autoria e participação.


<!-- pág. original: 158/465 -->
- Matriz de alinhamento mostrando conexão entre metas individuais → equipe → organização.

- Dashboards de acompanhamento (frequência de atualização, nível de acesso).

- Atas de reuniões de definição, revisão e ajuste de metas (1:1s, team meetings, all-hands).

- Registros de feedback (formulários, sistemas de avaliação).

- Programas de reconhecimento (critérios, frequência, exemplos).

- PDIs (Planos de Desenvolvimento Individual) vinculados a metas.

- Comunicações sobre metas (e-mails, intranet, apresentações).

##### Métricas/KPIs

- % de colaboradores que conhecem suas metas e entendem como contribuem para objetivos
        organizacionais (pesquisa).
- Taxa de alinhamento entre metas (individual/equipe/organização).

- Frequência de definição, revisão e ajuste de metas.

- % de metas com métricas quantitativas e fontes de dados definidas.

- % de metas co-criadas vs. impostas. Índice de engajamento e motivação (pesquisa eNPS,
        clima).
- Taxa de alcance de metas.

- Frequência de feedback formal e informal.

- % de colaboradores que receberam reconhecimento vinculado a metas.

- Tempo de resposta entre mudança estratégica e ajuste de metas. Índice de autonomia
        (pesquisa sobre ownership das metas).
- Taxa de uso de dashboards e ferramentas de acompanhamento.

##### Sinais por nível

- Nível 0:


  - sem metas formais para Indústria 4

  - iniciativas ad-hoc ou ausentes


- Nível 1:


<!-- pág. original: 159/465 -->
  - metas definidas unilateralmente pela liderança

  - comunicação informal

  - sem acompanhamento estruturado

  - colaboradores desconhecem ou não se engajam


- Nível 2:


  - metas definidas top-down com comunicação formal

  - acompanhamento anual/semestral

  - alinhamento fraco

  - feedback esporádico

  - reconhecimento pontual


- Nível 3:


  - consulta às equipes na definição

  - alinhamento parcial documentado

  - revisões trimestrais

  - feedback periódico

  - sistema básico de reconhecimento

  - motivação moderada


- Nível 4:


  - co-criação de metas com dados

  - alinhamento claro e documentado

  - dashboards digitais

  - feedback contínuo (mensal)

  - reconhecimento estruturado


<!-- pág. original: 160/465 -->
  - alta motivação

  - metas revisadas com base em contexto


- Nível 5:


  - sistema ágil com ciclos curtos (sprints)

  - alta autonomia

  - dashboards com tempo real e analytics preditivos

  - reconhecimento personalizado e automatizado

  - ajustes dinâmicos baseados em dados

  - motivação intrínseca


- Nível 6:


  - autogestão completa

  - times definem e ajustam metas continuamente

  - transparência total

  - feedback e reconhecimento em tempo real

  - cultura de metas integrada

  - celebração sistemática de conquistas

  - metas adaptativas com ajustes automáticos

##### Amostragem

- com evidências de autoria e participação

- Matriz de alinhamento mostrando conexão entre metas individuais → equipe → organização

- Dashboards de acompanhamento (frequência de atualização, nível de acesso)

- Atas de reuniões de definição, revisão e ajuste de metas (1:1s, team meetings, all-hands)

- Registros de feedback (formulários, sistemas de avaliação)

- Programas de reconhecimento (critérios, frequência, exemplos)


<!-- pág. original: 161/465 -->
- PDIs (Planos de Desenvolvimento Individual) vinculados a metas

- Comunicações sobre metas (e-mails, intranet, apresentações)

- B) Métricas/KPIs % de colaboradores que conhecem suas metas e entendem como contribuem
     para objetivos organizacionais (pesquisa)
- Taxa de alinhamento entre metas (individual/equipe/organização)

- Frequência de definição, revisão e ajuste de metas

- % de metas com métricas quantitativas e fontes de dados definidas

- % de metas co-criadas vs

- impostas

- Índice de engajamento e motivação (pesquisa eNPS, clima)

- Taxa de alcance de metas

- Frequência de feedback formal e informal

- % de colaboradores que receberam reconhecimento vinculado a metas

- Tempo de resposta entre mudança estratégica e ajuste de metas

- Índice de autonomia (pesquisa sobre ownership das metas)

- Taxa de uso de dashboards e ferramentas de acompanhamento

- C) Sinais por nível N0: sem metas formais para Indústria 4

- 0; iniciativas ad-hoc ou ausentes

- N1: metas definidas unilateralmente pela liderança; comunicação informal; sem
     acompanhamento estruturado; colaboradores desconhecem ou não se engajam
- N2: metas definidas top-down com comunicação formal; acompanhamento anual/semestral;
     alinhamento fraco; feedback esporádico; reconhecimento pontual
- N3: consulta às equipes na definição; alinhamento parcial documentado; revisões trimestrais;
     feedback periódico; sistema básico de reconhecimento; motivação moderada
- N4: co-criação de metas com dados; alinhamento claro e documentado; dashboards digitais;
     feedback contínuo (mensal); reconhecimento estruturado; alta motivação; metas revisadas com
     base em contexto
- N5: sistema ágil com ciclos curtos (sprints); alta autonomia; dashboards com tempo real e
     analytics preditivos; reconhecimento personalizado e automatizado; ajustes dinâmicos
     baseados em dados; motivação intrínseca


<!-- pág. original: 162/465 -->
- N6: autogestão completa; times definem e ajustam metas continuamente; transparência total;
          feedback e reconhecimento em tempo real; cultura de metas integrada; celebração sistemática
          de conquistas; metas adaptativas com ajustes automáticos
- D) Amostragem Selecionar 3-5 ciclos de definição de metas dos últimos 12-24 meses

- Analisar 10-15 metas de diferentes níveis hierárquicos e funções, verificando: processo de
          definição (quem participa), comunicação (canais e clareza), alinhamento (vínculo com objetivos
          superiores), métricas (quantificação e fontes de dados), acompanhamento (frequência e
          ferramentas), feedback (registros e frequência), ajustes (histórico de revisões e justificativas),
          reconhecimento (exemplos concretos), autonomia (nível de participação dos colaboradores)
- Realizar entrevistas com 5-10 colaboradores de diferentes níveis para avaliar percepção sobre
          clareza, motivação, alinhamento e ownership das metas
- Analisar resultados de pesquisas de engajamento correlacionando com dados de performance
          em metas
- —


##### I.14.5.2 Questão: Como as metas são formuladas em termos de clareza, especificidade e...
Como as metas são formuladas em termos de clareza, especificidade e mensurabilidade?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Metas vagas e genéricas (“melhorar”, “aumentar”) sem especificações concretas ou critérios de sucesso. |
| 1 | Alguma especificidade nas metas, mas sem métricas claras ou mensuráveis definidas. |
| 2 | Metas específicas com métricas definidas, mas sem prazos estabelecidos ou relevância clara. |
| 3 | Metas SMART básicas (específicas, mensuráveis, alcançáveis, relevantes e com prazo definido). |
| 4 | Metas SMART bem definidas, desafiadoras mas alcançáveis, com critérios de sucesso claros e documentados. |
| 5 | Metas SMART com múltiplas dimensões e interdependências mapeadas entre diferentes áreas e níveis organizacionais. |
| 6 | Sistema dinâmico de metas SMART que se auto-ajustam baseado em dados em tempo real e contexto de negócio, mantendo relevância e desafio apropriado. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentos de metas verificando presença de elementos SMART (especificidade, métricas,
          prazos, relevância).
- Templates e frameworks utilizados para definição de metas (OKR canvas, formulários SMART).

- Matriz de metas com detalhamento de cada critério SMART.

- Exemplos de metas bem formuladas vs. mal formuladas em documentação.

- Guias internos de formulação de metas.

##### Métricas/KPIs

- % de metas que atendem todos os critérios SMART (auditoria de qualidade de metas).

- % de metas com métricas quantitativas vs. qualitativas.

- % de metas com prazo definido e responsável claro.

- Clareza percebida das metas por colaboradores (pesquisa/survey).

- Taxa de alcance de metas correlacionada com especificidade (metas SMART têm maior taxa
          de alcance).
- Tempo médio para definir uma meta (muito rápido pode indicar falta de rigor).

##### Sinais por nível

- Nível 0:


  - metas como “melhorar produção”, “aumentar qualidade”, sem números ou datas


- Nível 1:


  - metas com algum número ("aumentar 10%") mas sem contexto temporal ou baseline


<!-- pág. original: 164/465 -->
- Nível 2:


  - metas com número e prazo, mas sem clareza de como medir ou se é alcançável


- Nível 3:


  - metas seguem estrutura SMART básica

  - maioria tem todos elementos presentes


- Nível 4:


  - metas SMART consistentes

  - revisão de qualidade garante elementos bem definidos

  - desafio apropriado


- Nível 5:


  - metas complexas que consideram múltiplas variáveis

  - interdependências entre metas documentadas

  - cenários alternativos


- Nível 6:


  - sistema que monitora qualidade SMART automaticamente

  - ajusta dinamicamente dificuldade

  - sugere refinamentos baseados em dados

##### Amostragem

- Amostragem Analisar amostra de 20-30 metas de diferentes áreas e níveis hierárquicos

- Para cada meta, avaliar presença e qualidade de cada critério SMART individualmente (0-5
       pontos)
- Calcular score médio SMART da organização


<!-- pág. original: 165/465 -->
- Entrevistar 5-8 colaboradores sobre clareza e compreensão de suas metas


##### I.14.5.3 Questão: Qual o nível de transparência e visibilidade das metas individuais,...
Qual o nível de transparência e visibilidade das metas individuais, de equipe e organizacionais?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Metas confidenciais, conhecidas apenas pela liderança sênior. Não há compartilhamento estruturado. |
| 1 | Metas individuais privadas, compartilhadas apenas entre líder e liderado em conversas 1:1. |
| 2 | Metas de equipe compartilhadas dentro do time, mas não há visibilidade entre diferentes áreas ou departamentos. |
| 3 | Metas organizacionais públicas e acessíveis, metas individuais parcialmente visíveis dentro da organização. |
| 4 | Alta transparência - todas as metas (individuais, equipe, organizacionais) visíveis para toda a organização através de sistemas integrados. |
| 5 | Transparência total com dashboards públicos e acessíveis em tempo real por todos os colaboradores, incluindo progresso e status. |
| 6 | Transparência radical com visualização em tempo real de contribuições individuais para metas coletivas, impacto organizacional e interdependências visíveis. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Sistemas de gestão de metas (OKR tools, HRIS, performance management systems) e
          configurações de acesso.
- Políticas de transparência de metas e diretrizes de compartilhamento.

- Níveis de acesso e permissões em sistemas (quem pode ver quais metas).

- Dashboards públicos e sua frequência de atualização.


<!-- pág. original: 166/465 -->
- Intranet/wikis com metas organizacionais publicadas.

- All-hands presentations compartilhando metas.

##### Métricas/KPIs

- % de metas visíveis para toda organização vs. restritas.

- Frequência de acesso a dashboards de metas por colaborador.

- % de colaboradores que conseguem visualizar metas de outras áreas/níveis. Índice de
        transparência percebida (pesquisa sobre conhecimento de metas alheias).
- Tempo médio até meta ser publicada após definição.

- Taxa de atualização de status de metas em sistemas públicos.

##### Sinais por nível

- Nível 0:


  - metas em documentos locais da liderança

  - colaboradores não têm acesso


- Nível 1:


  - metas individuais apenas em 1:1s ou sistemas com acesso restrito


- Nível 2:


  - metas de equipe em boards/drives do time

  - silos entre áreas


- Nível 3:


  - metas estratégicas em apresentações/intranet

  - individuais parcialmente acessíveis (mesmo nível hierárquico)


- Nível 4:


<!-- pág. original: 167/465 -->
  - sistema centralizado onde todos podem buscar e visualizar metas de qualquer pessoa/área


- Nível 5:


  - dashboards ao vivo mostrando progresso

  - atualizações frequentes (semanal/diária)

  - cultura de transparência


- Nível 6:


  - visualização de rede de metas mostrando como trabalho individual conecta-se a objetivos coletivos
  - gamificação de progresso visível

##### Amostragem

- Amostragem Testar níveis de acesso a metas: tentar acessar metas de diferentes níveis
          hierárquicos e áreas funcionais
- Entrevistar 8-12 colaboradores de diversos níveis sobre: conhecimento das metas de outras
          áreas, facilidade de acesso, cultura de compartilhamento
- Verificar última atualização de metas em sistemas públicos


##### I.14.5.4 Questão: Qual a frequência dos ciclos de definição, revisão e ajuste de metas?
Qual a frequência dos ciclos de definição, revisão e ajuste de metas?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Sem ciclos definidos ou metas permanentes sem revisão estruturada. Ajustes apenas reativos. |
| 1 | Ciclos anuais rígidos com pouca ou nenhuma flexibilidade para ajustes durante o ano. |
| 2 | Ciclos anuais com revisão mid-year (semestral) para ajustes pontuais baseados em mudanças significativas. |
| 3 | Ciclos trimestrais ou semestrais com revisões estruturadas e documentadas, permitindo ajustes planejados. |
| 4 | Ciclos bimestrais ou mensais com acompanhamento contínuo, rituais regulares e ajustes frequentes baseados em dados. |
| 5 | Ciclos curtos tipo sprint (2-4 semanas) com rituais ágeis de planejamento, revisão e retrospectiva; alta cadência de ajustes. |
| 6 | Metas adaptativas com revisão contínua baseada em dados em tempo real, ajustes automáticos e dinâmicos conforme contexto. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Calendário de ciclos de metas e rituais associados (planning, reviews, retrospectives).

- Atas de reuniões de revisão de metas ao longo do tempo.

- Histórico de versões de metas em sistemas, mostrando ajustes e modificações.

- Políticas de gestão de metas especificando frequência de ciclos.

- Cronograma anual de processos de RH/gestão de performance.

- Templates de revisão com campos de ajustes e justificativas.

##### Métricas/KPIs

- Duração média dos ciclos de metas (em dias/semanas).

- Frequência de revisões formais por ano/trimestre.

- % de metas que foram ajustadas durante o ciclo (vs. mantidas inalteradas até o fim).

- Tempo médio entre identificação de necessidade de mudança e efetivo ajuste de meta.

- Taxa de participação em rituais de revisão.

- Número de iterações de uma meta antes de ser considerada completa.

##### Sinais por nível

- Nível 0:


<!-- pág. original: 169/465 -->
  - metas definidas informalmente e raramente revisitadas

  - sem calendário


- Nível 1:


  - ciclo anual fixo (ex

  - : definição em janeiro, avaliação em dezembro)

  - metas não mudam


- Nível 2:


  - ciclo anual com check-in semestral

  - ajustes apenas se mudança drástica no negócio


- Nível 3:


  - ciclos trimestrais ou semestrais estabelecidos

  - atas documentam revisões

  - alguns ajustes permitidos


- Nível 4:


  - ciclos mensais ou bimestrais

  - rituais regulares (monthly reviews)

  - dados guiam ajustes

  - cultura de adaptação


- Nível 5:


  - sprints de 2-4 semanas


<!-- pág. original: 170/465 -->
  - planning/review/retro regulares

  - metas de curto prazo alinhadas a objetivos maiores

  - alta flexibilidade


- Nível 6:


  - monitoramento contínuo com alertas automáticos

  - metas ajustadas em tempo quase real baseado em dashboards

  - cultura de experimentação rápida

##### Amostragem

- Amostragem Rastrear histórico de 10-15 metas ao longo de 12 meses

- Para cada meta, documentar: data de definição inicial, datas de todas as revisões, natureza
          dos ajustes (escopo, métrica, prazo), razão documentada para ajuste
- Calcular tempo médio entre revisões

- Verificar aderência ao calendário planejado de revisões


##### I.14.5.5 Questão: Como as metas individuais e de equipe conectam-se ao propósito e...
Como as metas individuais e de equipe conectam-se ao propósito e visão de longo prazo da
organização?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Sem propósito organizacional claro ou conexão explícita com metas estabelecidas. Metas puramente operacionais. |
| 1 | Propósito organizacional existe e é comunicado, mas desconectado das metas operacionais e individuais diárias. |
| 2 | Metas estratégicas de alto nível conectadas ao propósito, mas metas operacionais e individuais ainda desalinhadas. |
| 3 | Conexão explícita entre a maioria das metas e o propósito organizacional, documentada formalmente na definição de metas. |
| 4 | Todas as metas articulam claramente sua contribuição ao propósito e impacto organizacional esperado. Narrativa presente. |
| 5 | Sistema robusto de narrativas que conecta cada meta individual ao impacto organizacional e social de forma tangível e inspiradora. |
| 6 | Cultura onde propósito é vivenciado diariamente, com visualização em tempo real do impacto individual no propósito coletivo; celebração de contribuições. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentos de propósito, missão e visão organizacional amplamente divulgados.

- Matriz de conexão entre metas e propósito (cascading from purpose).

- Templates de metas com campo obrigatório de “contribuição ao propósito”.

- Comunicações e apresentações que articulam o “porquê” das metas.

- Storytelling em all-hands e town halls conectando trabalho individual a impacto maior.

- Onboarding materials que explicam propósito.

##### Métricas/KPIs

- % de metas que explicitam conexão com propósito em sua descrição.

- Compreensão do propósito pelos colaboradores (pesquisa: “você sabe o propósito da
         empresa?”).
- % de colaboradores que conseguem articular como seu trabalho contribui para propósito
         (pesquisa).
- Motivação intrínseca relacionada ao propósito (eNPS, engagement scores). Índice de
         alinhamento entre valores pessoais e organizacionais.
- Turnover correlacionado com senso de propósito.


<!-- pág. original: 172/465 -->
##### Sinais por nível

- Nível 0:


  - propósito inexistente ou desconhecido

  - metas puramente numéricas sem contexto maior


- Nível 1:


  - propósito em parede/site mas não mencionado em conversas de metas

  - desconexão clara


- Nível 2:


  - metas estratégicas do C-level mencionam propósito

  - metas operacionais não fazem essa ponte


- Nível 3:


  - maioria das metas tem campo “por que isso importa” preenchido

  - referência ao propósito em documentação


- Nível 4:


  - todas as metas incluem narrativa clara de contribuição

  - líderes consistentemente fazem essa conexão em comunicações


- Nível 5:


  - histórias e exemplos concretos de como trabalho individual impactou propósito

  - cultura de storytelling

  - reconhecimento baseado em impacto


<!-- pág. original: 173/465 -->
- Nível 6:


  - dashboards mostram contribuição em tempo real para objetivos de propósito

  - celebrações frequentes

  - propósito guia decisões diárias visivelmente

##### Amostragem

- Amostragem Analisar 20-30 metas de diferentes níveis verificando presença de narrativa de
          conexão com propósito (sim/não/parcial)
- Entrevistar 10-15 colaboradores de diversos níveis com perguntas: “Qual o propósito da
          organização?”, “Como seu trabalho contribui para ele?”, “Você sente que seu trabalho tem
          impacto maior?”
- Avaliar qualidade das respostas (específicas vs

- vagas)

- Revisar últimas 3-5 comunicações de liderança sobre metas verificando menção a propósito


##### I.14.5.6 Questão: Como dados, métricas e analytics são utilizados no processo de...
Como dados, métricas e analytics são utilizados no processo de definição e acompanhamento de
metas?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Metas definidas sem base em dados, apenas intuição ou experiência da liderança. Decisões puramente qualitativas. |
| 1 | Uso básico de dados históricos para contextualizar metas, mas sem análise estruturada ou sistemática. |
| 2 | Análise de dados históricos estruturada para definir metas (baselines, trends), mas sem ferramentas dedicadas ou processos formais. |
| 3 | Uso de dashboards e relatórios periódicos para acompanhar progresso e ajustar metas. Analytics descritivos consolidados. |
| 4 | Analytics avançados com indicadores preditivos e benchmarking externo para definição de metas. Análise de causas e correlações. |
| 5 | Sistema integrado de business intelligence com análises preditivas e prescritivas em tempo real. Simulações e cenários. |
| 6 | Inteligência artificial e machine learning para otimização contínua e automática de metas baseada em múltiplas variáveis e contexto dinâmico. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Relatórios de análise de dados utilizados na definição de metas (data packs, business reviews).

- Dashboards e ferramentas de BI (Tableau, PowerBI, Looker) com métricas de performance.

- Registros de benchmarking e comparações com mercado/competidores.

- Modelos preditivos e simulações usadas no planejamento.

- Data catalog com fontes de dados disponíveis para análise.

- Decision logs citando dados que embasaram metas.

##### Métricas/KPIs

- % de metas definidas com base em análise de dados documentada (vs. intuição).

- Frequência de uso de dashboards por líderes e times.

- % de metas com baseline histórico documentado.

- Qualidade das fontes de dados (atualização, completude, confiabilidade).

- Sofisticação das análises (descritiva, diagnóstica, preditiva, prescritiva).

- Tempo de acesso a dados para tomada de decisão.

- % de decisões com simulações/modelagens prévias.

##### Sinais por nível

- Nível 0:


<!-- pág. original: 175/465 -->
  - metas tipo “aumentar 10%” sem análise de viabilidade ou histórico

  - decisões de feeling


- Nível 1:


  - dados históricos consultados informalmente (planilhas pessoais)

  - não há processo estruturado


- Nível 2:


  - relatórios periódicos (mensais/trimestrais) usados para contextualizar

  - análise retrospectiva básica


- Nível 3:


  - dashboards consolidados acessados regularmente

  - métricas padronizadas

  - análise descritiva do que aconteceu


- Nível 4:


  - análise de causas com dados (por que aconteceu)

  - benchmarking sistemático

  - correlações identificadas

  - dados guiam ambição das metas


- Nível 5:


  - modelos preditivos (o que vai acontecer)

  - simulações de cenários

  - análises what-if


<!-- pág. original: 176/465 -->
  - metas otimizadas por algoritmos

  - prescrições


- Nível 6:


  - AI/ML monitorando performance em tempo real

  - ajustes automáticos de metas

  - aprendizado contínuo

  - otimização multi-objetivo

##### Amostragem

- Amostragem Revisar processo de definição de 15-20 metas, rastreando: quais dados foram
        consultados, que análises foram feitas, como dados influenciaram decisão final
- Entrevistar 5-8 líderes sobre processo de uso de dados na definição de metas

- Avaliar maturidade das ferramentas de analytics disponíveis e taxa de adoção

#### Glossário
[Sem glossário]
### I.15 Dimensão: Colaboração inter e intra-organização

#### I.15.1 Capacidade: Comunicação aberta
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Colaboração inter e intra-organização

#### Resumo Descritivo
A Colaboração Inter e Intra Empresarial refere-se ao processo de trabalhar em conjunto, por meio de
equipes multifuncionais e com parceiros externos, para alcançar uma visão e propósito
compartilhados. A comunicação aberta estabelece canais formais e transparentes que permitem o
compartilhamento efetivo de informações, ideias e conhecimento entre diferentes áreas, níveis
hierárquicos e organizações, promovendo a cooperação, coordenação e integração necessárias para
a transformação digital.
#### Questões
##### I.15.1.1 Questão: Como a comunicação e o compartilhamento de informações acontecem...
Como a comunicação e o compartilhamento de informações acontecem entre diferentes equipes,
áreas e parceiros externos na sua organização?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A comunicação acontece de forma informal e ad hoc. Equipes trabalham em silos, e o compartilhamento de informações ocorre apenas casualmente, sem estrutura ou registro. |
| 1 | Canais formais são estabelecidos para comunicação e compartilhamento de informações entre equipes. Existem procedimentos definidos, mas a comunicação ainda é limitada e reativa. |
| 2 | Canais formais permitem que equipes cooperem em tarefas e projetos pontuais. Há instrumentos visíveis para compartilhamento de informações, mas a colaboração depende de mediação da liderança. |
| 3 | Equipes têm autonomia para fazer ajustes que facilitam a cooperação. A comunicação é mais proativa, com reuniões regulares e compartilhamento estruturado de informações entre áreas. |
| 4 | Equipes compartilham recursos, responsabilidades e riscos em projetos discretos e de longo prazo. A comunicação é bidirecional, transparente e baseada em dados quantificáveis. |
| 5 | Canais formais permitem a formação dinâmica de equipes para trabalhar em projetos multifuncionais com metas, recursos e KPIs compartilhados. A comunicação é totalmente transparente e integrada. |
| 6 | A organização opera como uma rede altamente adaptável com comunicação em tempo real. Equipes se formam e se ajustam dinamicamente, com total transparência de informações e decisões distribuídas. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Calendário de rituais interfuncionais (cadência, pauta e presença).

- Atas de reuniões com lista de participantes e decisões.

- Plataformas de comunicação (Slack, Teams, Confluence) com histórico de canais e threads.

- RAACIs/matrizes de responsabilidade compartilhadas.

- Portais de conhecimento e wikis corporativos com métricas de acesso.

- Documentos de governança de comunicação e protocolos de compartilhamento de informação.

- Acordos de colaboração e parcerias com stakeholders externos.

##### Métricas/KPIs

- Taxa de participação em canais de comunicação por função/área.

- Número de interações entre áreas (mensagens, reuniões, documentos compartilhados).

- Tempo de resposta médio entre áreas.

- Taxa de retrabalho ou falhas de comunicação.


<!-- pág. original: 18/465 -->
- Número de projetos/iniciativas interáreas concluídos por período. Índice de transparência (% de
        decisões e informações documentadas e acessíveis).
- NPS interno de comunicação e colaboração.

##### Sinais por nível

- Nível 0:


  - Comunicação informal e verbal

  - silos organizacionais

  - ausência de documentação

  - handoffs não estruturados


- Nível 1:


  - Canais formais existem mas pouco utilizados

  - comunicação predominantemente top-down

  - informações concentradas em poucos indivíduos


- Nível 2:


  - Procedimentos de comunicação definidos

  - compartilhamento reativo

  - colaboração pontual mediada pela liderança

  - baixa autonomia das equipes


- Nível 3:


  - Reuniões regulares interfuncionais

  - equipes têm autonomia para ajustar processos de comunicação

  - início de compartilhamento proativo de informações


<!-- pág. original: 19/465 -->
- Nível 4:


  - Comunicação bidirecional e transparente

  - dados quantitativos suportam discussões

  - responsabilidades e riscos parcialmente compartilhados

  - rotinas de comunicação bem estabelecidas


- Nível 5:


  - Canais integrados e transparentes

  - equipes multifuncionais se formam dinamicamente

  - metas e KPIs compartilhados

  - alta colaboração baseada em dados preditivos


- Nível 6:


  - Rede adaptativa com comunicação em tempo real

  - transparência total

  - decisões distribuídas

  - ajustes dinâmicos e autônomos

  - cultura de compartilhamento arraigada

##### Amostragem

- Amostragem Selecionar 3-5 iniciativas recentes que exigiram colaboração entre áreas ou com
        parceiros externos e mapear o fluxo de comunicação (frequência, canais, participantes, tempo
        de resposta, qualidade das informações compartilhadas)
- Entrevistar representantes de diferentes áreas sobre a efetividade dos canais de comunicação

- Analisar atas de reuniões interfuncionais dos últimos 90 dias


##### I.15.1.2 Questão: Como a organização compartilha informações estratégicas, decisões e...
Como a organização compartilha informações estratégicas, decisões e mudanças com todos os níveis
hierárquicos?


<!-- pág. original: 20/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Informações estratégicas são mantidas apenas na alta liderança, sem comunicação formal. Decisões não são compartilhadas ou justificadas. |
| 1 | Comunicação top-down básica apenas quando estritamente necessário. Informações compartilhadas de forma seletiva e tardia. |
| 2 | Informações são compartilhadas formalmente através de canais oficiais, mas de forma seletiva e com atraso significativo. Pouca justificativa das decisões. |
| 3 | Comunicação regular de informações estratégicas através de múltiplos canais formais. Decisões importantes são comunicadas com contexto básico. |
| 4 | Transparência estruturada com dashboards acessíveis, comunicação frequente e bidirecional. Decisões são explicadas com dados e contexto. |
| 5 | Transparência total com acesso em tempo real a informações estratégicas, métricas de desempenho e processos decisórios. Comunicação proativa e bidirecional. |
| 6 | Cultura de transparência radical com governança distribuída, comunicação contínua em tempo real e acesso universal a todas as informações relevantes. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentos de política de transparência organizacional (governança de comunicação).

- Cronogramas de comunicações oficiais (town halls, all-hands meetings, newsletters
         executivas).
- Plataformas de comunicação institucional (intranet, portais, aplicativos corporativos).

- Atas de comitês executivos e decisões estratégicas publicadas.


<!-- pág. original: 21/465 -->
- Gravações ou transcrições de reuniões de liderança compartilhadas.

- Políticas de acesso à informação e classificação de dados.

- Canais de comunicação bidirecional (fóruns, AMAs - Ask Me Anything).

- Pesquisas de transparência e confiança organizacional.

- Métricas de acesso e engajamento com comunicações institucionais.

##### Métricas/KPIs

- Taxa de abertura de comunicações oficiais (e-mails, newsletters).

- Frequência de comunicações top-down vs bottom-up.

- Tempo médio entre decisão estratégica e comunicação formal.

- % de decisões com contexto e justificativa compartilhados. Índice de transparência percebida
        (survey).
- NPS interno de comunicação da liderança.

- Taxa de participação em canais bidirecionais (perguntas em AMAs, postagens em fóruns).

- % de colaboradores que se sentem informados sobre estratégia (pesquisa de clima).

##### Sinais por nível

- Nível 0:


  - informações estratégicas restritas à alta liderança

  - sem comunicação formal de decisões

  - colaboradores desconhecem estratégia e mudanças

  - ausência de canais de comunicação descendente


- Nível 1:


  - comunicação top-down esporádica

  - informações compartilhadas apenas quando necessário

  - atrasos na comunicação de mudanças

  - seletividade no compartilhamento


<!-- pág. original: 22/465 -->
- Nível 2:


  - canais oficiais de comunicação existem

  - informações compartilhadas com atraso significativo

  - seletividade no que é comunicado

  - justificativas limitadas ou ausentes


- Nível 3:


  - múltiplos canais formais de comunicação

  - comunicação regular e programada

  - decisões importantes comunicadas com contexto básico

  - calendário de comunicações estruturado


- Nível 4:


  - dashboards acessíveis a todos

  - comunicação frequente e bidirecional

  - decisões explicadas com dados e contexto

  - canais para perguntas e feedback


- Nível 5:


  - acesso em tempo real a informações estratégicas

  - métricas de desempenho transparentes

  - comunicação proativa da liderança

  - processos decisórios visíveis


- Nível 6:


<!-- pág. original: 23/465 -->
  - transparência radical institucionalizada

  - governança distribuída e participativa

  - comunicação contínua em tempo real

  - acesso universal a todas informações

  - cultura de abertura total

##### Amostragem

- Mapear todas as comunicações estratégicas dos últimos 90 dias: tipo, canal, audiência, timing
          entre decisão e comunicação, presença de contexto/justificativa
- Entrevistar 8-12 colaboradores de diferentes níveis sobre percepção de transparência e acesso
          à informação
- Analisar políticas de governança de comunicação e classificação de informações


##### I.15.1.3 Questão: Como a organização pratica e incentiva o feedback contínuo entre...
Como a organização pratica e incentiva o feedback contínuo entre líderes, equipes e colaboradores?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existe prática formal de feedback. Feedback acontece raramente e de forma ad hoc, geralmente apenas negativo ou em situações de crise. |
| 1 | Feedback anual via avaliação de desempenho formal. Processo burocrático e unidirecional (líder → colaborador). |
| 2 | Feedback trimestral ou semestral estruturado, mas ainda limitado ao fluxo top-down. Pouca abertura para feedback upward ou lateral. |
| 3 | Feedback mensal com canais formais estabelecidos. Início de feedback bidirecional (upward e downward), mas ainda irregular. |
| 4 | Feedback contínuo e multidirecional (upward, downward, lateral) com ferramentas digitais. Cultura que valoriza feedback construtivo. |
| 5 | Cultura forte de feedback em tempo real com feedback 360°, ferramentas automatizadas e alta segurança psicológica. |
| 6 | Feedback contínuo totalmente integrado ao fluxo de trabalho, com IA para análise de padrões, reconhecimento automatizado e coaching contínuo. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Sistema de gestão de performance e feedback (HRIS, plataformas de feedback contínuo).

- Registros de sessões de feedback (1:1s, avaliações, check-ins).

- Templates e guias de feedback estruturado.

- Calendário de ciclos de feedback.

- Plataformas de feedback 360° e multi-rater.

- Pesquisas de clima sobre cultura de feedback.

- Programas de treinamento em dar e receber feedback.

- Métricas de frequência e qualidade de feedback.

- Canais de feedback anônimo.

- Políticas de segurança psicológica e feedback construtivo.

##### Métricas/KPIs

- Frequência média de feedback (dias entre sessões).

- % de colaboradores que receberam feedback no último mês/trimestre.

- Taxa de uso de ferramentas de feedback. Índice de segurança psicológica (survey).

- % de feedback multidirecional vs unidirecional.

- NPS de qualidade do feedback recebido.

- Tempo médio de resposta a feedback (closure do loop).

- % de colaboradores treinados em práticas de feedback.


<!-- pág. original: 25/465 -->
- Correlação entre frequência de feedback e engajamento.

##### Sinais por nível

- Nível 0:


  - ausência de práticas formais de feedback

  - feedback esporádico e apenas negativo

  - foco em críticas durante crises

  - sem estrutura ou processos


- Nível 1:


  - avaliação de desempenho anual formal

  - processo burocrático

  - feedback unidirecional (líder para colaborador)

  - sem feedback upward ou lateral


- Nível 2:


  - feedback trimestral ou semestral estruturado

  - limitado ao fluxo top-down

  - baixa abertura para feedback upward

  - feedback lateral inexistente


- Nível 3:


  - feedback mensal com canais formais

  - início de feedback bidirecional

  - upward feedback ainda irregular

  - abertura crescente mas inconsistente


<!-- pág. original: 26/465 -->
- Nível 4:


  - feedback contínuo e multidirecional

  - ferramentas digitais para feedback

  - cultura que valoriza feedback construtivo

  - feedback upward, downward e lateral estabelecidos


- Nível 5:


  - feedback em tempo real

  - feedback 360° estruturado

  - ferramentas automatizadas

  - alta segurança psicológica

  - cultura forte de feedback


- Nível 6:


  - feedback integrado ao fluxo de trabalho

  - IA para análise de padrões

  - reconhecimento automatizado

  - coaching contínuo

  - cultura de melhoria contínua enraizada

##### Amostragem

- Analisar registros de feedback dos últimos 6 meses: frequência, direção
       (upward/downward/lateral), qualidade, ações resultantes
- Entrevistar 10-15 colaboradores de diferentes níveis sobre experiência com feedback

- Revisar ferramentas e plataformas disponíveis

- Analisar pesquisas de clima sobre segurança psicológica e cultura de feedback


<!-- pág. original: 27/465 -->
##### I.15.1.4 Questão: Como a organização comunica durante crises, mudanças significativas...
Como a organização comunica durante crises, mudanças significativas ou situações de incerteza?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Silêncio ou comunicação muito inconsistente durante crises. Rumores e desinformação proliferam. Alta ansiedade organizacional. |
| 1 | Comunicação mínima e tardia, apenas quando pressionado. Mensagens vagas e pouco esclarecedoras. |
| 2 | Comunicação formal mas limitada e altamente controlada. Informações parciais, causando especulação e ansiedade. |
| 3 | Comunicação regular durante crises mas ainda predominantemente top-down. Atualizações periódicas com informações relevantes. |
| 4 | Comunicação transparente e frequente com espaço para dúvidas e preocupações. Liderança visível e acessível. |
| 5 | Comunicação em tempo real através de múltiplos canais bidirecionais. Alta transparência, empatia e responsividade a questões. |
| 6 | Comunicação radical e contínua com transparência total, canais bidirecionais ativos, co-criação de soluções e governança participativa. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Plano de comunicação de crise documentado.

- Protocolos de comunicação em situações de emergência.

- Histórico de comunicações durante crises anteriores (e-mails, town halls, vídeos).

- Canais de comunicação de emergência (aplicativos, SMS, hotlines).

- Pesquisas de percepção durante e após crises.


<!-- pág. original: 28/465 -->
- Atas de reuniões de gestão de crise.

- FAQs atualizados durante crises.

- Registros de perguntas e respostas em canais bidirecionais.

- Análise de sentimento durante períodos de crise.

- Treinamentos de porta-vozes e gestão de crise.

##### Métricas/KPIs

- Tempo entre início da crise e primeira comunicação oficial.

- Frequência de atualizações durante crise.

- Taxa de abertura/visualização de comunicações de crise.

- % de colaboradores que se sentem informados durante crises (survey).

- Número de perguntas recebidas vs respondidas.

- Tempo médio de resposta a perguntas. Índice de ansiedade organizacional (survey pré e pós).

- Taxa de disseminação de rumores/desinformação.

- NPS de comunicação de crise.

##### Sinais por nível

- Nível 0:


  - silêncio ou comunicação inconsistente

  - proliferação de rumores

  - alta ansiedade organizacional

  - desinformação disseminada


- Nível 1:


  - comunicação mínima e tardia

  - mensagens apenas quando pressionado

  - conteúdo vago e pouco claro

  - falta de proatividade


<!-- pág. original: 29/465 -->
- Nível 2:


  - comunicação formal mas limitada

  - alto controle sobre informações

  - informações parciais

  - especulação e ansiedade persistem


- Nível 3:


  - comunicação regular durante crises

  - fluxo predominantemente top-down

  - atualizações periódicas

  - informações relevantes compartilhadas


- Nível 4:


  - comunicação transparente e frequente

  - espaço para dúvidas e preocupações

  - liderança visível e acessível

  - canais bidirecionais ativos


- Nível 5:


  - comunicação em tempo real

  - múltiplos canais bidirecionais

  - alta transparência

  - empatia e responsividade

  - questões respondidas rapidamente


<!-- pág. original: 30/465 -->
- Nível 6:


  - comunicação radical e contínua

  - transparência total

  - co-criação de soluções

  - governança participativa em crises

  - colaboradores como agentes ativos

##### Amostragem

- Analisar as 3-5 crises ou mudanças significativas mais recentes: tempo de resposta, frequência
          de comunicação, canais utilizados, transparência, responsividade
- Entrevistar 10-15 colaboradores sobre experiência de comunicação durante crises

- Revisar planos de comunicação de crise

- Analisar pesquisas de clima durante e após crises


##### I.15.1.5 Questão: Como a organização pratica a escuta ativa, capturando e respondendo...
Como a organização pratica a escuta ativa, capturando e respondendo às preocupações, ideias e
sentimentos dos colaboradores?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Sem mecanismos de escuta. Comunicação totalmente unidirecional (top-down). Colaboradores não têm voz. |
| 1 | Mecanismos básicos de escuta (caixa de sugestões física/digital) existem mas são raramente utilizados e sem resposta. |
| 2 | Canais de escuta existem mas as respostas são lentas, genéricas ou inexistentes. Colaboradores sentem que não são ouvidos. |
| 3 | Escuta estruturada com processos de captura e resposta estabelecidos. Fechamento do loop de feedback acontece mas ainda é lento. |
| 4 | Escuta ativa com análise sistemática de inputs, respostas tempestivas e fechamento consistente do loop de feedback. |
| 5 | Plataformas de escuta multicanal com análise de sentimento, categorização automática e resposta ágil. Alta responsividade. |
| 6 | Escuta contínua em tempo real com IA, análise preditiva de sentimentos, identificação proativa de problemas e ação preventiva. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Plataformas de escuta organizacional (caixas de sugestões digitais, pulse surveys, fóruns).

- Sistema de gestão de ideias e sugestões.

- Registros de inputs recebidos e status de resposta.

- Políticas de escuta ativa e tempo de resposta.

- Pesquisas de engajamento e clima.

- Canais de comunicação anônimos.

- Ferramentas de análise de sentimento.

- Atas de comitês de revisão de sugestões.

- Métricas de tempo de resposta e taxa de implementação.

- Programas de reconhecimento de ideias implementadas.

##### Métricas/KPIs

- Número de inputs recebidos por canal por período.

- Taxa de resposta a inputs (% respondidos).

- Tempo médio de resposta a inputs.

- Taxa de fechamento do loop (% com resolução comunicada).

- % de sugestões implementadas. Índice de satisfação com escuta organizacional (survey).

- Taxa de utilização de canais de escuta.


<!-- pág. original: 32/465 -->
- Diversidade de fontes de input (diferentes áreas, níveis).

- Correlação entre escuta ativa e engajamento.

- Tempo entre identificação de problema e ação corretiva.

##### Sinais por nível

- Nível 0:


  - ausência de mecanismos de escuta

  - comunicação totalmente unidirecional

  - colaboradores sem voz

  - sem canais para expressão


- Nível 1:


  - caixa de sugestões existe mas subutilizada

  - sem resposta a inputs

  - baixíssima utilização

  - percepção de inutilidade


- Nível 2:


  - canais de escuta existem

  - respostas lentas ou genéricas

  - colaboradores sentem que não são ouvidos

  - baixo fechamento do loop


- Nível 3:


  - processos estruturados de escuta

  - captura e resposta estabelecidos


<!-- pág. original: 33/465 -->
  - fechamento do loop acontece mas lento

  - responsividade moderada


- Nível 4:


  - análise sistemática de inputs

  - respostas tempestivas

  - fechamento consistente do loop

  - alta responsividade


- Nível 5:


  - plataformas multicanal integradas

  - análise de sentimento automatizada

  - categorização automática

  - resposta ágil

  - alta responsividade


- Nível 6:


  - escuta contínua em tempo real

  - IA para análise preditiva

  - identificação proativa de problemas

  - ação preventiva

  - cultura de escuta enraizada

##### Amostragem

- Analisar todos os inputs recebidos nos últimos 6 meses: volume, canais, temas, tempo de
       resposta, ações tomadas
- Entrevistar 10-15 colaboradores sobre percepção de escuta organizacional


<!-- pág. original: 34/465 -->
- Revisar processos e políticas de gestão de inputs

- Analisar taxa de implementação de sugestões e reconhecimento dado

#### Glossário
[Sem glossário]
#### I.15.2 Capacidade: Comunicação eficiente
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Colaboração inter e intra-organização

#### Resumo Descritivo
A comunicação entre colaboradores deve ser rastreável, livre de redundâncias e atender às
necessidades dos grupos de stakeholders, garantindo que a informação correta chegue à pessoa
certa, no momento certo e no formato adequado. O objetivo é reduzir o tempo que os funcionários
despendem procurando e esperando por informações, utilizando armazenamento centralizado de
dados (fonte única da verdade), assinaturas digitais para aprovações e sistemas de groupware para
suportar a comunicação contextualizada e eficiente.
#### Questões
##### I.15.2.1 Questão: Como a comunicação e a troca de informações são estruturadas e...
Como a comunicação e a troca de informações são estruturadas e gerenciadas na empresa?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A comunicação é predominantemente informal, baseada em conversas e trocas de e-mails não estruturados. Não há rastreabilidade e as informações são frequentemente duplicadas ou perdidas. |
| 1 | Existem canais de comunicação formais (ex. e-mail, pastas compartilhadas), mas o uso é inconsistente. O compartilhamento de arquivos como anexos é uma prática comum, levando a múltiplas versões e redundância. |
| 2 | A organização utiliza ferramentas digitais básicas para comunicação (ex aplicativos de mensagens), mas elas não são integradas aos processos de negócio. As aprovações ainda são tratadas de forma manual ou via e-mail. |
| 3 | Uma plataforma centralizada (groupware) é utilizada para armazenamento de documentos, estabelecendo uma "fonte única da verdade" para arquivos. A comunicação começa a ser contextualizada em canais ou grupos específicos. |
| 4 | A comunicação é rastreável e contextualizada, vinculada a processos de negócio (ex. ordens de produção, projetos). Aprovações são gerenciadas por meio de assinaturas digitais e fluxos de trabalho transparentes. |
| 5 | A comunicação é totalmente integrada aos sistemas de negócio (ERP, MES, PLM). Perfis de função e credenciais são usados para incluir colaboradores em processos de comunicação de forma contextual e automática. |
| 6 | Os sistemas de comunicação são proativos e inteligentes, analisando fluxos de trabalho para sugerir melhorias, automatizar a disseminação de informações e garantir que todos os stakeholders sejam informados em tempo real sobre o status dos processos. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Políticas e Procedimentos: Política de comunicação interna; Manual de uso de ferramentas de
         colaboração; Procedimentos para aprovação de documentos e decisões.


<!-- pág. original: 39/465 -->
- Sistemas: Plataformas de colaboração e groupware (ex: Microsoft Teams, Slack, intranets
        corporativas); Sistemas de Gestão Eletrônica de Documentos; Logs e trilhas de auditoria de
        sistemas que demonstrem fluxos de aprovação digital.
- Documentação: Atas de reunião com ações e responsáveis definidos em sistema; Registros de
        fluxos de aprovação digital; Documentação de projetos em repositórios centralizados.

##### Métricas/KPIs

- Tempo médio para aprovação de documentos, requisições ou decisões.

- Percentual de adesão e uso das plataformas de comunicação oficiais.

- Tempo médio gasto por funcionários na busca por informações (pode ser medido via pesquisa
        interna ou análise de sistemas).
- Redução no volume de e-mails internos com anexos em favor de links para uma fonte única da
        verdade.
- Índice de satisfação dos colaboradores com as ferramentas e processos de comunicação.

##### Sinais por nível

- Nível 0:


  - A principal fonte de informação é o "rádio corredor"

  - e-mails são longos e com múltiplos destinatários em cópia

  - a pergunta "qual é a última versão deste arquivo?" é frequente


- Nível 1:


  - Existem pastas compartilhadas em um servidor, mas a organização é caótica e o controle de versão é manual


- Nível 2:


  - A empresa adota um chat corporativo, mas ele é usado principalmente para conversas informais, enquanto a comunicação e as decisões importantes continuam por e-mail


- Nível 3:


<!-- pág. original: 40/465 -->
  - As equipes de projeto possuem seus próprios canais ou grupos na plataforma de colaboração, onde centralizam discussões e arquivos


- Nível 4:


  - A aprovação de uma requisição de compra gera notificações automáticas para os aprovadores, e todo o histórico fica registrado no sistema, de forma transparente e auditável


- Nível 5:


  - Ao abrir uma ordem de manutenção para uma máquina específica, o sistema automaticamente cria um grupo de comunicação com o técnico, o supervisor de produção e o planejador de manutenção, compartilhando a documentação técnica relevante


- Nível 6:


  - O sistema de comunicação identifica gargalos em processos de aprovação e sugere a delegação de tarefas ou a redefinição do fluxo para otimizar o tempo de resposta

##### Amostragem

- Amostragem Selecionar 3 a 5 processos de negócio críticos (ex: desenvolvimento de novo
        produto, gestão de não conformidade, planejamento de produção) e mapear como a
        comunicação e as aprovações ocorrem
- Realizar entrevistas com colaboradores de diferentes níveis e áreas (ex: chão de fábrica,
        engenharia, administrativo) para entender como eles se comunicam com outras equipes e
        como buscam as informações necessárias para seu trabalho
- Acompanhar uma reunião de equipe e observar como as decisões são documentadas e as
        tarefas são distribuídas e rastreadas
- Solicitar a demonstração do uso das ferramentas de colaboração para gerenciar um projeto em
        andamento

##### I.15.2.2 Questão: Como se dá a comunicação com Parceiros?
Como se dá a comunicação com Parceiros?


<!-- pág. original: 41/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A comunicação com fornecedores e clientes é totalmente manual (ex telefone, e-mails individuais, fax). Não há rastreabilidade e os dados precisam ser redigitados manualmente nos sistemas internos. |
| 1 | São utilizados métodos digitais básicos, mas não padronizados (ex ordens de compra enviadas como PDF por e-mail). A comunicação é reativa e os dados ainda são inseridos manualmente. |
| 2 | A empresa utiliza um canal digital unidirecional, como um portal simples onde disponibiliza informações (ex previsões de compra) para os parceiros baixarem, mas a interação (confirmação, NF-e) volta por e-mail. |
| 3 | Existe um portal de colaboração (ex Portal de Fornecedores) onde os parceiros podem interagir (ex: confirmar pedidos, enviar faturas, atualizar status). A comunicação é bidirecional, mas contida no portal (silo). |
| 4 | A comunicação é automatizada via integração de sistemas (ex EDI, APIs) para transações-chave (ex: pedidos, faturas). A troca de dados é estruturada e elimina a redigitação, mas é limitada a processos específicos. |
| 5 | A integração de sistemas é ampla e ocorre em tempo real, permitindo o compartilhamento de dados operacionais (ex status de produção do fornecedor, níveis de estoque do cliente). A comunicação é contextualizada e proativa. |
| 6 | Existe uma rede de valor dinâmica e conectada. Os sistemas da empresa e dos parceiros comunicam-se de forma autônoma para otimizar a cadeia (ex reabastecimento automático, ajuste dinâmico de planos de entrega). |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Sistemas: Existência e uso de Portais de Fornecedores ou Clientes; Logs de transações EDI
        (Electronic Data Interchange); Documentação de APIs (Interfaces de Programação de
        Aplicações) para parceiros.
- Documentação: Contratos ou Acordos de Nível de Serviço (SLAs) com parceiros que definem
        canais de comunicação; Manuais de integração para fornecedores.
- Processos: Mapeamento do fluxo de pedido de compra (Procure-to-Pay) e do fluxo de pedido
        de venda (Order-to-Cash) para identificar pontos de comunicação manual vs. automática.

##### Métricas/KPIs

- Percentual de pedidos de compra/venda processados "sem toque" (touchless).

- Tempo médio para confirmação de pedido por parte do fornecedor.

- Percentual de fornecedores críticos integrados via portal ou EDI/API.

- Acuracidade do On-Time Delivery in Full (OTIF) de fornecedores, correlacionada com a
        visibilidade da informação.
- Custo de processamento de pedidos (manual vs. automático).

##### Sinais por nível

- Nível 0:


  - "Preciso ligar para o fornecedor para saber se ele recebeu meu pedido


- Nível 1:


  - O departamento de compras envia e-mails em massa com planilhas de previsão para os fornecedores


- Nível 2:


  - O fornecedor reclama que precisa entrar "todo dia" no portal para ver se há algo novo, pois não recebe notificações


- Nível 3:


<!-- pág. original: 43/465 -->
  - Um fornecedor anexa a Nota Fiscal diretamente no pedido dentro do portal, e o sistema interno de recebimento é notificado


- Nível 4:


  - O pedido de compra é enviado do ERP da empresa e recebido diretamente no sistema de vendas do fornecedor, sem intervenção humana


- Nível 5:


  - O planejador de produção da empresa consegue ver, em seu próprio sistema, o status de produção (real) do item que está sendo fabricado no fornecedor


- Nível 6:


  - O sistema detecta um atraso na produção de um fornecedor A (via dados em tempo real) e automaticamente gera uma ordem de compra de emergência para o fornecedor B

##### Amostragem

- Amostragem Selecionar os 5 principais fornecedores (em volume ou criticidade) e verificar
         como a comunicação de pedidos, previsões e faturamento é realizada com cada um
- Acompanhar o processo de um pedido de cliente, desde o recebimento até a entrega, e
         mapear todos os pontos de comunicação com o cliente (confirmação, status, rastreamento,
         fatura)
- Entrevistar o time de Compras e o de Logística para entender como gerenciam exceções com
         parceiros (atrasos, problemas de qualidade)

##### I.15.2.3 Questão: Como se dá normalmente a comunicação entre os funcionários?
Como se dá normalmente a comunicação entre os funcionários?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | As instruções de trabalho são predominantemente verbais (ex "o supervisor explica o que fazer") e baseadas na experiência do colaborador. Não há suporte de sistemas. |
| 1 | As instruções de trabalho são documentos físicos (papel) estáticos, como folhas de processo ou especificações impressas, que ficam disponíveis no posto de trabalho. |
| 2 | As instruções são digitais (ex PDFs, arquivos de texto) e armazenadas em pastas de rede. O colaborador precisa localizar e abrir ativamente o documento correto para a tarefa. |
| 3 | Os sistemas (ex terminal MES) exibem a instrução de trabalho correta associada à ordem de produção ativa. A informação é contextual, mas apresentada de forma básica (texto, tabelas). |
| 4 | Os sistemas fornecem informações de forma visual e sensível ao contexto. Por exemplo, escanear um produto exibe seu modelo 3D, vídeos curtos de montagem ou seus pontos de verificação de qualidade. |
| 5 | A empresa utiliza sistemas de assistência avançados (ex Realidade Aumentada - AR) que fornecem orientação passo a passo, sobrepondo digitalmente a informação ao ambiente de trabalho real. |
| 6 | Os sistemas de assistência são adaptativos e proativos. Eles não apenas guiam o operador (ex AR), mas também validam a execução da tarefa em tempo real (ex: usando visão computacional) e documentam o processo automaticamente. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Postos de Trabalho: Verificar a presença de instruções impressas (pastas, quadros); Existência
         de terminais MES/SFC (Shop Floor Control).
- Sistemas: Software de gestão de Instruções de Trabalho (ITs); Módulos de MES que exibem
         ITs; Existência de software e hardware de Realidade Aumentada (AR) ou Realidade Mista
         (MR).
- Documentação: Padrão de criação e atualização de Instruções de Trabalho; Vídeos ou guias
         de montagem digitais.


<!-- pág. original: 45/465 -->
##### Métricas/KPIs

- Tempo médio de treinamento (onboarding) de um novo operador para uma tarefa.

- Taxa de erro humano (ex: refugos, retrabalho) por posto de trabalho.

- Tempo médio de ciclo da tarefa (Task Cycle Time) vs. tempo padrão.

- Aderência ao processo (quantas vezes o operador consulta a instrução).

##### Sinais por nível

- Nível 0:


  - "Eu aprendi olhando o colega do lado fazer


- Nível 1:


  - O operador consulta uma pasta de plástico com folhas de processo e com anotações manuais possivelmente desatualizadas


- Nível 2:


  - O operador precisa usar o computador do setor para abrir a "Pasta P" na rede, navegar até o modelo do produto e abrir o PDF da instrução


- Nível 3:


  - Ao dar "play" na ordem de produção no terminal da máquina, a tela exibe automaticamente as especificações e parâmetros daquela Ordem de Produção


- Nível 4:


  - O operador do controle de qualidade escaneia o código de barras da peça e o monitor exibe uma imagem destacando os 3 pontos exatos que ele deve medir


- Nível 5:


  - O técnico de manutenção usa um tablet ou óculos AR que projeta setas indicando qual componente da máquina deve ser inspecionado ou substituído


<!-- pág. original: 46/465 -->
- Nível 6:


  - O operador de montagem é guiado por luzes (pick-by-light) e, ao tentar pegar a peça errada, o sistema emite um alerta sonoro e visual antes que o erro ocorra

##### Amostragem

- Selecionar e observar 3 a 5 postos de trabalho críticos (ex: montagem complexa, setup de
        máquina, inspeção final)
- Pedir a um operador (um experiente e um novato) para demonstrar como eles acessam e
        utilizam as instruções de trabalho para uma tarefa específica
- Entrevistar a Engenharia de Processos ou Industrial sobre como as instruções são criadas,
        distribuídas, atualizadas e como medem sua eficácia
#### Glossário
[Sem glossário]
#### I.15.3 Capacidade: Comunidades flexíveis
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Colaboração inter e intra-organização

#### Resumo Descritivo
As comunidades flexíveis representam uma abordagem de configuração dinâmica de recursos
humanos, onde a estrutura de trabalho tradicional e rígida é substituída por uma organização baseada
em equipes orientadas a tarefas ou objetivos específicos
#### Questões


<!-- pág. original: 47/465 -->
##### I.15.3.1 Questão: Como a estrutura organizacional da empresa apoia a colaboração e a...
Como a estrutura organizacional da empresa apoia a colaboração e a formação dinâmica de equipes?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Estrutura organizacional tradicional e rígida, voltada para a operação eficiente de departamentos individuais (silos) |
| 1 | A empresa possui uma estrutura organizacional tradicional focada na eficiência departamental |
| 2 | Métodos tradicionais de gerenciamento de projetos são empregados; a abordagem é estruturada, mas pesada e carece de agilidade, dificultando ajustes rápidos |
| 3 | Estruturas operacionais tradicionais começam a ser quebradas; plataformas de colaboração são usadas para fortalecer a cooperação entre diferentes partes do negócio |
| 4 | Ocorre colaboração entre especialistas de diferentes departamentos; técnicas de gerenciamento ágil são usadas para processos de mudança |
| 5 | A estrutura organizacional é modificada para que a capacidade possa ser rapidamente ajustada a novas situações |
| 6 | Comunidades flexíveis e gerenciamento ágil de projetos criam uma organização orgânica; o trabalho é executado pelos funcionários com as habilidades corretas, independentemente da hierarquia ou departamento |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Plataformas de colaboração baseadas em TI

- Documentação de perfis de habilidades dos funcionários

- Ferramentas de gerenciamento de atribuições (Assignment management)

- Atas de reunião de equipes de projeto (Comunidades)


<!-- pág. original: 48/465 -->
- Organogramas (formais e funcionais/projetos)

##### Métricas/KPIs

- Transparência e Engajamento em Comunidades

- Dinamismo Organizacional

- Aceleração da Resposta a Eventos (Redução de Latência)

- Eficiência na Execução de Tarefas por Habilidade

- Medição de Desempenho de Equipes e Aprendizado

##### Sinais por nível

- Nível 0:


  - Estrutura organizacional tradicional e rígida, voltada para a operação eficiente de departamentos individuais isolados (silos)


- Nível 1:


  - A empresa possui uma estrutura organizacional tradicional focada na eficiência departamental


- Nível 2:


  - Métodos tradicionais de gerenciamento de projetos são empregados

  - A abordagem para mudança, embora estruturada, é pesada e carece de agilidade, dificultando ajustes rápidos


- Nível 3:


  - A organização começa a quebrar estruturas operacionais tradicionais

  - Os funcionários são envolvidos mais de perto nos processos de mudança


- Nível 4:


<!-- pág. original: 49/465 -->
  - Ocorre colaboração entre especialistas de diferentes departamentos

  - Técnicas de gerenciamento ágil são utilizadas para processos de mudança


- Nível 5:


  - A estrutura organizacional é modificada para que a capacidade possa ser rapidamente ajustada a novas situações


- Nível 6:


  - Comunidades flexíveis e gerenciamento ágil de projetos criam uma organização orgânica
  - O trabalho é executado por funcionários com as habilidades corretas, independentemente da hierarquia ou departamento

##### Amostragem

- Amostragem Entrevistas com funcionários de diferentes departamentos para avaliar a
          comunicação e colaboração interdepartamental
- Análise da composição de equipes de projeto, verificando se são temporárias ou permanentes
          e se reúnem membros de diferentes áreas
- Revisão de como as equipes são formadas (orientadas a tarefas ou hierarquia)


##### I.15.3.2 Questão: De que forma as ferramentas de TI e plataformas de colaboração dão...
De que forma as ferramentas de TI e plataformas de colaboração dão transparência às competências
dos funcionários para apoiar a formação de equipes flexíveis?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Nenhuma ferramenta de TI é usada para isso. A alocação de pessoas para tarefas ou equipes é baseada puramente no conhecimento pessoal e na memória dos gestores. |
| 1 | Listas básicas (ex planilhas, documentos de texto) de funcionários e suas funções existem, mas não há perfis de competências detalhados ou pesquisáveis. |
| 2 | Existem sistemas de TI (ex sistema de RH) que armazenam competências, mas esses dados são estáticos, raramente atualizados e não estão integrados às ferramentas de trabalho diário. |
| 3 | Ferramentas de colaboração (ex chats, intranets) são usadas, mas a identificação de competências ainda depende muito da rede de contatos pessoal; não há um sistema formal de "busca por especialistas". |
| 4 | Plataformas de TI (ex intranet avançada, perfis em ferramentas de colaboração) começam a fornecer transparência sobre os perfis de competências dos funcionários e seu envolvimento atual em projetos ou comunidades |
| 5 | Existem plataformas de TI integradas que facilitam ativamente a comunicação e dão suporte ao "assignment management" (gestão de alocação), permitindo pesquisar e encontrar especialistas de forma eficiente |
| 6 | As plataformas de TI não apenas dão transparência às competências existentes, mas também se integram a novas tecnologias de treinamento (ex Realidade Aumentada) para capacitar rapidamente os funcionários para novas tarefas, permitindo a formação de comunidades de forma ainda mais ágil |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Sistema de Informação de RH (HRIS) e seus módulos de competências.

- Plataformas de colaboração (ex: perfis de usuário no Microsoft Teams, Slack, Workplace).

- Intranet corporativa (ex: função "Páginas Amarelas" ou "Busca por Especialista").

- Software de gestão de projetos (ex: Jira, Asana) para verificar como as equipes são montadas
         e os recursos alocados.
- Plataformas de gestão de conhecimento (Knowledge Management).


<!-- pág. original: 51/465 -->
##### Métricas/KPIs

- Tempo médio para identificar e alocar um especialista para uma nova equipe/projeto.

- Taxa de atualização dos perfis de competências dos funcionários no sistema.

- Percentual de projetos/equipes formadas com membros de diferentes departamentos.

##### Sinais por nível

- Nível 0:


  - Inexistente

  - A identificação de competências é totalmente informal

  - Os gestores dependem da memória ou de perguntar a outros gestores ("quem sabe fazer X?")
  - Não há repositório digital de competências


- Nível 1:


  - Listas estáticas e isoladas

  - O RH ou os departamentos mantêm planilhas básicas listando funcionários e seus cargos ou treinamentos concluídos
  - Essas listas não são centralizadas, não são pesquisáveis e ficam rapidamente desatualizadas


- Nível 2:


  - Repositório passivo

  - Existe um sistema de RH (como um SIRH) onde as competências podem ser registradas (muitas vezes apenas para avaliações de desempenho)
  - O sistema funciona como um "currículo" digital, mas não é usado ativamente para formar equipes no dia a dia


- Nível 3:


  - Ferramentas de colaboração com perfis


<!-- pág. original: 52/465 -->
  - A empresa utiliza ferramentas de comunicação (como intranet ou chat corporativo) onde os funcionários podem preencher seus próprios perfis, incluindo um campo opcional de "habilidades"
  - A busca é simples e a qualidade da informação depende inteiramente do funcionário


- Nível 4:


  - Transparência ativa

  - Plataformas de colaboração baseadas em TI fornecem transparência sobre os perfis de competências dos funcionários
  - É possível pesquisar ativamente por habilidades (ex: "especialista em Python") e ver os perfis de quem as possui


- Nível 5:


  - Suporte à alocação (Assignment Management)

  - As plataformas de TI facilitam ativamente a comunicação e apoiam a gestão de alocação
  - Os gestores podem ver não apenas quem tem a competência, mas também verificar a disponibilidade (taxa de alocação) e o envolvimento atual dessa pessoa em outras comunidades ou projetos


- Nível 6:


  - Alocação inteligente e dinâmica

  - O sistema de TI sugere ativamente especialistas para novas tarefas com base nos requisitos do projeto
  - Ele usa dados (ex: projetos anteriores, feedback de 360º) para classificar o nível de proficiência e pode até identificar lacunas de competência na equipe e sugerir treinamentos rápidos

##### Amostragem

- Amostragem Simular uma busca por um especialista em uma competência específica (ex:
       "análise de dados Python") nas ferramentas internas e avaliar a facilidade e precisão dos
       resultados


<!-- pág. original: 53/465 -->
- Entrevistar gestores de projeto sobre como eles encontram e recrutam membros para suas
         equipes
- Verificar os perfis de funcionários nas plataformas de colaboração para ver se as competências
         estão listadas e se são pesquisáveis

##### I.15.3.3 Questão: Como a gestão de desempenho e os sistemas de metas estão adaptados...
Como a gestão de desempenho e os sistemas de metas estão adaptados para apoiar o trabalho em
equipes flexíveis e multifuncionais?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A avaliação de desempenho e as metas são 100% individuais e definidas estritamente dentro dos silos departamentais. Não há reconhecimento formal do trabalho interdepartamental. |
| 1 | As metas são puramente departamentais e muitas vezes unidimensionais (ex "número de peças produzidas"). O trabalho em projetos fora do departamento não é formalmente reconhecido. |
| 2 | A avaliação de desempenho é tradicional e totalmente controlada pelo gerente departamental. O trabalho em equipes multifuncionais pode ser mencionado informalmente, mas não tem peso estruturado na avaliação. |
| 3 | A organização reconhece a colaboração. A avaliação de desempenho inclui um item genérico sobre "trabalho em equipe", mas as metas principais ainda são departamentais. O feedback de outros líderes é esporádico. |
| 4 | A empresa começa a introduzir metas multidimensionais. O feedback de líderes de projeto ou comunidade é solicitado formalmente durante a avaliação de desempenho, embora o gerente departamental ainda tenha a decisão final. |
| 5 | São implementados sistemas de metas motivacionais que equilibram objetivos departamentais (funcionais) e objetivos de equipe (projeto/comunidade). A avaliação de desempenho considera formalmente o feedback de múltiplos líderes (matricial). |
| 6 | O sucesso da equipe de especialistas/comunidade é formalmente medido (ex controladoria financeira de comunidades). Os sistemas de metas e incentivos (monetários e não monetários) estão diretamente alinhados aos resultados da equipe, e não apenas aos silos departamentais. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Formulários de avaliação de desempenho (ex: verificar se há campos para feedback de líderes
          de projeto).
- Documentação oficial da política de metas (ex: OKRs, Balanced Scorecard).

- Política de bônus e remuneração variável (ex: verificar se o bônus é baseado em metas de
          equipe ou apenas departamentais/individuais).
- Atas de reuniões de avaliação de desempenho (com permissão).

##### Métricas/KPIs

- Percentual da avaliação de desempenho de um funcionário que é determinado por metas de
          equipe/comunidade vs. metas departamentais.
- Métricas formais de "sucesso de equipes de especialistas".

- Métricas de "controladoria financeira de comunidades".

##### Sinais por nível

- Nível 0:


  - O trabalho em projetos multifuncionais é visto como "trabalho extra" ou uma distração das "metas reais" do departamento
  - Não há reconhecimento formal


- Nível 1:


<!-- pág. original: 55/465 -->
  - As metas são 100% definidas pelo gerente departamental e focadas em métricas de eficiência locais (mentalidade de silo)
  - O desempenho em uma equipe multifuncional não tem impacto formal na avaliação


- Nível 2:


  - A avaliação de desempenho é tradicional

  - O gerente departamental pode, se quiser, pedir um feedback informal ao líder de um projeto, mas esse feedback não tem peso estruturado e não afeta bônus ou promoções


- Nível 3:


  - O sistema de metas começa a incluir objetivos multidimensionais, como "eficiência do processo" ou "colaboração"
  - O trabalho em comunidades é incentivado como uma forma de "desenvolvimento pessoal", mas as metas financeiras ainda são departamentais


- Nível 4:


  - O sistema de avaliação de desempenho é formalmente matricial

  - O feedback do líder da comunidade/projeto é um input obrigatório e tem peso definido na avaliação final do funcionário


- Nível 5:


  - A maior parte das metas de desempenho está diretamente atrelada aos resultados e entregas da comunidade/equipe, e não às metas do departamento funcional
  - A empresa começa a medir ativamente o "sucesso das equipes de especialistas"


- Nível 6:


  - O sistema de remuneração (bônus) é diretamente atrelado ao desempenho da comunidade


<!-- pág. original: 56/465 -->
  - A empresa possui uma "controladoria financeira de comunidades" para medir o valor entregue por elas, e o departamento funcional age principalmente como um centro de competência para desenvolvimento de carreira, não como o principal avaliador de resultados

##### Amostragem

- Política de bônus e remuneração variável (ex: verificar se o bônus é baseado em metas de
       equipe ou apenas departamentais/individuais)
- Atas de reuniões de avaliação de desempenho (com permissão)

- B) Métricas/KPIs Percentual da avaliação de desempenho de um funcionário que é
       determinado por metas de equipe/comunidade vs
- metas departamentais

- Métricas formais de "sucesso de equipes de especialistas"

- Métricas de "controladoria financeira de comunidades"

- C) Sinais por nível N0: O trabalho em projetos multifuncionais é visto como "trabalho extra" ou
       uma distração das "metas reais" do departamento
- Não há reconhecimento formal

- N1: As metas são 100% definidas pelo gerente departamental e focadas em métricas de
       eficiência locais (mentalidade de silo)
- O desempenho em uma equipe multifuncional não tem impacto formal na avaliação

- N2: A avaliação de desempenho é tradicional

- O gerente departamental pode, se quiser, pedir um feedback informal ao líder de um projeto,
       mas esse feedback não tem peso estruturado e não afeta bônus ou promoções
- N3: O sistema de metas começa a incluir objetivos multidimensionais, como "eficiência do
       processo" ou "colaboração"
- O trabalho em comunidades é incentivado como uma forma de "desenvolvimento pessoal",
       mas as metas financeiras ainda são departamentais
- N4: O sistema de avaliação de desempenho é formalmente matricial

- O feedback do líder da comunidade/projeto é um input obrigatório e tem peso definido na
       avaliação final do funcionário
- N5: A maior parte das metas de desempenho está diretamente atrelada aos resultados e
       entregas da comunidade/equipe, e não às metas do departamento funcional
- A empresa começa a medir ativamente o "sucesso das equipes de especialistas"


<!-- pág. original: 57/465 -->
- N6:

- O sistema de remuneração (bônus) é diretamente atrelado ao desempenho da comunidade

- A empresa possui uma "controladoria financeira de comunidades" para medir o valor entregue
          por elas, e o departamento funcional age principalmente como um centro de competência para
          desenvolvimento de carreira, não como o principal avaliador de resultados
- D) Amostragem Entrevistar 3 funcionários de departamentos diferentes que participam da
          mesma comunidade/projeto e perguntar como esse trabalho impacta sua avaliação de
          desempenho e bônus
- Entrevistar 2 líderes de projeto/comunidade e perguntar qual é o seu papel formal no processo
          de avaliação de desempenho dos membros de sua equipe
- Revisar os formulários de avaliação de desempenho para ver se o "feedback 360 graus" ou
          feedback de líderes de projeto é um componente obrigatório

##### I.15.3.4 Questão: Como a gestão ágil e a distribuição de autoridade são aplicadas para...
Como a gestão ágil e a distribuição de autoridade são aplicadas para garantir que as comunidades
flexíveis possam tomar decisões rapidamente?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Estrutura rígida de comando e controle. Todas as decisões, mesmo as operacionais, são escaladas para a gerência departamental. As equipes não têm autonomia. |
| 1 | A gestão de projetos é tradicional (ex cascata, waterfall). As equipes apenas executam tarefas pré-definidas e não têm autoridade para alterar o plano. |
| 2 | A empresa experimenta métodos ágeis (ex Scrum), mas apenas em "ilhas" (como TI). As "comunidades" em outras áreas não têm autoridade real para mudar escopo ou alocar recursos. |
| 3 | Métodos ágeis (como Sprints ou Daily Scrums) são usados em algumas equipes. No entanto, as decisões importantes (orçamento, priorização) ainda são centralizadas nos gerentes de departamento. |
| 4 | Os direitos de decisão são gerenciados ativamente. As equipes têm autonomia definida para tomar decisões operacionais (o "como fazer"), enquanto a gerência define os objetivos estratégicos (o "o que fazer"). |
| 5 | A gestão ágil é a norma para a maioria dos projetos. As equipes são capacitadas pela organização para fazer ajustes que facilitem a cooperação e podem compartilhar recursos em projetos de longo prazo. |
| 6 | A organização opera com gestão ágil em larga escala. As comunidades flexíveis têm alto grau de responsabilidade individual e autoridade para tomar decisões descentralizadas rapidamente, alinhadas aos objetivos estratégicos. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Manuais de metodologia de gestão de projetos (ex: verificando se usam PMBOK, Scrum, SAFe, etc.).
- Quadros Kanban ou backlogs de Scrum (digitais ou físicos, como Trello, Jira, Azure DevOps).

- Atas de reuniões de Sprint Planning ou Sprint Review.

- Matrizes de responsabilidade (ex: RACI) para projetos, que definem quem aprova e quem
         decide.
- Documentação sobre processos de tomada de decisão (ex: quem aprova um gasto de R$
         5.000 para a equipe?).

##### Métricas/KPIs

- Cycle Time de Decisão (tempo médio entre a identificação de um problema pela equipe e sua
         resolução/decisão).
- Frequência de Sprints ou ciclos de feedback.

- Número de decisões que precisam ser "escaladas" para a gerência vs. número de decisões
         tomadas pela própria equipe.
- Velocidade da Equipe (Velocity) e gráficos de Burndown (em metodologias ágeis).


<!-- pág. original: 59/465 -->
##### Sinais por nível

- Nível 0:


  - Gestão de "comando e controle"

  - As equipes recebem instruções detalhadas e não têm autoridade para tomar decisões

  - Qualquer desvio ou problema exige a paralisação e a consulta a um supervisor, que toma todas as decisões


- Nível 1:


  - Processos de desenvolvimento inflexíveis e convencionais (ex: modelo em cascata / waterfall) são a norma
  - Os requisitos são definidos rigidamente no início e as equipes não têm permissão para alterá-los


- Nível 2:


  - A empresa usa métodos tradicionais de gerenciamento de projetos

  - Embora haja um "gerente de projeto", ele atua como um controlador, e todas as decisões sobre escopo, tempo ou custo devem ser escaladas para um comitê de direção ou para a gerência sênior


- Nível 3:


  - A organização começa a usar "ciclos de feedback de alta frequência"

  - As equipes podem desenvolver protótipos rapidamente, mas a autoridade para validar e agir sobre o feedback obtido (ex: mudar o produto) ainda é centralizada na gerência


- Nível 4:


  - Abordagens de gestão ágil, como o Scrum, são implementadas formalmente nas equipes
  - As equipes têm autoridade para gerenciar seu próprio backlog e tomar decisões táticas dentro de um Sprint, mas decisões estratégicas (ex: orçamento do projeto, metas de longo prazo) permanecem centralizadas


<!-- pág. original: 60/465 -->
- Nível 5:


  - O gerenciamento ágil é amplamente utilizado e os direitos de decisão são descentralizados
  - As equipes são autorizadas a tomar decisões significativas (ex: alterar recursos, ajustar prioridades de curto prazo) para responder rapidamente ao feedback, sem precisar da aprovação da alta administração


- Nível 6:


  - A organização opera com gestão ágil em escala e alta autonomia

  - As comunidades flexíveis têm autoridade para tomar decisões descentralizadas que afetam até mesmo a estratégia (ex: pivotar a funcionalidade de um produto com base em dados de uso), alinhando-se rapidamente às mudanças do ambiente

##### Amostragem

- Amostragem Participar como ouvinte de uma reunião diária (Daily Scrum) ou de uma
        retrospectiva de Sprint
- Entrevistar um Product Owner ou Scrum Master sobre como as decisões de priorização são
        tomadas e quem tem a palavra final
- Perguntar a um membro da equipe: "Qual foi a última decisão importante que sua equipe
        tomou sem precisar da aprovação de um gerente sênior?"
- Perguntar a um gerente: "Como você equilibra a necessidade de controle com a autonomia das
        equipes?"
#### Glossário
[Sem glossário]
#### I.15.4 Capacidade: Cooperação dentro da rede
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Colaboração inter e intra-organização

#### Resumo Descritivo
Capacidade de trabalhar colaborativamente através de equipes multifuncionais e com parceiros
externos para alcançar uma visão e propósito compartilhados. A Indústria 4.0 criou uma rede
conectada de sistemas e tecnologias que reduzem o custo da colaboração e redefinem a base da
competição. Neste contexto, empresas precisam colaborar efetivamente tanto internamente quanto
com parceiros externos (fornecedores, clientes, institutos de pesquisa, universidades) dentro de
ecossistemas de negócios digitais. Estruturas organizacionais mais horizontais permitem tomada de
decisão mais rápida, e o alinhamento de incentivos pode empoderar a força de trabalho para colaborar
mais efetivamente.
#### Questões
##### I.15.4.1 Questão: Como acontece a comunicação e o compartilhamento de informações entre...
Como acontece a comunicação e o compartilhamento de informações entre equipes internas e com
parceiros externos?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Comunicação e compartilhamento de informações acontecem de forma informal e ad hoc. Equipes trabalham em silos. |
| 1 | Existem canais formais estabelecidos para comunicação e troca de informações entre equipes. |
| 2 | Canais formais permitem que equipes trabalhem juntas em tarefas e projetos discretos/pontuais. |
| 3 | Equipes são empoderadas pela organização para fazer ajustes que facilitem a cooperação em tarefas e projetos discretos. |
| 4 | Equipes são empoderadas a compartilhar recursos em tarefas e projetos tanto discretos quanto de longo prazo. |
| 5 | Canais formais permitem formar dinamicamente equipes multifuncionais com metas, recursos e KPIs compartilhados. |
| 6 | Times multidisciplinares autônomos se formam dinamicamente, incluindo parceiros e clientes, com total compartilhamento de riscos e recompensas. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Calendário de rituais interfuncionais (cadência, pauta e presença).

- RACIs/matrizes de responsabilidade e OKRs compartilhados entre áreas e com parceiros
          externos.
- Contratos e acordos de colaboração com fornecedores, clientes e parceiros.

- Plataformas de colaboração digital (portais compartilhados, sistemas integrados).

- Arquiteturas de integração (mapas de fluxo de informação interno e externo).

- Post-mortems/A3s com participantes de múltiplas áreas e organizações.

##### Métricas/KPIs

- Taxa de presença por função em rituais colaborativos; nº de itens interáreas e
          inter-organizações concluídos por sprint/mês.
- Tempo de handoff e retrabalho por fronteira (ex.: engenharia→produção,
          empresa→fornecedor).
- Fluxo (lead time, throughput, WIP) em itens que cruzam times e organizações.

- Número de projetos colaborativos com parceiros externos.

- Taxa de sucesso de iniciativas colaborativas na rede.

##### Sinais por nível

- Nível 0:


  - silos organizacionais

  - handoffs verbais


<!-- pág. original: 63/465 -->
  - sem canais formais com parceiros


- Nível 1:


  - compartilhamento sob demanda/autorização da liderança

  - comunicação formal básica


- Nível 2:


  - procedimentos formais suportam a colaboração pontual

  - projetos discretos com parceiros


- Nível 3:


  - reuniões pontuais de status

  - ajustes para facilitar cooperação

  - poucos owners claros


- Nível 4:


  - rotinas formais com análise de causa e plano conjunto

  - responsabilidades documentadas

  - compartilhamento parcial de riscos e recursos


- Nível 5:


  - planos preventivos interáreas baseados em prognósticos

  - times formados dinamicamente com KPIs compartilhados


- Nível 6:


  - células autônomas e rede dinâmica de colaboração


<!-- pág. original: 64/465 -->
  - decisões distribuídas

  - ecossistema integrado com parceiros

##### Amostragem

- Amostragem Selecionar 2-3 iniciativas que exigiram colaboração interna e externa e seguir o
          “fio” dos registros ponta-a-ponta nos últimos 90 dias
- —


##### I.15.4.2 Questão: Sua empresa coopera com parceiros na cadeia de valor (fornecedores,...
Sua empresa coopera com parceiros na cadeia de valor (fornecedores, clientes, distribuidores) para
aumentar a competitividade?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há cooperação formal; cada organização atua de forma isolada na cadeia de valor. |
| 1 | Existe comunicação básica com parceiros, mas sem colaboração estruturada. |
| 2 | Cooperação pontual em projetos específicos através de canais formais estabelecidos. |
| 3 | Coordenação com parceiros para reduzir barreiras e facilitar cooperação em iniciativas conjuntas. |
| 4 | Colaboração estabelecida com compartilhamento parcial de recursos, riscos e responsabilidades em projetos de médio prazo. |
| 5 | Integração dinâmica com parceiros através de tecnologias digitais, com metas e KPIs compartilhados. |
| 6 | Ecossistema de negócios totalmente integrado com fluxo dinâmico de informações, decisões colaborativas e inovação conjunta. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Acordos de colaboração e parcerias estratégicas na cadeia de valor.


<!-- pág. original: 65/465 -->
- Plataformas de integração digital com fornecedores e clientes.

- Infraestrutura técnica digital para integração (APIs, EDI, portais B2.

##### Métricas/KPIs

- Projetos de co-desenvolvimento e co-inovação documentados.

- Políticas de governança de dados compartilhados.

- Certificações e protocolos para participação na rede.

- Registros de transferência de conhecimento e melhores práticas.

- B) Métricas/KPIs Nível de investimento em parcerias (tempo, recursos, orçamento).

- Nível de colaboração e confiança com parceiros (surveys, índices).

- Número de projetos colaborativos ativos na cadeia de valor.

- % de novos produtos/serviços desenvolvidos em colaboração com parceiros.

- Redução de tempo de ciclo através de colaboração.

- Taxa de adoção de tecnologias digitais pelos parceiros.

- Melhoria de qualidade/redução de custos através de colaboração.

##### Sinais por nível

- Nível 0:


  - transações puramente comerciais

  - sem colaboração estruturada


- Nível 1:


  - comunicação formal básica

  - trocas de informação limitadas


- Nível 2:


  - projetos pontuais de colaboração


<!-- pág. original: 66/465 -->
  - canais formais para tarefas específicas


- Nível 3:


  - mandato organizacional para ajustar processos e facilitar cooperação


- Nível 4:


  - compartilhamento de recursos e dados

  - análises conjuntas

  - responsabilidades parcialmente compartilhadas


- Nível 5:


  - infraestrutura digital permite formação ágil de times com parceiros

  - KPIs conjuntos


- Nível 6:


  - ecossistema digital integrado

  - inovação colaborativa contínua

  - decisões distribuídas na rede

##### Amostragem

- Amostragem Analisar 3-5 iniciativas colaborativas com parceiros externos nos últimos 12
        meses, verificando nível de integração, compartilhamento e resultados

##### I.15.4.3 Questão: Sua empresa participa de redes e ecossistemas que colaboram em...
Sua empresa participa de redes e ecossistemas que colaboram em inovação?


<!-- pág. original: 67/465 -->
##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não participa de nenhuma rede de inovação; desenvolvimento interno isolado. |
| 1 | Participa de forma limitada através de canais informais (eventos, feiras, contatos ad hoc). |
| 2 | Participa formalmente de redes, mas com colaboração pontual e limitada. |
| 3 | Engajamento ativo em redes com ajustes organizacionais para facilitar participação em projetos específicos. |
| 4 | Colaboração estabelecida em redes de inovação com compartilhamento de recursos e riscos em projetos de P&D. |
| 5 | Integração em ecossistemas de inovação com universidades, institutos de pesquisa e parceiros, compartilhando metas e KPIs. |
| 6 | Protagonismo em ecossistemas digitais de inovação com fluxo contínuo de conhecimento, co-criação e inovação aberta. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Acordos com universidades, institutos de pesquisa e centros de inovação.

- Participação em consórcios, clusters e hubs de inovação.

- Projetos de pesquisa colaborativa documentados.

- Plataformas digitais de inovação aberta.

- Registros de transferência de tecnologia e licenciamento.

- Publicações conjuntas e patentes compartilhadas.

- Programas de corporate venture e aceleração.

##### Métricas/KPIs

- Número de parcerias ativas em inovação.


<!-- pág. original: 68/465 -->
- Investimento em colaboração para inovação (% do budget de P&D).

- % de projetos de inovação que requerem colaboração externa.

- Tempo para incorporar tecnologias/conhecimentos externos.

- Número de inovações resultantes de colaborações.

- Taxa de sucesso de projetos colaborativos de inovação.

- ROI de investimentos em redes de inovação.

##### Sinais por nível

- Nível 0:


  - desenvolvimento isolado

  - sem participação em redes


- Nível 1:


  - contatos informais

  - participação passiva em eventos


- Nível 2:


  - participação formal mas limitada

  - projetos pontuais


- Nível 3:


  - engajamento ativo

  - ajustes para facilitar participação em iniciativas específicas


- Nível 4:


  - colaboração estabelecida


<!-- pág. original: 69/465 -->
  - compartilhamento de recursos em P&D

  - projetos conjuntos


- Nível 5:


  - integração em ecossistemas

  - metas compartilhadas

  - acesso a conhecimento complementar


- Nível 6:


  - liderança em ecossistemas digitais

  - inovação aberta contínua

  - co-criação sistemática

##### Amostragem

- % de projetos de inovação que requerem colaboração externa

- Tempo para incorporar tecnologias/conhecimentos externos

- Número de inovações resultantes de colaborações

- Taxa de sucesso de projetos colaborativos de inovação

- ROI de investimentos em redes de inovação

- C) Sinais por nível N0: desenvolvimento isolado; sem participação em redes

- N1: contatos informais; participação passiva em eventos

- N2: participação formal mas limitada; projetos pontuais

- N3: engajamento ativo; ajustes para facilitar participação em iniciativas específicas

- N4: colaboração estabelecida; compartilhamento de recursos em P&D; projetos conjuntos

- N5: integração em ecossistemas; metas compartilhadas; acesso a conhecimento
       complementar
- N6: liderança em ecossistemas digitais; inovação aberta contínua; co-criação sistemática


<!-- pág. original: 70/465 -->
- D) Amostragem Mapear todas as parcerias de inovação ativas, analisando profundidade da
          colaboração, recursos compartilhados e resultados gerados nos últimos 24 meses

##### I.15.4.4 Questão: Projetos de novos produtos e serviços requerem inputs/componentes...
Projetos de novos produtos e serviços requerem inputs/componentes desenvolvidos em colaboração
com outras empresas da rede?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Desenvolvimento totalmente interno sem colaboração externa. |
| 1 | Fornecimento básico de componentes/serviços sem co-desenvolvimento. |
| 2 | Colaboração pontual em componentes específicos através de projetos discretos. |
| 3 | Co-desenvolvimento coordenado de componentes com ajustes mútuos para facilitar integração. |
| 4 | Desenvolvimento colaborativo com compartilhamento de riscos, recursos e propriedade intelectual. |
| 5 | Integração de desenvolvimento com parceiros através de plataformas digitais e processos compartilhados. |
| 6 | Ecossistema de co-criação contínua com modularidade, interoperabilidade e inovação distribuída. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Pipeline de desenvolvimento de produtos/serviços.

- Acordos de co-desenvolvimento e NDA com parceiros.

- Especificações técnicas compartilhadas e interfaces definidas.

- Plataformas de colaboração em desenvolvimento (PLM integrado, repositórios compartilhados).

- Documentação de integração e interoperabilidade.


<!-- pág. original: 71/465 -->
- Roadmaps tecnológicos compartilhados.

- Registros de propriedade intelectual conjunta.

##### Métricas/KPIs

- % de projetos que envolvem colaboração externa no desenvolvimento.

- Número de componentes/módulos desenvolvidos colaborativamente.

- Tempo de ciclo de desenvolvimento com colaboração vs. interno.

- Taxa de reuso de componentes colaborativos.

- Qualidade e performance de soluções colaborativas.

- Custo de desenvolvimento compartilhado.

- Taxa de sucesso de lançamentos colaborativos.

##### Sinais por nível

- Nível 0:


  - desenvolvimento 100% interno

  - sem colaboração externa


- Nível 1:


  - fornecimento tradicional

  - sem co-desenvolvimento


- Nível 2:


  - projetos pontuais de colaboração

  - desenvolvimento discreto de componentes


- Nível 3:


  - coordenação no desenvolvimento


<!-- pág. original: 72/465 -->
  - ajustes mútuos para integração


- Nível 4:


  - co-desenvolvimento estabelecido

  - compartilhamento de riscos e IP

  - responsabilidades claras


- Nível 5:


  - plataformas digitais integram desenvolvimento

  - processos sincronizados

  - decisões conjuntas


- Nível 6:


  - ecossistema modular de co-criação

  - inovação distribuída

  - capacidade adaptativa contínua

##### Amostragem

- Amostragem Analisar 5-7 projetos recentes de desenvolvimento, identificando grau de
          colaboração externa, parceiros envolvidos e contribuições específicas de cada participante

##### I.15.4.5 Questão: Como as tecnologias digitais são utilizadas para melhorar a...
Como as tecnologias digitais são utilizadas para melhorar a colaboração interna e com parceiros
externos?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há uso de tecnologias digitais específicas para colaboração; processos manuais ou isolados. |
| 1 | Uso básico de ferramentas de comunicação digital (e-mail, mensagens). |
| 2 | Plataformas digitais para compartilhamento de documentos e colaboração em projetos específicos. |
| 3 | Sistemas integrados que permitem coordenação e ajustes para facilitar colaboração em tempo real. |
| 4 | Infraestrutura digital robusta com integração de dados, processos e ferramentas colaborativas avançadas. |
| 5 | Plataformas digitais permitem formar dinamicamente equipes virtuais com visibilidade completa e tomada de decisão compartilhada. |
| 6 | Ecossistema digital integrado com IoT, IA e analytics que permitem colaboração autônoma, adaptativa e preditiva. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Inventário de ferramentas digitais de colaboração em uso.

- Arquitetura de integração de sistemas (internos e com parceiros).

- APIs e interfaces de integração documentadas.

- Plataformas de colaboração em nuvem.

- Dashboards compartilhados e visibilidade de dados.

- Infraestrutura de IoT e conectividade.

- Capacidades de analytics e IA para suporte à colaboração.

- Políticas de segurança e governança de dados compartilhados.

##### Métricas/KPIs

- Grau de digitalização da comunicação e colaboração (% de interações digitais).

- Número de integrações ativas com sistemas de parceiros.


<!-- pág. original: 74/465 -->
- Volume de dados trocados digitalmente.

- Latência de comunicação e sincronização.

- Disponibilidade e performance de plataformas colaborativas.

- Taxa de adoção de ferramentas digitais colaborativas.

- Automação de processos colaborativos.

##### Sinais por nível

- Nível 0:


  - processos manuais

  - sem ferramentas digitais específicas


- Nível 1:


  - comunicação digital básica

  - ferramentas isoladas


- Nível 2:


  - plataformas para projetos específicos

  - compartilhamento de documentos


- Nível 3:


  - sistemas integrados internamente

  - coordenação digital em tempo real


- Nível 4:


  - integração robusta com parceiros

  - dados e processos compartilhados


<!-- pág. original: 75/465 -->
  - visibilidade avançada


- Nível 5:


  - plataformas permitem formação ágil de times virtuais

  - decisões baseadas em dados compartilhados


- Nível 6:


  - ecossistema digital com IoT, IA e analytics

  - colaboração autônoma e adaptativa

  - otimização preditiva

##### Amostragem

- Amostragem Mapear arquitetura de integração atual, listar todas as ferramentas/plataformas de
         colaboração digital e avaliar maturidade de uso em 3-5 casos de colaboração recentes

##### I.15.4.6 Questão: Como sua empresa gerencia relacionamentos e confiança com parceiros...
Como sua empresa gerencia relacionamentos e confiança com parceiros na rede/ecossistema de
negócios?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há gestão formal de relacionamentos; interações transacionais e isoladas. |
| 1 | Gestão básica através de contratos e comunicação formal mínima. |
| 2 | Processos formais de gestão de relacionamentos para projetos e iniciativas específicas. |
| 3 | Gestão ativa com mecanismos para ajustar responsabilidades e reduzir barreiras à cooperação. |
| 4 | Gestão estruturada com governança compartilhada, métricas de relacionamento e resolução de conflitos. |
| 5 | Gestão integrada com alinhamento de incentivos, metas compartilhadas e cultura de confiança estabelecida. |
| 6 | Ecossistema auto-organizado com reputação digital, contratos inteligentes e governança distribuída. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Sistema de gestão de relacionamentos com parceiros (PRM/CRM estendido).

- Contratos e SLAs com parceiros.

- Modelos de governança compartilhada documentados.

- Mecanismos de resolução de conflitos.

- Políticas de compartilhamento de valor e incentivos.

- Acordos de confidencialidade e segurança.

- Pesquisas de satisfação e confiança com parceiros.

- Registro de histórico de colaborações e performance.

##### Métricas/KPIs

- Índice de satisfação de parceiros. Índice de confiança e reputação na rede.

- Número de conflitos e tempo de resolução.

- Taxa de renovação de parcerias.

- Crescimento do valor gerado em colaborações.

- Net Promoter Score (NPS) com parceiros.

- Diversidade e tamanho do ecossistema.

- Velocidade de onboarding de novos parceiros.

##### Sinais por nível

- Nível 0:


<!-- pág. original: 77/465 -->
  - sem gestão formal

  - relacionamentos ad hoc e instáveis


- Nível 1:


  - gestão contratual básica

  - comunicação formal mínima


- Nível 2:


  - processos de gestão para projetos específicos

  - relacionamentos discretos


- Nível 3:


  - gestão ativa

  - flexibilidade para ajustar termos

  - foco em facilitar cooperação


- Nível 4:


  - governança estruturada

  - métricas compartilhadas

  - mecanismos de resolução de conflitos


- Nível 5:


  - alinhamento estratégico

  - cultura de confiança

  - incentivos compartilhados

  - reputação gerenciada


<!-- pág. original: 78/465 -->
- Nível 6:


  - governança distribuída

  - contratos inteligentes

  - reputação digital

  - auto-organização

##### Amostragem

- Amostragem Analisar gestão de relacionamento com 5-10 parceiros-chave, avaliando
        maturidade dos mecanismos de governança, confiança e alinhamento de incentivos
#### Glossário
[Sem glossário]
### I.16 Dimensão: Estratégia & Governança

#### I.16.1 Capacidade: Dar forma à mudança
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Estratégia & Governança

#### Resumo Descritivo
Esta capacidade define a aptidão de uma empresa e de seus colaboradores para reagir de maneira
rápida e apropriada a eventos externos, maximizando os benefícios da mudança para todos os
envolvidos. Ela pressupõe que a transformação não deve ser apenas aceita passivamente, mas sim
protagonizada pelos próprios funcionários
#### Questões
##### I.16.1.1 Questão: Qual é a atitude e o nível de autonomia dos funcionários para iniciar...
Qual é a atitude e o nível de autonomia dos funcionários para iniciar e implementar mudanças?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | As mudanças são impostas pela gestão e geralmente recebidas com resistência. Os funcionários não têm voz nem iniciativa no processo de mudança. |
| 1 | Os funcionários executam mudanças apenas quando instruídos. A iniciativa de mudança não é esperada nem incentivada no nível operacional. |
| 2 | Os funcionários são incentivados a sugerir melhorias (ex: caixas de sugestão), mas não têm autoridade para iniciar ou implementar mudanças. A gestão centraliza todas as decisões de mudança. |
| 3 | Os funcionários mais próximos dos processos são consultados sobre mudanças, mas a autoridade de decisão permanece centralizada. A iniciativa de mudança ainda é vista como uma responsabilidade primária da gestão. |
| 4 | Os funcionários têm autonomia para iniciar e implementar pequenas mudanças dentro de suas áreas imediatas. Eles entendem que são parcialmente responsáveis por moldar a mudança. |
| 5 | Os funcionários com o conhecimento técnico relevante têm autoridade para iniciar e implementar mudanças significativas. Eles são proativos e dão o primeiro passo por conta própria para que a mudança aconteça. |
| 6 | A organização depende da iniciativa da linha de frente para impulsionar a adaptação. Os funcionários têm autonomia total para iniciar, implementar e concluir mudanças rapidamente, e são avaliados pela sua capacidade de fazê-lo. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Registros de sistemas de sugestão de melhoria

- Documentação de projetos de melhoria contínua.

- Atas de reuniões de equipes operacionais que discutem a implementação de mudanças.

- Matrizes de responsabilidade para processos de gestão de mudança, evidenciando a
         descentralização do poder de decisão.

##### Métricas/KPIs

- Número de melhorias/mudanças implementadas iniciadas por funcionários da linha de frente
         (não-gerenciais).
- Tempo de ciclo da mudança (desde a identificação do evento até a implementação da medida).


<!-- pág. original: 180/465 -->
- Taxa de participação em programas de sugestão/melhoria.

- Percentual de decisões de mudança delegadas às equipes de processo.

##### Sinais por nível

- Nível 0:


  - Funcionários afirmam: "Eu apenas faço o que me mandam" ou "A gestão decide tudo, não adianta sugerir"


- Nível 1:


  - Funcionários afirmam: "Eu apenas faço o que me mandam" ou "A gestão decide tudo, não adianta sugerir"


- Nível 2:


  - Existem caixas de sugestão, mas os funcionários relatam que raramente veem suas ideias implementadas ou recebem feedback


- Nível 3:


  - Operadores relatam problemas e sugerem soluções, mas afirmam que precisam esperar dias ou semanas pela aprovação da gerência ou engenharia para implementar qualquer mudança


- Nível 4:


  - Equipes de linha de frente demonstram autonomia para mudanças locais (ex: organização do local de trabalho), mas mudanças de processo maiores ainda são iniciadas e controladas pela gestão


- Nível 5:


  - Um operador identifica uma falha recorrente e tem autoridade para parar, testar uma solução e documentar a mudança para a equipe, iniciando o processo por conta própria


<!-- pág. original: 181/465 -->
- Nível 6:


  - As equipes operacionais têm metas de melhoria e autonomia para experimentar, falhar e implementar mudanças de processo em tempo real, comunicando as mudanças horizontalmente

##### Amostragem

- Realizar entrevistas com operadores, líderes de equipe, supervisores e gerentes de melhoria
          contínua
- Perguntas-chave: "Descreva a última vez que você identificou uma oportunidade de melhoria
          ou um problema no seu trabalho
- " "O que você fez a respeito?" "Você teve autoridade para implementar a mudança sozinho ou
          precisou de aprovação? "Quem na empresa é responsável por iniciar mudanças?" Observação:
          Analisar 3-5 processos de mudança recentes e rastrear a origem da iniciativa (quem deu o
          primeiro passo)

##### I.16.1.2 Questão: Como a estrutura de gestão reage (apoia, bloqueia, ignora) quando um...
Como a estrutura de gestão reage (apoia, bloqueia, ignora) quando um funcionário da linha de frente
propõe ou tenta implementar uma mudança?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A gestão desencoraja ativamente as sugestões ou iniciativas de mudança dos funcionários, considerando-as "fora de função" ou "indisciplina". |
| 1 | A gestão ignora sistematicamente as iniciativas de mudança. Funcionários que tentam são vistos como "problemáticos" ou "perda de tempo". |
| 2 | A gestão ouve as propostas, mas a iniciativa é bloqueada por burocracia excessiva (ex: múltiplos formulários, longos tempos de espera por aprovação) que desencoraja a ação. |
| 3 | A gestão apoia verbalmente a iniciativa, mas raramente fornece os recursos (tempo, orçamento, pessoal) ou a autoridade necessários para a implementação. A mudança não avança. |
| 4 | A gestão apoia ativamente iniciativas de baixo risco. Para mudanças maiores, a gestão assume o controle do projeto, retirando a liderança do funcionário que a iniciou. |
| 5 | A gestão atua como facilitadora, fornecendo ativamente os recursos e o "leeway" (espaço de manobra) necessários para que o funcionário ou a equipe teste e implemente a mudança que iniciou. |
| 6 | A gestão espera que os funcionários iniciem e liderem mudanças. O papel principal da gestão é remover barreiras, garantir recursos rapidamente e proteger a equipe durante a experimentação (mesmo que falhe). |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Fluxogramas do processo de "sugestão-para-implementação".

- Registros de alocação de tempo (ex: horas de engenharia, tempo de máquina parada) ou
          orçamento para projetos de melhoria iniciados por funcionários.
- Atas de reunião de gestão (procurar por aprovações/rejeições de iniciativas da linha de frente).

- Documentação de projetos de melhoria (verificar quem é o "dono" ou líder do projeto).

##### Métricas/KPIs

- Taxa de conversão (sugestões de funcionários vs. implementações).

- Tempo de aprovação (tempo entre a sugestão do funcionário e a alocação de recursos pela
          gestão).
- Percentual de projetos de melhoria liderados por funcionários não-gerenciais.

##### Sinais por nível

- Nível 0:


  - Funcionários relatam: "Eu nem me dou ao trabalho de sugerir", "Na última vez que tentei, levei uma bronca por parar a linha" ou "A gestão não gosta que a gente se meta"


<!-- pág. original: 183/465 -->
- Nível 1:


  - Funcionários relatam: "Eu nem me dou ao trabalho de sugerir", "Na última vez que tentei, levei uma bronca por parar a linha" ou "A gestão não gosta que a gente se meta"


- Nível 2:


  - "Eu sugeri uma melhoria há 6 meses

  - Preenchi três formulários e nunca mais ouvi falar


- Nível 3:


  - "Meu chefe disse 'ótima ideia', mas falou que 'não temos tempo para isso agora' e o assunto morreu


- Nível 4:


  - "Conseguimos mudar o layout da nossa célula, mas quando sugerimos alterar o fluxo de TI, a gerência sênior assumiu o projeto e perdemos o controle


- Nível 5:


  - "Eu disse ao meu gerente que nosso processo estava gerando refugo

  - Ele me deu 4 horas de 'tempo de máquina' e um colega da manutenção para testar minha nova ideia


- Nível 6:


  - "Nosso gerente nos pergunta diariamente: 'O que está bloqueando sua mudança?' O trabalho dele é nos ajudar a implementar nossas próprias ideias o mais rápido possível

##### Amostragem

- Amostragem Entrevistas: Realizar entrevistas focadas com funcionários da linha de frente
       (operadores, técnicos) e seus supervisores diretos (líderes de turno, gerentes de produção)


<!-- pág. original: 184/465 -->
- Perguntas-chave (para funcionários): "O que acontece quando você leva uma ideia de
          mudança para seu supervisor?" "Você recebe apoio (tempo, dinheiro, ajuda) para testar suas
          ideias?" "Descreva uma mudança que você tentou implementar
- Quem o ajudou? Quem o atrapalhou?" Perguntas-chave (para gestores): "Qual é o seu papel
          quando um membro da sua equipe sugere uma mudança de processo?" "Como você decide
          quais recursos alocar para uma ideia vinda da equipe?"

##### I.16.1.3 Questão: Qual é a postura do funcionário em relação à sua responsabilidade...
Qual é a postura do funcionário em relação à sua responsabilidade pessoal de iniciar mudanças,
mesmo que não seja explicitamente solicitado?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Os funcionários veem a mudança como uma ameaça ou um fardo. Eles ativamente evitam ou se opõem a ela. |
| 1 | Os funcionários acreditam que "mudar" não é parte do seu trabalho. Eles esperam passivamente por instruções e executam apenas o que é mandado. |
| 2 | Os funcionários reconhecem problemas, mas acreditam que é responsabilidade exclusiva da gestão (supervisores, engenharia) identificá-los e resolvê-los. |
| 3 | Os funcionários tomam a iniciativa de relatar problemas, mas não se sentem responsáveis por propor ou desenvolver a solução. A responsabilidade termina na comunicação do problema. |
| 4 | Os funcionários sentem-se responsáveis por identificar problemas e propor soluções. Eles preparam e apresentam suas ideias à gestão para aprovação. |
| 5 | Os funcionários sentem responsabilidade pessoal não apenas por propor, mas por liderar a implementação da mudança. Eles tomam a iniciativa e estão preparados para dar o primeiro passo por conta própria. |
| 6 | A responsabilidade pela melhoria é totalmente internalizada. Os funcionários veem o ato de "mudar" como parte central do seu trabalho diário, tomam a iniciativa de forma autônoma e ajudam os colegas a fazer o mesmo. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Quadros de gestão à vista para verificar a autoria das iniciativas de melhoria (se são dos
          operadores ou dos gestores).
- Registros de "donos" de projetos de melhoria para ver se funcionários da linha de frente estão
          liderando as ações.
- Descrições de cargo (verificar se "melhoria contínua" ou "iniciativa proativa" são listadas como
          responsabilidades formais da função).

##### Métricas/KPIs

- Percentual de funcionários que participaram ativamente (não apenas como ouvintes) de pelo
          menos um evento de melhoria no último ano.
- Número de problemas (ex: cartões de melhoria) abertos versus fechados pela própria equipe
          (sem intervenção direta da gestão/engenharia).
- Tempo médio entre a identificação de um problema pela equipe e a primeira ação de
          contenção/correção (mede a prontidão para agir).

##### Sinais por nível

- Nível 0:


  - "Eu sou pago para operar esta máquina, não para consertá-la", "Esse é o trabalho da engenharia


- Nível 1:


  - "Eu sou pago para operar esta máquina, não para consertá-la", "Esse é o trabalho da engenharia


- Nível 2:


<!-- pág. original: 186/465 -->
  - "Eu avisei meu supervisor sobre o problema

  - Minha parte eu fiz

  - Se ele não resolveu, não é mais comigo


- Nível 3:


  - "Eu sempre aponto os problemas para o meu líder na reunião diária

  - Cabe a ele decidir o que fazer


- Nível 4:


  - "Eu vi que o sensor falhava, então passei um tempo pensando em uma solução e apresentei um esboço ao meu gerente


- Nível 5:


  - "Quando vi o problema, eu mesmo documentei o que estava acontecendo, chamei o time e comecei a testar uma solução
  - Eu sou o responsável por fazer isso funcionar"


- Nível 6:


  - "Faz parte da minha rotina diária identificar e corrigir problemas

  - Não preciso pedir permissão para melhorar meu próprio processo

##### Amostragem

- Amostragem Observação: Observe as reuniões de início de turno (Daily Huddles)

- Quem relata os problemas? Quem se voluntaria para resolvê-los? Entrevistas
       (Operadores/Técnicos): "De quem é a responsabilidade de identificar melhorias por aqui?"
       "Quando você vê algo que pode ser melhorado, qual é o seu primeiro impulso: (a) Ignorar, (b)
       Esperar que alguém veja, (c) Relatar ao chefe, ou (d) Tentar resolver?" "Você se sente
       responsável por garantir que a mudança realmente aconteça?"


<!-- pág. original: 187/465 -->
##### I.16.1.4 Questão: Qual é a abordagem predominante da organização para implementar...
Qual é a abordagem predominante da organização para implementar mudanças?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A implementação de mudanças pela equipe não é uma prática; qualquer desvio do padrão é ativamente corrigido. |
| 1 | Mudanças, se aprovadas, seguem um processo de implementação rígido, linear (cascata) e lento, que leva meses. O plano não pode ser alterado após o início. |
| 2 | A implementação é caótica e ad-hoc. As mudanças são feitas, mas não há um processo estruturado para medir o impacto, aprender ou adaptar a solução. |
| 3 | A mudança requer um plano de projeto detalhado e completo antes da implementação. O foco está em seguir o plano original, e adaptações são vistas como falhas de planejamento. |
| 4 | A implementação segue ciclos formais de melhoria (ex: PDCA). A equipe coleta dados após a implementação e planeja ajustes em ciclos subsequentes (ex: mensalmente). |
| 5 | A equipe é incentivada a usar abordagens de "teste rápido" (prototipagem). As mudanças são implementadas em pequena escala para coletar dados e o aprendizado é usado para "moldar" a solução final. |
| 6 | A implementação é ativamente ágil, usando ciclos curtos (ex: diários/semanais). A equipe tem autonomia para adaptar a solução em tempo real com base em dados, focando em "falhar rápido" e aprender iterativamente. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documentação de projetos de melhoria (ex: A3, DMAIC, Sprints Ágeis).


<!-- pág. original: 188/465 -->
- Quadros de gestão de mudança (Kanban, Scrum boards) usados pelas equipes.

- Registros de "lições aprendidas" ou retrospectivas de projetos de mudança.

- Evidências de prototipagem ou MVPs (Minimum Viable Products) usados em mudanças de
        processo.

##### Métricas/KPIs

- Duração do ciclo de mudança (do início da implementação ao primeiro feedback de dados).

- Frequência de iteração (quantas vezes a solução foi ajustada após o início da implementação).

- Taxa de sucesso de mudanças (mudanças que atingiram o resultado esperado vs. as que
        foram revertidas).
- Tempo para validar uma hipótese de mudança (Time-to-learn).

##### Sinais por nível

- Nível 0:


  - "Se o procedimento diz 'A', fazemos 'A'", "Se você tentar fazer 'B', mesmo que seja melhor, você está errado


- Nível 1:


  - "Se o procedimento diz 'A', fazemos 'A'", "Se você tentar fazer 'B', mesmo que seja melhor, você está errado


- Nível 2:


  - "Nós mudamos o processo na semana passada, mas não sei dizer se melhorou

  - Simplesmente fizemos e seguimos em frente


- Nível 3:


  - "Estamos há 3 meses planejando a mudança do software da máquina

  - Não podemos testar nada até o plano mestre ser 100% aprovado pela engenharia e TI


<!-- pág. original: 189/465 -->
- Nível 4:


  - "Implementamos a mudança

  - Mês que vem, na reunião de gestão, vamos olhar os KPIs para ver se deu certo e decidir o próximo passo


- Nível 5:


  - "Achamos que a mudança funcionaria

  - O chefe nos deu permissão para testar na máquina 2 por uma tarde

  - Vimos que 70% funcionou, mas 30% deu errado

  - Amanhã vamos testar de novo com os ajustes


- Nível 6:


  - "Temos um 'quadro de sprint' de melhoria

  - Nossa meta é testar 3 pequenas mudanças esta semana

  - A primeira falhou em 1 hora (o que foi ótimo, aprendemos rápido), a segunda está funcionando e vamos escalar

##### Amostragem

- Amostragem Entrevistas (Equipes de Melhoria, Líderes de Equipe, Engenheiros de Processo):
        "Descreva o processo para implementar uma nova ideia
- Você precisa de um plano completo antes de começar?" "Com que frequência você pode
        ajustar a solução depois que ela já começou a ser implementada?" "O que é mais valorizado:
        seguir o plano original perfeitamente ou adaptar o plano rapidamente para obter um resultado
        melhor?" Observação: Acompanhe uma reunião de revisão de melhoria
- O foco está em "culpar quem desviou do plano" ou em "o que aprendemos com o desvio"?

#### Glossário
[Sem glossário]
#### I.16.2 Capacidade: Gestão de direitos de decisão
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Estratégia & Governança

#### Resumo Descritivo
Esta capacidade refere-se ao equilíbrio estratégico entre a centralização e a descentralização da
autoridade para tomar decisões dentro de uma empresa. O objetivo principal é alocar o poder de
decisão de forma que a eficácia e a eficiência dos processos sejam maximizadas, garantindo que as
escolhas sejam feitas por quem possui as melhores informações.
#### Questões
##### I.16.2.1 Questão: Como a sua empresa gerencia os direitos de decisão, equilibrando a...
Como a sua empresa gerencia os direitos de decisão, equilibrando a autoridade centralizada e a
descentralizada para maximizar a eficácia e a eficiência da tomada de decisão?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | As decisões são tomadas de forma ad-hoc, reativa, e baseadas primariamente na intuição da gestão. A autoridade é totalmente centralizada. |
| 1 | As decisões são centralizadas e baseadas em procedimentos formais. A TI é usada de forma isolada (ex planilhas locais) para coletar dados, mas não suporta a tomada de decisão descentralizada |
| 2 | Os sistemas de TI estão conectados (ex ERP, MES), permitindo a partilha de informação. No entanto, a autoridade de decisão permanece rigidamente centralizada na gestão. |
| 3 | A empresa possui um "digital shadow" e tem visibilidade do estado atual dos processos. A informação está disponível, mas a autoridade para agir sobre ela ainda é predominantemente centralizada e requer aprovação manual. |
| 4 | A empresa entende por que os eventos ocorrem (causa e efeito). Esta transparência sobre as consequências permite que a gestão comece a delegar formalmente direitos de decisão para níveis mais baixos, permitindo ações descentralizadas mais rápidas. |
| 5 | A capacidade preditiva permite a simulação de cenários futuros. Poderes de decisão ajustados são formalmente delegados a níveis operacionais (descentralizados) com base nessas previsões. As equipes podem tomar decisões antes que os problemas ocorrem. |
| 6 | A empresa atinge o equilíbrio ideal entre centralização e descentralização. Decisões de rotina complexas são automatizadas (delegadas a sistemas de TI), e as equipes operacionais são totalmente capacitadas para tomar decisões táticas descentralizadas de forma rápida. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Organogramas formais e matrizes de responsabilidade.

- Manuais de governança corporativa e políticas de aprovação.

- Fluxos de trabalho (workflows) de aprovação documentados e configurados nos sistemas de
          TI.

##### Métricas/KPIs

- Tempo de latência da decisão (tempo entre o evento e a aprovação da medida).

- Tempo de latência da ação (tempo para a medida corretiva ter efeito)

- Percentual de decisões tomadas de forma descentralizada vs. centralizada.

- Percentual de decisões automatizadas (delegadas a sistemas de TI).

##### Sinais por nível

- Nível 0:


<!-- pág. original: 192/465 -->
  - As decisões são tomadas de forma ad-hoc, reativa, e baseadas primariamente na intuição da gestão
  - A autoridade é totalmente centralizada


- Nível 1:


  - A tomada de decisão é centralizada

  - A TI é usada de forma isolada (ex: planilhas locais), o que não suporta a tomada de decisão descentralizada


- Nível 2:


  - Os sistemas de TI estão conectados, permitindo a partilha básica de informação (ex: dados de engenharia para a produção)
  - No entanto, a autoridade de decisão permanece centralizada na gestão


- Nível 3:


  - A visibilidade é alcançada (existe um "digital shadow")

  - As informações sobre o estado atual dos processos estão disponíveis, mas a autoridade para agir sobre essas informações ainda é predominantemente centralizada


- Nível 4:


  - A transparência é alcançada

  - a empresa entende por que os eventos ocorrem

  - Esta transparência sobre as consequências permite que a gestão delegue decisões, possibilitando ações descentralizadas mais rápidas e alinhadas aos objetivos


- Nível 5:


  - A capacidade preditiva permite a simulação de cenários futuros


<!-- pág. original: 193/465 -->
  - Poderes de decisão ajustados são formalmente delegados a níveis operacionais (descentralizados) com base nessas previsões


- Nível 6:


  - A adaptabilidade é alcançada

  - A empresa atinge o equilíbrio ideal entre centralização e descentralização

  - Decisões de rotina são automatizadas (delegadas a sistemas de TI), e as equipes operacionais são totalmente capacitadas para tomar decisões descentralizadas complexas de forma rápida e eficaz

##### Amostragem

- Selecionar 3-5 decisões recentes (ex: mudança não planejada na ordem de produção,
         aprovação de manutenção de emergência, alteração de design de produto)
- Entrevistar as equipes operacionais e gestores envolvidos para verificar quem (ou qual
         sistema) teve a autoridade real para tomar a decisão final
- Revisar os registros de aprovação nos sistemas para validar o processo documentado vs

- o processo real


##### I.16.2.2 Questão: Em que medida a empresa delega a autoridade de decisão de processos...
Em que medida a empresa delega a autoridade de decisão de processos operacionais, movendo-a de
operadores humanos para sistemas de TI (automação)?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há delegação para sistemas. Todas as decisões de processo (ex parar uma máquina, ajustar parâmetros, mudar fila) são 100% manuais e reativas. |
| 1 | Os sistemas de TI são usados apenas para registrar dados (ex planilhas, terminais de CNC). A decisão ainda é 100% humana e manual. |
| 2 | Os sistemas de TI (ex ERP, MES) estão conectados e apresentam relatórios consolidados, mas a decisão ainda é 100% humana (ex: um gerente aprova uma ordem no sistema). |
| 3 | Os sistemas (Digital Shadow) alertam ativamente sobre desvios em tempo real (ex "Alerta: Máquina X está fora da especificação"). A decisão sobre o que fazer ainda é totalmente humana. |
| 4 | Os sistemas analisam os dados (transparência) e diagnosticam a causa raiz de um problema (ex "Alerta: Máquina X parou porque o sensor Y falhou"). A decisão de como corrigir ainda é humana. |
| 5 | Os sistemas (capacidade preditiva) antecipam eventos e recomendam ações corretivas (ex "Sugerir parada de máquina X para manutenção em 2 horas"). Um humano ainda precisa aprovar a recomendação. |
| 6 | Os sistemas de TI (adaptabilidade) têm autonomia para tomar e executar decisões táticas complexas automaticamente (ex reordenar fila de produção, ajustar parâmetros de máquina) para otimizar o processo sem intervenção humana. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Logs de sistemas (MES, SCADA, ERP) para verificar aprovações e ações automatizadas.

- Documentação de regras de negócio (Business Rules Engine) configuradas nos sistemas.

- Manuais de operação e fluxos de processo documentados.

##### Métricas/KPIs

- Percentual de decisões de processo (ex: ajuste de parâmetro, gestão de fila) tomadas
         automaticamente por sistemas.
- Tempo de resposta do sistema a um desvio (desde a detecção até a ação corretiva).


<!-- pág. original: 195/465 -->
##### Sinais por nível

- Nível 0:


  - Inexistente


- Nível 1:


  - Sistemas registram dados passivamente para decisão humana posterior


- Nível 2:


  - Sistemas apresentam relatórios consolidados para decisão humana ativa


- Nível 3:


  - Sistemas emitem alertas (ex: dashboards, luzes andon) quando um desvio ocorre

  - ação é 100% humana


- Nível 4:


  - Sistemas diagnosticam causas (transparência) e sugerem análises

  - ação é 100% humana


- Nível 5:


  - Sistemas oferecem recomendações de ação (capacidade preditiva) que requerem aprovação humana


- Nível 6:


  - Sistemas têm autonomia para tomar e executar decisões táticas (ex: reordenar produção, ajustar parâmetros de máquina) sem aprovação humana


<!-- pág. original: 196/465 -->
##### Amostragem

- Amostragem Analisar logs de 3-5 eventos de desvio recentes (ex: falha de máquina, problema
          de qualidade, atraso de material)
- Verificar nos logs do sistema se a correção foi feita por um operador, um gerente ou
          automaticamente pelo sistema
- Entrevistar operadores do "shop floor" sobre quais decisões eles tomam e quais o sistema
          toma por eles

##### I.16.2.3 Questão: Em que medida os tomadores de decisão (em todos os níveis) têm acesso...
Em que medida os tomadores de decisão (em todos os níveis) têm acesso à informação relevante,
integrada e contextualizada para fundamentar suas decisões?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | As decisões são tomadas com base em intuição, relatórios de papel atrasados ou informação verbal não estruturada. |
| 1 | As decisões são baseadas em dados de sistemas isolados (ex uma planilha de produção, um relatório de inventário separado). Os dados não são integrados, estão frequentemente desatualizados e podem ser conflitantes. |
| 2 | Os sistemas estão minimamente conectados. O tomador de decisão pode buscar ativamente os dados em diferentes sistemas (ex consultar o ERP, depois o MES), mas precisa compilar e analisar tudo manualmente. |
| 3 | Os tomadores de decisão têm acesso a um "Digital Shadow" (ex um dashboard centralizado) que mostra o que está acontecendo em tempo real (Visibilidade). As decisões são baseadas no estado atual real. |
| 4 | O sistema não apenas mostra o estado atual, mas também fornece análises de causa-raiz (Transparência), explicando por que algo está acontecendo (ex "Máquina 5 parada por falta de material"). As decisões são mais precisas e assertivas. |
| 5 | O sistema fornece informações preditivas e simulações de impacto (Capacidade Preditiva) aos tomadores de decisão (ex "Se a Ordem X for priorizada, a Ordem Y atrasará 2 dias"). As decisões consideram o impacto futuro. |
| 6 | A informação certa (preditiva, diagnóstica e de estado) é entregue de forma proativa, autônoma e contextualizada ao tomador de decisão correto (seja humano ou sistema) no momento exato em que a decisão é necessária (Adaptabilidade). |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Dashboards de gestão (em tempo real vs. relatórios estáticos).

- Telas de terminais no "shop floor" (MES).

- Relatórios de análise de causa-raiz (RCA) e se eles usam dados de sistema ou são baseados
          em entrevistas.
- Ferramentas de BI (Business Intelligence) e seus níveis de integração.

##### Métricas/KPIs

- Tempo médio para coletar dados necessários para uma decisão não rotineira.

- Percentual de decisões operacionais suportadas por dados em tempo real vs. relatórios
          históricos.
- Taxa de adoção de dashboards de BI ou MES pelos gestores e operadores.

##### Sinais por nível

- Nível 0:


  - Gestores passam a maior parte do tempo "apagando incêndios" sem dados


- Nível 1:


  - Reuniões de produção baseadas em planilhas impressas na noite anterior


<!-- pág. original: 198/465 -->
- Nível 2:


  - O gestor precisa abrir 3 sistemas diferentes para entender um problema


- Nível 3:


  - A reunião de produção usa um dashboard ao vivo (Digital Shadow) que todos confiam


- Nível 4:


  - O dashboard mostra a causa do problema (ex: gargalo) automaticamente


- Nível 5:


  - O sistema envia um alerta ao gestor: "Atenção: Risco de 80% de atraso na Ordem X se a Máquina Y não for ajustada em 1h"


- Nível 6:


  - O sistema alerta o operador da Máquina Y com a instrução de ajuste exata, já prevendo o problema antes que o gestor precise intervir

##### Amostragem

- Apresentar a um gestor de produção um cenário hipotético (ex: "Um cliente importante ligou
        querendo dobrar um pedido
- Como você decide se aceita?")

- Observar quais ferramentas e dados ele usa para tomar a decisão (tempo, fontes de dados,
        nível de confiança na informação)
- Perguntar a um operador: "Quando sua máquina para, qual informação você recebe e de
        onde?"
#### Glossário
[Sem glossário]
#### I.16.3 Capacidade: Governança de dados
#### Bloco/Pilar
- Bloco: Organização

- Pilar: Estrutura e Gestão

- Dimensão: Estratégia & Governança

#### Resumo Descritivo
A governança de dados refere-se às políticas e orientações para o processamento, armazenamento,
gerenciamento e apresentação de dados de alta qualidade em toda a empresa. A implementação de
uma governança de dados eficaz é fundamental para melhorar a qualidade dos dados, o que, por sua
vez, sustenta a confiança nos sistemas de informação e viabiliza a tomada de decisões baseada em
dados. Para que uma empresa se beneficie das mudanças, ela deve ser capaz de fornecer respostas
rápidas a eventos externos. As mudanças necessárias devem ser iniciadas, implementadas e
concluídas o mais rápido possível. A iniciativa para a mudança deve partir dos funcionários que
possuem o conhecimento adequado para interpretar o evento, que são frequentemente aqueles que
trabalham mais próximos do sistema ou máquina em questão. Isso requer a transferência de poderes
de decisão e a criação de oportunidades para que os especialistas técnicos compartilhem seu
conhecimento. O fator crítico é que os funcionários entendam que também são responsáveis por
moldar a mudança; eles devem estar dispostos a iniciá-la por conta própria e preparados para dar o
primeiro passo para que ela aconteça.
#### Questões
##### I.16.3.1 Questão: Qual o nível atual da 'Governança de Dados' na sua organização?
Qual o nível atual da 'Governança de Dados' na sua organização?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não existem políticas ou processos formais para a gestão de dados. A qualidade e o gerenciamento dos dados são tratados de maneira ad-hoc e reativa. |
| 1 | Políticas básicas de dados existem de forma isolada em alguns departamentos. Não há uma abordagem unificada ou responsabilidades claras sobre os dados em toda a organização. |
| 2 | A empresa possui políticas formais de governança de dados documentadas, mas sua implementação é inconsistente entre os departamentos. As responsabilidades sobre os dados começam a ser definidas. |
| 3 | Políticas de governança de dados são implementadas em toda a empresa, com papéis e responsabilidades definidos (ex Data Stewards). A qualidade dos dados é monitorada, proporcionando visibilidade sobre os principais problemas. |
| 4 | A empresa utiliza ferramentas para o gerenciamento de metadados e dados mestres, além de processos automatizados para a limpeza e padronização dos dados. A governança é uma prática estabelecida e proativa. |
| 5 | A estrutura de governança de dados é usada para prever e mitigar riscos relacionados à qualidade dos dados, garantindo que as informações sejam adequadas para análises preditivas e tomada de decisão automatizada. |
| 6 | A governança de dados é totalmente integrada e dinâmica, adaptando-se continuamente a novas fontes de dados e necessidades de negócio. A cultura da empresa é orientada por dados, com processos ágeis e decisões automatizadas baseadas em dados confiáveis. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Documento de Política de Governança de Dados.

- Dicionário de dados e catálogo de dados.

- Plano de gerenciamento de dados mestres (Master Data Management).

- Atas de reunião do comitê de governança de dados.

- Relatórios de qualidade de dados (Data Quality reports).


<!-- pág. original: 201/465 -->
##### Métricas/KPIs

- Percentual de elementos de dados críticos sob governança formal.

- Índices de qualidade dos dados (ex: precisão, completude, consistência).

- Número de incidentes de dados reportados por mês.

- Tempo médio para resolução de problemas de qualidade de dados.

##### Sinais por nível

- Nível 0:


  - Inexistência de documentação sobre gestão de dados

  - problemas de dados são frequentes e sem solução estruturada


- Nível 1:


  - Documentos isolados sobre tratamento de dados em alguns departamentos

  - ausência de um responsável central pelo tema


- Nível 2:


  - Existência de uma política de dados formal, porém pouco divulgada

  - conflitos sobre a "verdade" dos dados entre departamentos


- Nível 3:


  - Papéis como Data Stewards ou Data Owners estão formalmente designados

  - dashboards de qualidade de dados são utilizados pela gestão


- Nível 4:


  - Uso de sistemas de MDM (Master Data Management) e ferramentas de data cleansing

  - a qualidade dos dados é tratada como um requisito para novos projetos


<!-- pág. original: 202/465 -->
- Nível 5:


  - A governança de dados é um pilar para iniciativas de Business Intelligence e Analytics

  - há uma clara vinculação entre a qualidade dos dados e os resultados de negócio


- Nível 6:


  - A empresa participa de ecossistemas de dados com parceiros, baseada em sua forte estrutura de governança
  - a tomada de decisão automatizada é uma realidade em diversos processos

##### Amostragem

- Entrevistas com o Chief Data Officer (CDO), Data Stewards, analistas de dados e gestores de
         áreas de negócio para entender a aplicação das políticas
- Análise da documentação de governança de dados

- Revisão dos relatórios e painéis de qualidade de dados

- Observação de como os problemas de dados são discutidos e resolvidos nas reuniões de
         equipe

##### I.16.3.2 Questão: Como se dá a Gestão de Dados Mestres (MDM)?
Como se dá a Gestão de Dados Mestres (MDM)?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | Não há gestão de dados mestres. Dados críticos (ex clientes, produtos) são cadastrados de forma independente em cada sistema (ERP, CRM, etc.), resultando em alta duplicidade e inconsistência. |
| 1 | A empresa reconhece os problemas de inconsistência de dados, mas as correções são feitas manualmente, de forma reativa e pontual (ex "limpando" planilhas) quando um erro é descoberto. |
| 2 | Existem processos departamentais para tentar padronizar a entrada de dados mestres (ex um departamento "possui" o cadastro de produtos), mas não há integração entre os sistemas. |
| 3 | A empresa definiu formalmente seus dados mestres e utiliza ferramentas ou processos de data quality para identificar duplicatas e inconsistências de forma sistemática, embora a correção ainda seja largamente manual. |
| 4 | Um sistema ou plataforma de MDM está implementado. Dados mestres são consolidados, padronizados e limpos automaticamente. Há uma "fonte única da verdade" (SSOT) lógica ou física para os dados críticos. |
| 5 | O sistema MDM é usado proativamente para gerenciar o ciclo de vida completo dos dados mestres e para simular o impacto de mudanças (ex fusão de cadastros de clientes) antes que elas afetem os sistemas de produção. |
| 6 | Os dados mestres são gerenciados de forma dinâmica e federada, permitindo a integração ágil de novos parceiros ou fontes de dados (ex IoT, e-commerce) na "fonte da verdade", suportando a adaptabilidade do negócio. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Arquitetura de sistemas (mapa de sistemas mostrando ERP, CRM, PLM).

- Documentação do projeto ou plataforma de MDM.

- Regras de negócio documentadas para data cleansing e padronização.

- Relatórios de duplicidade de dados (antes e depois da implementação do MDM).

##### Métricas/KPIs

- Percentual de registros de dados mestres duplicados (ex: clientes, produtos).

- Percentual de campos de dados críticos preenchidos e padronizados.

- Tempo gasto em conciliação manual de dados entre sistemas.

- Nível de confiança nos dados (pesquisa com usuários de negócio).


<!-- pág. original: 204/465 -->
##### Sinais por nível

- Nível 0:


  - Relatórios de vendas de um mesmo cliente são diferentes no ERP e no CRM

  - contagem de produtos em estoque é notoriamente imprecisa


- Nível 1:


  - Equipes financeiras e de logística gastam dias no fechamento do mês para "bater" os números de diferentes relatórios


- Nível 2:


  - O departamento de engenharia cadastra o produto no PLM, e o departamento fiscal/logística recadastra o mesmo produto no ERP, com códigos diferentes


- Nível 3:


  - A empresa possui um "Dicionário de Dados" oficial

  - Painéis de Data Quality mostram ativamente as inconsistências


- Nível 4:


  - Ao cadastrar um novo cliente, o sistema consulta ativamente o MDM para evitar duplicatas


- Nível 5:


  - O sistema MDM é auditável e rastreia quem alterou o quê e quando, garantindo a governança preditiva


- Nível 6:


  - A empresa consegue consolidar dados de uma nova aquisição (empresa) em seu sistema MDM em tempo recorde, adaptando-se rapidamente


<!-- pág. original: 205/465 -->
##### Amostragem

- Entrevistas com analistas de TI (responsáveis pelo ERP/CRM), analistas de negócio e
         arquitetos de dados
- Demonstração ao vivo do sistema de MDM (se existir)

- Solicitar um relatório simples (ex: "vendas por cliente") e verificar se os dados são extraídos de
         uma fonte única ou se exigem consolidação manual
- Verificar o processo de cadastro de um novo produto ou fornecedor


##### I.16.3.3 Questão: Como se dá a Gestão da Qualidade de Dados (DQM)?
Como se dá a Gestão da Qualidade de Dados (DQM)?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A qualidade dos dados não é uma preocupação. Os dados são usados "como estão" (as is). Erros em relatórios são comuns e geralmente ignorados ou contornados manualmente. |
| 1 | A qualidade dos dados é tratada de forma reativa. Os erros são corrigidos manualmente em planilhas ou relatórios finais apenas quando um usuário de negócio os identifica e reclama. |
| 2 | Existem processos manuais ou checklists para validar a entrada de dados em alguns sistemas-chave, na tentativa de prevenir dados ruins, mas não há monitoramento ativo dos dados já existentes. |
| 3 | A empresa começa a medir ativamente a qualidade dos dados. Existem painéis (dashboards) e KPIs de qualidade (ex % de completude, % de duplicatas) que dão visibilidade aos problemas. |
| 4 | A empresa analisa a causa-raiz dos problemas de qualidade de dados. Existem processos formais de remediação para corrigir os dados na fonte (ex no ERP), e não apenas no relatório. |
| 5 | A qualidade de dados é gerenciada de forma proativa e preditiva. Regras de qualidade são automatizadas e integradas aos processos de negócio (ex: impedindo que um pedido sem CEP válido seja salvo). |
| 6 | A gestão da qualidade de dados é um processo adaptativo e de ciclo fechado (closed-loop). O sistema pode identificar e, em alguns casos, autocorrigir anomalias em tempo real, aprendendo e se adaptando a novos padrões de dados. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Painéis (Dashboards) de Qualidade de Dados (ex: Power BI, Qlik).

- Relatórios de Perfilamento de Dados (Data Profiling).

- Documentação de Regras de Negócio de Qualidade (ex: "CPF deve ser válido", "Produto deve
          ter peso").
- Planos de remediação de dados e logs de correção.

- Catálogo de Dados com data quality scores associados.

##### Métricas/KPIs

- % de registros completos em tabelas críticas (ex: cadastro de clientes).

- % de precisão (ex: % de e-mails válidos, % de endereços padronizados).

- Tempo médio para detecção de um erro de dados (MTTD).

- Tempo médio para correção de um erro de dados (MTTR).

- Nível de confiança do usuário nos dados (via pesquisa interna).

##### Sinais por nível

- Nível 0:


  - A equipe de finanças não confia nos dados de vendas do CRM

  - o ditado "lixo entra, lixo sai" (GIGO) é comum


- Nível 1:


<!-- pág. original: 207/465 -->
  - O analista de BI passa 80% do tempo "limpando" planilhas antes de poder iniciar uma análise


- Nível 2:


  - Existência de manuais de procedimento para "como preencher o cadastro de produto"


- Nível 3:


  - Um gestor de logística consegue ver um gráfico que mostra: "Nos últimos 30 dias, 12% dos pedidos foram cadastrados sem a informação do transportador"


- Nível 4:


  - Criação de uma task-force para analisar por que o campo "transportador" não está sendo preenchido no sistema de vendas e implementar uma correção no sistema


- Nível 5:


  - O sistema de vendas agora torna o campo "transportador" obrigatório e valida o código digitado contra a tabela de transportadoras ativas, impedindo o erro


- Nível 6:


  - O sistema identifica um volume atípico de pedidos para um CEP inexistente, bloqueia preventivamente o faturamento para esse CEP e notifica o administrador do sistema

##### Amostragem

- Entrevistas com Data Stewards (guardiões dos dados), analistas de BI e usuários-chave (ex:
       finanças, marketing, logística)
- Solicitar a visualização dos painéis de qualidade de dados

- Pedir que descrevam o processo que acontece quando um dado incorreto é encontrado em um
       relatório importante
- Verificar a existência de regras de validação nos formulários de entrada de dados dos sistemas
       (ERP, CRM)


<!-- pág. original: 208/465 -->
##### I.16.3.4 Questão: Há Padronização de Interfaces de Dados?
Há Padronização de Interfaces de Dados?

##### Respostas

| Nível | Item de resposta |
|---|---|
| 0 | A troca de dados entre sistemas é quase inexistente ou totalmente manual (ex: exportação/importação de planilhas e arquivos .csv). |
| 1 | A integração é feita caso a caso, através de conexões "ponto a ponto" personalizadas e frágeis. Cada nova conexão é um projeto de desenvolvimento separado, e os dados são frequentemente duplicados. |
| 2 | A empresa utiliza um barramento de serviço (ESB) ou ferramenta de EAI (Enterprise Application Integration) para gerenciar algumas integrações centrais, mas a maioria ainda é ponto a ponto. Os formatos de dados (ex XML) começam a ser padronizados. |
| 3 | A empresa adota padrões de indústria (ex OPC-UA para o chão de fábrica) e possui diretrizes internas para a criação de APIs, mas seu uso ainda não é universal. |
| 4 | A empresa possui uma plataforma de gerenciamento de APIs (API Management) ou uma arquitetura de microsserviços. A troca de dados é tratada como um serviço gerenciado, seguro e monitorado. |
| 5 | As interfaces são usadas para habilitar fluxos de dados em tempo real (arquitetura orientada a eventos). O catálogo de APIs é usado para acelerar a inovação, permitindo que novas aplicações consumam dados de forma ágil e governada. |
| 6 | A empresa opera com interfaces abertas e padronizadas que permitem a integração "plug-and-play" não apenas de sistemas internos, mas também de parceiros externos, clientes e fornecedores, criando um ecossistema digital dinâmico. |

##### Possíveis fontes de evidências

##### Artefatos e onde buscar

- Diagrama de arquitetura de sistemas (para identificar conexões P2P vs. centralizadas).

- Documentação da plataforma de integração (ESB, API Management).

- Catálogo de APIs e microsserviços da empresa.

- Diretrizes de desenvolvimento (padrões de codificação para APIs).

- Especificações de padrões de dados (ex: JSON, XML, OPC-UA).

##### Métricas/KPIs

- Tempo médio para integrar um novo sistema.

- Número de integrações ponto a ponto vs. número de APIs reutilizáveis.

- % de reutilização de APIs em novos projetos.

- Custo de manutenção das integrações.

- Número de falhas de integração por mês.

##### Sinais por nível

- Nível 0:


  - O funcionário de logística digita manualmente o pedido do CRM no sistema de faturamento (WMS/ERP)


- Nível 1:


  - O TI gasta semanas para fazer o CRM "conversar" com o ERP

  - se o ERP atualiza, a integração quebra


- Nível 2:


<!-- pág. original: 210/465 -->
  - O sistema de vendas envia um arquivo XML para um diretório, que o sistema de logística "lê" a cada 30 minutos


- Nível 3:


  - A máquina nova no chão de fábrica é conectada à rede via OPC-UA, e seus dados aparecem no MES sem um projeto de software customizado


- Nível 4:


  - A equipe de marketing cria um novo app móvel em dias, consumindo a mesma "API de Clientes" que o portal web utiliza


- Nível 5:


  - Quando um pedido é aprovado no ERP, um "evento" é disparado, e os sistemas de logística, financeiro e CRM são notificados instantaneamente via interfaces


- Nível 6:


  - Um novo fornecedor logístico (3PL) se conecta diretamente ao barramento de eventos da empresa em 24h para receber pedidos e enviar status de entrega

##### Amostragem

- Entrevistas com o Arquiteto de Soluções/TI, Gerente de Desenvolvimento e equipe de
        DevOps/Integração
- Revisão da documentação de arquitetura

- Pedir para ver o portal de desenvolvedores ou o catálogo de APIs

- Questionar o processo: "Se comprarmos um novo software de RH (ex: Workday), quanto tempo
        leva para integrá-lo ao nosso sistema financeiro?"
#### Glossário
[Sem glossário]
## ANEXO II - GUIA DE AVALIAÇÃO DE MATURIDADE DA INDÚSTRIA 4.0

<!-- pág. original: 405/465 -->
ANEXO II - GUIA DE AVALIAÇÃO DE MATURIDADE DA INDÚSTRIA 4.0




                Processo e Modelo de Avaliação




                Versão 1.0 - Fevereiro de 2026


<!-- pág. original: 406/465 -->
  Sumário Executivo Este guia apresenta um modelo de medição e processo completo e estruturado para a avaliação da maturidade de organizações industriais em relação à Indústria 4.0 . O guia inspira-se na Portaria Inmetro nº 171, de 2026, ou substituta, para aplicar a avaliação de maturidade em indústrias através de três blocos, oito pilares e 16 dimensões, utilizando um índice e uma escala de maturidade de 6 níveis (1 a 6).


<!-- pág. original: 407/465 -->
### II.1 Visão Geral
O Processo de avaliação proposto visa medir a maturidade de uma organização industrial em relação sob a perspectiva dos conceitos inerentes à indústria 4.0. Sobre os benefícios e a aplicabilidade das avaliações, podemos destacar:


#### II.1.1 Benefícios da Avaliação
   •   Diagnóstico Objetivo: Aferir o nível de maturidade da organização em uma escala padronizada de 0 a 6.
   •   Visão Holística: Avaliar 16 dimensões distribuídas em 3 blocos sócio-técnicos (Processo, Tecnologia e Organização).
   •   Identificação de Lacunas: Detectar áreas críticas (dimensões) que necessitam de maior atenção e investimentos.
   •   Priorização de Investimentos: Orientar decisões sobre onde alocar recursos para maximizar resultados.
   •   Benchmarking: Permitir comparações entre diferentes unidades organizacionais ou ao longo do tempo.
   •   Roadmap de Transformação: Apoiar a definição de um plano estruturado de evolução.
   •   Engajamento de Stakeholders: Criar uma linguagem comum para discussão sobre Indústria 4.0.


#### II.1.2 Aplicabilidade
As avaliações são aplicáveis a qualquer indústria engajada em iniciativas de transformação digital. Elas permitem a avaliação e comparações sob diferentes perspectivas. Dentre elas podemos destacar:

   •   Setores industriais: Por exemplo, eletroeletrônicos, farmacêutico, automotivo, e outros setores de manufatura de bens;
   •   Portes de organização: Desde pequenas e médias empresas até grandes corporações multinacionais;
   •   Níveis de maturidade: Organizações em qualquer estágio de transformação digital, desde iniciantes até avançadas;
   •   Escopo de avaliação: Pode ser aplicado a uma planta industrial específica, a uma unidade de negócio ou organização como um todo.


<!-- pág. original: 408/465 -->
### II.2 Objetivo e Escopo

#### II.2.1 Objetivo
Este documento descreve o Modelo de Medição e o Processo de Avaliação de Maturidade da Indústria 4.0, definidos de forma a:

   •   Permitirem a avaliação objetiva e sistemática das capacidades da organização;
   •   Permitirem a atribuição de um Índice de Maturidade com base no resultado da avaliação;
   •   Serem aplicáveis a indústrias de bens, por exemplo, eletroeletrônicos, farmacêutica e automotivo, etc.;
   •   Fornecer um método replicável e auditável de avaliação;
   •   Gerar evidências documentadas que suportem os resultados da avaliação.


#### II.2.2 Escopo
O escopo deste guia é cobrir e explicitar o seguinte escopo:

   •   O processo completo de avaliação, desde o planejamento até a documentação dos resultados;
   •   A estrutura do modelo de medição com seus três blocos, 8 pilares e 16 dimensões;
   •   Os critérios detalhados para atribuição de níveis de maturidade (0 a 6) para cada dimensão;
   •   O método de cálculo do índice final de maturidade através de uma ponderação das dimensões;
   •   Modelos de documentos, questionários e relatórios.
   •   Exemplos práticos e casos de uso

Este guia não cobre:

   •   A implementação de tecnologias ou processos de Indústria 4.0;
   •   Consultoria específica sobre soluções tecnológicas, e;
   •   Certificação formal de maturidade I4.0.


<!-- pág. original: 409/465 -->
### II.3 Termos e Definições
Para os propósitos deste guia, aplicam-se os seguintes termos e definições:


#### II.3.1 Termos Gerais
Indústria 4.0: Paradigma de manufatura que integra tecnologias digitais avançadas, sistemas ciber-físicos, Internet das Coisas e análise de dados para criar fábricas inteligentes e cadeias de valor conectadas.

Maturidade: Grau de efetividade e eficiência com que uma organização implementa e utiliza processos, tecnologias e práticas relacionadas à Indústria 4.0.

Avaliação: Processo repetível e sistemático de examinar e julgar o nível de maturidade de uma organização em relação a critérios estabelecidos.

Evidência Objetiva: Dados que suportam a existência ou veracidade de algo, podendo ser obtidos através de observação, artefatos, medição, teste ou outros meios.


#### II.3.2 Termos do Modelo de Medição da Maturidade da Indústria 4.0

Bloco: Agrupamento de mais alto nível que representa uma área fundamental da transformação digital do ponto de vista sócio-técnico. O Modelo de Medição da Maturidade da Indústria 4.0 (MA-I4.0) possui 3 blocos: Processo, Tecnologia e Organização.

Pilar: Uma segmentação conceitual de nível intermediário dentro de um bloco, representando subdivisões facilmente observáveis, nas quais as empresas devem focar para se tornarem organizações preparadas para a Indústria 4.0. O MA-I4.0 possui 8 pilares.

Dimensão: Área de avaliação específica dentro de um pilar, representando o constructo ou uma variável mensurável de alto nível de abstração. O MA-I4.0 possui 16 dimensões.

Capacidade: São medidas que visam qualitativamente caracterizar e operacionalizar as dimensões. O MA-I4.0 possui 27 capacidades. Uma capacidade é avaliada por uma ou mais questões em uma escala ordinal de 0 a 6.

Nível de Maturidade: Grau de evolução de uma dimensão, medido em uma escala de 0 (inexistente) a 6 (adaptativo).

Índice de Maturidade: Valor numérico final que representa o nível geral de maturidade 4.0 da organização, calculado através de média ponderada das dimensões.


#### II.3.3 Termos do Processo de Avaliação
Avaliador Líder: Profissional responsável por planejar, conduzir e documentar a avaliação de maturidade.


<!-- pág. original: 410/465 -->
Equipe de Avaliação: Grupo de profissionais que conduz a avaliação, liderado pelo Avaliador Líder.

Patrocinador: Executivo da organização avaliada que autoriza e apoia a realização da avaliação.

Participante: Profissional da organização avaliada que fornece informações durante a avaliação.

Escopo da Avaliação: Definição clara dos limites organizacionais, geográficos e funcionais da avaliação.

Plano de Avaliação: Documento que descreve como a avaliação será conduzida, incluindo cronograma, recursos e métodos.

Relatório de Auditoria: Documento que apresenta os resultados da avaliação, incluindo o índice de maturidade, pontuações por dimensão e recomendações.


<!-- pág. original: 411/465 -->
### II.4 Visão Geral do Processo de Avaliação
O Processo de avaliação para o MA-I4.0 é estruturado em quatro subprocessos principais, inspirados na norma ISO/IEC 33020:


#### II.4.1 Diagrama do Processo




                           Figura 1. Processo de Avaliação para o MA-I4.0



#### II.4.2 Descrição de Alto Nível dos Subprocessos

Subprocesso 1: Preparar a Avaliação Objetivo: Planejar e organizar todos os aspectos da avaliação.

Atividades principais:

   •   Definir o escopo da avaliação
   •   Identificar os participantes
   •   Elaborar o plano de avaliação
   •   Preparar os instrumentos de coleta de dados
   •   Comunicar o processo aos stakeholders

Produtos gerados:

   •   Plano de Avaliação
   •   Cronograma de atividades
   •   Lista de participantes
   •   Questionários e checklists

Subprocesso 2: Realizar Avaliação Inicial Objetivo: Coletar informações preliminares e realizar uma primeira análise.


<!-- pág. original: 412/465 -->
Atividades principais:

   •   Conduzir entrevistas iniciais
   •   Aplicar questionários
   •   Revisar documentação existente
   •   Realizar observações in loco
   •   Consolidar informações coletadas

Produtos gerados:

   •   Registros de entrevistas
   •   Questionários preenchidos
   •   Lista de evidências coletadas
   •   Relatório preliminar de achados

Subprocesso 3: Realizar Avaliação Final Objetivo: Validar as informações coletadas e atribuir os níveis de maturidade.

Atividades principais:

   •   Validar evidências com participantes
   •   Atribuir níveis de maturidade às 16 dimensões
   •   Calcular o índice de maturidade
   •   Identificar pontos fortes e oportunidades de melhoria
   •   Elaborar recomendações

Produtos gerados:

   •   Matriz de avaliação preenchida
   •   índice de maturidade calculado
   •   Lista de pontos fortes
   •   Lista de oportunidades de melhoria

Subprocesso 4: Documentar Resultados Objetivo: Formalizar e comunicar os resultados da avaliação.

Atividades principais:

   •   Elaborar o relatório final de avaliação
   •   Preparar apresentação executiva
   •   Revisar e aprovar o relatório
   •   Apresentar resultados aos stakeholders
   •   Arquivar documentação da avaliação

Produtos gerados:

   •   Relatório Final de Avaliação


<!-- pág. original: 413/465 -->
•   Apresentação executiva
•   Relatório de Recomendações
•   Armazenamento da Documentação
•   Divulgação de Resultados


<!-- pág. original: 414/465 -->
### II.5 Descrição Detalhada do Processo de Avaliação

#### II.5.1 Subprocesso 1: Preparar a Realização da Avaliação

##### II.5.1.1 Atividade: Estabelecer o Compromisso para a Avaliação
Objetivo: Obter o comprometimento formal da organização para a realização da avaliação.

Tarefas:

II.5.1.1.1 Tarefa: Identificar o Patrocinador da Avaliação

   •   Identificar o executivo que autorizará e apoiará a avaliação
   •   Garantir que o patrocinador tenha autoridade e influência adequadas
   •   Documentar o comprometimento formal

Critérios de Entrada:

   •   Interesse da organização em avaliar sua maturidade I4.0

Critérios de Saída:

   •   Patrocinador identificado e comprometido
   •   Carta de compromisso assinada

II.5.1.1.2 Tarefa: Definir o Propósito e Escopo da Avaliação

   •   Definir claramente por que a avaliação está sendo realizada
   •   Estabelecer os limites organizacionais (unidades, departamentos)
   •   Estabelecer os limites geográficos (plantas, localizações)
   •   Estabelecer os limites funcionais (processos, sistemas)
   •   Definir se a avaliação será completa (16 dimensões) ou parcial

Critérios de Entrada:

   •   Patrocinador comprometido

Critérios de Saída:

   •   Documento de escopo aprovado
   •   Limites da avaliação claramente definidos

II.5.1.1.3 Tarefa: Definir Restrições da Avaliação

   •   Identificar restrições de tempo (prazo para conclusão)
   •   Identificar restrições de orçamento
   •   Identificar restrições de acesso (áreas restritas, informações confidenciais)


<!-- pág. original: 415/465 -->
   •   Identificar restrições de recursos (disponibilidade de pessoas)

Critérios de Entrada:

   •   Escopo definido

Critérios de Saída:

   •   Lista de restrições documentada
   •   Plano de mitigação de restrições elaborado

##### II.5.1.2 Atividade: Selecionar e Preparar a Equipe de Avaliação
Objetivo: Formar uma equipe competente para conduzir a avaliação.

Tarefas:

II.5.1.2.1 Tarefa: Selecionar o Avaliador Líder

   •   Identificar profissional com conhecimento em Indústria 4.0
   •   Verificar experiência em avaliações de maturidade
   •   Verificar habilidades de liderança e comunicação
   •   Formalizar a designação

Critérios de Entrada:

   •   Necessidade de avaliação estabelecida

Critérios de Saída:

   •   Avaliador Líder designado

II.5.1.2.2 Tarefa: Selecionar Avaliadores Adicionais

   •   Determinar o tamanho necessário da equipe com base no escopo
   •   Identificar profissionais com conhecimentos complementares
   •   Garantir cobertura de conhecimento nos blocos áreas de Processo, Tecnologia e Organizacional
   •   Formalizar as designações

Critérios de Entrada:

   •   Avaliador Líder designado
   •   Escopo da avaliação definido

Critérios de Saída:

   •   Equipe de avaliação completa


<!-- pág. original: 416/465 -->
   •   Papéis e responsabilidades definidos

II.5.1.2.3 Tarefa: Preparar a Equipe de Avaliação

   •   Realizar reunião de alinhamento da equipe
   •   Revisar o MA-I4.0 e os critérios de avaliação
   •   Revisar o Processo de avaliação
   •   Distribuir materiais de referência
   •   Esclarecer dúvidas

Critérios de Entrada:

   •   Equipe de avaliação selecionada

Critérios de Saída:

   •   Equipe alinhada e preparada
   •   Materiais de referência distribuídos

##### II.5.1.3 Atividade: Elaborar o Plano de Avaliação
Objetivo: Documentar como a avaliação será conduzida.

Tarefas:

II.5.1.3.1 Tarefa: Identificar os Participantes da Avaliação

   •   Identificar gestores e profissionais-chave em cada área
   •   Garantir representação de todas as áreas relevantes ao escopo
   •   Verificar disponibilidade dos participantes
   •   Obter compromisso de participação

Critérios de Entrada:

   •   Escopo da avaliação definido

Critérios de Saída:

   •   Lista de participantes elaborada
   •   Compromisso de participação obtido

II.5.1.3.2 Tarefa: Definir Métodos de Coleta de Dados

   •   Selecionar métodos apropriados (entrevistas, questionários, observação, análise documental)
   •   Definir quando cada método será utilizado
   •   Preparar instrumentos de coleta (roteiros de entrevista, questionários)

Critérios de Entrada:


<!-- pág. original: 417/465 -->
   •   Escopo e participantes definidos

Critérios de Saída:

   •   Métodos de coleta definidos
   •   Instrumentos preparados

II.5.1.3.3 Tarefa: Elaborar o Cronograma da Avaliação

   •   Definir datas para cada atividade do Processo
   •   Alocar tempo adequado para cada entrevista/atividade
   •   Considerar disponibilidade dos participantes
   •   Incluir marcos e entregas
   •   Obter aprovação do patrocinador

Critérios de Entrada:

   •   Participantes e métodos definidos

Critérios de Saída:

   •   Cronograma elaborado e aprovado

II.5.1.3.4 Tarefa: Consolidar o Plano de Avaliação

   •   Documentar todos os elementos do planejamento
   •   Incluir: escopo, objetivos, equipe, participantes, métodos, cronograma, restrições
   •   Revisar o plano com a equipe de avaliação
   •   Obter aprovação do patrocinador

Critérios de Entrada:

   •   Todos os elementos do planejamento definidos

Critérios de Saída:

   •   Plano de Avaliação completo e aprovado

##### II.5.1.4 Atividade: Comunicar a Avaliação
Objetivo: Informar os stakeholders sobre a avaliação e obter seu engajamento.

Tarefas:

II.5.1.4.1 Tarefa: Preparar Material de Comunicação

   •   Elaborar apresentação sobre a avaliação


<!-- pág. original: 418/465 -->
   •   Preparar FAQ (perguntas frequentes)
   •   Preparar comunicados para diferentes públicos

Critérios de Entrada:

   •   Plano de Avaliação aprovado

Critérios de Saída:

   •   Material de comunicação preparado

II.5.1.4.2 Tarefa: Realizar Reunião de Abertura

   •   Convocar reunião com patrocinador e principais stakeholders
   •   Apresentar o propósito, escopo e Processo da avaliação
   •   Esclarecer expectativas
   •   Responder perguntas
   •   Obter comprometimento

Critérios de Entrada:

   •   Material de comunicação preparado

Critérios de Saída:

   •   Reunião de abertura realizada
   •   Stakeholders informados e engajados

II.5.1.4.3 Tarefa: Comunicar aos Participantes

   •   Enviar convites formais aos participantes
   •   Fornecer informações sobre o Processo
   •   Informar datas e horários das atividades
   •   Esclarecer o que será esperado deles

Critérios de Entrada:

   •   Reunião de abertura realizada

Critérios de Saída:

   •   Participantes informados e preparados


<!-- pág. original: 419/465 -->
#### II.5.2 Subprocesso 2: Realizar a Avaliação Inicial

##### II.5.2.1 Atividade: Coletar Informações Documentais
Objetivo: Obter informações preliminares através de documentos existentes.

Tarefas:

II.5.2.1.1 Tarefa: Solicitar Documentação Relevante

   •   Elaborar lista de documentos necessários
   •   Solicitar formalmente à organização
   •   Estabelecer prazo para fornecimento

Documentos típicos solicitados:

   •   Organogramas
   •   Descrições de Processos
   •   Diagramas de arquitetura de TI/OT
   •   Políticas e procedimentos
   •   Planos estratégicos
   •   Relatórios de desempenho
   •   Inventários de tecnologias

Critérios de Entrada:

   •   Plano de Avaliação aprovado

Critérios de Saída:

   •   Documentação solicitada e recebida

II.5.2.1.2 Tarefa: Analisar a Documentação

   •   Revisar cada documento recebido
   •   Extrair informações relevantes para cada dimensão do MA-I4.0
   •   Identificar evidências de práticas implementadas
   •   Identificar lacunas de informação
   •   Preparar perguntas para entrevistas

Critérios de Entrada:

   •   Documentação recebida

Critérios de Saída:

   •   Análise documental concluída
   •   Perguntas para entrevistas preparadas


<!-- pág. original: 420/465 -->
##### II.5.2.2 Atividade: Conduzir Entrevistas e Observações
Objetivo: Coletar informações através de interação direta com os participantes.

Tarefas:

II.5.2.2.1 Tarefa: Realizar Entrevistas Estruturadas

   •   Conduzir entrevistas conforme cronograma
   •   Utilizar roteiros preparados
   •   Fazer perguntas sobre cada dimensão relevante ao entrevistado
   •   Registrar respostas de forma estruturada
   •   Solicitar evidências adicionais quando necessário

Critérios de Entrada:

   •   Cronograma de entrevistas estabelecido
   •   Roteiros preparados

Critérios de Saída:

   •   Entrevistas realizadas
   •   Registros de entrevistas documentados

II.5.2.2.2 Tarefa: Aplicar Questionários

   •   Distribuir questionários aos participantes
   •   Fornecer instruções claras de preenchimento
   •   Estabelecer prazo para devolução
   •   Acompanhar o preenchimento
   •   Coletar questionários preenchidos

Critérios de Entrada:

   •   Questionários preparados
   •   Participantes identificados

Critérios de Saída:

   •   Questionários preenchidos e coletados

II.5.2.2.3 Tarefa: Realizar Observações In Loco

   •   Visitar áreas operacionais (chão de fábrica, escritórios)
   •   Observar processos em execução
   •   Verificar tecnologias implementadas
   •   Observar práticas de trabalho
   •   Registrar observações com fotos (quando permitido)


<!-- pág. original: 421/465 -->
Critérios de Entrada:

   •   Autorização para visitas obtida
   •   Cronograma de visitas estabelecido

Critérios de Saída:

   •   Observações realizadas
   •   Registros de observações documentados

##### II.5.2.3 Atividade: Consolidar Informações Coletadas
Objetivo: Organizar e estruturar todas as informações coletadas.

Tarefas:

II.5.2.3.1 Tarefa: Organizar Evidências por Dimensão

   •   Criar uma matriz de evidências
   •   Classificar cada evidência coletada por dimensão do MA-I4.0
   •   Identificar múltiplas evidências para a mesma dimensão
   •   Identificar dimensões com evidências insuficientes

Critérios de Entrada:

   •   Todas as atividades de coleta concluídas

Critérios de Saída:

   •   Matriz de evidências elaborada

II.5.2.3.2 Tarefa: Realizar Análise Preliminar

   •   Revisar evidências para cada dimensão
   •   Fazer uma avaliação preliminar do nível de maturidade
   •   Identificar inconsistências ou lacunas
   •   Preparar lista de questões a esclarecer

Critérios de Entrada:

   •   Matriz de evidências elaborada

Critérios de Saída:

   •   Análise preliminar concluída
   •   Lista de questões a esclarecer preparada


<!-- pág. original: 422/465 -->
II.5.2.3.3 Tarefa: Elaborar Relatório Preliminar

   •   Documentar achados preliminares
   •   Incluir avaliações preliminares por dimensão
   •   Incluir lista de questões a esclarecer
   •   Incluir lista de evidências adicionais necessárias

Critérios de Entrada:

   •   Análise preliminar concluída

Critérios de Saída:

   •   Relatório preliminar elaborado




#### II.5.3 Subprocesso 3: Realizar a Avaliação Final

##### II.5.3.1 Atividade: Validar Informações Coletadas
Objetivo: Garantir a precisão e completude das informações.

Tarefas:

II.5.3.1.1 Tarefa: Esclarecer Questões Pendentes

   •   Agendar reuniões de esclarecimento
   •   Apresentar questões identificadas
   •   Obter respostas e evidências adicionais
   •   Registrar esclarecimentos

Critérios de Entrada:

   •   Relatório preliminar elaborado
   •   Lista de questões a esclarecer

Critérios de Saída:

   •   Questões esclarecidas
   •   Evidências adicionais coletadas

II.5.3.1.2 Tarefa: Validar Achados com Participantes

   •   Apresentar achados preliminares aos participantes


<!-- pág. original: 423/465 -->
   •   Solicitar confirmação ou correção
   •   Resolver discrepâncias
   •   Obter concordância sobre os fatos

Critérios de Entrada:

   •   Questões esclarecidas

Critérios de Saída:

   •   Achados validados pelos participantes

##### II.5.3.2 Atividade: Atribuir Níveis de Maturidade
Objetivo: Determinar o nível de maturidade de cada dimensão.

Tarefas:

II.5.3.2.1 Tarefa: Avaliar Cada Dimensão Individualmente

   •   Para cada uma das 16 dimensões:
           ● Revisar todas as evidências coletadas
           ● Comparar com os critérios de cada nível (0 a 6)
           ● Determinar o nível que melhor descreve a situação atual
           ● Documentar a justificativa da avaliação
           ● Identificar evidências-chave que suportam a avaliação

Critérios de Entrada:

   •   Achados validados
   •   Critérios de níveis de maturidade disponíveis

Critérios de Saída:

   •   Nível de maturidade atribuído a cada dimensão
   •   Justificativas documentadas

II.5.3.2.2 Tarefa: Revisar Consistência das Avaliações

   •   Revisar todas as 16 avaliações em conjunto
   •   Verificar consistência entre dimensões relacionadas
   •   Identificar e resolver inconsistências
   •   Obter consenso da equipe de avaliação

Critérios de Entrada:

   •   Todas as dimensões avaliadas


<!-- pág. original: 424/465 -->
Critérios de Saída:

   •   Avaliações consistentes e consensuadas

##### II.5.3.3 Atividade: Calcular o índice de maturidade
Objetivo: Calcular o índice geral de maturidade da organização.

Tarefas:

II.5.3.3.1 Tarefa: Calcular Médias dos Pilares

   •   Para cada um dos 8 pilares:
           ● Somar as notas das dimensões do pilar
           ● Dividir pelo número de dimensões
           ● Registrar a média do pilar

Critérios de Entrada:

   •   Níveis de todas as dimensões atribuídos

Critérios de Saída:

   •   Médias dos 8 pilares calculadas

II.5.3.3.2 Tarefa: Calcular Médias dos Blocos

   •   Para cada um dos 3 blocos:
           ● Somar as médias dos pilares do bloco
           ● Dividir pelo número de pilares
           ● Registrar a média do bloco

Critérios de Entrada:

   •   Médias dos pilares calculadas

Critérios de Saída:

   •   Médias dos 3 blocos calculadas

II.5.3.3.3 Tarefa: Calcular o índice de maturidade Final

   •   Calcular a média aritmética das dimensões
   •   Registrar o índice de maturidade final (0 a 6)
   •   Classificar o nível geral de maturidade

Critérios de Entrada:


<!-- pág. original: 425/465 -->
   •   Médias dos dimensões calculadas

Critérios de Saída:

   •   índice de maturidade final calculado
   •   Nível geral de maturidade determinado

##### II.5.3.4 Atividade: Identificar Pontos Fortes e Oportunidades
Objetivo: Analisar os resultados e gerar insights.

Tarefas:

II.5.3.4.1 Tarefa: Identificar Pontos Fortes

   •   Identificar dimensões com níveis mais altos
   •   Identificar práticas exemplares observadas
   •   Documentar fatores que contribuem para o sucesso
   •   Identificar capacidades e dimensões que podem ser alavancadas

Critérios de Entrada:

   •   índice de maturidade calculado

Critérios de Saída:

   •   Lista de pontos fortes documentada

II.5.3.4.2 Tarefa: Identificar Oportunidades de Melhoria

   •   Identificar dimensões com níveis mais baixos
   •   Identificar lacunas críticas
   •   Priorizar oportunidades por impacto e viabilidade
   •   Identificar dependências entre melhorias

Critérios de Entrada:

   •   índice de maturidade calculado

Critérios de Saída:

   •   Lista de oportunidades de melhoria documentada

II.5.3.4.3 Tarefa: Elaborar Recomendações

   •   Desenvolver recomendações específicas e acionáveis
   •   Priorizar recomendações (curto, médio, longo prazo)
   •   Estimar esforço e recursos necessários


<!-- pág. original: 426/465 -->
   •   Identificar ganhos rápidos

Critérios de Entrada:

   •   Pontos fortes e oportunidades identificados

Critérios de Saída:

   •   Recomendações elaboradas e priorizadas




#### II.5.4 Subprocesso 4: Documentar os Resultados da Avaliação

##### II.5.4.1 Atividade: Elaborar o Relatório Final
Objetivo: Documentar formalmente os resultados da avaliação.

Tarefas:

II.5.4.1.1 Tarefa: Estruturar o Relatório

   •   Utilizar o modelo de relatório padrão (APÊNDICE B)
   •   Incluir todas as seções obrigatórias
   •   Organizar informações de forma lógica e clara

Critérios de Entrada:

   •   Todos os resultados da avaliação disponíveis

Critérios de Saída:

   •   Estrutura do relatório definida

II.5.4.1.2 Tarefa: Redigir o Relatório

   •   Redigir sumário executivo
   •   Documentar metodologia utilizada
   •   Apresentar resultados por dimensão
   •   Apresentar índice de maturidade e interpretação
   •   Documentar pontos fortes e oportunidades
   •   Apresentar recomendações
   •   Incluir gráficos e visualizações

Critérios de Entrada:

   •   Estrutura do relatório definida


<!-- pág. original: 427/465 -->
Critérios de Saída:

   •   Relatório redigido

II.5.4.1.3 Tarefa: Revisar e Aprovar o Relatório

   •   Revisar o relatório pela equipe de avaliação
   •   Corrigir erros e inconsistências
   •   Obter aprovação do Avaliador Líder
   •   Finalizar o documento

Critérios de Entrada:

   •   Relatório redigido

Critérios de Saída:

   •   Relatório final aprovado

##### II.5.4.2 Atividade: Apresentar os Resultados
Objetivo: Comunicar os resultados aos stakeholders.

Tarefas:

II.5.4.2.1 Tarefa: Preparar Apresentação Executiva

   •   Criar apresentação resumida dos resultados
   •   Focar em insights e recomendações
   •   Preparar visualizações impactantes
   •   Antecipar perguntas

Critérios de Entrada:

   •   Relatório final aprovado

Critérios de Saída:

   •   Apresentação executiva preparada

II.5.4.2.2 Tarefa: Realizar Reunião de Apresentação

   •   Agendar reunião com patrocinador e stakeholders-chave
   •   Apresentar os resultados
   •   Responder perguntas
   •   Discutir próximos passos
   •   Obter feedback


<!-- pág. original: 428/465 -->
Critérios de Entrada:

   •   Apresentação executiva preparada

Critérios de Saída:

   •   Resultados apresentados
   •   Feedback coletado

II.5.4.2.3 Tarefa: Entregar o Relatório Final

   •   Entregar formalmente o relatório ao patrocinador
   •   Distribuir cópias conforme acordado
   •   Disponibilizar versão digital

Critérios de Entrada:

   •   Reunião de apresentação realizada

Critérios de Saída:

   •   Relatório final entregue

##### II.5.4.3 Atividade: Arquivar a Documentação
Objetivo: Preservar a documentação da avaliação para referência futura.

Tarefas:

II.5.4.3.1 Tarefa: Organizar a Documentação

   •   Compilar todos os artefatos da avaliação
   •   Organizar em estrutura lógica
   •   Incluir: plano, evidências, registros, relatórios
   •   Gerar um pacote de artefatos da avaliação
   •   Obter hash criptográfico do pacote de artefatos
   •   Disponibilizar informações públicas da avaliação

Critérios de Entrada:

   •   Avaliação concluída

Critérios de Saída:

   •   Documentação organizada

II.5.4.3.2 Tarefa: Arquivar a Documentação


<!-- pág. original: 429/465 -->
   •   Armazenar em local seguro e acessível
   •   Garantir backup adequado
   •   Aplicar/Definir período de retenção (não inferior a 5 anos)
   •   Documentar localização do arquivo

Critérios de Entrada:

   •   Documentação organizada

Critérios de Saída:

   •   Documentação arquivada


<!-- pág. original: 430/465 -->
### II.6 Papéis e Responsabilidades

#### II.6.1 Avaliador Líder
Descrição: Profissional responsável por planejar, conduzir e documentar a avaliação de maturidade I4.0.

Responsabilidades:

   •   Elaborar o plano de avaliação
   •   Liderar a equipe de avaliação
   •   Coordenar todas as atividades do processo
   •   Garantir a qualidade e objetividade da avaliação
   •   Tomar decisões finais sobre níveis de maturidade
   •   Elaborar e aprovar o relatório final
   •   Apresentar resultados aos stakeholders

Competências requeridas:

   ●   Conhecimento profundo do MA-I4.0
   •   Conhecimento de tecnologias e processos de Indústria 4.0
   •   Experiência em avaliações de maturidade ou auditorias
   •   Habilidades de liderança e gestão de equipes
   •   Excelentes habilidades de comunicação oral e escrita
   •   Capacidade analítica e pensamento crítico
   •   Imparcialidade e objetividade


#### II.6.2 Avaliador
Descrição: Membro da equipe de avaliação que apoia o Avaliador-Líder na condução da avaliação.

Responsabilidades:

   •   Participar do planejamento da avaliação
   •   Coletar informações e evidências
   •   Conduzir entrevistas e observações
   •   Analisar documentação
   •   Contribuir para a atribuição de níveis de maturidade
   •   Apoiar na elaboração do relatório

Competências requeridas:

   •   Conhecimento do MA-I4.0
   •   Conhecimento em uma ou mais áreas (Processo, Tecnologia, Organização)
   •   Experiência em avaliações ou auditorias (desejável)
   •   Boas habilidades de comunicação
   •   Capacidade analítica


<!-- pág. original: 431/465 -->
   •   Imparcialidade e objetividade


#### II.6.3 Patrocinador
Descrição: Executivo da organização avaliada que autoriza e apoia a realização da avaliação.

Responsabilidades:

   •   Autorizar a realização da avaliação
   •   Definir o escopo e objetivos
   •   Alocar recursos necessários
   •   Garantir acesso da equipe de avaliação
   •   Apoiar o engajamento dos participantes
   •   Receber e revisar os resultados
   •   Decidir sobre ações de melhoria

Competências requeridas:

   •   Autoridade organizacional adequada
   •   Compreensão da importância da Indústria 4.0
   •   Compromisso com a transformação digital


#### II.6.4 Participante
Descrição: Profissional da organização avaliada que fornece informações durante a avaliação.

Responsabilidades:

   •   Participar de entrevistas conforme agendado
   •   Responder questionários
   •   Fornecer documentação e evidências
   •   Esclarecer dúvidas da equipe de avaliação
   •   Validar achados preliminares

Competências requeridas:

   •   Conhecimento da área/Processo que representa
   •   Disponibilidade para participar
   •   Honestidade e transparência


#### II.6.5 Responsável Técnico
Descrição: Profissional da organização avaliada que facilita a logística da avaliação.

Responsabilidades:

   •   Servir como ponto de contato principal
   •   Facilitar o acesso da equipe de avaliação
   •   Agendar entrevistas e reuniões


<!-- pág. original: 432/465 -->
   •   Providenciar documentação solicitada
   •   Resolver questões logísticas
   •   Comunicar internamente sobre a avaliação

Competências requeridas:

   •   Conhecimento da organização
   •   Boas habilidades de comunicação e coordenação
   •   Capacidade de mobilizar recursos


<!-- pág. original: 433/465 -->
### II.7 Estrutura do Modelo de Maturidade da Indústria 4.0 (MA-I4.0): Estrutura Completa

#### II.7.1 Visão Geral
O MA-I4.0 foi desenvolvido para ajudar empresas de manufatura a avaliar sua atual prontidão para a Indústria 4.0 e ajudar a desenvolver um roadmap de transformação digital. O método identifica 3 blocos (ou áreas) de construção fundamentais que qualquer fábrica ou planta deve considerar para se transformar em uma organização preparada para a Indústria 4.0.


#### II.7.2 Blocos do MA-I4.0

##### II.7.2.1 Processo

Definição: O bloco de Processo abrange a integração de processos dentro das operações da empresa, ao longo da cadeia de suprimentos e através do ciclo de vida do produto.

Importância: Para maximizar valor, a tecnologia deve sempre ser aplicada em conjunto com processos efetivos e bem desenhados. Usar tecnologia para digitalizar um processo mal desenhado resultará apenas em um processo digital mal desenhado. Por outro lado, aplicar tecnologia a um processo bem desenvolvido aumentará sua eficiência e permitirá a criação de valor.

Foco: A Indústria 4.0 expandiu o conceito de melhoria de processos para focar na integração de processos dentro das operações da empresa (Operação), cadeia de suprimentos (Cadeia de Suprimentos) e ciclo de vida do produto (Ciclo de Vida de Produto). À medida que os processos se tornam integrados, eles convergem em um sistema unificado onde dados são compartilhados, processados e integrados através das camadas de gestão de produto, produção e empresa da organização.

##### II.7.2.2 Tecnologia

Definição: O bloco de Tecnologia abrange as tecnologias digitais que habilitam a Indústria 4.0, incluindo automação, conectividade e inteligência.

Importância: O avanço tecnológico tem sido a pedra angular das últimas três grandes revoluções industriais. A descoberta da energia a vapor possibilitou a primeira revolução industrial, enquanto inovações em energia elétrica catalisaram a segunda. De forma similar, a Indústria 3.0 foi impulsionada pelo advento da eletrônica e Tecnologia da Informação (TI), que permitiram às empresas alcançar um grau inigualável de precisão e eficiência através da automação.

Foco: A tecnologia permanece crítica na Indústria 4.0. Novas tecnologias digitais, como computação em nuvem, machine learning e Internet das Coisas (IoT), estão criando um cenário industrial hiper-conectado, onde ativos físicos e equipamentos são integrados com sistemas empresariais para permitir a constante e dinâmica troca e análise de dados. Para realizar suas ambições de Indústria 4.0, um alto grau de automação, conectividade ubíqua e sistemas inteligentes são necessários. Para refletir isso, o bloco de Tecnologia foi segmentado nos 3 pilares de Automação, Conectividade e Inteligência.

##### II.7.2.3 Organização

 Definição: O bloco de Organização abrange as pessoas, estruturas e sistemas de gestão que permitem à organização executar efetivamente sua estratégia de Indústria 4.0.

 Importância: A organização é o terceiro bloco da Indústria 4.0. Frequentemente subestimada, a Organização desempenha um papel igualmente importante ao lado de Tecnologia e Processos. Para permanecer relevante diante da crescente competição na Indústria 4.0, as empresas devem adaptar suas estruturas organizacionais e Processos para permitir que sua força de trabalho acompanhe o ritmo.

 Foco: A Indústria 4.0 demanda um foco maior em dois componentes-chave que podem afetar a efetividade de uma organização. O primeiro componente são as pessoas que compõem a organização — toda a força de trabalho desde a alta gestão até às equipes operacionais. O segundo componente são os sistemas institucionais que governam como a empresa funciona. Ambos os componentes devem ser levados em conta para colher plenamente os benefícios da Indústria 4.0. O bloco de Organização foi segmentado nos pilares de Prontidão de Talento, Estrutura e Gestão.


#### II.7.3 Os 8 Pilares

 Na Tabela 1, há uma breve descrição dos oito pilares, indicando como estão distribuídos pelos 3 blocos do MA-I4.0.

*Tabela 1. Os pilares distribuídos pelos 3 blocos do MA-I4.0*

| Bloco | Pilar | Descrição |
|---|---|---|
| Processo | 1. Operação | Planejamento e execução de Processos que levam à produção de bens e serviços |
| Processo | 2. Cadeia de Suprimentos | Planejamento e gestão de materiais brutos e inventário ao longo da cadeia de valor |
| Processo | 3. Ciclo de Vida de Produto | Sequência de estágios pelos quais um produto passa desde sua concepção até sua remoção do mercado |
| Tecnologia | 4. Automação | Aplicação de tecnologia para monitorar, controlar e executar a produção e entrega de produtos e serviços |
| Tecnologia | 5. Conectividade | Interconexão de equipamentos, máquinas e sistemas baseados em computador para permitir comunicação e troca de dados |
| Tecnologia | 6. Inteligência | Processamento e análise de dados para otimizar Processos existentes e criar novas aplicações, produtos e serviços |
| Organização | 7. Prontidão de Talentos | Capacidade da força de trabalho de conduzir e entregar iniciativas de Indústria 4.0 |
| Organização | 8. Estrutura & Gestão | Sistema de regras e políticas explícitas e implícitas que determinam como papéis e responsabilidades são atribuídos, controlados e coordenados |


#### II.7.4 As 16 Dimensões de Avaliação

    Na Tabela 2, são brevemente descritas as dimensões, bem como são indicadas as duas distribuições dentro dos pilares e blocos do MA-I4.0.

*Tabela 2. 16 dimensões do MA-I4.0.*

| # | Dimensão | Pilar | Bloco | Descrição Resumida |
|---|---|---|---|---|
| 1 | Integração Vertical | Operação | Processo | Integração de Processos e sistemas através de todos os níveis hierárquicos da pirâmide de automação |
| 2 | Integração Horizontal | Cadeia de Suprimentos | Processo | Integração de Processos empresariais através da organização e com stakeholders ao longo da cadeia de valor |
| 3 | Ciclo de Vida de Produto Integrado | Ciclo de Vida de Produto | Processo | Integração de pessoas, Processos e sistemas ao longo de todo o ciclo de vida do produto |
| 4 | Automação do Chão de Fábrica | Automação | Tecnologia | Aplicação de tecnologia para monitorar, controlar e executar Processos no chão de fábrica |
| 5 | Automação Corporativa | Automação | Tecnologia | Aplicação de tecnologia para monitorar, controlar e executar Processos administrativos |
| 6 | Automação de Instalações (Facility) | Automação | Tecnologia | Aplicação de tecnologia para monitorar, controlar e executar Processos de gestão de instalações |
| 7 | Conectividade de Chão de Fábrica | Conectividade | Tecnologia | Interconexão de equipamentos, máquinas e sistemas no chão de fábrica |
| 8 | Conectividade Corporativa | Conectividade | Tecnologia | Interconexão de sistemas de TI empresariais |
| 9 | Conectividade de Instalações (Facility) | Conectividade | Tecnologia | Interconexão de equipamentos e sistemas de gestão de instalações |
| 10 | Inteligência de Chão de Fábrica | Inteligência | Tecnologia | Processamento e análise de dados do chão de fábrica para otimização e tomada de decisão |
| 11 | Inteligência Corporativa | Inteligência | Tecnologia | Processamento e análise de dados empresariais para otimização e tomada de decisão |
| 12 | Inteligência de Instalações (Facility) | Inteligência | Tecnologia | Processamento e análise de dados de instalações para otimização e tomada de decisão |
| 13 | Desenvolvimento e Aprendizado de Força de Trabalho | Prontidão de Talentos | Organização | Programas e práticas para desenvolver competências da força de trabalho em I4.0 |
| 14 | Competência de Liderança | Prontidão de Talentos | Organização | Capacidade da liderança de conduzir a transformação I4.0 |
| 15 | Colaboração inter e intra-organização | Estrutura & Gestão | Organização | Estruturas e práticas que facilitam a colaboração interna e externa |
| 16 | Estratégia & Governança | Estrutura & Gestão | Organização | Estratégia formal e estrutura de governança para I4.0 |

### II.8 Método de Cálculo do Índice de Maturidade

#### II.8.1 Visão Geral do Método
O cálculo do índice de maturidade (idx4.0) é realizado através da média aritmética das dimensões.


#### II.8.2 Passo 1: Avaliar Cada Capacidade (0 a 6)

Neste passo, cada capacidade é avaliada por um conjunto de questões em que os itens de respostas são valorados em uma escala ordinal que varia de 0 a 6. Os valores do nível em cada uma das respostas são utilizados como valores para se obter uma média aritmética dessas respostas, resultando na Nota da Capacidade (NC).

A Escala de Níveis é indicada a seguir, bem como a taxonomia de conceitos que podem definir um determinado nível.

   •   Nível 0: Inexistente / Indefinido / Nenhum
   •   Nível 1: Inicial / Definido / Básico / Conectado / Computadorizado
   •   Nível 2: Gerenciado / Digital / Avançado / Interoperável / Visível
   •   Nível 3: Definido / Integrado / Interoperável e Seguro / Medido
   •   Nível 4: Diagnosticável / Automatizado / Flexível / Escalável
   •   Nível 5: Inteligente / Real-Time / Preditivo
   •   Nível 6: Otimizado / Adaptativo

Nota: A nomenclatura específica dos níveis varia conforme a dimensão. Consulte o APÊNDICE A para os critérios detalhados de cada nível para cada dimensão.


#### II.8.3 Passo 2: Calcular a Média de Cada Dimensão

Cada uma das 16 dimensões é avaliada individualmente por um conjunto de questões relacionadas. A Média da Dimensão (MD) é calculada como a média aritmética das notas dessas questões.

Fórmula:




                      Onde:
                         • MDj = Média da j-ésima dimensão
                         • Qi,j = Nota da i-ésima questão da j-ésima dimensão
                         • nj = Número de questões da dimensão j-ésima dimensão


<!-- pág. original: 439/465 -->
 Atenção: Todas as médias das dimensões devem ser calculadas obedecendo as regras de arredondamentos para duas (2) casas decimais.



#### II.8.4 Passo 4: Calcular o Índice MA-I4.0

 O Índice MA-I4.0 (idx4.0) é calculado como a média aritmética das médias das dimensões. Nesse caso, cada dimensão tem contribuição de 1/16 (6.25%) no índice final e os pesos atribuídos a cada bloco podem ser calculados, multiplicando o número de dimensões contidas em cada bloco por essa contribuição. Assim, os pesos de cada bloco na construção do índice final são apresentados na tabela a seguir:

*Tabela 3. Pesos atribuídos a cada bloco devido as suas dimensões.*

| Bloco | Peso | Justificativa |
|---|---|---|
| Processo | 18,75% (0,1875) | Processos bem desenhados são fundamentais para o sucesso |
| Tecnologia | 56,25% (0,5625) | Tecnologia é o principal habilitador da I4.0 |
| Organização | 25% (0,25) | Pessoas e estruturas são críticas para sustentabilidade |
| Total | 100% (1,00) | |


 Nota: Em avaliações ad-hoc, os pesos podem ser ajustados conforme o contexto específico da organização ou indústria, desde que a soma seja sempre 1,00 (100%). Entretanto, para efeitos de avaliações e benchmarkings oficiais, deve-se sempre adotar os pesos apresentados na Tabela 3.

 Fórmula:




                             Onde:

                                 •   MDj = Média da j-ésima Dimensão

 Atenção: O índice idx4.0 deve ser calculado obedecendo as regras de arredondamentos para duas (2) casas decimais.


<!-- pág. original: 440/465 -->
 Exemplo:

*Tabela 4. Exemplo de médias das dimensões.*

| # | Dimensão | Nota |
|---|---|---|
| 1 | Integração Vertical | 3,00 |
| 2 | Integração Horizontal | 2,00 |
| 3 | Ciclo de Vida de Produto Integrado | 3,00 |
| 4 | Automação do Chão de Fábrica | 3,00 |
| 5 | Automação Corporativa | 2,00 |
| 6 | Automação de Instalações (Facility) | 2,00 |
| 7 | Conectividade de Chão de Fábrica | 3,00 |
| 8 | Conectividade Corportativa | 3,00 |
| 9 | Conectividade de Instalações (Facility) | 3,00 |
| 10 | Inteligência de Chão de Fábrica | 3,00 |
| 11 | Inteligência Corporativa | 2,00 |
| 12 | Inteligência de Instalações (Facility) | 3,00 |
| 13 | Desenvolvimento e Aprendizado de Força de Trabalho | 2,00 |
| 14 | Competência de Liderança | 3,00 |
| 15 | Colaboração inter e intra-organização | 2,00 |
| 16 | Estratégia & Governança | 2,00 |

 Desta forma:

          idx4.0 = ( 3,00 + 2,00 + 3,00 + 3,00 + 2,00 + 2,00 + 3,00 + 3,00 + 3,00 + 3,00 + 2,00 + 3,00 + 2,00 + 3,00 + 2,00 + 2,00) /16 = 2,56

          idx4.0 = 2,56


#### II.8.5 Interpretação do Índice Final

 O índice idx4.0 final varia de 0,00 a 6,00 e deve ser interpretado conforme os níveis de maturidade descritos na Tabela 5, a seguir:




*Tabela 5. Relação entre as faixas do índice idx4.0 e o nível de maturidade.*

| Faixa do Índice (idx4.0) | Nível de Maturidade | Descrição |
|---|---|---|
| 0,00 - 1,00 | Nível 1: Incipiente | A organização está nos estágios iniciais da jornada I4.0. Processos são majoritariamente manuais ou ad-hoc, tecnologias digitais são limitadas, e não há estratégia formal de I4.0. |
| 1,01 - 2,00 | Nível 2: Em Desenvolvimento | A organização iniciou sua jornada I4.0. Alguns processos estão definidos e digitalizados, tecnologias básicas estão implementadas, e há consciência sobre I4.0 na liderança. |
| 2,01 - 3,00 | Nível 3: Padronizado | A organização tem processos bem definidos e sistemas digitais implementados. Há integração inicial entre sistemas, e a organização possui uma estratégia de I4.0 em desenvolvimento. |
| 3,01 - 4,00 | Nível 4: Integrado | A organização possui processos integrados e sistemas automatizados. Há conectividade entre sistemas e dados fluem através da organização. A estratégia de I4.0 está sendo executada ativamente. |
| 4,01 - 5,00 | Nível 5: Otimizado | A organização possui processos e sistemas altamente integrados e automatizados. Utiliza análise de dados avançada para otimização contínua. A cultura de I4.0 está estabelecida. |
| 5,01 - 6,00 | Nível 6: Adaptativo | A organização é líder em I4.0. Possui sistemas autônomos e adaptativos, utiliza, por exemplo, IA e machine learning extensivamente, e inova continuamente em produtos e Processos. |



 Interpretação Final: A organização está no Nível 3: Padronizado, com um índice idx4.0 de 2,56. Possui processos bem definidos e sistemas digitais implementados, com integração inicial entre sistemas.


#### II.8.7 Visualização dos Resultados

 Além dos cálculos usados para se chegar ao índice idx4.0, os resultados da avaliação devem ser apresentados através de múltiplas visualizações para facilitar sua compreensão. Dessa forma, as seções a seguir trazem algumas orientações.

##### II.8.7.1 Gráfico Radar

 Embora não sejam diretamente utilizados para o cálculo do índice idx4.0 de uma organização, a utilização de gráficos radar com as médias para os três blocos ou os 8 pilares permite visualizar rapidamente os pontos fortes e fracos da organização.

 Desse modo, em avaliações oficiais é requerido que o avaliador apresente a visualização desses resultados à organização avaliada.


<!-- pág. original: 442/465 -->
Exemplos:




                  Figura 2. Gráficos radar para os pilares do exemplo da Tabela 4.

Da ilustração acima, podemos concluir, por exemplo, que as principais deficiências da organização avaliada são nas dimensões “Cadeia de Suprimentos” e “Estrutura e Gestão”. Já em termos dos blocos sócio-técnicos, podemos dizer que o bloco “Organização” é o mais atrasado.




##### II.8.7.2 Gráfico de Barras por Dimensão

Por outro lado, mostrar as MDs das 16 dimensões, diretamente relacionadas ao índice idx4.0, em um gráfico de barras permite identificar rapidamente as dimensões mais e menos maduras.


<!-- pág. original: 443/465 -->
                   Figura 3. Gráfico radar para os blocos do exemplo da Tabela 4.


Em avaliações e benchmarkings oficiais, também é requerido que o avaliador apresente tal resultado.




                                  Figura 4. Gráfico das dimensões.


<!-- pág. original: 444/465 -->
#### II.8.8 Dados de Suporte Usados nos Gráficos

 Os dados utilizados na construção do gráficos também devem ser formatados e apresentados em tabelas, como nos exemplos a seguir, para conferência da organização avaliada. Considerando os dados da Tabela 4 e os gráficos das Figuras 2, 3 e 4, temos os exemplos das Tabelas 6 e 7.

*Tabela 6. Dados de Suporte a Gráficos: Médias dos Pilares*

| Pilar | Dimensões | Cálculo | Média |
|---|---|---|---|
| Operação | 1 | 3,00 / 1 | 3,00 |
| Cadeia de Suprimentos | 2 | 2,00 / 1 | 2,00 |
| Ciclo de Vida de Produto | 3 | 3,00 / 1 | 3,00 |
| Automação | 4, 5, 6 | (3,00+2,00+2,00) / 3 | 2,33 |
| Conectividade | 7, 8, 9 | (3,00+3,00+3,00) / 3 | 3,00 |
| Inteligência | 10, 11, 12 | (3,00+2,00+3,00) / 3 | 2,67 |
| Prontidão de Talentos | 13, 14 | (2,00+3,00) / 2 | 2,50 |
| Estrutura & Gestão | 15, 16 | (2,00+2,00) / 2 | 2,00 |

*Tabela 7. Dados de Suporte a Gráficos: Médias dos blocos*

| Bloco | Pilares | Cálculo | Média |
|---|---|---|---|
| Processo | Operação, Cadeia de Suprimentos, Ciclo de Vida de Produto | (3,00+2,00+3,00) / 3 | 2,67 |
| Tecnologia | Automação, Conectividade, Inteligência | (2,33+3,00+2,67) / 3 | 2,67 |
| Organização | Prontidão de Talentos, Estrutura & Gestão | (2,50+2,00) / 2 | 2,25 |



 Atenção: Todos os dados e cálculos efetuados e apresentados na visualização de resultados devem obedecer as regras de arredondamento com duas (2) casas decimais.




### APÊNDICE A - Detalhamento das 16 Dimensões

Este APÊNDICE apresenta as 16 dimensões do modelo de maturidade em Indústria 4.0, com sua definição, objetivo e níveis de maturidade. A escala utilizada vai de 0 a 6, onde o nível 0 é equivalente ao nível 0 do modelo SIRI (processos essencialmente analógicos/não digitalizados) e os níveis 1 a 6 resultam da combinação dos estágios do modelo acatech (Informatização, Conectividade, Visibilidade, Transparência, Capacidade preditiva e Adaptabilidade) com os conceitos de prontidão do SIRI.

#### Dimensão 1: Integração Vertical

**Definição:** Integração Vertical é uma das três características-chave de uma instalação digitalizada definida pela Indústria 4.0 segundo a acatech. Pode ser entendida como a integração de processos e sistemas através de todos os níveis hierárquicos da pirâmide de automação dentro de uma instalação para estabelecer um fluxo de dados conectado de ponta a ponta. Esta dimensão busca avaliar a extensão de conexões formais e vínculos entre e através de Processos e sistemas, e também leva em conta como os dados são trocados e analisados.

**Objetivo:** Em sua forma ideal, a dimensão Integração Vertical define um estado onde todos os sistemas OT (Tecnologia Operacional) e IT (Tecnologia da Informação) através dos níveis de produção e empresa são integrados em redes automatizadas, interoperáveis e flexíveis que permitirão troca de dados, análise e tomada de decisão sem emendas. Isso por sua vez permitirá melhor comunicação, flexibilidade e eficiência operacional, e também possibilitará respostas mais rápidas e concertadas a quaisquer mudanças na disponibilidade de recursos, demandas operacionais ou tipos de produtos.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Não há integração vertical estruturada; as atividades do chão de fábrica, supervisão e gestão operam de forma isolada, com decisões e trocas de informação majoritariamente manuais. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Processos de operação passam a ser suportados por CLPs, CNCs e sistemas computadorizados locais, mas os dados permanecem em ilhas, sem integração consistente com níveis superiores de gestão. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Começam a surgir conexões ponto a ponto entre máquinas, sistemas de supervisão e sistemas corporativos (por exemplo, ERP ou MES), de forma parcial e pouco padronizada. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Dados de diferentes níveis (máquina, célula, linha, planta, negócio) são integrados para gerar visibilidade sobre o desempenho dos processos, com indicadores consolidados ao longo da cadeia vertical. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | As relações de causa e efeito entre parâmetros de processo, paradas, qualidade e resultados de negócio tornam-se transparentes; a organização entende como decisões em um nível impactam os demais níveis da hierarquia. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos analíticos utilizam dados integrados verticalmente para prever gargalos, falhas, impactos de variações de mix de produtos, disponibilidade de recursos e seus efeitos em custos, prazos e qualidade. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | A programação da produção, alocação de ordens e ajuste de parâmetros de processo se adaptam dinamicamente ao longo dos níveis, com base em previsões e objetivos de negócio, reduzindo intervenções manuais. |

#### Dimensão 2: Integração Horizontal

**Definição:** Integração Horizontal, a segunda característica-chave da Indústria 4.0, refere-se à integração de processos empresariais através da organização e com outros stakeholders ao longo da cadeia de valor. Os processos empresariais incluem planejamento de demanda, aquisição, logística e serviços de pós-venda, enquanto os stakeholders incluem fornecedores, parceiros de negócios e clientes.

**Objetivo:** Assim como Integração Vertical, Integração Horizontal avalia a presença de canais formais que permitem o compartilhamento de informações, bem como como por meio dos quais os dados são trocados e analisados. À medida que processos e sistemas se tornam cada vez mais definidos e digitais, a dimensão Integração Horizontal descreve um estado final onde os processos internos de uma empresa convergem com aqueles de seus fornecedores e parceiros. Isso cria uma rede interoperável e transparente dentro da qual todos os stakeholders são capazes de coordenar e otimizar seus processos, tarefas e decisões através de toda a cadeia de valor.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Não há integração estruturada entre funções internas ou com parceiros externos; a cadeia de valor é coordenada de forma manual, com uso intensivo de e-mails, telefonemas e planilhas isoladas. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros mas puramente manuais. | Processos ao longo da cadeia de suprimentos são em grande parte digitais dentro de cada empresa, informações entre áreas internas, unidades e parceiros ainda circulam de forma pouco estruturada. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Surgem conexões entre sistemas de diferentes elos da cadeia (fornecedores, transportadores, clientes), por meio de EDI, portais ou integrações básicas, permitindo troca de dados sobre pedidos, entregas e estoques. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Dados integrados ao longo da cadeia produzem visibilidade sobre pedidos em aberto, níveis de estoque, status logístico e atendimento ao cliente, com painéis que cobrem múltiplas empresas ou unidades. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | A organização consegue entender, de forma transparente, como variações em demanda, lead times e desempenho logístico em um elo da cadeia afetam os demais, apoiando decisões colaborativas de replanejamento. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos preditivos são utilizados para antecipar demandas, riscos de ruptura, atrasos logísticos e impactos em níveis de serviço, alimentando planos conjuntos com fornecedores e clientes. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | A cadeia de valor torna-se adaptativa: planos de produção, reposição e distribuição são ajustados de forma colaborativa e quase automática entre os elos, com realocação dinâmica de volumes e capacidades. |

#### Dimensão 3: Ciclo de Vida de Produto Integrado

**Definição:** Ciclo de Vida de Produto Integrado integra pessoas, processos e sistemas ao longo de todo o ciclo de vida do produto, e também examina como os dados são coletados, gerenciados e analisados através dos diferentes estágios do ciclo de vida do produto. Estes estágios incluem design e desenvolvimento, engenharia, produção, uso pelo cliente, serviço e descarte.

**Objetivo:** Avanços em ferramentas digitais tornaram mais fácil do que nunca reunir dados, Processos, sistemas de negócios e pessoas para criar uma espinha dorsal de informações unificada que pode ser gerenciada digitalmente. A Indústria 4.0 também introduziu o conceito de "gêmeo digital" (digital twin), que é uma representação virtual dos ativos físicos, processos e sistemas envolvidos ao longo do ciclo de vida de um produto. Um gêmeo digital oferece dois benefícios-chave. Primeiro, as informações geradas em cada estágio podem ser compartilhadas perfeitamente, facilitando melhor tomada de decisão e permitindo que Processos sejam dinamicamente otimizados em outros estágios. Segundo, um gêmeo digital remove as limitações de trabalhar com protótipos físicos. Trabalhando com o gêmeo digital, múltiplos protótipos podem ser criados e testados virtualmente em velocidade, escala e a um custo muito menor.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Informações de projeto, produção, uso e serviço de produtos são dispersas, majoritariamente em documentos físicos ou arquivos locais, sem integração entre as fases do ciclo de vida. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Atividades de desenvolvimento, produção, serviço e descarte utilizam ferramentas digitais locais (CAD, planilhas, sistemas específicos), com baixa integração entre fases do ciclo de vida. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Existem conexões básicas entre sistemas de engenharia, produção, vendas e assistência técnica (por exemplo, troca de arquivos e integrações pontuais), permitindo algum reaproveitamento de dados. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Dados de produto são consolidados em estruturas de gestão do ciclo de vida (por exemplo, PLM ou repositórios integrados), garantindo visibilidade de versões, estruturas, alterações e histórico de uso/manutenção. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Torna-se transparente como decisões de projeto afetam custos de produção, manutenção, confiabilidade e descarte; análises de causa e efeito suportam melhorias de produto ao longo de seu ciclo de vida. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos preditivos utilizam dados de campo, simulações e histórico de falhas para antecipar problemas, orientar melhorias de projeto, definir campanhas de manutenção e otimizar o desempenho ao longo do ciclo de vida. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | Produtos e serviços são continuamente ajustados com base em dados de uso, feedback de clientes e previsões, permitindo atualizações de projeto, serviços remotos e modelos de negócio adaptativos (como servitização). |

#### Dimensão 4: Automação do Chão de Fábrica

**Definição:** Automação do Chão de Fábrica é a aplicação de tecnologia para monitorar, controlar e executar a produção e entrega de produtos e serviços, dentro do local onde a produção e gestão de bens é realizada.

**Objetivo:** Avaliar o grau de automação dos processos produtivos e de suporte no chão de fábrica, desde processos totalmente manuais até sistemas flexíveis e convergentes com automação empresarial e de instalações.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | As operações de chão de fábrica são predominantemente manuais ou suportadas por equipamentos convencionais, sem automação eletrônica relevante. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Máquinas e linhas possuem controles eletrônicos e sistemas computadorizados locais (CLPs, CNCs), substituindo controles manuais, porém a automação é isolada. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Surgem células e linhas com automação integrada, conectando máquinas, sensores e atuadores em sistemas de controle coordenados, ainda com pouca integração com outros sistemas. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | A automação de chão de fábrica é monitorada em sistemas SCADA/MES, que fornecem visibilidade dos estados de máquinas, alarmes, produção e paradas em tempo quase real. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | A organização compreende como configurações de automação, lógicas de controle e sequências de operação influenciam desempenho, qualidade e consumo de recursos, permitindo ajustes mais precisos. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos analíticos e simulações apoiam a otimização da automação (por exemplo, sequenciamento, lógica de intertravamento, tempos de ciclo), antecipando gargalos e efeitos de mudanças na operação. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | Sistemas de automação tornam-se adaptativos, ajustando automaticamente parâmetros, lógicas e sequências de operação em função de variações de demanda, mix de produtos e condições de processo. |

#### Dimensão 5: Automação Corporativa

**Definição:** Automação Corporativa é a aplicação de tecnologia para monitorar, controlar e executar processos, dentro do local onde o trabalho administrativo é realizado. Esses processos incluem, mas não estão limitados a, vendas e marketing, planejamento de demanda, aquisição e gestão e planejamento de recursos humanos.

**Objetivo:** Avaliar o grau de automação dos Processos administrativos e de gestão empresarial.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Processos administrativos e de gestão são majoritariamente manuais ou baseados em documentos físicos, com uso limitado de sistemas informatizados. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Processos administrativos e de gestão utilizam sistemas computadorizados básicos (ERP, sistemas financeiros, de RH), substituindo registros em papel, mas com grande uso de planilhas paralelas. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Integrações entre sistemas corporativos (ERP, CRM, SCM, RH) passam a ser estabelecidas, permitindo troca de dados entre áreas e redução de retrabalho na alimentação de informações. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Fluxos corporativos (compras, vendas, financeiro, RH, planejamento) são suportados por workflows e painéis que dão visibilidade ao andamento de processos, prazos e responsabilidades. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Torna-se transparente como processos administrativos e de gestão impactam custos, níveis de serviço, prazos e desempenho operacional, permitindo revisão de políticas e regras de negócio. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos analíticos são utilizados para prever demandas internas, carga de trabalho, riscos financeiros e impactos de decisões administrativas, apoiando o planejamento de recursos e políticas. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | A automação corporativa suporta processos adaptativos, ajustando automaticamente fluxos, alçadas, prioridades e alocação de recursos administrativos em função de eventos e previsões de negócio. |

#### Dimensão 6: Automação de Instalações
**Definição:** Automação de Instalações (Facility) é a aplicação de tecnologia para monitorar, controlar e executar Processos dentro do edifício físico e/ou instalações onde a área de produção está localizada. Esses Processos incluem, mas não estão limitados à gestão de HVAC (aquecimento, ventilação e ar condicionado), resfriamento, segurança e sistemas de iluminação.

**Objetivo:** Avaliar o grau de automação dos sistemas prediais e de infraestrutura.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico uso ou modelo | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há relevante de soluções digitais forma sistemas de suporte, correspondendo ao nível 0 do SIRI. | Sistemas de instalações (energia, HVAC, ar comprimido, segurança, iluminação) são operados predominantemente de manual ou por dispositivos simples não integrados. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Sistemas de instalações utilizam controladores locais e dispositivos eletrônicos básicos, substituindo controles puramente manuais, mas com pouca coordenação entre subsistemas. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Controle de instalações passa a ser centralizado em sistemas BMS ou supervisórios simples, conectando diferentes subsistemas em um mesmo ambiente de operação. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Operadores têm visibilidade em tempo quase real do status de equipamentos, consumos de energia e alarmes de infraestrutura, com painéis que consolidam informações por área ou planta. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | As relações entre condições de operação das instalações, consumo de recursos, conforto e impacto na produção tornam-se transparentes, permitindo ajustes de políticas e parâmetros. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos preditivos são usados para antecipar falhas em equipamentos de utilidades, identificar oportunidades de economia de energia e apoiar decisões de investimento em infraestrutura. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | Sistemas de instalações ajustam automaticamente setpoints, modos de operação e prioridades com base em previsões de demanda, clima, produção e tarifação, otimizando custo, conforto e disponibilidade. |

#### Dimensão 7: Conectividade de Chão de Fábrica

**Definição:** Conectividade de Chão de Fábrica é o grau em que máquinas, dispositivos de automação, sensores, atuadores e sistemas de controle em nível de operação estão conectados entre si e com os sistemas de níveis superiores ao longo da pirâmide de automação. Essa dimensão observa não apenas a existência de redes industriais, mas também a padronização de protocolos, a capacidade de troca bidirecional de dados entre equipamentos de diferentes fabricantes e a qualidade desse fluxo de dados.

**Objetivo:** Avaliar em que medida o chão de fábrica dispõe de uma infraestrutura de comunicação confiável, interoperável, segura, em tempo quase real e escalável, capaz de suportar monitoramento contínuo, controle avançado de processos, análise de dados e, nos níveis superiores, funcionalidades inteligentes e autônomas típicas da Indústria 4.0.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Não há conectividade estruturada entre dispositivos de chão de fábrica; dados permanecem em equipamentos ou registros manuais. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Máquinas, sensores e atuadores utilizam recursos digitais, mas com conectividade limitada ou inexistente a outros sistemas. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Dispositivos de chão de fábrica são conectados em redes industriais ou IIoT, permitindo troca básica de dados entre máquinas, células e sistemas de supervisão. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | A conectividade fornece visibilidade consolidada do status de equipamentos, produção e condições de processo, com monitoramento em tempo quase real a partir de diferentes pontos da fábrica. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Relações entre falhas de comunicação, qualidade de rede e desempenho do processo tornam-se transparentes; a organização entende o impacto da conectividade nas operações. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos e ferramentas monitoram continuamente a rede de chão de fábrica, antecipando congestionamentos, pontos de falha e riscos à disponibilidade da comunicação. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | Arquitetura de conectividade de chão de fábrica adapta-se dinamicamente à carga e às necessidades de processo, priorizando tráfego crítico, redirecionando fluxos e reconfigurando segmentos de rede. |

#### Dimensão 8: Conectividade Corporativa

**Definição:** Conectividade Corporativa é o grau em que sistemas de gestão e de apoio ao negócio (ERP, CRM, sistemas financeiros, de RH, de planejamento e de cadeia de suprimentos) estão integrados entre si e com outros sistemas internos e externos à organização, por meio de padrões de integração e fluxos de dados consistentes.

**Objetivo:** Avaliar em que medida a organização dispõe de um tecido informacional integrado que suporta processos ponta a ponta, colaboração interfuncional e visão unificada de informações-chave, permitindo decisões táticas e estratégicas mais rápidas e fundamentadas.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Sistemas corporativos operam isolados, com pouca ou nenhuma troca eletrônica de dados entre áreas; integrações são feitas manualmente. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Principais sistemas corporativos (ERP, CRM, financeiro, RH) são informatizados, porém com muitas ilhas de informação e baixa comunicação entre áreas. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Integrações entre sistemas corporativos passam a ser estabelecidas por meio de APIs, serviços ou troca estruturada de arquivos, permitindo fluxo básico de dados entre áreas. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | A conectividade corporativa gera visibilidade integrada de pedidos, estoques, resultados financeiros, indicadores de clientes e outros dados de negócio, apoiando o acompanhamento em tempo quase real. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Os impactos de integrações corporativas sobre desempenho, riscos e conformidade tornam-se transparentes, permitindo gestão estruturada da arquitetura de sistemas e das interfaces. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos e ferramentas monitoram integrações e fluxos de dados corporativos, prevendo gargalos, falhas de integração e riscos de inconsistência de dados. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | A arquitetura de conectividade corporativa adapta-se com rapidez à inclusão de novos sistemas, unidades e parceiros, reconfigurando integrações e roteando dados de forma dinâmica conforme as necessidades do negócio. |

#### Dimensão 9: Conectividade de Instalações

**Definição:** Conectividade de Instalações (Facility) é o grau em que sistemas de infraestrutura física da planta (energia, água, ar comprimido, HVAC, refrigeração, iluminação, segurança, monitoramento ambiental e outros sistemas prediais) estão conectados entre si e com os sistemas de produção e corporativos.

**Objetivo:** Avaliar em que medida a organização consegue monitorar, controlar e otimizar sua infraestrutura física por meio de redes integradas, suportando eficiência energética, confiabilidade operacional, conforto ocupacional e metas de sustentabilidade.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Sistemas de instalações operam de forma isolada, sem rede estruturada ou comunicação entre equipamentos e sistemas prediais. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Sistemas de instalações utilizam equipamentos informatizados localmente (controladores eletrônicos, medidores digitais), porém com baixa integração entre subsistemas. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Sistemas de instalações (energia, HVAC, segurança etc.) passam a ser conectados em redes prediais, permitindo troca básica de dados entre controladores e um ponto central. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | A conectividade de instalações oferece visibilidade consolidada de consumos, alarmes e estados de equipamentos, com monitoramento em tempo quase real. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Torna-se transparente como falhas de conectividade, qualidade da rede e configurações de comunicação impactam segurança, conforto e eficiência energética. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Ferramentas monitoram a rede de instalações e utilizam modelos para prever degradação, sobrecargas e riscos de indisponibilidade de comunicação entre sistemas prediais. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | A conectividade de instalações adapta-se automaticamente a mudanças de carga, topologia e condições externas, mantendo desempenho e disponibilidade por meio de reconfiguração dinâmica da rede. |

#### Dimensão 10: Inteligência de Chão de Fábrica
**Definição:** Inteligência de Chão de Fábrica é a capacidade de transformar dados gerados no ambiente produtivo (sensores, máquinas, sistemas MES/SCADA, registros de qualidade, manutenção, logística interna) em informação, conhecimento e ações concretas de melhoria, por meio de visualização, análise e modelos avançados.

**Objetivo:** Avaliar até que ponto o chão de fábrica evoluiu de um ambiente meramente automatizado para um ambiente orientado a dados, com uso consistente de analytics e, gradualmente, de inteligência artificial para otimização contínua de processos, confiabilidade, qualidade e produtividade.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Decisões operacionais no chão de fábrica são tomadas com base em observações informais e experiência, sem uso sistemático de dados registrados. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Dados de produção passam a ser registrados digitalmente em sistemas locais ou planilhas, reduzindo a dependência de registros em papel. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Dados de diferentes máquinas e processos são conectados em bases ou sistemas comuns, permitindo análises simples sobre volumes produzidos, paradas e rejeitos. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Indicadores e painéis de desempenho fornecem visibilidade em tempo quase real sobre OEE, produtividade, qualidade e outras métricas de chão de fábrica. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Análises permitem compreender causas de paradas, perdas de eficiência e problemas de qualidade, tornando claras as relações entre parâmetros de processo e resultados. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos preditivos identificam com antecedência riscos de falha, deriva de processo, desvios de qualidade e gargalos de capacidade, apoiando decisões de manutenção e ajustes de operação. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | Algoritmos ajustam automaticamente parâmetros de processo, sequenciamento de ordens e estratégias de operação com base em previsões, metas e restrições, tornando o chão de fábrica adaptativo. |

#### Dimensão 11: Inteligência Corporativa

**Definição:** Inteligência Corporativa é a capacidade de coletar, integrar, analisar e disseminar dados de negócio provenientes de diversas fontes (vendas, finanças, cadeia de suprimentos, marketing, risco, RH, atendimento ao cliente) para sustentar decisões táticas e estratégicas.


<!-- pág. original: 458/465 -->
**Objetivo:** Avaliar o grau em que a organização atua como empresa orientada a dados, utilizando informações confiáveis, tempestivas e analiticamente tratadas para otimizar processos, reduzir riscos, identificar oportunidades e suportar a execução da estratégia.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Decisões de negócio são predominantemente qualitativas, com pouco uso de dados estruturados e sem sistemas analíticos relevantes. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Dados de negócio (vendas, finanças, RH, logística) são registrados em sistemas informatizados básicos, reduzindo o uso de planilhas e registros manuais isolados. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Bases de dados corporativas passam a ser conectadas e consolidadas em repositórios comuns (por exemplo, data marts ou data warehouse), permitindo consultas mais abrangentes. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Painéis de BI e relatórios gerenciais oferecem visibilidade integrada de indicadores financeiros, comerciais, operacionais e de pessoas para diferentes níveis de gestão. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Análises multidimensionais e estudos de causa e efeito permitem compreender o impacto de decisões de negócio em resultados e riscos, aumentando a transparência da gestão. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos preditivos são utilizados para previsão de demanda, receita, churn de clientes, riscos financeiros e operacionais, apoiando o planejamento e a definição de estratégias. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | Sistemas corporativos recomendam ou executam automaticamente ações (por exemplo, ajustes de preços, campanhas, alocação de recursos) com base em previsões e objetivos, tornando a organização mais adaptativa. |

#### Dimensão 12: Inteligência de Instalações (Facility)
**Definição:** Inteligência de Instalações (Facility) é a capacidade de utilizar dados gerados pelos sistemas prediais e de utilidades para compreender, prever e otimizar o desempenho da infraestrutura física da planta.

**Objetivo:** Avaliar em que grau a infraestrutura física da organização é gerida com base em dados e analytics, permitindo redução de custos, aumento de disponibilidade, melhoria do ambiente de trabalho e suporte a metas de sustentabilidade e certificações ambientais.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Uso de dados para gestão de instalações é praticamente inexistente; decisões são reativas, baseadas em quebras e reclamações. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Medições de consumo de energia, água, ar comprimido e outros recursos passam a ser registradas digitalmente, ainda de forma simples e pouco integrada. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Dados de instalações de diferentes subsistemas são conectados em uma base ou sistema comum, permitindo análises consolidadas por área, turno ou equipamento. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Painéis de monitoramento oferecem visibilidade de consumos, demandas de pico, alarmes e disponibilidade de equipamentos de infraestrutura em tempo quase real. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Análises permitem compreender causas de desperdícios, vazamentos, falhas recorrentes e ineficiências energéticas, tornando transparentes os impactos das instalações no desempenho global. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos preditivos antecipam falhas em equipamentos críticos de instalações e apontam oportunidades de economia, considerando padrões de uso, clima e produção. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | Sistemas de gerenciamento de instalações adotam estratégias adaptativas, ajustando automaticamente setpoints, horários de operação e modos de controle com base em previsões de demanda e condições externas. |

#### Dimensão 13: Desenvolvimento e Aprendizado de Força de Trabalho

**Definição:** Desenvolvimento e Aprendizado de Força de Trabalho é a forma como a organização planeja, estrutura e implementa estratégias para desenvolver as competências necessárias à Indústria 4.0, abrangendo aspectos técnicos, de processo e comportamentais.

**Objetivo:** Verificar o alinhamento entre a estratégia de desenvolvimento de pessoas e a jornada de transformação digital, desde iniciativas pontuais até programas contínuos, estruturados e integrados à gestão de desempenho, carreiras e sucessão.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Não há ações estruturadas de desenvolvimento relacionadas à Indústria 4.0; aprendizagem ocorre de modo informal e não sistematizado. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Iniciativas de desenvolvimento ligadas à Indústria 4.0 são pontuais, focadas em treinamentos básicos sobre tecnologias e conceitos, com registros informatizados simples. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Programas de treinamento passam a ser estruturados em trilhas por função, com registro centralizado de cursos, competências e planos de desenvolvimento. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | A organização tem visibilidade das competências existentes e das lacunas relacionadas à Indústria 4.0, utilizando painéis e relatórios para acompanhar evolução de capacitações. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Torna-se transparente como lacunas de competências impactam projetos e resultados; informações sobre habilidades são usadas para planejar ações de desenvolvimento alinhadas à estratégia. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos e análises são usados para prever necessidades de competências futuras, riscos de obsolescência e impactos de mudanças tecnológicas na força de trabalho. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | O sistema de desenvolvimento é adaptativo, ajustando continuamente trilhas, conteúdos e formatos de aprendizagem com base em dados de desempenho, engajamento e evolução do negócio. |

#### Dimensão 14: Competência de Liderança

**Definição:** Competência de Liderança é o grau em que os líderes da organização compreendem a relevância da Indústria 4.0, possuem competências para atuar nesse contexto e exercem o papel de patrocinadores e condutores da transformação digital.

**Objetivo:** Verificar se a liderança atua apenas como observadora ou se se torna agente central da transformação, passando de consciência básica para uma atuação estruturante e visionária, coerente com os níveis mais altos de maturidade 4.0.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Lideranças não consideram de forma estruturada a Indústria 4.0; decisões e prioridades não refletem uma visão de transformação digital. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Lideranças começam a ter acesso e registro digitalizado de informações e iniciativas de Indústria 4.0, construindo entendimento inicial sobre o tema. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Líderes participam de fóruns estruturados, programas de capacitação e comunidades internas sobre transformação digital, reforçando conexões entre áreas. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Há visibilidade clara sobre o patrocínio, envolvimento e atuação das lideranças em iniciativas de Indústria 4.0, com indicadores de engajamento e suporte. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Fica transparente o impacto das decisões de liderança sobre o avanço da maturidade 4.0; práticas exemplares e lacunas são identificadas e tratadas. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Ferramentas e modelos ajudam a antecipar riscos de liderança (por exemplo, resistência, falta de patrocínio) e necessidades de desenvolvimento para sustentar a transformação. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | O estilo e as práticas de liderança evoluem de forma adaptativa, ajustando-se às exigências da transformação digital, promovendo continuamente inovação, aprendizado e colaboração. |

#### Dimensão 15: Colaboração inter e intra-organização

**Definição:** Colaboração inter e intra-organização é o grau em que áreas internas, unidades de negócio, plantas e parceiros externos trabalham de forma integrada na concepção, implementação e operação de soluções de Indústria 4.0.

**Objetivo:** Medir a evolução desde um ambiente fragmentado, de silos funcionais, até um ecossistema colaborativo em que inovação e melhoria contínua são construídas de forma conjunta, integrando fornecedores, clientes, instituições de pesquisa e outros atores relevantes.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | A colaboração entre áreas internas e com parceiros externos é mínima, ocorrendo apenas de forma informal e não registrada. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Práticas de colaboração são registradas de forma básica (reuniões, grupos de trabalho), com uso limitado de ferramentas digitais para suporte a equipes e projetos 4.0. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Ferramentas colaborativas passam a conectar áreas, plantas e alguns parceiros externos, permitindo trocas estruturadas de informações sobre projetos e operações. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Há visibilidade das redes de colaboração internas e externas, com painéis que mostram projetos conjuntos, participação das áreas e resultados alcançados. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Torna-se transparente como a colaboração (ou a falta dela) impacta prazos, custos, inovação e qualidade; gargalos e boas práticas são identificados de forma sistemática. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Análises são utilizadas para prever riscos de falhas na colaboração (por exemplo, silos, dependência de indivíduos-chave) e para planejar ações de fortalecimento de redes e parcerias. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | Arranjos colaborativos adaptam-se dinamicamente, reorganizando equipes, parcerias e fluxos de informação em função de desafios e oportunidades da transformação 4.0. |

#### Dimensão 16: Estratégia & Governança

**Definição:** Estratégia & Governança é o grau em que a organização possui uma estratégia explícita para Indústria 4.0, alinhada à estratégia de negócio e suportada por estrutura de governança clara, com papéis, responsabilidades e mecanismos de priorização e acompanhamento.

**Objetivo:** Verificar se a transformação digital está desconectada do planejamento estratégico ou se é tratada como vetor central de competitividade, respaldada por mecanismos de governança consistentes com o nível de ambição da organização, permitindo ajustes ágeis de rumo e alocação eficiente de recursos.


| Nível | Estágio | Definição do estágio | Descrição na dimensão |
|---|---|---|---|
| 0 | Inexistente / Analógico | Processos nesta dimensão são predominantemente manuais ou baseados em tecnologias convencionais não digitais. Não há uso relevante de soluções digitais ou sistemas de suporte, correspondendo ao nível 0 do modelo SIRI. | Não há estratégia ou governança específica para Indústria 4.0; iniciativas digitais são isoladas e desconectadas do planejamento formal. |
| 1 | Informatização | Processos e recursos passam a utilizar soluções digitais e sistemas computadorizados localmente, substituindo controles e registros puramente manuais. | Elementos de estratégia e governança para Indústria 4.0 começam a ser documentados de forma digital, com diretrizes iniciais e alguns projetos mapeados. |
| 2 | Conectividade | Sistemas, máquinas, produtos e pessoas tornam-se conectados em rede, permitindo a troca estruturada de dados entre diferentes pontos do processo e da organização. | Estratégia e governança são conectadas a planos, portfólios de projetos e estruturas de responsabilidade, permitindo coordenação básica das iniciativas 4.0. |
| 3 | Visibilidade | Dados integrados fornecem uma visão em tempo quase real do estado dos processos, produtos e recursos, por meio de indicadores e painéis consolidados. | Há visibilidade consolidada do portfólio de projetos, dos investimentos, dos resultados e dos riscos associados à jornada de maturidade 4.0. |
| 4 | Transparência | Relações de causa e efeito são compreendidas e modeladas; os dados permitem explicar por que determinados eventos ocorrem e simular alternativas de decisão. | Fica transparente como decisões estratégicas e de governança impactam diretamente a evolução da maturidade 4.0, permitindo correções de rumo baseadas em evidências. |
| 5 | Capacidade preditiva | Modelos analíticos e algoritmos são utilizados para prever estados futuros, eventos e riscos relevantes, antecipando problemas e oportunidades. | Modelos são utilizados para simular cenários de investimento, risco e retorno relacionados à transformação digital, apoiando decisões de priorização e alocação de recursos. |
| 6 | Adaptabilidade | Sistemas e processos ajustam-se de forma autônoma com base em previsões, objetivos e regras, tornando a organização mais ágil e resiliente. | Estratégia e governança tornam-se adaptativas, ajustando continuamente metas, portfólio e mecanismos de decisão em função de mudanças tecnológicas, de mercado e regulatórias. |

### APÊNDICE B - Modelo de Relatório de Avaliação
(Este APÊNDICE conteria um template completo de relatório)




### APÊNDICE C - Planilha de Cálculo do Índice idx4.0
(Este APÊNDICE conteria o link para o download de uma planilha em formato .xlsx para cálculo
automatizado)



## Bibliografia

As referências bibliográficas que embasam o modelo de maturidade e as capacidades avaliadas neste DOQ, anteriormente repetidas ao final de cada capacidade no Anexo I, foram consolidadas nesta seção única, em ordem alfabética, conforme o padrão ABNT NBR 6023.

- ACATECH. *Industrie 4.0 Maturity Index: Managing the Digital Transformation of Companies – Update 2020*. Munique: acatech – National Academy of Science and Engineering. Disponível em: https://en.acatech.de/publication/industrie-4-0-maturity-index-update-2020/download-pdf. Acesso em: 3 out. 2025.
- ALAGIRI GOVINDASAMY; ARIVARASI ARULARASAN. *Readiness and Maturity Assessment Model to Measure the Industry 4.0 Ecosystem*. Lecture Notes in Electrical Engineering, p. 57–67, 1 jan. 2021.
- ALAVI, M.; LEIDNER, D. E. Review: *Knowledge management and knowledge management systems: Conceptual foundations and research issues*. MIS Quarterly, v. 25, n. 1, p. 107–136, 2001.
- ALBU, O. B.; FLYVERBOM, M. *Organizational transparency: Conceptualizations, conditions, and consequences*. Business & Society, v. 58, n. 2, p. 268–297, 2019.
- ALNUAIMI, B. K. et al. *Mastering digital transformation: The nexus between leadership, agility, and digital strategy*. Journal of Business Research, v. 145, p. 636–648, 2022.
- ARGOTE, L.; MIRON-SPEKTOR, E. *Organizational learning: From experience to knowledge*. Organization Science, v. 22, n. 5, p. 1123–1137, 2011.
- AUTIO, E. et al. *Digital affordances, spatial affordances, and the genesis of entrepreneurial ecosystems*. Strategic Entrepreneurship Journal, v. 12, n. 1, p. 72–95, 2018.
- BDO. *The Importance of Trust in Digital Transformation*. BDO Insights, dez. 2023. Disponível em: https://www.bdo.com/insights/assurance/it-s-always-been-a-matter-of-trust. Acesso em: 10 nov. 2025.
- BENNETT, N.; LEMOINE, G. J. *What a difference a word makes: Understanding threats to performance in a VUCA world*. Business Horizons, v. 57, n. 3, p. 311–317, 2014.
- BERNSTEIN, E. S. *The transparency trap*. Harvard Business Review, v. 92, n. 10, p. 58–66, 2014.
- BONINI, A. et al. *The relationship between leadership and adaptive performance: A systematic review and meta-analysis*. PLOS ONE, v. 19, p. 1–29, out. 2024.
- BROWNELL, J. *Listening: Attitudes, principles, and skills*. Nova York: Routledge, 2015.
- BUCKINGHAM, M.; GOODALL, A. *Reinventing performance management*. Harvard Business Review, v. 93, n. 4, p. 40–50, 2015.
- BUER, S.-V.; STRANDHAGEN, J. O.; CHAN, F. T. S. *The link between Industry 4.0 and lean manufacturing: mapping current research and establishing a research agenda*. International Journal of Production Research, v. 56, n. 8, p. 2924–2940, 2018.
- CAPPELLI, P.; TAVIS, A. *The performance management revolution*. Harvard Business Review, v. 94, n. 10, p. 58–67, 2016.
- COOMBS, W. T. *Ongoing crisis communication: Planning, managing, and responding*. 5. ed. Thousand Oaks: Sage Publications, 2019.
- CROSS, R.; PARKER, A. *The hidden power of social networks: Understanding how work really gets done in organizations*. Boston: Harvard Business Press, 2004.
- CYBERSIERRA. *NIST CSF Maturity Levels Explained (Model, Stages, Importance)*. CyberSierra Blog, out. 2024. Disponível em: https://cybersierra.co/blog/nist-csf-maturity-levels-everything-you-need-to-know/. Acesso em: 10 nov. 2025.
- DAVENPORT, T. H. *Competing on Analytics: The New Science of Winning*. Boston: Harvard Business School Press, 2007.
- DECI, E. L.; RYAN, R. M. *Self-determination theory: A macrotheory of human motivation, development, and health*. Canadian Psychology, v. 49, n. 3, p. 182–185, 2008.
- DECUYPERE, A.; SCHAUFELI, W. *Exploring the Leadership–Engagement Nexus: A Moderated Meta-Analysis and Review of Explaining Mechanisms*. International Journal of Environmental Research and Public Health, v. 18, n. 16, p. 8592, 2021.
- DELOITTE. *Organizational Trust: The foundation of meaningful relationships*. Deloitte Insights, 2025. Disponível em: https://www.deloitte.com/us/en/insights/topics/trust.html. Acesso em: 10 nov. 2025.
- DOERR, J. *Measure What Matters: How Google, Bono, and the Gates Foundation Rock the World with OKRs*. Nova York: Portfolio/Penguin, 2018.
- DORAN, G. T. *There's a S.M.A.R.T. way to write management's goals and objectives*. Management Review, v. 70, n. 11, p. 35–36, 1981.
- DREMEL, C. et al. *How AUDI AG established big data analytics in its digital transformation*. MIS Quarterly Executive, v. 16, n. 2, p. 81–100, 2017.
- DUHIGG, C. *What Google learned from its quest to build the perfect team*. The New York Times Magazine, v. 26, n. 2016, p. 20, 2016.
- DWECK, C. S. *Mindset: The New Psychology of Success*. Nova York: Random House, 2006.
- EDB. *The Smart Industry Readiness Index: Catalysing the transformation of manufacturing*. Singapura: Economic Development Board. Disponível em: https://www.edb.gov.sg/content/dam/edb-en/about-edb/media-releases/news/the-smart-industry-readiness-index/the-sg-smart-industry-readiness-index-whitepaper%20(1).pdf. Acesso em: 3 out. 2025.
- EDMONDSON, A. C. *Psychological safety and learning behavior in work teams*. Administrative Science Quarterly, v. 44, n. 2, p. 350–383, 1999.
- EDMONDSON, A. C. *The fearless organization: Creating psychological safety in the workplace for learning, innovation, and growth*. Hoboken: Wiley, 2018.
- ELVING, W. J. *The role of communication in organisational change*. Corporate Communications: An International Journal, v. 10, n. 2, p. 129–138, 2005.
- FLEURY, A. et al. *Digital Maturity Capability and Internationalization of Brazilian Multinationals*. International Business Review, v. 33, 2024.
- FLEURY, A. et al. *Digital maturity, multinationality, and value chain and ecosystem integration*. International Business Review, v. 33, 2024.
- FLEURY, A. et al. *Going digital in emerging market multinational enterprises: A focus on resources, organizational capabilities and digital maturity*. International Business Review, v. 33, 2024.
- FRAZIER, M. L. et al. *Psychological safety: A meta-analytic review and extension*. Personnel Psychology, v. 70, n. 1, p. 113–165, 2017.
- GARTENBERG, C.; PRAT, A.; SERAFEIM, G. *Corporate purpose and financial performance*. Organization Science, v. 30, n. 1, p. 1–18, 2019.
- GIACOSA, E.; CULASSO, F.; CROCCO, E. *Customer agility in the modern automotive sector: How lead management shapes agile digital companies*. Technological Forecasting and Social Change, v. 175, 2022.
- GUINAN, P. J.; PARISE, S.; LANGOWITZ, N. *Creating an innovative digital project team: Levers to enable digital transformation*. Business Horizons, v. 62, n. 6, p. 717–727, 2019.
- HULT, G. T. M. et al. *The theoretical evolution and use of the Uppsala Model of internationalization in the international business ecosystem*. Journal of International Business Studies, v. 51, p. 38–49, 2020.
- INCIT. *The Global Smart Industry Readiness Index Initiative: Manufacturing Transformation Insights Report 2025*. Singapura: INCIT. Disponível em: https://assets.incit.org/large-documents/manual/The_global_smart_industry_readiness_index_initiative_2025-manual.pdf. Acesso em: 3 out. 2025.
- INFOSEC. *Understanding maturity models in cybersecurity: definition and types*. Infosec Resources, 2024. Disponível em: https://www.infosecinstitute.com/resources/cmmc/understanding-maturity-models-in-cybersecurity-definition-and-types/. Acesso em: 10 nov. 2025.
- ISO/IEC. *ISO/IEC 20000:2018 – IT Service Management*. Genebra: International Organization for Standardization, 2018.
- ISO/IEC. *ISO/IEC 27001:2022 – Information security management systems*. Genebra: International Organization for Standardization, 2022.
- ITIL. *ITIL 4: Service Design and Service Operation*. Reading: AXELOS, 2019.
- JACOBIDES, M. G.; CENNAMO, C.; GAWER, A. *Towards a theory of ecosystems*. Strategic Management Journal, v. 39, n. 8, p. 2255–2276, 2018.
- JIANG, H.; LUO, Y. *Crafting employee trust: From authentic leadership to transparent organizational communication*. Corporate Communications: An International Journal, v. 23, n. 2, p. 138–160, 2018.
- JIANG, H.; MEN, L. R. *Creating an engaged workforce: The impact of authentic leadership, transparent organizational communication, and work-life enrichment*. Communication Research, v. 44, n. 2, p. 225–243, 2017.
- KACHE, F.; SEURING, S. *Challenges and opportunities of digital information at the intersection of Big Data Analytics and supply chain management*. International Journal of Operations & Production Management, v. 37, n. 1, p. 10–36, 2017.
- KAPLAN, R. S.; NORTON, D. P. *The Balanced Scorecard: Translating Strategy into Action*. Boston: Harvard Business School Press, 1996.
- KARIMI, J.; WALTER, Z. *The role of dynamic capabilities in responding to digital disruption: A factor-based study of the newspaper industry*. Journal of Management Information Systems, v. 32, n. 1, p. 39–81, 2015.
- KASAPOĞLU, C. et al. *Industry 4.0 maturity assessment in manufacturing enterprises: a mixed-methods approach for SMEs*. Central European Management Journal, abr. 2025.
- KEEPNET. *Security Culture Maturity Model (SCMM): Benchmark & Strengthen Security Culture*. Keepnet Blog, mar. 2025. Disponível em: https://keepnetlabs.com/blog/what-is-the-security-culture-maturity-model. Acesso em: 10 nov. 2025.
- KEITH, N.; FRESE, M. *Enhancing firm performance and innovativeness through error management culture*. In: Handbook of Organizational Culture and Climate, p. 137–157, 2011.
- KHASSAWNEH, O.; ELREHAIL, H. *The Effect of Participative Leadership Style on Employees' Performance: The Contingent Role of Institutional Theory*. Administrative Sciences, v. 12, n. 4, p. 195, 15 dez. 2022.
- KNASTER, R.; LEFFINGWELL, D. *SAFe 5.0 Distilled: Achieving Business Agility with the Scaled Agile Framework*. Boston: Addison-Wesley, 2020.
- LAURSEN, K.; SALTER, A. *Open for innovation: The role of openness in explaining innovation performance among UK manufacturing firms*. Strategic Management Journal, v. 27, n. 2, p. 131–150, 2006.
- LEONARD-BARTON, D. *Core capabilities and core rigidities: A paradox in managing new product development*. Strategic Management Journal, v. 13, n. S1, p. 111–125, 1992.
- LEONARDI, P. M.; HUYSMAN, M.; STEINFIELD, C. *Enterprise social media: Definition, history, and prospects for the study of social technologies in organizations*. Journal of Computer-Mediated Communication, v. 19, n. 1, p. 1–19, 2013.
- LI, J. et al. *Ecosystem-specific advantages in international digital commerce*. Journal of International Business Studies, v. 50, p. 1448–1463, 2019.
- LICHTBLAU, K. et al. *Industrie 4.0 Readiness*. Aachen/Colônia: Impuls-Stiftung des VDMA, 2015.
- LIN, W. D. et al. *Application of SIRI for Industry 4.0 Maturity Assessment and Analysis*. In: 2021 IEEE International Conference on Industrial Engineering and Engineering Management (IEEM), 1 dez. 2019.
- LOCKE, E. A.; LATHAM, G. P. *Building a practically useful theory of goal setting and task motivation: A 35-year odyssey*. American Psychologist, v. 57, n. 9, p. 705–717, 2002.
- LOCKE, E. A.; LATHAM, G. P. *New directions in goal-setting theory*. Current Directions in Psychological Science, v. 15, n. 5, p. 265–268, 2006.
- MACNAMARA, J. *Evaluating public communication: Exploring models and metrics*. Nova York: Routledge, 2018.
- MACNAMARA, J. *Organizational listening: The missing essential in public communication*. Nova York: Peter Lang, 2016.
- MEN, L. R. *Measuring the impact of leadership style and employee empowerment on perceived organizational reputation*. Gainesville: Institute for Public Relations, 2012.
- MEN, L. R.; STACKS, D. W. *The effects of authentic leadership on strategic internal communication and employee-organization relationships*. Journal of Public Relations Research, v. 26, n. 4, p. 301–324, 2014.
- MEN, L. R.; YOON, H. J. *Organizational crisis communication and new technologies: Building a public relations capability*. Public Relations Review, v. 47, n. 1, 2021.
- MEYER, J. P.; ALLEN, N. J. *A three-component conceptualization of organizational commitment*. Human Resource Management Review, v. 1, n. 1, p. 61–89, 1991.
- MOR BARAK, M. E. *Managing diversity: Toward a globally inclusive workplace*. Thousand Oaks: Sage Publications, 2016.
- NAMBISAN, S. et al. *Global platforms and ecosystems: Implications for international business theories*. Journal of International Business Studies, v. 50, n. 9, p. 1464–1486, 2019.
- NEWMAN, A.; DONOHUE, R.; EVA, N. *Psychological safety: A systematic review of the literature*. Human Resource Management Review, v. 27, n. 3, p. 521–535, 2017.
- NEWMAN, A. et al. *The effects of employees' creative self-efficacy on innovative behavior: The role of entrepreneurial leadership*. Journal of Business Research, v. 89, p. 1–9, 2020.
- NISHII, L. H. *The benefits of climate for inclusion for gender-diverse groups*. Academy of Management Journal, v. 56, n. 6, p. 1754–1774, 2013.
- NIST. *Cybersecurity Framework Version 2.0*. Gaithersburg: National Institute of Standards and Technology, 2024. Disponível em: https://www.nist.gov/cyberframework. Acesso em: 10 nov. 2025.
- NONAKA, I.; TAKEUCHI, H. *The knowledge-creating company: How Japanese companies create the dynamics of innovation*. Oxford: Oxford University Press, 1995.
- PEREIRA, V. et al. *A longitudinal investigation into multilevel agile & ambidextrous strategic dualities in an information technology high performing EMNE*. Technological Forecasting and Social Change, v. 169, 2021.
- PINK, D. H. *Drive: The Surprising Truth About What Motivates Us*. Nova York: Riverhead Books, 2009.
- PORATH, C. *An antidote to incivility*. Harvard Business Review, v. 94, n. 4, p. 108–111, 2016.
- QUINN, R. E.; THAKOR, A. V. *Creating a purpose-driven organization*. Harvard Business Review, v. 96, n. 4, p. 78–85, 2018.
- RAWLINS, B. *Give the emperor a mirror: Toward developing a stakeholder measurement of organizational transparency*. Journal of Public Relations Research, v. 21, n. 1, p. 71–99, 2008.
- REAGANS, R.; ZUCKERMAN, E. W. *Networks, diversity, and productivity: The social capital of corporate R&D teams*. Organization Science, v. 12, n. 4, p. 502–517, 2001.
- RIGBY, D. K.; SUTHERLAND, J.; TAKEUCHI, H. *Embracing Agile*. Harvard Business Review, p. 40–50, mai. 2016.
- ROBERSON, Q. M. *Disentangling the meanings of diversity and inclusion in organizations*. Group & Organization Management, v. 31, n. 2, p. 212–236, 2006.
- ROGITO, J.; MAKABE, M. *The role of continuous feedback in performance improvement*. International Journal of Human Resource Management, v. 31, n. 15, p. 1942–1965, 2020.
- SANS. *Security Awareness Maturity Model*. SANS Security Awareness Training, 2011–2025. Disponível em: https://www.sans.org/security-awareness-training/resources/maturity-model/. Acesso em: 10 nov. 2025.
- SCHAEFER, K. J. *Entrepreneurs' social relationships and their resource mobilization under different levels of uncertainty*. International Entrepreneurship and Management Journal, v. 16, p. 1–31, 2020.
- SCHAUFELI, W. B.; BAKKER, A. B. *Job demands, job resources, and their relationship with burnout and engagement: A multi-sample study*. Journal of Organizational Behavior, v. 25, n. 3, p. 293–315, 2004.
- SCHUH, G. et al. *Industrie 4.0 Maturity Index: Managing the Digital Transformation of Companies*. Munique: Herbert Utz Verlag, 2017. (acatech STUDY).
- SCHUMACHER, A.; EROL, S.; SIHN, W. *A maturity model for assessing Industry 4.0 readiness and maturity of manufacturing enterprises*. Procedia CIRP, v. 52, p. 161–166, 2016.
- SCHWABER, K.; SUTHERLAND, J. *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*. Disponível em: https://scrumguides.org/. Acesso em: 16 out. 2025.
- SEMERARO, C. et al. *A maturity model for evaluating the impact of Industry 4.0 technologies and principles in SMEs*. Manufacturing Letters, v. 37, p. 61–65, 1 set. 2023.
- SHORE, L. M. et al. *Inclusion and diversity in work groups: A review and model for future research*. Journal of Management, v. 37, n. 4, p. 1262–1289, 2011.
- SINEK, S. *Start with Why: How Great Leaders Inspire Everyone to Take Action*. Nova York: Portfolio, 2009.
- SMITHER, J. W.; LONDON, M.; REILLY, R. R. *Does performance improve following multisource feedback? A theoretical model, meta-analysis, and review of empirical findings*. Personnel Psychology, v. 58, n. 1, p. 33–66, 2005.
- STOHL, C.; STOHL, M.; LEONARDI, P. M. *Managing opacity: Information visibility and the paradox of transparency in the digital age*. International Journal of Communication, v. 10, p. 123–137, 2016.
- SUTHERLAND, J.; SUTHERLAND, J. J. *Scrum: The Art of Doing Twice the Work in Half the Time*. Nova York: Crown Business, 2014.
- TEECE, D. J. *A dynamic capabilities-based entrepreneurial theory of the multinational enterprise*. Journal of International Business Studies, v. 45, n. 1, p. 8–37, 2014.
- TEECE, D. J. *Explicating dynamic capabilities: The nature and microfoundations of (sustainable) enterprise performance*. Strategic Management Journal, v. 28, n. 13, p. 1319–1350, 2007.
- TOUFIGHI, S. P. et al. *Participative leadership, cultural factors, and speaking-up behaviour: An examination of intra-organisational knowledge sharing*. Journal of Innovation & Knowledge, v. 9, n. 3, p. 100548, 1 jul. 2024.
- TREEM, J. W.; LEONARDI, P. M. *Social media use in organizations: Exploring the affordances of visibility, editability, persistence, and association*. Communication Yearbook, v. 36, p. 143–189, 2013.
- TREND MICRO. *How to Improve Cybersecurity Awareness and Training: Capability Maturity Model*. Trend Micro CISO, set. 2023. Disponível em: https://trendmicro.com/en_us/ciso/23/i/improve-cybersecurity-awareness-training.html. Acesso em: 10 nov. 2025.
- TRIPSAS, M.; GAVETTI, G. *Capabilities, cognition, and inertia: Evidence from digital imaging*. Strategic Management Journal, v. 21, n. 10-11, p. 1147–1161, 2000.
- TURBAN, D. B.; GREENING, D. W. *Corporate social performance and organizational attractiveness to prospective employees*. Academy of Management Journal, v. 40, n. 3, p. 658–672, 1997.
- VAN DYCK, C.; FRESE, M.; BAER, M.; SONNENTAG, S. *Organizational error management culture and its impact on performance: A two-study replication*. Journal of Applied Psychology, v. 90, n. 6, p. 1228–1240, 2005.
- VERIZON. *2024 Data Breach Investigations Report*. Basking Ridge: Verizon Business, 2024.
- WANG, S. L.; LUO, Y.; LU, X.; SUN, J.; MAKSIMOV, V. *Autonomy delegation to foreign subsidiaries: An enabling mechanism for emerging-market multinationals*. Journal of International Business Studies, v. 45, n. 2, p. 111–130, 2014.
- WATSON, T.; NOBLE, P. *Evaluating public relations: A best practice guide to public relations planning, research and evaluation*. Londres: Kogan Page, 2014.
- WEF. *The Global Smart Industry Readiness Index Initiative: Manufacturing Transformation Insights Report 2022*. Genebra: World Economic Forum. Disponível em: https://www3.weforum.org/docs/WEF_The_Global_Smart_Industry_Readiness_Index_Initiative_2022.pdf.
- YANG, A.; LIM, J. S. *The rise and fall of public trust: Examining the role of ethical organizational communication during COVID-19*. Journal of Public Relations Research, v. 32, n. 3-4, p. 139–160, 2020.


### Controle de Versões
Versão               Data                    Descrição                Autor
1.0                  28/10/2025              Versão inicial do guia   Wladmir A. Chapetta
