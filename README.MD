# DEPENDÊNCIAS
O projeto roda e é iniciado a partir de uma aplicação Docker, portanto, é necessário ter instalado na máquina a versão mais recente do Docker, e também, o docker-compose

# EXECUÇÃO DO PROJETO
O projeto foi containerizado com o docker, usando um banco de dados postgres e uma aplicação python.

Para rodar o sitema, basta contruir as images com o comando "docker-compose build"

Após isso, basta rodar "docker-compose up" para ligar a aplicação com as dependencias necessárias.

