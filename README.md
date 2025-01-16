# Deploy

Este repositório contém um projeto desenvolvido para realizar o deploy de uma aplicação web utilizando Python, HTML e CSS.  
O objetivo do projeto é demonstrar como configurar e implantar uma aplicação simples com dependências específicas e uma estrutura organizada.  

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para a lógica do back-end.  
- **Flask**: Framework utilizado para criar a aplicação web.  
- **HTML**: Utilizado para a estruturação das páginas web.  
- **CSS**: Responsável pela estilização das páginas web.  
- **Gunicorn**: Servidor WSGI usado para deploy de aplicações Python.  

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.  
Para instalar todas as dependências necessárias, execute:  

```bash
pip install -r requirements.txt
```

### Dependências principais:

- Flask  
- Gunicorn  

## Como Executar o Projeto

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/gabriela-data/Deploy.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd Deploy
   ```

3. Instale as dependências conforme mencionado acima.

4. Inicie a aplicação localmente para testes:

   ```bash
   python app.py
   ```

5. Acesse [http://localhost:5000](http://localhost:5000) no seu navegador para visualizar a aplicação.

### Deploy com Gunicorn:

Caso deseje realizar o deploy com Gunicorn, execute o seguinte comando:

```bash
gunicorn app:app
```

## Estrutura do Projeto

- **app.py**: Arquivo principal que contém a lógica do back-end.
- **templates/**: Diretório que contém os arquivos HTML para renderização das páginas.
- **static/**: Diretório que contém os arquivos CSS e outros recursos estáticos como imagens.
- **requirements.txt**: Arquivo com as dependências do projeto.
- **Procfile**: Arquivo de configuração para deployment em plataformas como Heroku.

## Deployment

Este projeto foi configurado para ser facilmente implantado em plataformas de hospedagem como Heroku ou outros serviços compatíveis com Python.

### Configuração do Procfile

O arquivo `Procfile` inclui as configurações para rodar o servidor Gunicorn:

```
web: gunicorn app:app
```

Certifique-se de configurar as variáveis de ambiente e o runtime corretamente para o deploy.

## Contribuição

Contribuições são bem-vindas!  
Se você encontrar algum problema ou quiser propor melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
