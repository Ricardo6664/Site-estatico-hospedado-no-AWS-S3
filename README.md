**Sobre o projeto:**  Este projeto é um site estático hospedado na provedora cloud AWS (Amazon Web Services) utilizando o serviço S3 (Simple Storage Service). Em se tratando de hospedagem de sites estáticos o S3 já foi a única opção existente, mas hoje a própria AWS recomenda a utilização do serviço AWS Amplify, um serviço específico para implementação de sites de maneira rápida e simples, porém mesmo assim ainda está disponível e é válido a utilização do S3 para tal tarefa, mas é importante salientar que não é específico para isso.

O principal objetivo do S3 é armazenar arquivos de texto, áudio, vídeo ou imagem. Este armazenamento em muitos casos pode ser utilizado de maneira inteligente, conversando com outros serviços em funcionamento na AWS, como uma função Lambda ou EC2.
Foi utilizado em conjunto ao S3 o AWS CloudFront, ele tem por objeto acelerar a entrega de conteúdo a clientes globais, busca reduzir ao máximo a latência e para isso faz uso das Edge locations, por estarem mais próximos ao usuários.

**Stack / Tecnologias —** HTML e CSS, AWS S3 e CLOUDFRONT

**Como fazer deploy —** Primeiramente é preciso desativar o bloqueio de acesso público indo em permissões dentro da _bucket_. Ainda na aba permissões, é necessário criar uma política para a _bucket_ autorizando a leitura e a obtenção do(s) arquivo(s). Por último, basta ir em propriedades e configurar a _Hospedagem de site estático_.


![static_site_s3](https://github.com/user-attachments/assets/b3e942fc-8edf-4766-8afc-7b8375138144)
