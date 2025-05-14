# trilha-devops-lab
Laboratório do Treinamento A Trilha DevOps

# A Trilha DevOps - Laboratório Prático Completo

Bem-vindo ao laboratório prático "A Trilha DevOps"! Este projeto foi desenhado para fornecer uma experiência hands-on na construção de uma infraestrutura e pipeline de CI/CD do zero, utilizando ferramentas DevOps modernas com foco na AWS.

Este README detalha a estrutura do projeto, as tecnologias utilizadas, e como configurar e executar cada parte do laboratório.

## Sobre o Laboratório

Este laboratório simula a criação de uma infraestrutura para uma aplicação web, desde o provisionamento da infraestrutura na AWS com Terraform, passando pela containerização com Docker, até a automação do build, teste e deploy com GitHub Actions. O objetivo é que, ao final, os alunos tenham uma compreensão prática de como essas ferramentas se integram para formar um pipeline DevOps robusto.

## Tecnologias Utilizadas

*   **AWS (Amazon Web Services):** Plataforma de nuvem onde a infraestrutura será provisionada (ex: VPC, EC2, S3, ECR, ECS/EKS, IAM).
*   **Terraform:** Ferramenta de Infraestrutura como Código (IaC) para definir e provisionar a infraestrutura na AWS de forma declarativa e versionada.
*   **Docker:** Plataforma de containerização para empacotar a aplicação e suas dependências, garantindo consistência entre ambientes.
*   **GitHub:** Plataforma de hospedagem de código e controle de versão (Git).
*   **GitHub Actions:** Ferramenta de CI/CD integrada ao GitHub para automatizar workflows de build, teste e deploy.
*   **Selenium (Opcional/Avançado):** Ferramenta para automação de testes de interface de usuário (UI), que pode ser integrada ao pipeline de CI/CD.
*   **Shell Script (Bash):** Utilizado para scripts auxiliares e automação de tarefas.
*   **Python:** Pode ser utilizado para scripts de automação ou para a aplicação de exemplo.

## Estrutura do Projeto (Exemplo Sugerido)

```
trilha-devops-lab/
├── .github/                    # Configurações do GitHub
│   └── workflows/              # Workflows do GitHub Actions
│       ├── ci-pipeline.yml     # Pipeline principal de CI (Build, Test)
│       └── cd-pipeline.yml     # Pipeline de CD (Deploy)
├── terraform/                  # Código Terraform para provisionamento da infraestrutura
│   ├── modules/                # Módulos Terraform reutilizáveis (ex: vpc, ec2, ecs)
│   │   ├── vpc/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   └── outputs.tf
│   │   └── ...                 # Outros módulos
│   ├── environments/           # Configurações específicas por ambiente (ex: dev, prod)
│   │   ├── dev/
│   │   │   ├── main.tf
│   │   │   ├── terraform.tfvars
│   │   │   └── backend.tf      # Configuração do backend state do Terraform
│   │   └── prod/
│   │       └── ...             # Configurações de produção
│   └── main.tf                 # Arquivo Terraform raiz (pode chamar módulos)
│   └── variables.tf
│   └── outputs.tf
│   └── versions.tf             # Versões de providers e do Terraform
├── app/                        # Código da aplicação de exemplo
│   ├── src/                    # Código fonte da aplicação (ex: Python/Flask, Node.js/Express)
│   │   └── ...
│   ├── Dockerfile              # Instruções para construir a imagem Docker da aplicação
│   ├── requirements.txt        # Dependências da aplicação (se Python)
│   └── ...                     # Outros arquivos da aplicação
├── scripts/                    # Scripts auxiliares (Bash, Python)
│   ├── setup_env.sh            # Script para configurar ambiente local
│   └── run_tests.sh            # Script para executar testes
├── tests/                      # Testes automatizados
│   ├── unit/                   # Testes unitários da aplicação
│   └── e2e/                    # Testes End-to-End (ex: com Selenium)
│       └── selenium_tests.py
├── .gitignore                  # Especifica arquivos e diretórios a serem ignorados pelo Git
└── README.md                   # Este arquivo :)
```

### Descrição dos Principais Diretórios e Arquivos

