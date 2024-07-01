# Bot de Automação para MathTrainer.ai

Este é um bot desenvolvido em Python utilizando Selenium para automatizar interações no site MathTrainer.ai. O bot realiza as seguintes funcionalidades:

- Resolve automaticamente problemas matemáticos exibidos na interface.
- Envia respostas automaticamente para os problemas apresentados.

## Como Usar

1. **Instalação:**
   - Certifique-se de ter o Python e o Selenium instalados no seu ambiente.
   
2. **Configuração:**
   - Baixe o arquivo `mathtrainer_bot.py` deste repositório.
   - Instale o Selenium via pip, se ainda não o tiver instalado:
     ```
     pip install selenium
     ```
   - Certifique-se de ter o WebDriver correto para o navegador de sua escolha (por exemplo, ChromeDriver para Google Chrome).
   - Abra o arquivo `mathtrainer_bot.py` e ajuste o caminho do driver do Selenium para o navegador de sua preferência, caso necessário.
   - Substitua `'SeuNome'` na linha `nome_usuario = "SeuNome"` pelo seu nome de usuário no MathTrainer.ai.

3. **Execução:**
   - Execute o script `mathtrainer_bot.py`:
     ```
     python mathtrainer_bot.py
     ```
   - O bot abrirá o navegador, acessará o MathTrainer.ai e começará a resolver problemas matemáticos automaticamente.

4. **Como Parar o Script:**
   - Pressione `F9` a qualquer momento para encerrar o script manualmente.

## Contribuição

Este projeto foi desenvolvido por pura diversão e como uma ferramenta experimental para praticar a automação de exercícios matemáticos no MathTrainer.ai. Por isso, não espere que esteja completamente funcional ou pronto para uso em produção.
