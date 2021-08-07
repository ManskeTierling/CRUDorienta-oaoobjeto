from flask import Flask, render_template, redirect, request
from produtos import Produto
from programa import conexao, salvar, select, delete, select_id, update

app = Flask(__name__)

@app.route('/', methods=['get'])
def pagina_inicial():
    return render_template('index.html')

@app.route('/salvar', methods=["POST"])
def inserir():
    novo_produto = Produto(request.form["nome"],
                            request.form["descricao"], 
                            request.form["marca"], 
                            request.form["preco"], 
                            request.form["cor"])
    db = conexao()
    salvar(db, novo_produto)
    return redirect('/')

@app.route('/listar', methods=["GET"])
def listar():
    db = conexao()
    lista_banco = select(db)
    lista_objetos = []
    for registro in lista_banco:
        lista_objetos.append(Produto(registro[1], registro[2], registro[3], registro[4], registro[5], registro[0]))
    return render_template("vizualizar.html", lista_banco_no_html = lista_objetos)

@app.route('/deletar')
def deletar():
    id = int(request.args['id'])
    db = conexao()
    delete(db, id)
    return redirect('/listar') 

@app.route('/alterar')
def alterar():
    id = int(request.args['id'])
    db = conexao()
    registro = select_id(db, id)
    produto = Produto(registro[1], registro[2], registro[3], registro[4], registro[5], registro[0])
    return render_template("alterar.html", produto = produto)
 
@app.route("/alterar/salvar", methods=["POST"])
def alterar_salvar():
    novo_produto = Produto(request.form["nome"],
                            request.form["descricao"], 
                            request.form["marca"], 
                            request.form["preco"], 
                            request.form["cor"])
    db = conexao()    
    update(db, novo_produto)
    return redirect('/listar')  

app.run(debug=True)