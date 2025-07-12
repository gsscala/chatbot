## Chatbot Nutricional com Rasa + Docker

Este projeto utiliza o framework [Rasa](https://rasa.com/) para criar um chatbot nutricional, com todas as dependências configuradas em um ambiente Docker baseado em Python 3.10.14.

---

### Como *dar build* no Docker (criar imagem)

O comando abaixo cria a imagem Docker que contém o ambiente completo (Python, Rasa, dependências etc.):

```bash
docker build -t chatbot-rasa .
```

Explicando o comando:

* `docker build`: comando do Docker que constrói a imagem.
* `-t chatbot-rasa`: dá o nome `chatbot-rasa` para a imagem gerada.
* `.` (ponto): indica que o `Dockerfile` está no diretório atual.

Obs: a primeira vez pode demorar, pois o Docker baixa a imagem base e instala mais de 100 dependências.

---

### Como rodar o container com o chatbot

```bash
docker run -p 5005:5005 -it chatbot-rasa
```

Explicando o comando:

* `docker run`: executa a imagem criada.
* `-p 5005:5005`: mapeia a porta do container (5005, onde o Rasa escuta) para a porta 5005 do seu computador.
* `-it`: modo interativo com terminal.
* `chatbot-rasa`: nome da imagem criada no passo anterior.

---

### Se quiser montar seu diretório local (opcional)

Se o código estiver no seu computador e você quiser que ele rode dentro do container (útil no desenvolvimento), adicione `-v`:

```bash
docker run -p 5005:5005 -v $(pwd):/app -it chatbot-rasa
```

---

### Guia rápido para quem nunca usou Docker

Se você nunca usou Docker, siga estes passos:

1. Instalar o Docker:

   * [Instalar no Linux](https://docs.docker.com/engine/install/)
   * [Instalar no Windows](https://docs.docker.com/desktop/install/windows-install/)
   * [Instalar no macOS](https://docs.docker.com/desktop/install/mac-install/)

2. Testar se está funcionando:

```bash
docker --version
```

3. Tutorial oficial (recomendado):

   * [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)

