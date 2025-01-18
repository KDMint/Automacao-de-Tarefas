# 📊 **Automatização de Cadastro de Produtos**

Este projeto automatiza o processo de cadastro de produtos em um sistema web utilizando **Python** e a biblioteca **PyAutoGUI**. O objetivo é preencher rapidamente os campos de cadastro com os dados de um arquivo CSV contendo informações sobre os produtos.

---

## 📝 **Descrição**

Este projeto utiliza **PyAutoGUI** para controlar o mouse e o teclado e preencher os campos de um formulário web automaticamente com os dados de um arquivo CSV. Ele foi desenvolvido para otimizar o processo de cadastro de múltiplos produtos, minimizando o tempo gasto com preenchimento manual.

### 📁 **Arquivos principais**
- **`codigo.py`**: Script principal que automatiza o processo de login, acesso ao formulário e preenchimento de dados de produtos.
- **`auxiliar.py`**: Script para auxiliar na obtenção das coordenadas de tela (X, Y) para o clique nos campos.
- **`produtos.csv`**: Arquivo CSV contendo os dados dos produtos a serem cadastrados. Cada linha contém informações como código, marca, tipo, categoria, preço unitário, custo e observações.

---

## 🛠️ **Ferramentas e Bibliotecas**
- **PyAutoGUI**: Biblioteca para automação do controle do mouse e teclado.
- **Pandas**: Biblioteca para manipulação e leitura do arquivo CSV.
- **Time**: Usado para adicionar pausas entre as ações e garantir o tempo necessário para os processos.
  
---

## 🚀 **Como usar**

### ✅ **Pré-requisitos**
1. **Instale o Python**: Verifique se o Python está instalado em seu sistema.
2. **Instale as dependências**:
    ```bash
    pip install pyautogui pandas openpyxl
    ```

### ▶️ **Executando o projeto**

1. **Configure as posições na tela**:
   - Antes de rodar o script principal, execute o **`auxiliar.py`**. Isso abrirá uma janela para que você consiga identificar as coordenadas (X, Y) dos campos que precisam ser preenchidos no formulário.
   - Execute o **`auxiliar.py`** e anote as coordenadas de cada campo de input.

2. **Preencha o arquivo CSV (`produtos.csv`)** com as informações dos produtos. O arquivo deve conter as seguintes colunas:
    - `codigo`: Código do produto.
    - `marca`: Marca do produto.
    - `tipo`: Tipo do produto.
    - `categoria`: Categoria do produto.
    - `preco_unitario`: Preço unitário do produto.
    - `custo`: Custo do produto.
    - `obs`: Observação adicional sobre o produto (opcional).

3. **Execute o script principal**:
    - Abra o terminal, navegue até a pasta do projeto e execute o **`codigo.py`**:
    ```bash
    python codigo.py
    ```
    - O script irá:
        - Abrir o navegador e acessar a página de login.
        - Fazer o login com as credenciais fornecidas.
        - Preencher os campos de cadastro com os dados extraídos do arquivo CSV.
        - Submeter o formulário para cada produto da lista.

---

## 📬 **Contato**

Para dúvidas ou sugestões, entre em contato via:
- **E-mail**: khadijalima2005@gmail.com

---

## 📜 **Licença**
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

💡 **Nota**: Certifique-se de que as coordenadas de clique estão corretamente ajustadas para o seu ambiente antes de rodar o script. As pausas podem ser ajustadas para garantir que os processos sejam executados corretamente.

