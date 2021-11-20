#  Pós UTFPR- tarefa 04 da matéria de PY.2021-2.M2.OOUML
## PY.2021-2.M2.OOUML(Orientação a Objetos em Python e Ferramentas UML)

👋 Olá, Seja Bem-vindo(a) ao 'Pós UTFPR- tarefa 04 da matéria de PY.2021-2.M2.OOUML'.

## Sobre o projeto:

Utilizamos docker para rodar o script.

### Permissões de arquivos:

Ao se criar arquivos dentro do contâiner Docker o proprietário para edição se torna o contêiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

# Referências utilizadas

[1° Conteinerização de scripts em Python](https://github.com/claudimf/containerized_python)