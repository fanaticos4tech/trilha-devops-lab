# AWS to Terraform Import Script

Este repositório contém um script em **Bash** que automatiza a importação de recursos da AWS para o Terraform utilizando o [Terraformer](https://github.com/GoogleCloudPlatform/terraformer).

---

## 🎯 Objetivo

Simplificar a importação de múltiplos recursos AWS para o Terraform, gerando automaticamente os arquivos `.tf` e o `terraform.tfstate` correspondente.

---

## 🛠️ Pré-requisitos

* **AWS CLI:** Configurado com perfil e credenciais válidas.
* **Terraform:** Versão mínima recomendada: 1.0. O script criará um `main.tf` temporário e executará `terraform init` para baixar os plugins necessários.
* **Terraformer:** Instalação manual recomendada.

  * **MacOS:** se você tiver [Homebrew](https://brew.sh/), execute:

    ```bash
    brew install terraformer
    ```
  * **Linux:** baixe o binário adequado do [GitHub Releases](https://github.com/GoogleCloudPlatform/terraformer/releases) e mova para o seu `$PATH`:

    ```bash
    curl -LO https://github.com/GoogleCloudPlatform/terraformer/releases/download/<versão>/terraformer-all-linux-amd64
    chmod +x terraformer-all-linux-amd64
    sudo mv terraformer-all-linux-amd64 /usr/local/bin/terraformer
    ```

---

## ⚙️ Configurações

Você pode ajustar as variáveis de ambiente ou editar diretamente o script:

| Variável      | Padrão           | Descrição                                   |
| ------------- | ---------------- | ------------------------------------------- |
| `AWS_PROFILE` | `default`        | Perfil AWS a ser utilizado.                 |
| `AWS_REGION`  | `us-east-1`      | Região AWS para importação.                 |
| `OUTPUT_DIR`  | `tf-import-temp` | Diretório temporário para arquivos gerados. |

---

## 🚀 Uso

1. Clone este repositório ou copie o arquivo `import-aws-terraform.sh` para o diretório raiz do seu projeto Terraform.

2. Dê permissão de execução:

   ```bash
   chmod +x import-aws-terraform.sh
   ```

3. (Opcional) Ajuste perfil e região:

   ```bash
   export AWS_PROFILE=meu-perfil
   export AWS_REGION=eu-central-1
   ```

4. Confira os serviços suportados pelo Terraformer:

   ```bash
   terraformer import aws list
   ```

5. Execute o script:

   ```bash
   ./import-aws-terraform.sh
   ```

Após a execução, os arquivos `.tf` e o `terraform.tfstate` estarão no seu diretório de trabalho. Em seguida, rode:

```bash
terraform init
terraform plan
```

---

## 📝 Script Completo

<details>
<summary>Clique para expandir o script</summary>

```bash
#!/usr/bin/env bash
set -euo pipefail

# -------------------------------------------------------
# Configurações (pode sobrescrever via variável de ambiente)
# -------------------------------------------------------
AWS_PROFILE=${AWS_PROFILE:-default}
AWS_REGION=${AWS_REGION:-us-east-1}
OUTPUT_DIR=${OUTPUT_DIR:-tf-import-temp}
WORK_DIR=$(pwd)

# -------------------------------------------------------
# Lista de serviços AWS para importar (ajuste conforme necessário)
# Use 'terraformer import aws list' para ver todos os serviços suportados
# -------------------------------------------------------
RESOURCES=(
  "ec2"
  "s3"
  "rds"
  "iam"
)

# -------------------------------------------------------
# Checagem de pré-requisitos
# -------------------------------------------------------
command -v aws >/dev/null 2>&1 || { echo "❌ AWS CLI não encontrada. Instale e configure antes."; exit 1; }
command -v terraform >/dev/null 2>&1 || { echo "❌ Terraform não encontrado. Instale antes."; exit 1; }
command -v terraformer >/dev/null 2>&1 || { echo "❌ Terraformer não encontrado. Instale-o manualmente conforme README."; exit 1; }

# -------------------------------------------------------
# Preparar diretório temporário e inicializar Terraform
# -------------------------------------------------------
rm -rf "${WORK_DIR}/${OUTPUT_DIR}"
mkdir -p "${WORK_DIR}/${OUTPUT_DIR}"
cd "${WORK_DIR}/${OUTPUT_DIR}"

# Criar main.tf temporário para baixar o provider AWS
echo "terraform {" > main.tf
cat <<EOF >> main.tf
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region  = "${AWS_REGION}"
  profile = "${AWS_PROFILE}"
}
EOF

echo "🚀 Inicializando Terraform para baixar provider AWS..."
terraform init -upgrade -input=false -no-color

# -------------------------------------------------------
# Importar cada serviço com Terraformer
# -------------------------------------------------------
for service in "${RESOURCES[@]}"; do
  echo "🚀 Importando serviço: ${service}..."
  terraformer import aws \
    --resources="${service}" \
    --regions="${AWS_REGION}" \
    --profile="${AWS_PROFILE}" \
    --connect=true \
    --output="$(pwd)" || echo "⚠️ Falha ao importar ${service}, pulando."
done

# -------------------------------------------------------
# Mover .tf e state para o diretório do projeto
# -------------------------------------------------------
echo "📦 Movendo arquivos gerados para: ${WORK_DIR}"
if compgen -G "aws/*.tf" > /dev/null; then
  mv aws/*.tf "${WORK_DIR}/"
  mv aws/terraform.tfstate* "${WORK_DIR}/"
else
  echo "⚠️ Nenhum arquivo .tf gerado." 
fi

# Limpa temporários
echo "✅ Importação concluída!"
rm -rf aws
rm main.tf
rm .terraform.lock.hcl 2>/dev/null || true
rm -rf .terraform
cd "${WORK_DIR}"

echo "👉 Agora:
     terraform init
     terraform plan"
```

</details>

---

## 💡 Dicas

* Use `terraformer import aws list` para ver todos os serviços suportados e ajustar `RESOURCES` conforme sua necessidade.
* Para importar de múltiplas regiões, você pode executar o script em diferentes valores de `AWS_REGION` ou adaptar o loop.

---

## 📄 Licença

MIT © Rodrigo Marins Piaba - @fanaticos4tech
