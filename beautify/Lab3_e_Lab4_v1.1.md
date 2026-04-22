# Laboratórios Práticos — Capítulos 3 e 4
## Segurança Defensiva 2026-1
### Baseado em *Mastering Linux Security and Hardening* — Donald A. Tevault, 3ª ed.

> **Versão 1.1** — Correções aplicadas em relação à v1.0:
> - LAB 3.1: nova Etapa 0 com explicação de permissões octais (rwx → 755/700); `HOME_MODE 0700` movido do Troubleshooting para o Passo a Passo (Etapa 3); sugestão alternativa na P3
> - LAB 3.2: Etapa 4 corrigida para testar como usuário normal desde o início; P4 substituída (era duplicada do LAB 3.1)
> - LAB 3.3: pontuação das perguntas de fixação adicionada aos Critérios de Avaliação; P4 reformulada
> - LAB 4.1: `sudo` adicionado ao `nc -lp 80`; P2 e P4 melhoradas
> - LAB 4.2: regra SSH original removida antes do rate limiting; P3 com referência ao fail2ban; P4 reformulada
> - LAB 4.3: redirecionamento com `sudo` corrigido; regra SSH duplicada removida na Etapa 7; P1 melhorada

---

## Sumário

- [Capítulo 3 — Protegendo Contas de Usuários Normais](#capítulo-3-protegendo-contas-de-usuários-normais)
  - [LAB 3.1 — Permissões de Diretórios Home e Senhas Básicas](#-lab-31--permissões-de-diretórios-home-e-senhas-básicas)
  - [LAB 3.2 — Políticas de Complexidade de Senha com pwquality](#-lab-32--políticas-de-complexidade-de-senha-com-pwquality)
  - [LAB 3.3 — Banners de Segurança e Proteção contra Força Bruta](#-lab-33--banners-de-segurança-e-proteção-contra-força-bruta)
- [Capítulo 4 — Protegendo o Servidor com Firewall — Parte 1](#capítulo-4-protegendo-o-servidor-com-firewall--parte-1)
  - [LAB 4.1 — Introdução ao iptables](#-lab-41--introdução-ao-iptables)
  - [LAB 4.2 — Regras Avançadas de iptables e Bloqueio ICMP](#-lab-42--regras-avançadas-de-iptables-e-bloqueio-icmp)
  - [LAB 4.3 — Migração para nftables e Proteção IPv6](#-lab-43--migração-para-nftables-e-proteção-ipv6)
- [Apêndice A — Relatório de Conclusão de Laboratório](#apêndice-a-relatório-de-conclusão-de-laboratório)

---

## Capítulo 3 — Protegendo Contas de Usuários Normais

Este capítulo foca na proteção das contas de usuários regulares do sistema. Os três laboratórios progridem da configuração básica de permissões e políticas de senha (LAB 3.1), passando por políticas avançadas de complexidade com o módulo PAM `pwquality` (LAB 3.2), até a implementação de banners legais de segurança e proteção ativa contra ataques de força bruta com `pam_faillock` (LAB 3.3).

---

## 🟢 LAB 3.1 — Permissões de Diretórios Home e Senhas Básicas

**Nível:** Iniciante | **Duração estimada:** 40 min

| Campo      | Valor |
|------------|-------|
| **Objetivo** | Verificar e corrigir permissões dos diretórios home dos usuários e explorar as políticas básicas de senha definidas em `/etc/login.defs`. |
| **Capítulo** | Capítulo 3 — Protegendo Contas de Usuários Normais |
| **Nível** | 🟢 Iniciante |
| **Duração** | 40 minutos |
| **Pré-req.** | LAB 1.2 concluído — VM Ubuntu 24.04 com usuário `aluno` criado e funcionando. |
| **Recursos** | VM Ubuntu 24.04 com acesso sudo. |

---

### Passo a Passo

#### ETAPA 0 — Entendendo permissões no Linux (notação octal)

No Linux, cada arquivo e diretório possui três conjuntos de permissões: **dono** (*user*), **grupo** (*group*) e **outros** (*others*). Cada conjunto pode ter permissão de **leitura** (`r`), **escrita** (`w`) e **execução** (`x`). Quando você vê `drwxr-xr-x` na saída do `ls -la`, o `d` indica diretório e os 9 caracteres seguintes representam essas permissões:

```
d rwx r-x r-x
  ─┬─ ─┬─ ─┬─
   │    │    └── outros (others): leitura + execução
   │    └─────── grupo  (group):  leitura + execução
   └──────────── dono   (user):   leitura + escrita + execução
```

A **notação octal** converte cada conjunto em um dígito de 0 a 7, somando os valores:

| Permissão | Letra | Valor |
|-----------|-------|-------|
| Leitura   | `r`   | **4** |
| Escrita   | `w`   | **2** |
| Execução  | `x`   | **1** |
| Nenhuma   | `-`   | 0     |

Exemplos de conversão:

| Octal | Binário | Letras      | Significado |
|-------|---------|-------------|-------------|
| `7`   | `111`   | `rwx`       | Leitura + escrita + execução |
| `5`   | `101`   | `r-x`       | Leitura + execução (sem escrita) |
| `0`   | `000`   | `---`       | Nenhuma permissão |

Juntando os três dígitos:

| Permissão | Dono | Grupo | Outros | Resultado `ls -la` |
|-----------|------|-------|--------|---------------------|
| `755`     | `rwx` (7) | `r-x` (5) | `r-x` (5) | `drwxr-xr-x` — qualquer usuário pode ler e acessar |
| `700`     | `rwx` (7) | `---` (0) | `---` (0) | `drwx------` — apenas o dono pode acessar |
| `644`     | `rw-` (6) | `r--` (4) | `r--` (4) | `-rw-r--r--` — todos leem, só o dono escreve |
| `600`     | `rw-` (6) | `---` (0) | `---` (0) | `-rw-------` — só o dono lê e escreve |

> **Regra prática:** para diretórios, a permissão de **execução** (`x`) significa "poder entrar no diretório" (listar conteúdo e acessar arquivos dentro dele). Sem `x`, mesmo com `r`, o conteúdo não pode ser listado.

Com essa base, o `chmod 700 /home/aluno` que usaremos a seguir significa: "dono pode tudo (`rwx`), grupo e outros não podem nada (`---`)".

---

#### ETAPA 1 — Verificar as permissões atuais dos diretórios home

Por padrão, o Ubuntu cria diretórios home com permissão `755` — o que permite que qualquer usuário do sistema leia os arquivos de outros usuários. Vamos verificar e corrigir isso.

```bash
# Listar os diretórios home com permissões visíveis:
ls -la /home/
# Esperado: drwxr-xr-x  (755) — qualquer usuário pode listar o conteúdo
```

Para entender o risco, crie um segundo usuário e teste o acesso cruzado:

```bash
# Criar usuário de teste:
sudo useradd -m -s /bin/bash testuser
sudo passwd testuser          # defina uma senha simples para o teste

# Criar um arquivo "sensível" como aluno:
echo "dados confidenciais" > ~/arquivo_privado.txt

# Trocar para testuser e tentar ler o arquivo de aluno:
su - testuser
cat /home/aluno/arquivo_privado.txt   # Esperado: leitura bem-sucedida — isso é o problema!
exit
```

#### ETAPA 2 — Corrigir as permissões para 700

A permissão `700` garante que apenas o dono pode acessar o diretório home.

```bash
# Corrigir o home de aluno:
chmod 700 /home/aluno
ls -la /home/
# Esperado: drwx------  (700) para aluno

# Verificar que testuser não consegue mais acessar:
su - testuser
ls /home/aluno        # Esperado: "Permission denied"
cat /home/aluno/arquivo_privado.txt   # Esperado: "Permission denied"
exit
```

Para aplicar a todos os homes existentes de uma vez:

```bash
sudo chmod 700 /home/*
ls -la /home/
```

#### ETAPA 3 — Configurar o padrão para novos usuários

Para que futuros usuários também recebam `700` automaticamente, é necessário ajustar **dois parâmetros** no `/etc/login.defs`:

```bash
# Ver o umask atual do sistema:
grep -i umask /etc/login.defs
# Valor atual: UMASK 022 → novos arquivos ficam 644, diretórios 755

# Alterar o UMASK para 077 → novos diretórios ficam 700, arquivos 600:
sudo nano /etc/login.defs
# Localize a linha "UMASK		022" e altere para:
#   UMASK		077
```

> **Importante:** no Ubuntu, o `UMASK` do `login.defs` afeta apenas sessões de login. Para garantir que o `useradd` também crie diretórios com `700`, é necessário configurar o parâmetro `HOME_MODE`:

```bash
# Ainda no /etc/login.defs, localize HOME_MODE (ou adicione ao final):
# HOME_MODE	0700
# Se a linha estiver comentada, descomente-a e ajuste o valor para 0700.
```

```bash
# Confirmar as duas alterações:
grep -i umask /etc/login.defs
# Esperado: UMASK   077

grep HOME_MODE /etc/login.defs
# Esperado: HOME_MODE	0700

# Testar criando um novo usuário e verificando o home:
sudo useradd -m -s /bin/bash novousuario
ls -la /home/
# Esperado: drwx------  (700) para novousuario
sudo userdel -r novousuario   # limpeza
```

#### ETAPA 4 — Explorar as políticas de senha em `/etc/login.defs`

O arquivo `/etc/login.defs` define parâmetros globais de validade de senha para novos usuários criados com `useradd`.

```bash
# Ver os parâmetros de senha:
grep -E "^PASS" /etc/login.defs
```

Os campos mais importantes:

| Parâmetro | Significado | Valor padrão Ubuntu |
|-----------|-------------|---------------------|
| `PASS_MAX_DAYS` | Dias até a senha expirar | 99999 (nunca) |
| `PASS_MIN_DAYS` | Dias mínimos entre trocas | 0 |
| `PASS_WARN_AGE` | Dias de aviso antes do vencimento | 7 |

```bash
# Ajustar para política mais segura (editar com nano):
sudo nano /etc/login.defs
# Altere:
#   PASS_MAX_DAYS	90
#   PASS_MIN_DAYS	1

# Confirmar:
grep -E "^PASS" /etc/login.defs
# Esperado: PASS_MAX_DAYS 90 / PASS_MIN_DAYS 1 / PASS_WARN_AGE 7
```

> **Atenção:** alterações no `login.defs` afetam apenas usuários criados **após** a mudança. Para aplicar a usuários existentes, use `chage` (tema do LAB 3.2).

#### ETAPA 5 — Verificar as políticas em vigor com `chage`

```bash
# Ver as informações de validade de senha do usuário aluno:
sudo chage -l aluno
# Campos relevantes:
# Last password change        : <data>
# Password expires            : never  (ainda — pois aluno foi criado antes da mudança)
# Maximum number of days      : 99999
# Minimum number of days      : 0
# Number of days of warning   : 7

# Criar um usuário novo e verificar que herda os novos valores:
sudo useradd -m -s /bin/bash novousuario2
sudo passwd novousuario2
sudo chage -l novousuario2
# Esperado: Maximum number of days: 90 / Minimum: 1
sudo userdel -r novousuario2   # limpeza
```

#### ETAPA 6 — Testar criação de senha fraca (comportamento padrão)

Sem o módulo `pwquality` (instalado no LAB 3.2), o Ubuntu aceita senhas fracas com apenas um aviso:

```bash
sudo passwd testuser
# Tente digitar: 123
# Esperado: "BAD PASSWORD: The password is shorter than 8 characters"
# Mas ao insistir uma segunda vez, a senha é aceita — o aviso não é bloqueio!
```

Anote este comportamento — o LAB 3.2 corrigirá isso com o `pwquality`.

```bash
# Limpeza final:
sudo userdel -r testuser
```

---

### Troubleshooting

| Problema | Solução |
|----------|---------|
| `chmod 700 /home/*` retorna erro em `/home/aluno` | Execute como root: `sudo chmod 700 /home/aluno` |
| `nano` ou `sed` não altera o `login.defs` | Verifique a formatação exata com `cat -A /etc/login.defs` — pode haver tabs em vez de espaços. Edite manualmente com `sudo nano /etc/login.defs` |
| `chage -l` mostra "Password expires: never" mesmo após mudar `login.defs` | Correto — `login.defs` só afeta novos usuários. Use `sudo chage -M 90 aluno` para aplicar ao usuário existente |
| `su - testuser` pede senha e falha | A senha do `testuser` foi definida com `sudo passwd testuser`. A senha pedida pelo `su` é a do `testuser`, não a do `aluno` |
| `useradd -m` cria diretório com permissão 755 mesmo após mudar `UMASK` | Verifique que `HOME_MODE 0700` está configurado no `/etc/login.defs` (Etapa 3). O `UMASK` sozinho pode não ser suficiente para o `useradd` |

---

### Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| Screenshot: `ls -la /home/` mostrando permissão `700` para os diretórios home (check `home_permissao_700`) | 20 pts |
| Screenshot: `su - testuser` tentando acessar `/home/aluno` e recebendo "Permission denied" (check `acesso_cruzado_bloqueado`) | 15 pts |
| Screenshot: `grep -E "^PASS" /etc/login.defs` com `PASS_MAX_DAYS 90` e `PASS_MIN_DAYS 1` (check `login_defs_atualizado`) | 20 pts |
| Screenshot: `grep -i umask /etc/login.defs` mostrando `UMASK 077` (check `umask_configurado`) | 15 pts |
| Screenshot: `chage -l novousuario` mostrando novos valores herdados de `login.defs` (check `chage_novo_usuario`) | 15 pts |
| Arquivo `resultado_lab31_<nome>.json` commitado no repositório Git | 10 pts |
| Respostas das perguntas de fixação | 5 pts |
| **TOTAL** | **100 pts** |

---

### ✔ Checklist de Entrega — LAB 3.1 (v1.2)

- [ ] Screenshot: `ls -la /home/` com permissão `700` para os diretórios home  (check `home_permissao_700`)
- [ ] Screenshot: `su - testuser` bloqueado ao tentar acessar `/home/aluno`  (check `acesso_cruzado_bloqueado`)
- [ ] Screenshot: `grep -E "^PASS" /etc/login.defs` com `PASS_MAX_DAYS 90` e `PASS_MIN_DAYS 1`  (check `login_defs_atualizado`)
- [ ] Screenshot: `grep -i umask /etc/login.defs` com `UMASK 077`  (check `umask_configurado`)
- [ ] Screenshot: `sudo chage -l <novo_usuario>` mostrando máximo de 90 dias  (check `chage_novo_usuario`)
- [ ] Arquivo `resultado_lab31_<meu_nome>.json` gerado pelo `check_lab31.sh`
- [ ] Arquivo `resultado_lab31_<meu_nome>.json` commitado no repositório Git da turma
- [ ] Respostas das 5 perguntas de fixação

---

### Perguntas de Fixação

Responda em até 4 linhas cada.

**1. Por que a permissão padrão `755` nos diretórios home é considerada insegura em ambientes multiusuário?**

**2. Qual a diferença entre alterar o `PASS_MAX_DAYS` no `login.defs` e usar `chage -M` diretamente em um usuário? Quando cada abordagem é necessária?**

**3. Se o umask `077` for configurado no `login.defs`, os arquivos criados por serviços do sistema (Apache, MySQL) também são afetados? Por quê?**

**4. Por que o Ubuntu aceita uma senha fraca mesmo exibindo "BAD PASSWORD"? O que impede que esse aviso se torne um bloqueio?**

**5. (Desafio) Um administrador criou 50 usuários antes de configurar `PASS_MAX_DAYS 90` no `login.defs`. Como aplicar a política de 90 dias a todos eles de uma vez com um único comando?**

---

## 🟡 LAB 3.2 — Políticas de Complexidade de Senha com pwquality

**Nível:** Intermediário | **Duração estimada:** 50 min

| Campo      | Valor |
|------------|-------|
| **Objetivo** | Instalar e configurar o módulo PAM `pwquality` para impor políticas rigorosas de complexidade de senha, e aplicar expiração de conta por usuário com `chage`. |
| **Capítulo** | Capítulo 3 — Protegendo Contas de Usuários Normais |
| **Nível** | 🟡 Intermediário |
| **Duração** | 50 minutos |
| **Pré-req.** | LAB 3.1 concluído — `login.defs` com `PASS_MAX_DAYS 90` e diretórios home com permissão `700`. |
| **Recursos** | VM Ubuntu 24.04 com acesso sudo. |

---

### Passo a Passo

#### ETAPA 1 — Instalar o módulo pwquality

O `libpam-pwquality` substitui o verificador de senha padrão do PAM, tornando a rejeição de senhas fracas **obrigatória** (não apenas um aviso).

```bash
sudo apt update && sudo apt install -y libpam-pwquality
# Confirmar instalação:
dpkg -l libpam-pwquality
# Esperado: linha com "ii  libpam-pwquality ..."
```

#### ETAPA 2 — Configurar as políticas em `/etc/security/pwquality.conf`

```bash
# Ver o arquivo de configuração atual (maioria das linhas está comentada):
grep -v "^#" /etc/security/pwquality.conf | grep -v "^$"
# Esperado: saída vazia — tudo comentado por padrão

sudo nano /etc/security/pwquality.conf
```

Adicione ou descomente as seguintes linhas:

```
# Comprimento mínimo da senha:
minlen = 12

# Créditos de complexidade (valores negativos = mínimo obrigatório):
dcredit = -1        # mínimo 1 dígito
ucredit = -1        # mínimo 1 letra maiúscula
ocredit = -1        # mínimo 1 caractere especial
lcredit = -1        # mínimo 1 letra minúscula

# Diferença mínima em relação à senha anterior:
difok = 5

# Máximo de caracteres repetidos consecutivos:
maxrepeat = 3

# Não permitir senha que contenha o nome do usuário:
usercheck = 1
```

Salve com `Ctrl+O → Enter → Ctrl+X`.

```bash
# Confirmar as configurações ativas:
grep -v "^#" /etc/security/pwquality.conf | grep -v "^$"
```

#### ETAPA 3 — Verificar a integração com o PAM

O `libpam-pwquality` já se integra automaticamente ao PAM no Ubuntu. Confirme:

```bash
grep pwquality /etc/pam.d/common-password
# Esperado: linha com "pam_pwquality.so retry=3" ou similar
```

O parâmetro `retry=3` permite até 3 tentativas antes de recusar definitivamente — ao contrário do comportamento anterior que aceitava insistência.

#### ETAPA 4 — Testar a política com senhas fracas e fortes

Crie um usuário de teste para os experimentos:

```bash
sudo useradd -m -s /bin/bash usuario_teste
sudo passwd usuario_teste   # defina uma senha forte inicial (ex.: Abcdefghij1!k)
```

> **Importante:** o `root` pode definir qualquer senha ignorando o `pwquality`. Para testar a política corretamente, **troque a senha como o próprio usuário**, não como root:

```bash
# Trocar para o usuario_teste e testar senhas:
su - usuario_teste
passwd
```

**Testes a realizar e anotar (como `usuario_teste`, via `passwd`):**

| Senha tentada | Esperado |
|---------------|----------|
| `abc` | Rejeitada — muito curta |
| `abcdefghijkl` | Rejeitada — sem maiúsculas, dígitos, especiais |
| `Abcdefghijk1` | Rejeitada — sem caractere especial |
| `Abcdefghij1!` | Rejeitada — 11 chars (minlen=12) |
| `Abcdefghij1!k` | **Aceita** — 13 chars, maiúscula, dígito, especial, minúsculas |

```bash
exit   # voltar para o aluno/root
```

#### ETAPA 5 — Configurar expiração de conta com `chage`

O `chage` aplica políticas de validade de senha **por usuário**, sobrepondo os valores do `login.defs`.

```bash
# Ver a situação atual do usuario_teste:
sudo chage -l usuario_teste

# Aplicar política individual:
sudo chage -M 90   usuario_teste   # senha expira em 90 dias
sudo chage -m 1    usuario_teste   # mínimo 1 dia entre trocas
sudo chage -W 14   usuario_teste   # aviso 14 dias antes

# Confirmar:
sudo chage -l usuario_teste
# Esperado:
# Maximum number of days between password change  : 90
# Minimum number of days between password change  : 1
# Number of days of warning before password expires: 14
```

Forçar a troca de senha no próximo login (útil para contas novas):

```bash
sudo chage -d 0 usuario_teste
sudo chage -l usuario_teste
# Esperado: "Password expires: <ontem>" — o sistema pedirá nova senha no próximo login

# Verificar o comportamento:
su - usuario_teste   # deve pedir imediatamente para trocar a senha
exit
```

#### ETAPA 6 — Aplicar expiração ao usuário `aluno`

```bash
sudo chage -M 90 -m 1 -W 14 aluno
sudo chage -l aluno
```

```bash
# Limpeza:
sudo userdel -r usuario_teste
```

---

### Troubleshooting

| Problema | Solução |
|----------|---------|
| `apt install libpam-pwquality` falha | Execute `sudo apt update` primeiro. Se persistir: `sudo apt install --fix-broken` |
| Senhas fracas ainda são aceitas após configurar `pwquality.conf` | Confirme que o módulo está no PAM: `grep pwquality /etc/pam.d/common-password`. Se não estiver, reinstale: `sudo apt reinstall libpam-pwquality` |
| `grep -v "^#"` no `pwquality.conf` mostra saída vazia | O arquivo está todo comentado. As configurações foram adicionadas mas precisam estar **sem** `#` no início |
| `chage -d 0` não força troca no próximo `su -` | O `su -` nem sempre aciona o `chage`. Teste com logout e login real (ou SSH) |
| `passwd` como root ignora o `pwquality` | Correto — root pode definir qualquer senha. Para testar a política, troque como o próprio usuário: `su - usuario_teste` → `passwd` |

---

### Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| Screenshot: `dpkg -l libpam-pwquality` confirmando instalação (check `pwquality_instalado`) | 10 pts |
| Screenshot: `grep -v "^#" /etc/security/pwquality.conf` mostrando `minlen = 12` e demais parâmetros (check `minlen_configurado`) | 20 pts |
| Screenshot: tentativa de senha fraca sendo **rejeitada** (ex.: `abcdefghijkl`) (check `senha_fraca_rejeitada`) | 20 pts |
| Screenshot: senha forte sendo **aceita** | 10 pts |
| Screenshot: `sudo chage -l aluno` com `Maximum number of days: 90` (check `chage_configurado`) | 20 pts |
| Arquivo `resultado_lab32_<nome>.json` commitado no repositório Git | 10 pts |
| Respostas das perguntas de fixação | 10 pts |
| **TOTAL** | **100 pts** |

---

### ✔ Checklist de Entrega — LAB 3.2 (v1.2)

- [ ] Screenshot: `dpkg -l libpam-pwquality` confirmando instalação  (check `pwquality_instalado`)
- [ ] Screenshot: `grep -v "^#" /etc/security/pwquality.conf` com `minlen = 12` e parâmetros de crédito  (check `minlen_configurado`)
- [ ] Screenshot: senha fraca sendo rejeitada pelo sistema  (check `senha_fraca_rejeitada`)
- [ ] Screenshot: senha forte sendo aceita
- [ ] Screenshot: `sudo chage -l aluno` mostrando `Maximum number of days: 90`  (check `chage_configurado`)
- [ ] Arquivo `resultado_lab32_<meu_nome>.json` gerado pelo `check_lab32.sh`
- [ ] Arquivo `resultado_lab32_<meu_nome>.json` commitado no repositório Git da turma
- [ ] Respostas das 5 perguntas de fixação

---

### Perguntas de Fixação

Responda em até 4 linhas cada.

**1. Qual a diferença entre o verificador de senha padrão do Ubuntu e o `pam_pwquality`? Por que o padrão permite insistência e o `pwquality` não?**

**2. O que significam valores negativos nos parâmetros `dcredit`, `ucredit`, `ocredit` e `lcredit`? O que acontece se você usar valores positivos?**

**3. Por que `root` pode definir qualquer senha ignorando o `pwquality`, e qual o risco de segurança disso em ambientes com múltiplos administradores?**

**4. Se um administrador configurar `minlen = 12` no `pwquality.conf`, mas o `login.defs` tiver `PASS_MIN_LEN 8`, qual valor prevalece? Por quê?**

**5. (Desafio) O parâmetro `maxrepeat = 3` bloqueia `aaabbb` mas permite `aabbcc`. Explique por que e qual parâmetro adicional poderia complementar essa proteção.**

---

## 🔴 LAB 3.3 — Banners de Segurança e Proteção contra Força Bruta

**Nível:** Avançado | **Duração estimada:** 80 min

| Campo      | Valor |
|------------|-------|
| **Objetivo** | Configurar banners legais de segurança nos pontos de login e implementar proteção contra ataques de força bruta com `pam_faillock`, incluindo bloqueio automático, desbloqueio manual e auditoria de tentativas. |
| **Capítulo** | Capítulo 3 — Protegendo Contas de Usuários Normais |
| **Nível** | 🔴 Avançado |
| **Duração** | 80 minutos |
| **Pré-req.** | LAB 3.2 concluído — `pwquality` configurado, `chage` aplicado ao usuário `aluno`. |
| **Recursos** | VM Ubuntu 24.04 com acesso sudo e SSH ativo (LAB 1.2). |

---

### Passo a Passo

#### ETAPA 1 — Configurar o banner pós-login (`/etc/motd`)

O `/etc/motd` (*Message of the Day*) é exibido **após** o login bem-sucedido, em sessões SSH e terminais locais.

```bash
# Ver o conteúdo atual:
cat /etc/motd
# Ubuntu 24.04 pode ter um motd dinâmico via /etc/update-motd.d/

# Desabilitar o motd dinâmico para usar apenas o estático:
sudo chmod -x /etc/update-motd.d/*
ls -la /etc/update-motd.d/   # todos os scripts devem aparecer sem +x

# Criar o banner pós-login:
sudo nano /etc/motd
```

Conteúdo sugerido (adapte ao contexto da instituição):

```
============================================================
  SISTEMA RESTRITO — ACESSO AUTORIZADO SOMENTE
============================================================

  Este sistema é de uso exclusivo de usuários autorizados.
  Toda atividade é monitorada e registrada.
  O acesso não autorizado é crime (Lei 12.737/2012).

  Em caso de problemas, contate: ti@instituicao.edu.br
============================================================
```

```bash
# Testar: faça logout e login novamente para ver o banner
```

#### ETAPA 2 — Configurar o banner pré-login no terminal local (`/etc/issue`)

O `/etc/issue` é exibido **antes** do prompt de login nos terminais virtuais (tty1–tty6).

```bash
# Ver o conteúdo atual:
cat /etc/issue
# Esperado: "Ubuntu 24.04 LTS \n \l"

sudo nano /etc/issue
```

Conteúdo sugerido:

```
============================================================
  ACESSO RESTRITO — APENAS USUÁRIOS AUTORIZADOS
  Atividades monitoradas — Lei 12.737/2012
============================================================

```

> Mantenha uma linha em branco ao final para separar o banner do prompt de login.

```bash
# Confirmar:
cat /etc/issue
```

#### ETAPA 3 — Configurar o banner pré-login para SSH (`/etc/issue.net`)

Para que o banner apareça **antes** do prompt de senha SSH, é necessário configurar o `sshd`:

```bash
# Criar o conteúdo do banner SSH:
sudo nano /etc/issue.net
```

```
============================================================
  SISTEMA RESTRITO — ACESSO SSH MONITORADO
  Tentativas de acesso não autorizado são registradas.
  Lei 12.737/2012 — Crime de Invasão de Dispositivo.
============================================================
```

```bash
# Habilitar o banner no sshd:
sudo nano /etc/ssh/sshd_config
```

Localize e descomente (ou adicione) a linha:

```
Banner /etc/issue.net
```

```bash
# Reiniciar o SSH para aplicar:
sudo systemctl restart ssh

# Testar a partir do host (PowerShell/terminal do Windows ou outra VM):
ssh aluno@<IP-da-VM>
# O banner deve aparecer ANTES do prompt de senha
```

#### ETAPA 4 — Configurar o `pam_faillock` para bloqueio por força bruta

O `pam_faillock` conta tentativas de autenticação falhas e bloqueia a conta temporariamente. Ele já está presente no Ubuntu 24.04 — só precisa ser ativado.

```bash
# Verificar o arquivo de configuração:
cat /etc/security/faillock.conf
```

Configure os parâmetros editando o arquivo:

```bash
sudo nano /etc/security/faillock.conf
```

Ajuste ou descomente as seguintes linhas:

```
# Número de falhas antes do bloqueio:
deny = 3

# Tempo (em segundos) que a conta fica bloqueada:
unlock_time = 300

# Janela de tempo (em segundos) para contar as falhas:
fail_interval = 900

# Registrar falhas mesmo para usuários inexistentes (evita enumeração):
audit

# Não bloquear o root (evita lockout acidental do administrador):
# even_deny_root    ← mantenha comentado por segurança
```

```bash
# Verificar a integração com o PAM (deve já estar configurado no Ubuntu 24.04):
grep faillock /etc/pam.d/common-auth
# Esperado: duas linhas com pam_faillock.so (auth required ... preauth e authfail)
```

Se as linhas não existirem, adicione manualmente ao `/etc/pam.d/common-auth`:

```bash
sudo nano /etc/pam.d/common-auth
```

A configuração correta deve conter, **nesta ordem**:

```
auth    required      pam_faillock.so preauth silent
auth    [default=die] pam_faillock.so authfail
```

#### ETAPA 5 — Testar o bloqueio com tentativas incorretas

```bash
# Criar usuário de teste:
sudo useradd -m -s /bin/bash usuario_bloqueio
sudo passwd usuario_bloqueio   # defina uma senha conhecida

# Em outro terminal (ou pelo SSH), tente logar com senha errada:
ssh usuario_bloqueio@localhost
# Tente 3x com senha errada

# Verificar o status de bloqueio:
sudo faillock --user usuario_bloqueio
# Esperado: entradas com "V" (válidas/falhas) e "FAILED" nas tentativas
```

Após a 3ª falha:

```bash
# Tentar login com a senha CORRETA — deve ser bloqueado:
ssh usuario_bloqueio@localhost
# Esperado: "Authentication failed" mesmo com senha correta
```

#### ETAPA 6 — Desbloqueio manual de conta

```bash
# Desbloquear manualmente (antes dos 300 segundos):
sudo faillock --user usuario_bloqueio --reset

# Confirmar que o bloqueio foi removido:
sudo faillock --user usuario_bloqueio
# Esperado: saída vazia ou sem entradas ativas

# Verificar que o login volta a funcionar:
ssh usuario_bloqueio@localhost   # agora com a senha correta — deve funcionar
```

#### ETAPA 7 — Auditoria: verificar tentativas registradas

```bash
# Ver os logs de autenticação para os eventos de faillock:
sudo grep "pam_faillock\|FAILED\|authentication failure" /var/log/auth.log | tail -20

# Ver o status de todos os usuários com falhas registradas:
sudo faillock
# Lista todos os usuários que tiveram tentativas falhas recentes

# Limpeza:
sudo userdel -r usuario_bloqueio
```

---

### Troubleshooting

| Problema | Solução |
|----------|---------|
| Banner SSH não aparece antes da senha | Confirme que `Banner /etc/issue.net` está no `sshd_config` **sem** `#` e que o SSH foi reiniciado: `sudo systemctl restart ssh` |
| `/etc/motd` não aparece no login | Verifique se os scripts em `/etc/update-motd.d/` estão com `+x`. Se sim, eles sobrescrevem o `motd` estático. Remova a permissão de execução: `sudo chmod -x /etc/update-motd.d/*` |
| `faillock --user X` mostra entradas mas o login ainda funciona | As entradas precisam atingir o valor `deny`. Confirme o valor configurado: `grep deny /etc/security/faillock.conf` |
| Login bloqueado mas `unlock_time` ainda não passou | Use `sudo faillock --user X --reset` para desbloquear imediatamente |
| `grep faillock /etc/pam.d/common-auth` retorna vazio | No Ubuntu 24.04 o faillock pode estar em `/etc/pam.d/login` e `/etc/pam.d/sshd`. Verifique: `grep -r faillock /etc/pam.d/` |
| `pam_faillock.so` não encontrado | Instale: `sudo apt install libpam-modules` (já incluso no Ubuntu padrão) |

---

### Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| Screenshot: `cat /etc/motd` mostrando o banner configurado (check `motd_configurado`) | 10 pts |
| Screenshot: `cat /etc/issue.net` mostrando o banner SSH configurado (check `issue_net_configurado`) | 10 pts |
| Screenshot: conexão SSH exibindo o banner **antes** do prompt de senha | 10 pts |
| Screenshot: `grep "deny\|unlock_time" /etc/security/faillock.conf` com valores configurados (check `faillock_configurado`) | 15 pts |
| Screenshot: `sudo faillock --user usuario_bloqueio` mostrando tentativas falhas registradas (check `faillock_tentativas_registradas`) | 15 pts |
| Screenshot: tentativa de login com senha correta sendo bloqueada após 3 falhas (check `conta_bloqueada_apos_falhas`) | 15 pts |
| Screenshot: `sudo faillock --user usuario_bloqueio --reset` e login bem-sucedido após desbloqueio | 5 pts |
| Arquivo `resultado_lab33_<nome>.json` commitado no repositório Git | 10 pts |
| Respostas das perguntas de fixação | 10 pts |
| **TOTAL** | **100 pts** |

---

### ✔ Checklist de Entrega — LAB 3.3 (v1.2)

- [ ] Screenshot: `cat /etc/motd` com o banner pós-login configurado  (check `motd_configurado`)
- [ ] Screenshot: `cat /etc/issue.net` com o banner SSH configurado  (check `issue_net_configurado`)
- [ ] Screenshot: sessão SSH mostrando o banner antes do prompt de senha
- [ ] Screenshot: `grep "deny\|unlock_time" /etc/security/faillock.conf` com `deny = 3`  (check `faillock_configurado`)
- [ ] Screenshot: `sudo faillock --user usuario_bloqueio` com tentativas falhas listadas  (check `faillock_tentativas_registradas`)
- [ ] Screenshot: login bloqueado após 3 tentativas incorretas  (check `conta_bloqueada_apos_falhas`)
- [ ] Screenshot: `faillock --reset` e login bem-sucedido após desbloqueio
- [ ] Arquivo `resultado_lab33_<meu_nome>.json` gerado pelo `check_lab33.sh`
- [ ] Arquivo `resultado_lab33_<meu_nome>.json` commitado no repositório Git da turma
- [ ] Respostas das 5 perguntas de fixação

---

### Perguntas de Fixação

Responda em até 4 linhas cada.

**1. Qual a diferença legal e técnica entre `/etc/motd`, `/etc/issue` e `/etc/issue.net`? Por que é importante ter banners em todos os três pontos?**

**2. Por que o parâmetro `audit` no `faillock.conf` é importante do ponto de vista de segurança, mesmo que registre tentativas com usuários inexistentes?**

**3. O parâmetro `even_deny_root` foi mantido comentado (desabilitado) no lab. Quais são os argumentos a favor e contra habilitá-lo em um servidor de produção?**

**4. O `fail_interval` padrão de 900s (15 min) cria uma janela de 15 minutos. Se o atacante espaça tentativas a cada 16 minutos, o contador zera. Além de aumentar o `fail_interval`, que outra camada de defesa (fora do PAM) poderia detectar esse padrão de ataque lento?**

**5. (Desafio) O `pam_faillock` bloqueia a conta no sistema local. Se um atacante tentar força bruta via SSH diretamente, o bloqueio funciona da mesma forma? O que mais poderia ser configurado para proteger o SSH especificamente?**

---

## Capítulo 4 — Protegendo o Servidor com Firewall — Parte 1

Este capítulo introduz os conceitos fundamentais de firewall no Linux. Os laboratórios progridem da sintaxe clássica do `iptables` para visualização e criação de regras básicas (LAB 4.1), passando por configurações avançadas com política DROP e logging (LAB 4.2), até a migração para a sintaxe nativa do `nftables` com suporte dual IPv4/IPv6 (LAB 4.3).

> **Nota sobre o Ubuntu 24.04:** o binário `iptables` neste sistema é um wrapper sobre o backend `nftables`. Isso significa que as regras criadas com `iptables` são internamente traduzidas para `nftables`. O comportamento é idêntico ao `iptables` tradicional para fins deste laboratório. O LAB 4.3 apresentará a sintaxe nativa do `nftables`.

---

## 🟢 LAB 4.1 — Introdução ao iptables

**Nível:** Iniciante | **Duração estimada:** 40 min

| Campo      | Valor |
|------------|-------|
| **Objetivo** | Compreender a estrutura de tabelas, chains e regras do `iptables`, criar regras básicas para controle de tráfego e salvar a configuração para persistência. |
| **Capítulo** | Capítulo 4 — Protegendo o Servidor com Firewall — Parte 1 |
| **Nível** | 🟢 Iniciante |
| **Duração** | 40 minutos |
| **Pré-req.** | LAB 1.2 concluído — VM Ubuntu 24.04 com SSH ativo e conectividade de rede. |
| **Recursos** | VM Ubuntu 24.04 com acesso sudo. |

---

### Passo a Passo

#### ETAPA 1 — Verificar o estado atual do firewall

```bash
# Verificar se o UFW (firewall padrão do Ubuntu) está ativo — deve estar inativo neste lab:
sudo ufw status
# Se estiver ativo, desabilite para trabalhar diretamente com iptables:
sudo ufw disable

# Ver as regras atuais do iptables (tabela filter, todas as chains):
sudo iptables -L -v --line-numbers
# Esperado: chains INPUT, FORWARD, OUTPUT com política ACCEPT e sem regras
```

A saída de `iptables -L -v` tem a seguinte estrutura:

| Campo | Significado |
|-------|-------------|
| `Chain INPUT (policy ACCEPT)` | Tráfego destinado a este host — política padrão: aceitar tudo |
| `Chain FORWARD (policy ACCEPT)` | Tráfego roteado através deste host |
| `Chain OUTPUT (policy ACCEPT)` | Tráfego originado deste host |
| `pkts / bytes` | Contadores de pacotes e bytes que passaram pela regra |
| `target` | Ação: ACCEPT, DROP, REJECT, LOG... |

#### ETAPA 2 — Criar regras para permitir SSH e HTTP

```bash
# Permitir conexões SSH estabelecidas e novas (porta 22, TCP):
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Permitir tráfego HTTP (porta 80, TCP):
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Permitir tráfego HTTPS (porta 443, TCP):
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Permitir tráfego de loopback (essencial para processos locais):
sudo iptables -A INPUT -i lo -j ACCEPT

# Ver as regras criadas:
sudo iptables -L INPUT -v --line-numbers
```

Anatomia de uma regra `iptables`:

```
iptables  -A     INPUT   -p tcp  --dport 22  -j ACCEPT
   ↑       ↑       ↑        ↑        ↑           ↑
ferram.  append  chain  protocolo  porta      ação
```

#### ETAPA 3 — Bloquear uma porta específica

```bash
# Bloquear acesso à porta 8080 (exemplo de porta de aplicação não autorizada):
sudo iptables -A INPUT -p tcp --dport 8080 -j DROP

# Ver as regras atualizadas:
sudo iptables -L INPUT -v --line-numbers
```

Diferença entre `DROP` e `REJECT`:

| Ação | Comportamento | Quando usar |
|------|---------------|-------------|
| `DROP` | Descarta silenciosamente — o emissor não recebe resposta | Ocultar a existência do serviço |
| `REJECT` | Retorna erro ao emissor (TCP RST ou ICMP port-unreachable) | Feedback explícito ao usuário legítimo |

#### ETAPA 4 — Testar as regras

```bash
# Instalar netcat para testar portas:
sudo apt install -y netcat-openbsd

# Em um terminal, simular um serviço na porta 80 (requer sudo por ser porta < 1024):
sudo nc -lp 80 &

# Em outro terminal (ou pelo SSH do host), testar as portas:
nc -zv localhost 22    # Esperado: Connection succeeded
nc -zv localhost 80    # Esperado: Connection succeeded
nc -zv localhost 8080  # Esperado: timeout (DROP)

# Encerrar o nc em background:
sudo kill %1 2>/dev/null; true
```

#### ETAPA 5 — Salvar as regras para persistência

No Ubuntu, as regras `iptables` são perdidas ao reiniciar. Para persistir:

```bash
# Instalar iptables-persistent:
sudo apt install -y iptables-persistent
# Durante a instalação, responda "Yes" para salvar as regras atuais

# As regras são salvas em:
cat /etc/iptables/rules.v4
# Deve mostrar as regras criadas nas etapas anteriores

# Para salvar manualmente (após novas alterações):
sudo netfilter-persistent save

# Verificar que o serviço de restauração está habilitado:
sudo systemctl is-enabled netfilter-persistent
# Esperado: enabled
```

#### ETAPA 6 — Listar e remover regras

```bash
# Listar com números de linha:
sudo iptables -L INPUT -v --line-numbers

# Remover uma regra pelo número de linha (ex: remover a regra 3):
sudo iptables -D INPUT 3

# Limpar todas as regras (flush) — CUIDADO: remove toda proteção:
# sudo iptables -F   ← não execute agora, apenas para referência

# Verificar estado final:
sudo iptables -L -v --line-numbers
```

---

### Troubleshooting

| Problema | Solução |
|----------|---------|
| `iptables: command not found` | Instale: `sudo apt install iptables` |
| UFW interfere com as regras do iptables | Desabilite: `sudo ufw disable`. Confirme: `sudo ufw status` → "inactive" |
| Regras somem após reboot | Instale `iptables-persistent` e execute `sudo netfilter-persistent save` |
| `nc -zv localhost 8080` não trava (DROP deveria ser silencioso) | Use `nc -zv -w 3 localhost 8080` para definir timeout de 3 segundos |
| `iptables -D INPUT 3` remove a regra errada | Liste sempre com `--line-numbers` antes de remover. A numeração muda após cada remoção |
| Perdi o acesso SSH após adicionar regra | Conecte pelo console da VM (VirtualBox) e remova a regra problemática: `sudo iptables -D INPUT <número>` |
| `nc -lp 80` retorna "Permission denied" | Portas abaixo de 1024 requerem root. Use: `sudo nc -lp 80 &` |

---

### Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| Screenshot: `sudo iptables -L INPUT -v --line-numbers` mostrando regras para SSH, HTTP e HTTPS (check `iptables_regras_basicas`) | 25 pts |
| Screenshot: `nc -zv localhost 22` e `nc -zv localhost 80` com sucesso (check `iptables_ssh_http_ok`) | 20 pts |
| Screenshot: `nc -zv -w 3 localhost 8080` com timeout — porta bloqueada (check `iptables_porta_bloqueada`) | 15 pts |
| Screenshot: `cat /etc/iptables/rules.v4` mostrando regras salvas (check `regras_salvas`) | 20 pts |
| Screenshot: `sudo systemctl is-enabled netfilter-persistent` retornando `enabled` | 10 pts |
| Arquivo `resultado_lab41_<nome>.json` commitado no repositório Git | 10 pts |
| **TOTAL** | **100 pts** |

---

### ✔ Checklist de Entrega — LAB 4.1 (v1.2)

- [ ] Screenshot: `sudo ufw status` mostrando "inactive"
- [ ] Screenshot: `sudo iptables -L INPUT -v --line-numbers` com regras para portas 22, 80, 443  (check `iptables_regras_basicas`)
- [ ] Screenshot: `nc -zv localhost 22` e porta 80 com sucesso  (check `iptables_ssh_http_ok`)
- [ ] Screenshot: `nc -zv -w 3 localhost 8080` com timeout  (check `iptables_porta_bloqueada`)
- [ ] Screenshot: `cat /etc/iptables/rules.v4` com regras persistidas  (check `regras_salvas`)
- [ ] Screenshot: `sudo systemctl is-enabled netfilter-persistent` → `enabled`
- [ ] Arquivo `resultado_lab41_<meu_nome>.json` gerado pelo `check_lab41.sh`
- [ ] Arquivo `resultado_lab41_<meu_nome>.json` commitado no repositório Git da turma
- [ ] Respostas das 5 perguntas de fixação

---

### Perguntas de Fixação

Responda em até 4 linhas cada.

**1. Qual a diferença entre as chains `INPUT`, `OUTPUT` e `FORWARD`? Dê um exemplo de tráfego que passa por cada uma.**

**2. Se você adicionar a regra de loopback (`-i lo -j ACCEPT`) DEPOIS de um `DROP` para tráfego local, o que acontece com resolução DNS e processos como `apt update`? Por que a ordem importa?**

**3. Qual a diferença prática entre `DROP` e `REJECT`? Do ponto de vista de um atacante fazendo port scan, qual é mais vantajoso para o defensor usar?**

**4. Se as regras `iptables` fossem persistentes por padrão (salvas automaticamente), quais riscos isso criaria durante troubleshooting de rede? Por que o comportamento volátil pode ser vantajoso?**

**5. (Desafio) No Ubuntu 24.04, o `iptables` é um wrapper sobre `nftables`. Como você pode verificar isso? Quais implicações isso tem para a administração do firewall?**

---

## 🟡 LAB 4.2 — Regras Avançadas de iptables e Bloqueio ICMP

**Nível:** Intermediário | **Duração estimada:** 55 min

| Campo      | Valor |
|------------|-------|
| **Objetivo** | Implementar uma política de firewall com regra padrão DROP, permitir apenas tráfego explicitamente autorizado, bloquear seletivamente ICMP, aplicar rate limiting e configurar logging de pacotes bloqueados. |
| **Capítulo** | Capítulo 4 — Protegendo o Servidor com Firewall — Parte 1 |
| **Nível** | 🟡 Intermediário |
| **Duração** | 55 minutos |
| **Pré-req.** | LAB 4.1 concluído — `iptables-persistent` instalado, regras básicas criadas. |
| **Recursos** | VM Ubuntu 24.04 com acesso sudo, segunda VM ou host para testes de ping e conexão. |

---

### Passo a Passo

#### ETAPA 1 — Preparar uma política DROP segura

> **Atenção:** definir a política padrão como DROP sem antes garantir o acesso SSH **pode travar sua sessão remota**. Siga a ordem exata abaixo.

```bash
# Ver o estado atual:
sudo iptables -L -v --line-numbers

# Limpar todas as regras existentes para começar do zero:
sudo iptables -F
sudo iptables -L -v   # deve mostrar chains vazias com política ACCEPT

# ORDEM OBRIGATÓRIA: adicionar as regras de permissão ANTES de mudar a política

# 1. Permitir loopback:
sudo iptables -A INPUT -i lo -j ACCEPT

# 2. Permitir conexões já estabelecidas e relacionadas (stateful):
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# 3. Permitir SSH com rate limiting (ESSENCIAL — adicione antes do DROP ou perderá o acesso):
#    Limita novas conexões SSH a 3 por minuto por IP (previne força bruta):
sudo iptables -A INPUT -p tcp --dport 22 \
  -m state --state NEW \
  -m limit --limit 3/minute --limit-burst 5 -j ACCEPT

# 4. Permitir ICMP echo (ping) para diagnóstico — vamos filtrar seletivamente depois:
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

# Agora é seguro mudar a política padrão para DROP:
sudo iptables -P INPUT DROP

# Verificar:
sudo iptables -L INPUT -v --line-numbers
# Esperado: policy DROP, com as 4 regras de exceção acima
```

#### ETAPA 2 — Bloquear um IP específico

```bash
# Bloquear todo tráfego de entrada de um IP específico (use o IP do host ou de outra VM):
sudo iptables -I INPUT 1 -s 192.168.56.1 -j DROP
# -I INPUT 1 insere no topo (antes das outras regras)

# Verificar:
sudo iptables -L INPUT -v --line-numbers

# Testar (do host, tente pingar a VM — deve parar de responder):
# ping <IP-da-VM>

# Remover a regra de bloqueio do IP:
sudo iptables -D INPUT 1
```

#### ETAPA 3 — Bloqueio seletivo de ICMP

O ICMP tem múltiplos tipos. Podemos permitir apenas os necessários:

```bash
# Remover a regra de ICMP ampla que adicionamos na etapa 1:
sudo iptables -L INPUT --line-numbers
# Identifique o número da linha com "icmp" e remova:
sudo iptables -D INPUT <número_da_linha_icmp>

# Permitir apenas echo-request (ping de entrada) com rate limiting (previne flood):
sudo iptables -A INPUT -p icmp --icmp-type echo-request \
  -m limit --limit 5/second --limit-burst 10 -j ACCEPT
sudo iptables -A OUTPUT -p icmp --icmp-type echo-reply -j ACCEPT

# Bloquear explicitamente timestamp e outros tipos menos usados:
sudo iptables -A INPUT -p icmp --icmp-type timestamp-request -j DROP
sudo iptables -A INPUT -p icmp --icmp-type address-mask-request -j DROP

# Testar:
ping -c 3 8.8.8.8        # deve funcionar (OUTPUT não está restrito)
# Do host: ping <IP-da-VM>  # deve responder (echo-request permitido)
```

#### ETAPA 4 — Verificar as regras de rate limiting

```bash
# Ver as regras atuais com os limites aplicados:
sudo iptables -L INPUT -v --line-numbers
# Esperado: regras com "limit" para SSH (3/min) e ICMP (5/sec)
```

#### ETAPA 5 — Logging de pacotes bloqueados

```bash
# Adicionar regra de LOG antes do DROP implícito da política:
# (regras são processadas em ordem — o LOG deve vir antes do final da chain)
sudo iptables -A INPUT -j LOG \
  --log-prefix "IPTABLES-DROP: " \
  --log-level 4

# Testar: faça uma conexão bloqueada (ex: porta 9999):
nc -zv -w 2 localhost 9999   # deve falhar

# Ver os logs gerados:
sudo dmesg | grep "IPTABLES-DROP" | tail -5
# ou:
sudo grep "IPTABLES-DROP" /var/log/kern.log | tail -5
```

> **Nota:** a regra `LOG` não consome o pacote — ela apenas registra e continua processando. Como está no final da chain (antes da política `DROP`), o pacote é logado e em seguida descartado pela política padrão.

#### ETAPA 6 — Backup e restauração de regras

```bash
# Fazer backup das regras atuais:
sudo iptables-save | sudo tee ~/backup_iptables_lab42.rules > /dev/null
cat ~/backup_iptables_lab42.rules

# Simular uma alteração destrutiva:
sudo iptables -F
sudo iptables -L   # chains vazias

# Restaurar do backup:
sudo iptables-restore < ~/backup_iptables_lab42.rules
sudo iptables -L INPUT --line-numbers   # regras restauradas

# Salvar como persistente:
sudo netfilter-persistent save
```

---

### Troubleshooting

| Problema | Solução |
|----------|---------|
| Perdi o acesso SSH após `iptables -P INPUT DROP` | Acesse pelo console do VirtualBox. Execute: `sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT`. Para próximas vezes, sempre adicione a regra SSH antes de mudar a política |
| `ping 8.8.8.8` não funciona com política DROP | A chain OUTPUT está com política ACCEPT, mas pode ter regra restritiva. Verifique: `sudo iptables -L OUTPUT`. Adicione se necessário: `sudo iptables -A OUTPUT -p icmp -j ACCEPT` |
| `--log-prefix` com espaço causa erro | O prefixo deve ter no máximo 29 caracteres incluindo o espaço final. Encurte se necessário |
| Regra de rate limiting bloqueia o próprio administrador | Adicione a exceção para o IP do host antes da regra de limite: `sudo iptables -I INPUT 1 -s <IP-do-host> -p tcp --dport 22 -j ACCEPT` |
| `dmesg` não mostra os logs do iptables | Verifique em: `sudo grep "IPTABLES" /var/log/syslog \| tail -10` |

---

### Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| Screenshot: `sudo iptables -L INPUT -v --line-numbers` com `policy DROP` e regras de exceção (check `politica_drop_input`) | 20 pts |
| Screenshot: regra `ESTABLISHED,RELATED` visível na listagem (check `regra_established_ok`) | 15 pts |
| Screenshot: regra de bloqueio de `timestamp-request` ICMP visível (check `icmp_tipo_bloqueado`) | 15 pts |
| Screenshot: regra de rate limiting para SSH na listagem | 10 pts |
| Screenshot: `dmesg` ou `kern.log` mostrando entradas `IPTABLES-DROP` (check `log_pacotes_ativo`) | 20 pts |
| Screenshot: `cat ~/backup_iptables_lab42.rules` com as regras exportadas | 10 pts |
| Arquivo `resultado_lab42_<nome>.json` commitado no repositório Git | 10 pts |
| **TOTAL** | **100 pts** |

---

### ✔ Checklist de Entrega — LAB 4.2 (v1.2)

- [ ] Screenshot: `sudo iptables -L INPUT -v --line-numbers` com `policy DROP`  (check `politica_drop_input`)
- [ ] Screenshot: regra `ESTABLISHED,RELATED` presente  (check `regra_established_ok`)
- [ ] Screenshot: regra de bloqueio de ICMP `timestamp-request`  (check `icmp_tipo_bloqueado`)
- [ ] Screenshot: regras de rate limiting para SSH e ICMP
- [ ] Screenshot: `dmesg` ou `kern.log` com entradas `IPTABLES-DROP`  (check `log_pacotes_ativo`)
- [ ] Screenshot: `cat ~/backup_iptables_lab42.rules` com regras exportadas
- [ ] Arquivo `resultado_lab42_<meu_nome>.json` gerado pelo `check_lab42.sh`
- [ ] Arquivo `resultado_lab42_<meu_nome>.json` commitado no repositório Git da turma
- [ ] Respostas das 5 perguntas de fixação

---

### Perguntas de Fixação

Responda em até 4 linhas cada.

**1. Por que a regra `ESTABLISHED,RELATED` é essencial em um firewall com política DROP? O que acontece sem ela?**

**2. Explique a diferença entre inserir uma regra com `-I INPUT 1` e anexar com `-A INPUT`. Quando cada abordagem deve ser usada?**

**3. O rate limiting com `--limit 3/minute` para SSH previne força bruta? Quais são as limitações dessa abordagem comparada ao `pam_faillock` (LAB 3.3) e ao `fail2ban`?**

**4. Se a regra `LOG` for adicionada DEPOIS de uma regra `DROP` explícita para o mesmo tráfego, os pacotes serão logados? Explique a ordem de processamento das regras numa chain.**

**5. (Desafio) Um atacante faz port scan com `nmap -sS` na VM. Quais pacotes seriam logados e quais não? Como o módulo de estado (`-m state`) interfere na detecção de scans furtivos?**

---

## 🔴 LAB 4.3 — Migração para nftables e Proteção IPv6

**Nível:** Avançado | **Duração estimada:** 85 min

| Campo      | Valor |
|------------|-------|
| **Objetivo** | Migrar as regras do `iptables` para a sintaxe nativa do `nftables`, criar tabelas e chains personalizadas, implementar proteção simultânea para IPv4 e IPv6, utilizar sets para gerenciamento de múltiplos IPs e configurar inicialização automática. |
| **Capítulo** | Capítulo 4 — Protegendo o Servidor com Firewall — Parte 1 |
| **Nível** | 🔴 Avançado |
| **Duração** | 85 minutos |
| **Pré-req.** | LAB 4.2 concluído — compreensão de chains, políticas e logging do `iptables`. |
| **Recursos** | VM Ubuntu 24.04 com acesso sudo. |

---

### Passo a Passo

#### ETAPA 1 — Preparar o ambiente para nftables

```bash
# Verificar a versão do nftables disponível:
nft --version
# Esperado: nftables v1.0.x

# Verificar o estado do serviço:
sudo systemctl status nftables
# Pode estar inactive — vamos habilitá-lo ao final

# Limpar as regras iptables do lab anterior para evitar conflito:
sudo iptables -F
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT

# Ver o estado atual do nftables (deve estar vazio):
sudo nft list ruleset
# Esperado: saída vazia
```

#### ETAPA 2 — Conceitos fundamentais do nftables

O `nftables` organiza as regras em uma hierarquia diferente do `iptables`:

```
nftables
└── table  (equivale à tabela "filter" do iptables)
    └── chain  (equivale às chains INPUT/OUTPUT/FORWARD)
        └── rule  (regra individual)
```

Diferenças principais:

| Característica | iptables | nftables |
|----------------|----------|----------|
| Tabelas padrão | filter, nat, mangle | Criadas pelo usuário |
| IPv4 e IPv6 | Comandos separados (iptables/ip6tables) | Unified em uma única regra com `meta nfproto` |
| Sets | Módulo `ipset` separado | Nativo: `{ 192.168.1.1, 10.0.0.1 }` |
| Sintaxe | `-A INPUT -p tcp --dport 22 -j ACCEPT` | `iif != "lo" tcp dport 22 accept` |

#### ETAPA 3 — Criar a estrutura base de tabelas e chains

```bash
# Criar uma tabela para filtro de pacotes IPv4 e IPv6:
sudo nft add table inet filter
# "inet" = família que cobre IPv4 e IPv6 simultaneamente

# Criar as chains com tipo e hook (ponto de interceptação no kernel):
sudo nft add chain inet filter input \
  '{ type filter hook input priority 0 ; policy drop ; }'

sudo nft add chain inet filter output \
  '{ type filter hook output priority 0 ; policy accept ; }'

sudo nft add chain inet filter forward \
  '{ type filter hook forward priority 0 ; policy drop ; }'

# Verificar a estrutura criada:
sudo nft list table inet filter
```

#### ETAPA 4 — Adicionar as regras fundamentais

```bash
# Permitir loopback:
sudo nft add rule inet filter input iif "lo" accept

# Permitir conexões estabelecidas e relacionadas:
sudo nft add rule inet filter input ct state established,related accept

# Permitir SSH (IPv4 e IPv6 simultaneamente) com counter para monitoramento:
sudo nft add rule inet filter input tcp dport 22 counter accept

# Permitir ping (echo-request) para diagnóstico:
sudo nft add rule inet filter input icmp type echo-request accept
sudo nft add rule inet filter input icmpv6 type echo-request accept

# Verificar as regras:
sudo nft list chain inet filter input
```

#### ETAPA 5 — Usar sets para gerenciar múltiplos IPs e portas

Os sets nativos do `nftables` permitem agrupar valores sem criar uma regra por elemento:

```bash
# Criar um set de IPs confiáveis (hosts de administração):
sudo nft add set inet filter ips_confiavel \
  '{ type ipv4_addr ; }'

# Adicionar IPs ao set:
sudo nft add element inet filter ips_confiavel \
  '{ 192.168.56.1, 127.0.0.1 }'

# Criar um set de portas de serviço:
sudo nft add set inet filter portas_servico \
  '{ type inet_service ; flags interval ; }'

sudo nft add element inet filter portas_servico \
  '{ 80, 443, 8080 }'

# Criar regras usando os sets:
sudo nft add rule inet filter input \
  ip saddr @ips_confiavel accept

sudo nft add rule inet filter input \
  tcp dport @portas_servico accept

# Verificar os sets:
sudo nft list sets
sudo nft list set inet filter ips_confiavel
```

#### ETAPA 6 — Regras específicas para IPv6

```bash
# Permitir ICMPv6 necessário para funcionamento correto do IPv6
# (Neighbor Discovery, Router Advertisements):
sudo nft add rule inet filter input \
  icmpv6 type { nd-neighbor-solicit, nd-router-advert, nd-neighbor-advert } accept

# Bloquear tráfego IPv6 de origem link-local para portas sensíveis
# (exceto os IPs confiáveis já permitidos):
sudo nft add rule inet filter input \
  ip6 saddr fe80::/10 tcp dport != 22 drop

# Ver regras IPv4 e IPv6 lado a lado:
sudo nft list ruleset
```

#### ETAPA 7 — Verificar counters de monitoramento

```bash
# Fazer algumas conexões SSH e verificar o contador:
ssh aluno@localhost exit 2>/dev/null; true
ssh aluno@localhost exit 2>/dev/null; true

sudo nft list chain inet filter input
# Esperado: "packets X bytes Y" na regra de SSH (counter adicionado na Etapa 4)
```

#### ETAPA 8 — Exportar para arquivo e configurar inicialização automática

```bash
# Exportar o ruleset atual para arquivo de configuração:
sudo sh -c 'nft list ruleset > /tmp/nftables_lab43.conf'
cat /tmp/nftables_lab43.conf

# Verificar a sintaxe do arquivo:
sudo nft -c -f /tmp/nftables_lab43.conf
# Esperado: sem erros (saída vazia = OK)

# Instalar o arquivo como configuração permanente:
sudo cp /tmp/nftables_lab43.conf /etc/nftables.conf

# Habilitar e iniciar o serviço nftables:
sudo systemctl enable --now nftables
sudo systemctl status nftables
# Esperado: active (running)

# Verificar que o ruleset foi carregado:
sudo nft list ruleset
```

#### ETAPA 9 — Testar o ruleset completo

```bash
# Verificar conectividade SSH (deve funcionar):
ssh aluno@localhost exit

# Verificar que portas não autorizadas estão bloqueadas:
nc -zv -w 2 localhost 9999   # deve falhar (timeout)

# Verificar que o serviço persiste após simulação de reload:
sudo systemctl restart nftables
sudo nft list ruleset   # regras devem estar presentes

# Testar proteção IPv6 (se disponível):
ip -6 addr show   # ver endereços IPv6
ping6 ::1         # loopback IPv6 deve funcionar
```

---

### Troubleshooting

| Problema | Solução |
|----------|---------|
| `nft list ruleset` mostra regras residuais de iptables | As regras do wrapper iptables aparecem em tabelas com nome `ip filter`. Limpe com: `sudo iptables -F && sudo iptables -t nat -F` |
| `policy drop` na chain bloqueia o próprio SSH | Ordem importa: adicione a regra de SSH (`tcp dport 22 accept`) **antes** de adicionar regras de DROP. Acesse pelo console do VirtualBox se necessário |
| `nft add element` retorna "No such set" | O set deve ser criado antes com `nft add set`. Verifique: `sudo nft list sets` |
| `systemctl enable nftables` não restaura as regras após reboot | O arquivo `/etc/nftables.conf` deve existir e ter sintaxe válida. Valide com: `sudo nft -c -f /etc/nftables.conf` |
| Regras ICMPv6 `nd-*` causam erro de sintaxe | Sintaxe correta: `icmpv6 type { nd-neighbor-solicit, nd-router-advert, nd-neighbor-advert }` — sem espaço antes de `{` |
| `nft list ruleset` vazio após `systemctl restart nftables` | Verifique o arquivo: `sudo cat /etc/nftables.conf`. Pode estar vazio ou com erro. Reexporte: `sudo sh -c 'nft list ruleset > /etc/nftables.conf'` |

---

### Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| Screenshot: `sudo nft list table inet filter` mostrando chains com `policy drop` (check `nftables_ativo`) | 15 pts |
| Screenshot: regras IPv4 e IPv6 presentes na mesma chain (check `regra_ipv4_ipv6_ok`) | 20 pts |
| Screenshot: `sudo nft list sets` mostrando os sets criados com elementos | 15 pts |
| Screenshot: counter na regra SSH incrementado após conexões | 10 pts |
| Screenshot: `sudo nft -c -f /etc/nftables.conf` sem erros (check `nftables_conf_valido`) | 15 pts |
| Screenshot: `sudo systemctl is-enabled nftables` retornando `enabled` (check `script_inicializacao_ok`) | 15 pts |
| Arquivo `resultado_lab43_<nome>.json` commitado no repositório Git | 10 pts |
| **TOTAL** | **100 pts** |

---

### ✔ Checklist de Entrega — LAB 4.3 (v1.2)

- [ ] Screenshot: `sudo nft list table inet filter` com chains e `policy drop`  (check `nftables_ativo`)
- [ ] Screenshot: regras IPv4 e IPv6 na mesma chain `input`  (check `regra_ipv4_ipv6_ok`)
- [ ] Screenshot: `sudo nft list sets` com os sets criados e seus elementos
- [ ] Screenshot: counter SSH incrementado após conexões de teste
- [ ] Screenshot: `sudo nft -c -f /etc/nftables.conf` sem erros  (check `nftables_conf_valido`)
- [ ] Screenshot: `sudo systemctl is-enabled nftables` → `enabled`  (check `script_inicializacao_ok`)
- [ ] Arquivo `resultado_lab43_<meu_nome>.json` gerado pelo `check_lab43.sh`
- [ ] Arquivo `resultado_lab43_<meu_nome>.json` commitado no repositório Git da turma
- [ ] Respostas das 5 perguntas de fixação

---

### Perguntas de Fixação

Responda em até 4 linhas cada.

**1. Dê um exemplo prático onde um set com 100 IPs bloqueados seria significativamente mais eficiente em `nftables` do que 100 regras individuais em `iptables`. O que muda em termos de performance no kernel?**

**2. Por que no `nftables` é possível proteger IPv4 e IPv6 com uma única regra usando a família `inet`, enquanto no `iptables` são necessários dois comandos separados (`iptables` e `ip6tables`)?**

**3. O que é um "hook" no `nftables` e quais são os hooks disponíveis para a família `inet`? Como a `priority` afeta a ordem de processamento?**

**4. Qual a diferença entre `ct state established,related accept` no `nftables` e `-m state --state ESTABLISHED,RELATED -j ACCEPT` no `iptables`? São funcionalmente equivalentes?**

**5. (Desafio) No Ubuntu 24.04, `iptables` e `nftables` coexistem. Se você criar regras com `iptables` e também com `nft`, qual a ordem de processamento? Pode haver conflito? Como verificar?**

---

## Apêndice A — Relatório de Conclusão de Laboratório

### A.1 Cabeçalho Obrigatório

| Campo | Valor |
|-------|-------|
| **Nome completo** | |
| **Matrícula** | |
| **Lab concluído** | |
| **Data de entrega** | |
| **Versão** | 1.0 |

### A.2 Estrutura do Relatório

O relatório é dividido em quatro seções fixas após o cabeçalho:

**Seção A — Confirmação da Entrega Automática**
Screenshot do terminal mostrando a execução do script `check_labNN.sh` e a mensagem de resultado final (ex.: `5/5 checks passaram — JSON gerado`). Prova que o aluno executou o script pessoalmente e não apenas copiou o arquivo JSON.

**Seção B — Evidências Visuais Sem Correspondente no Script (Canal 2a)**
Screenshots de itens que o script não consegue verificar automaticamente: configurações visíveis apenas na saída de comandos interativos, comportamentos de bloqueio/desbloqueio, banners em tela. Cada placeholder é nomeado `[IMG_<descrição>]`.

**Seção C — Dupla Evidência: Screenshots com Check_ID (Canal 2b)**
Esta é a seção principal. Cada item corresponde a um `check_id` do script. O placeholder inclui o ID do check, o comando executado e um espaço para a imagem.

**Seção D — Respostas às Perguntas de Fixação**
Texto livre. Cada pergunta de fixação do lab tem um espaço numerado no template. Responda em até 4 linhas por pergunta.

### A.3 Convenção de Nomes de Arquivo

| Arquivo | Padrão |
|---------|--------|
| JSON automático | `resultado_lab<NN>_<nome_sem_espacos>.json` |
| Relatório PDF | `lab<NN>_relatorio_<nome_sem_espacos>.pdf` |

### A.4 Estrutura do Repositório Git

```
turma-segdef-2026-1/
└── <nome_sem_espacos>/
    ├── lab31/
    │   ├── resultado_lab31_<nome_sem_espacos>.json
    │   └── lab31_relatorio_<nome_sem_espacos>.pdf
    ├── lab32/  lab33/  lab41/  lab42/  lab43/
    └── ...
```

### A.5 Como Gerar o PDF

1. Preencha todos os campos e cole os screenshots nos placeholders indicados.
2. Busque por `[IMG_` — todo placeholder em branco é item pendente.
3. **Microsoft Word:** Arquivo → Exportar → Criar PDF/XPS.
4. **LibreOffice:** Arquivo → Exportar como PDF...
5. Nomeie conforme a convenção: `lab31_relatorio_joao_pereira.pdf`

### A.6 Passo a Passo de Submissão via Git

```bash
# Substitua joao_pereira pelo seu nome_sem_espacos e 31 pelo número do lab

cd ~/lab31-joao-pereira          # repositório clonado do Classroom

# Copiar os arquivos gerados:
cp ~/resultado_lab31_joao_pereira.json .
cp ~/lab31_relatorio_joao_pereira.pdf  .

git add resultado_lab31_joao_pereira.json lab31_relatorio_joao_pereira.pdf
git commit -m "lab31: entrega joao_pereira"
git push origin main

# Verificar o resultado do autograding:
# Acesse a aba "Actions" do seu repositório no GitHub
# ✅ verde = todos os checks passaram
# ❌ vermelho = algum check falhou — corrija e faça novo push
```

### A.7 Checklist Final do Aluno

Marque todos os itens antes do `git push`:

- [ ] O script `check_labNN.sh` foi executado e exibiu o resultado no terminal
- [ ] O arquivo `resultado_labNN_<meu_nome>.json` existe na pasta `~/`
- [ ] Todos os placeholders `[IMG_` do template foram preenchidos
- [ ] Todos os screenshots estão legíveis e mostram claramente o resultado esperado
- [ ] O PDF foi gerado com o nome correto: `labNN_relatorio_<meu_nome>.pdf`
- [ ] Os dois arquivos (JSON e PDF) estão na pasta correta do repositório
- [ ] `git add` foi executado para os dois arquivos
- [ ] `git commit` foi executado com mensagem padrão: `"labNN: entrega <meu_nome>"`