*   **`.github/workflows/`**: Contém os arquivos YAML que definem os pipelines de CI/CD usando GitHub Actions.
    *   `ci-pipeline.yml`: Define o fluxo para build da aplicação, execução de testes unitários e de integração, e possivelmente a construção da imagem Docker.
    *   `cd-pipeline.yml`: Define o fluxo para deploy da aplicação em diferentes ambientes (ex: desenvolvimento, produção) após a aprovação do CI.
*   **`terraform/`**: Raiz do código de Infraestrutura como Código.
    *   `terraform/modules/`: Subdiretórios para cada módulo Terraform reutilizável (ex: um módulo para criar uma VPC, outro para um cluster ECS, etc.). Cada módulo tem seus próprios `main.tf`, `variables.tf`, e `outputs.tf`.
    *   `terraform/environments/`: Configurações específicas para cada ambiente (desenvolvimento, homologação, produção). Cada ambiente terá seu próprio `main.tf` (que instancia os módulos com variáveis específicas do ambiente), `terraform.tfvars` (para valores de variáveis), e `backend.tf` (para configurar onde o estado do Terraform será armazenado remotamente, ex: S3).
    *   `terraform/versions.tf`: Especifica as versões do Terraform e dos providers (ex: AWS) a serem utilizados, garantindo consistência.
*   **`app/`**: Contém o código fonte da aplicação de exemplo que será containerizada e implantada.
    *   `Dockerfile`: Define como construir a imagem Docker da aplicação, incluindo o sistema operacional base, dependências, cópia do código fonte e como executar a aplicação.
    *   `requirements.txt` (ou `package.json`, etc.): Lista as dependências da linguagem de programação da aplicação.
*   **`scripts/`**: Scripts utilitários para automação de tarefas comuns, como configuração de ambiente local, execução de testes, etc.
*   **`tests/`**: Contém os diferentes tipos de testes automatizados.
    *   `unit/`: Testes que verificam pequenas unidades de código da aplicação isoladamente.
    *   `e2e/`: Testes que simulam o fluxo completo do usuário através da aplicação (ex: usando Selenium para testar a interface web).
*   **`.gitignore`**: Arquivo crucial para evitar que arquivos desnecessários ou sensíveis (como arquivos de estado local do Terraform, dependências baixadas, logs, segredos) sejam commitados no repositório.

## Pré-requisitos para Executar o Laboratório

Antes de começar, garanta que você tem as seguintes ferramentas instaladas e configuradas em sua máquina local:

