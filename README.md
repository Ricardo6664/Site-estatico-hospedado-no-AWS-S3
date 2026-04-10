![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)
![CloudFront](https://img.shields.io/badge/CloudFront-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)

## 📁 Sobre o projeto  
##### Este projeto é um site estático hospedado na provedora cloud AWS (Amazon Web Services) utilizando o serviço S3 (Simple Storage Service). Em se tratando de hospedagem de sites estáticos o S3 já foi a única opção existente, mas hoje a própria AWS recomenda a utilização do serviço AWS Amplify, um serviço específico para implementação de sites de maneira rápida e simples, porém mesmo assim ainda está disponível e é válido a utilização do S3 para tal tarefa, mas é importante salientar que não é específico para isso.

##### O principal objetivo do S3 é armazenar arquivos de texto, áudio, vídeo ou imagem. Este armazenamento em muitos casos pode ser utilizado de maneira inteligente, conversando com outros serviços em funcionamento na AWS, como uma função Lambda ou EC2.
##### Foi utilizado em conjunto ao S3 o AWS CloudFront, ele tem por objeto acelerar a entrega de conteúdo a clientes globais, busca reduzir ao máximo a latência e para isso faz uso das Edge locations, por estarem mais próximos ao usuários.

## 🛠️ Stack / Tecnologias
##### HTML e CSS, AWS S3 e CLOUDFRONT

## 🚢 Como fazer deploy
##### Deverá criar e configurar as access key e access secret key da _AWS_;

##### Em seguida, execute o comando ```bash config_credentials.sh no terminal ```

##### E por último deverá executar ```bash start.sh ```


![static_site_s3](https://github.com/user-attachments/assets/b3e942fc-8edf-4766-8afc-7b8375138144)
