# Plano SaaS Agenda Facil

Atualizado em: 2026-06-15

## Objetivo

Transformar o Agenda Facil em um SaaS multi-saloes para o Brasil, inicialmente gratuito, onde cada salao consegue se cadastrar, configurar sua operacao, receber agendamentos online e gerenciar clientes, profissionais, servicos, agenda, caixa e relatorios.

No futuro, a plataforma tera um painel administrativo interno para acompanhar saloes, planos, uso, pagamentos e continuidade de assinatura.

## Decisoes De Produto

- [x] MVP com todos os saloes em plano gratuito.
- [x] Usar Supabase como base de dados/autenticacao.
- [x] Cada salao deve ter dados isolados dos outros saloes.
- [x] Manter link publico por salao usando slug.
- [x] Preparar estrutura para planos pagos no futuro.
- [x] Trocar todo o produto para Brasil: idioma, formatos, moeda, telefone e localizacao.
- [x] Capturar localizacao/endereco do salao no cadastro.
- [x] Mostrar rota/localizacao do salao antes da cliente seguir para o agendamento.
- [ ] Criar painel admin da plataforma para acompanhar contas e planos.

## Padrao Brasil

- [x] Moeda padrao: Real brasileiro.
- [x] Formato monetario: `pt-BR`, `BRL`, exemplo `R$ 120,00`.
- [x] Trocar simbolos e textos que usam euro por real.
- [x] Revisar todos os textos em portugues europeu para portugues brasileiro.
- [x] Telefone padrao: Brasil, com suporte a celular/WhatsApp.
- [x] Datas e horarios: `pt-BR`, timezone inicial `America/Sao_Paulo`.
- [x] Campos de endereco compatíveis com Brasil: CEP, rua, numero, complemento, bairro, cidade, estado, pais.

## Cadastro De Salao

Fluxo desejado:

- [x] Usuario acessa "Criar conta".
- [x] Informa nome da responsavel.
- [x] Informa email.
- [x] Informa senha.
- [x] Informa nome do salao.
- [x] Informa WhatsApp/telefone do salao.
- [x] Informa localizacao/endereco.
- [x] Aceita usar a localizacao do navegador, se quiser.
- [x] Sistema tenta preencher automaticamente cidade, estado e pais quando houver permissao/localizacao.
- [x] Sistema tenta preencher dados pelo CEP quando o CEP for informado.
- [x] Conta e criada como administradora do salao.
- [x] Salao entra automaticamente no plano `free`.
- [x] Sistema cria configuracoes iniciais do salao, slug publico, servicos padrao e profissional inicial.

Dados minimos escolhidos pelo cliente:

- [x] Nome da responsavel.
- [x] Email.
- [x] Senha.
- [x] Nome do salao.
- [x] WhatsApp/telefone.
- [x] CEP ou localizacao.

Dados que podemos tentar preencher automaticamente:

- [x] Cidade.
- [x] Estado.
- [x] Pais.
- [x] Latitude e longitude.
- [x] Timezone aproximado.
- [x] Endereco a partir do CEP.
- [x] Slug publico baseado no nome do salao.
- [x] Dados de auditoria: data de cadastro, origem, plano inicial, status.

## Fluxo Publico De Agendamento

Fluxo desejado para a cliente:

- [x] Cliente abre o link publico do salao.
- [x] Sistema carrega dados do salao pelo `public_slug`.
- [x] Sistema mostra nome, endereco resumido e opcao de ver rota.
- [x] Cliente pode tocar em "Ver rota" antes de escolher o horario.
- [x] Rota abre em Google Maps/Waze/Apple Maps quando possivel.
- [x] Depois de conferir a rota, cliente segue para escolher servico.
- [x] Cliente escolhe profissional.
- [x] Cliente escolhe data e horario.
- [x] Cliente informa nome e WhatsApp.
- [x] Cliente confirma o agendamento.

Regras:

- [x] A rota deve usar latitude/longitude quando existir.
- [x] Se nao houver coordenadas, usar endereco completo formatado.
- [x] Se nao houver endereco, esconder botao de rota e seguir com agendamento normal.
- [x] A rota deve abrir em nova aba/app externo para nao perder o fluxo.
- [x] Ao voltar, a cliente continua no mesmo passo do agendamento.
- [x] O salao deve poder conferir/editar endereco nas configuracoes.

## Banco De Dados

Estado atual observado:

- [x] Tabelas principais usam `user_id` como dono do salao.
- [x] Existe `business_settings` por salao.
- [x] Existe `public_slug` para agendamento publico.
- [x] Existe `user_roles` com `admin` e `staff`.
- [x] Existe `salon_owner_id` para funcionarias.
- [x] RLS esta ativo em tabelas principais.

Melhorias recomendadas para SaaS:

- [ ] Criar tabela `salons` no futuro para separar tenant de usuario.
- [ ] Enquanto isso, tratar `business_settings.user_id` como `salon_owner_id`.
- [x] Criar tabela `salon_subscriptions`.
- [x] Criar tabela `platform_plans`.
- [ ] Criar papel `platform_admin` separado da administradora do salao.
- [x] Adicionar campos de localizacao em `business_settings` ou tabela propria `salon_locations`.
- [x] Garantir que toda mutation de staff grave dados no `salonOwnerId`, nao no `auth.uid()`.

Campos sugeridos para localizacao:

```sql
postal_code text,
street text,
street_number text,
complement text,
neighborhood text,
city text,
state text,
country text default 'BR',
latitude numeric,
longitude numeric,
timezone text default 'America/Sao_Paulo'
```

Campos sugeridos para assinatura:

```sql
plan_code text default 'free',
status text default 'active',
started_at timestamptz default now(),
current_period_ends_at timestamptz,
cancel_at timestamptz,
notes text
```

## Sequencia De Implementacao

- [x] Revisar acesso ao Supabase.
- [x] Confirmar que o build roda.
- [x] Identificar arquitetura atual multi-salao.
- [x] Criar/atualizar documentos `plano.md` e `AGENTS.md`.
- [x] Ajustar helper de moeda para Real brasileiro.
- [x] Trocar simbolos `€` por formatador BRL.
- [x] Revisar telas que exibem precos e totais.
- [x] Ajustar cadastro para pedir nome do salao.
- [x] Ajustar cadastro para pedir telefone/WhatsApp.
- [x] Ajustar cadastro para pedir CEP/endereco.
- [x] Adicionar opcao de usar localizacao do navegador.
- [x] Adicionar etapa/opcao de "Ver rota" no fluxo publico antes do agendamento.
- [x] Criar helper para gerar links de rota por coordenadas ou endereco.
- [x] Preencher cidade/estado automaticamente via reverse geocoding (cadastro e perfil).
- [x] Criar migration para campos de localizacao do salao.
- [x] Criar funcao/fluxo para preencher endereco via CEP.
- [x] Criar plano `free` no banco.
- [x] Criar assinatura inicial automatica ao cadastrar salao.
- [x] Ajustar mutations para usarem `salonOwnerId`.
- [x] Remover fallback automatico de salao em `/agendar` sem slug.
- [x] Criar tela simples de onboarding pos-cadastro.
- [x] Criar base do admin interno da plataforma.
- [x] Criar relatorio de saloes cadastrados no admin interno.
- [x] Criar controles manuais de plano/status no admin interno.
- [x] Rodar build e corrigir erros.
- [ ] Rodar lint e decidir se sera corrigido por etapas.

## Admin Interno Futuro

Objetivo: permitir que a equipe da plataforma acompanhe o SaaS.

- [x] Papel `platform_admin` separado (tabela `platform_admins` + RPCs `is_current_user_platform_admin`, `admin_list_salons`, `admin_update_subscription`).
- [x] Lista de saloes em `/admin`.
- [x] Busca por nome, email, cidade, estado e slug.
- [x] Visualizar responsavel, data de cadastro, slug publico e volume basico de uso (clientes/agendamentos).
- [x] Ver plano atual.
- [x] Alterar plano manualmente (free/pro).
- [x] Pausar/reativar salao.
- [x] Ver metricas mais completas: faturamento registrado, profissionais ativos.
- [ ] Preparar integracao de pagamentos no futuro.
- [ ] Login/rota `/admin` ainda usa o mesmo login do salao — avaliar fluxo dedicado se necessario.

## Cuidados

- [ ] Nunca expor `SUPABASE_SERVICE_ROLE_KEY` no cliente.
- [ ] Rotas server que usam admin precisam da service role configurada no ambiente.
- [ ] Manter RLS como barreira principal de isolamento.
- [ ] Testar sempre admin e staff separadamente.
- [ ] Evitar consultas anonimas diretas em tabelas sensiveis.
- [ ] Agendamento publico deve passar por RPCs controladas.
- [ ] Dados de localizacao exigem consentimento quando vierem do navegador.

## Proximas Acoes Imediatas

- [x] Implementar formatador BRL central em `src/lib/format.ts`.
- [x] Substituir exibicoes manuais de preco por esse formatador.
- [x] Atualizar signup para capturar nome do salao, telefone e localizacao.
- [x] Criar migration de localizacao e assinatura free.
- [x] Preencher cidade/estado automaticamente via geolocalizacao (reverse geocoding) no cadastro e no perfil.
- [x] Criar base do admin interno da plataforma (rota `/admin`, papel `platform_admin`, listagem de saloes e planos).
- [x] Criar conta de teste `rodrigoexer1@gmail.com` (senha em `ADMIN_TEST_PASSWORD` no `.env`) para validar login e admin.
- [x] Criar monitoramento de acessos: migration `20260615170000_access_logs.sql`, endpoint `/api/geo`, lib `accessTracking.ts`, integracao em `auth.tsx`/`__root.tsx`/`agendar.tsx`, pagina `/admin/atividade`.

### PENDENTE - aplicar migrations manualmente no Supabase Dashboard (SQL Editor)

O assistente nao tem SUPABASE_SERVICE_ROLE_KEY. O usuario precisa rodar estas
migrations no painel do Supabase -> SQL Editor, **nesta ordem**:

1. `supabase/migrations/20260615120000_add_brazil_saas_signup_fields.sql`
2. `supabase/migrations/20260615143000_update_audit_summary_brazil.sql`
3. `supabase/migrations/20260615150000_platform_admin.sql`
4. `supabase/migrations/20260615170000_access_logs.sql`

Apos isso: login em `/admin` com `rodrigoexer1@gmail.com` (senha: `ADMIN_TEST_PASSWORD`
do `.env`) vai funcionar, e a tabela `access_logs` vai comecar a receber dados.

- [ ] Validar cadastro completo criando um salao novo.
- [ ] Rodar lint e decidir se sera corrigido por etapas.