1.  **Conta AWS:** Com permissões adequadas para criar os recursos necessários (IAM, VPC, EC2, S3, ECR, ECS/EKS, etc.).
2.  **AWS CLI:** Instalado e configurado com suas credenciais AWS. ([Guia de Instalação](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))
3.  **Terraform:** Instalado. ([Guia de Instalação](https://learn.hashicorp.com/tutorials/terraform/install-cli))
4.  **Git:** Instalado. ([Guia de Instalação](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
5.  **Docker Desktop (ou Docker Engine no Linux):** Instalado e rodando. ([Guia de Instalação](https://docs.docker.com/get-docker/))
6.  **GitHub CLI (gh) (Opcional, mas recomendado):** Para interagir com o GitHub via linha de comando. ([Guia de Instalação](https://cli.github.com/))
7.  **Editor de Código:** Como VS Code, Sublime Text, Atom, etc.
8.  **Python (se a aplicação de exemplo ou scripts usarem):** Instalado.
9.  **Navegador Web Moderno:** Para acessar a aplicação e o console AWS.

## Como Configurar e Executar o Laboratório

Este laboratório é progressivo. Siga as sessões na ordem proposta.

### 1. Clonar o Repositório

```bash
git clone https://github.com/SEU_USUARIO/trilha-devops-lab.git
cd trilha-devops-lab
```
*(Substitua `SEU_USUARIO` pelo seu nome de usuário no GitHub se você for fazer um fork)*

### 2. Configuração Inicial do Ambiente

*   Verifique se suas credenciais AWS CLI estão configuradas corretamente (`aws configure`).
*   Pode haver um script em `scripts/setup_env.sh` para ajudar a configurar variáveis de ambiente ou outras dependências locais. Consulte-o se existir.

### 3. Provisionamento da Infraestrutura com Terraform

1.  **Navegue até o diretório do ambiente Terraform desejado:**
    ```bash
    cd terraform/environments/dev
    ```
2.  **Inicialize o Terraform:** (Baixa os providers e configura o backend)
    ```bash
    terraform init
    ```
3.  **Planeje as mudanças na infraestrutura:** (Mostra o que o Terraform fará)
    ```bash
    terraform plan
    ```
    *Revise o plano cuidadosamente.*
4.  **Aplique as mudanças na infraestrutura:** (Cria os recursos na AWS)
    ```bash
    terraform apply
    ```
    *Confirme com `yes` quando solicitado.*

### 4. Construção e Teste da Aplicação (Localmente)

1.  **Navegue até o diretório da aplicação:**
    ```bash
    cd ../../../app  # Voltando para a raiz do projeto e entrando em app/
    ```
2.  **Construa a imagem Docker:**
    ```bash
    docker build -t minha-aplicacao-devops:latest .
    ```
3.  **Execute os testes unitários (se aplicável):**
    *Pode haver um comando específico ou um script em `scripts/run_tests.sh`.*
4.  **Execute a aplicação localmente usando Docker (para teste):**
    ```bash
    docker run -d -p 8080:PORTA_DA_APP minha-aplicacao-devops:latest
    ```
    *(Substitua `PORTA_DA_APP` pela porta que sua aplicação expõe dentro do container, ex: 5000 para Flask)*
    *Acesse `http://localhost:8080` no seu navegador.*

### 5. Configurando o Pipeline de CI/CD com GitHub Actions

1.  **Segredos do GitHub:**
    *   No seu repositório GitHub, vá em `Settings` > `Secrets and variables` > `Actions`.
    *   Adicione os segredos necessários para os workflows, como:
        *   `AWS_ACCESS_KEY_ID`: Sua chave de acesso AWS.
        *   `AWS_SECRET_ACCESS_KEY`: Sua chave secreta AWS.
        *   `AWS_REGION`: A região AWS onde os recursos serão implantados (ex: `us-east-1`).
        *   `ECR_REGISTRY`: O URI do seu Amazon ECR (ex: `ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com`).
2.  **Revise os Workflows:**
    *   Analise os arquivos em `.github/workflows/` (`ci-pipeline.yml`, `cd-pipeline.yml`) para entender os passos de cada pipeline.
3.  **Faça um Push para o GitHub:**
    *   Adicione suas alterações, faça commit e dê push para o branch principal (ou um branch de feature para testar o PR).
        ```bash
        git add .
        git commit -m "Configura pipeline inicial de CI/CD"
        git push origin main
        ```
    *   Isso deve disparar o workflow de CI no GitHub Actions. Acompanhe a execução na aba "Actions" do seu repositório.

### 6. Testes End-to-End com Selenium (Opcional/Avançado)

*   Se os testes E2E com Selenium estiverem configurados, eles podem ser parte do pipeline de CI ou executados separadamente.
*   Os scripts de teste estariam em `tests/e2e/`.

## Limpando os Recursos (Destruindo a Infraestrutura)

**Importante:** Para evitar custos inesperados na AWS, lembre-se de destruir a infraestrutura criada pelo Terraform quando não precisar mais dela.

1.  **Navegue até o diretório do ambiente Terraform:**
    ```bash
    cd terraform/environments/dev
    ```
2.  **Destrua a infraestrutura:**
    ```bash
    terraform destroy
    ```
    *Confirme com `yes` quando solicitado.*

## Contribuindo

Se este fosse um projeto colaborativo, aqui estariam as diretrizes de contribuição. Para este laboratório, sinta-se à vontade para experimentar e modificar o código.

## Solução de Problemas Comuns

*   **Erros de Permissão AWS:** Verifique se suas credenciais AWS CLI têm as políticas IAM necessárias.
*   **Falhas no `terraform apply`:** Leia atentamente a mensagem de erro do Terraform. Muitas vezes, ela indica o problema (ex: nome de recurso já existe, cota excedida, dependência faltando).
*   **Falhas no Build do Docker:** Verifique a sintaxe do seu `Dockerfile` e se todas as dependências estão corretas.
*   **Falhas no GitHub Actions:** Abra o log do workflow na aba "Actions" do GitHub para ver detalhes do erro.

---


