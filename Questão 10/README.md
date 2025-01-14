# Questão 10

Para esta questão  foi utilizado a ferramenta Postman. 

### Requesitos
 - Cliente Postman
 - Conta na plataforma Postman


### Motivo de escolha da ferramenta

 -  É simples
 - Permite *criar e exportar coleções de requisição*, facilitando a reprodução e avaliação deste desafio
 - Permite escrever scripts de validação utilizando Javascript 
 - Já vem com a biblioteca Chai que permite fazer asserções


## Coleção de requisição
Foi criada uma coleção chamada loja-api no Postman que possui *5* requisições e um total de  *13* testes.

### Detalhamento das Requisições

 - POST Cadastrar placa de vídeo
	 - Test: Código de status deve ser 201
	 - Test: Deve cadastrar placa de vídeo NVDIA RTX 4060
	 - Test: Tempo de resposta deve ser menor que 1s
- POST Cadastrar aspirador de pó
	- Test: Código de status deve ser 201
	- Test: Deve cadastrar aspirador de pó
	-  Test: Tempo de resposta deve ser menor que 1s
- GET Listar todos os produtos
	- Test: Código de status deve ser 200
	- Test: Deve haver pelo menos dois produtos
	- Test: Tempo de resposta deve ser menor que 3s
- GET Filtrar produto pelo id=2
	- Test: Código de status deve ser 200
	- Test: Produto de Id=2 deve ter o nome de Aspirador de pó
- GET Filtrar produto pelo id=99999
	- Test: Código de status de ser 404
	- Test: Produto de Id=99999 não deve existir

*Obs:* A Requisição GET Filtrar produto pelo id=2 pode apresentar falha porque assume que o banco de dados se encontra vazio e o registro de id=2 seria o do Aspirador de pó.

### Como executar
- Faça o download da coleção `loja-api.postman_collection.json`
- Abra seu Postman
- Clique no botão `import`
- Importe o arquivo `loja-api.postman_collection.json`
- Após carregar, clique no item `loja-api` que aparecerá na listagem esquerda do menu `Collections`.
- Aperte no botão com o texto `Run`
- A aba `Runner` será aberta. Deixe as configurações como estão e aperte no botão `Run loja-api`
- Visualize o resultados

**Obs**: O texto nas URLs `{{baseUrl}}` é uma varíavel de ambiente que vai por padrão com o valor ``localhost:8000``. se seu serviço estiver rodando em outra porta. Altere o valor desta variável. 