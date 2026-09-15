# 💱 Conversor de Moedas em Python

Um aplicativo desktop desenvolvido em Python para cotação e conversão de moedas em tempo real, com interface gráfica amigável e integração de dados cambiais.

---

## 📌 Sobre o Projeto

O **Conversor de Moedas** permite ao usuário consultar taxas de câmbio atualizadas e converter valores entre diversas moedas globais (como Real brasileiro, Dólar americano, Euro, entre outras). A aplicação consome e processa listagens de moedas e pares de conversão, oferecendo rapidez e precisão nas consultas.

---

## 🚀 Funcionalidades

- **Consulta Dinâmica de Moedas**: Lista de moedas e pares de conversão suportados atualizados.
- **Conversão em Tempo Real**: Cálculo imediato da taxa de câmbio atualizada para o par selecionado.
- **Interface Intuitiva**: Janela interativa para seleção de moeda de origem, moeda de destino e inserção de valores.
- **Cache Local de Metadados**: Armazenamento e leitura de formatos suportados através de arquivos XML (`moedas.xml` e `conversoes.xml`).

---

## 📁 Estrutura de Arquivos

```plaintext
Conversor_moeda/
├── main.py              # Ponto de entrada da aplicação e interface gráfica (GUI)
├── pegar_moedas.py      # Módulo de requisição e processamento de moedas e taxas
├── conversoes.xml       # Registro dos pares de conversão aceitos pela aplicação
├── moedas.xml           # Lista de moedas suportadas com suas nomenclaturas/códigos
└── requirements.txt     # Dependências e bibliotecas externas necessárias
```

---

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- **Interface Gráfica**: Tkinter / CustomTkinter
- **Manipulação de Dados**: `xml.etree.ElementTree` / `xmltodict`
- **Requisições HTTP**: `requests` (para integração com APIs cambiais)

---

## ⚙️ Pré-requisitos

Certifique-se de ter o **Python 3.10** ou superior instalado em sua máquina. Você pode verificar executando:

```bash
python --version
```

---

## 📦 Como Instalar e Rodar

1. **Clone ou baixe o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Conversor_moeda.git
   cd Conversor_moeda
   ```

2. **(Opcional, mas recomendado) Crie e ative um ambiente virtual:**
   - **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   python main.py
   ```

---

## 💡 Como Usar

1. Ao abrir o programa, selecione a **moeda de origem** (a moeda que você possui).
2. Escolha a **moeda de destino** (a moeda para a qual deseja converter).
3. Insira o valor desejado no campo numérico.
4. Clique no botão de conversão para obter o total convertido e a cotação utilizada.

---

## 📈 Melhorias Futuras

- [ ] Implementação de gráfico com histórico de variação cambial dos últimos 30 dias.
- [ ] Alternância de temas (Modo Claro / Modo Escuro).
- [ ] Notificações de alerta quando uma moeda atingir determinado patamar de preço.
- [ ] Suporte a conversão de criptomoedas populares (BTC, ETH, etc.).

---

## 📝 Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes (se aplicável).
