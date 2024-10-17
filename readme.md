## criar o ambiente venv
python3 -m venv env
## acessar o ambiente venv
source env/bin/activate

- - também usei o gerenciador pipenv
```pip install pipenv```
```pipenv shell```
pipenv shell cria o ambiente e depois acessa o ambiente
## lib ORM SQLAlchemy
- -  criar uma class para Modelar a tabela 
- - - depois em um terminal rodar o comando flask shell
- - - rodar o comando db.create_all() //para criar o banco com a tabela modelo em class
- - - rodar o comando db.session.commit() //efetuar as mudanças
- - - - posso fazer isso direto no código
- - - - - 
```
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Isso cria as tabelas no banco de dados
    app.run(debug=True)
```

## Criando a rota POST
```
@app.route('/api/products/add', methods=['POST'])
def add_product():
    data = request.json
    return data
```
## Navega do Postman e teste a rota com post, passando um body json com os valores
```
{{baseUrl}}/api/products/add
```
# api-python-flask

## Utilizando CORS no python com uma lib flask_cors
### agora vc pode abrir seu swagger 
- https://editor.swagger.io
- - escolher /api/products, clicar no botão [Try it out] e depois no botão [execute], vc já verá o swagger trazendo os dados da sua consulta usando o seu servidor local como endereço de pesquisa

## vamos para o flask-login agora para a parte da api com rota autenticada
- Class/Model User criada
- - para criar, pode usar o comando ```flask shell```
- - - ```db.drop_all()``` apagará todas as tabelas já criadas
- - - ```db.create_all()``` criará todas as Class/Model novamente
- - - ```db.session.commit()``` efeturá a execução dos comandos acima
- - - ```exit()```

- - - ou pode rodar continuar rodando no _main_
```
with app.app_context():
        db.create_all() 
```
- - criando o usuario pelo flask shell
- - - >>> user = User(username="Admin", password="Admin123@")
- - - >>> user
- - - <User (transient 4464376672)>
- - - >>> user.id
- - - >>> db.session.add(user)
- - - >>> db.session.commit()
- - - >>> exit()

- - pode verificar no banco tabela User
