from app import app, db
from flask import render_template, request, redirect, url_for
from app.forms import FormEstoque, FormFuncionario, FormCliente, FormHistoricoCompra, FormProduto, FormRegistroInteracao, FormTarefa
from app.models import Cliente, Estoque, Funcionario, HistoricoCompra, Produto, RegistroInteracao, Tarefa
from datetime import datetime

# Cria as tabelas
with app.app_context():
    db.create_all()

# Restante do seu código
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/adicionar', methods=['POST', 'GET'])
def adicionar():
    formFuncionario = FormFuncionario()
    if request.method == 'POST':
        if formFuncionario.validate_on_submit():
            nome_funcionario = formFuncionario.nome_funcionario.data
            cpf_funcionario = formFuncionario.cpf_funcionario.data
            email_funcionario = formFuncionario.email_funcionario.data

            funcionario = Funcionario(nome_funcionario, cpf_funcionario, email_funcionario)
            db.session.add(funcionario)
            db.session.commit()

            return redirect(url_for('index'), code=302 )

    return render_template('adicionar_funcionario.html', form=formFuncionario)

@app.route('/adicionar_cliente', methods=['POST', 'GET'])
def adicionar_cliente():
    formCliente = FormCliente()
    if request.method == 'POST':
        if formCliente.validate_on_submit():
            nome_cliente = formCliente.nome_cliente.data
            cpf_cliente = formCliente.cpf_cliente.data
            email_cliente = formCliente.email_cliente.data
            data_ultima_interacao_str = formCliente.data_ultima_interacao.data
            status_follow_up = formCliente.status_follow_up.data
            data_proximo_followup = formCliente.data_proximo_followup.data
            descricao_ultima_interacao = formCliente.descricao_ultima_interacao.data

            # Convertendo a string da data para formato ISO8601
            data_ultima_interacao = datetime.strptime(data_ultima_interacao_str, '%d-%m-%Y').isoformat()

            cliente = Cliente(
                nome_cliente=nome_cliente,
                cpf_cliente=cpf_cliente,
                email_cliente=email_cliente,
                data_ultima_interacao=data_ultima_interacao,
                status_follow_up=status_follow_up,
                data_proximo_followup=data_proximo_followup,
                descricao_ultima_interacao=descricao_ultima_interacao
            )

            db.session.add(cliente)
            db.session.commit()

            return redirect(url_for('index'), code=302)

    return render_template('adicionar_cliente.html', form=formCliente)


@app.route('/adicionar_produto', methods=['POST', 'GET'])
def adicionar_produto():
    formProduto = FormProduto()
    if request.method == 'POST':
        if formProduto.validate_on_submit():
            nome_produto = formProduto.nome_produto.data
            preco_produto = formProduto.preco_produto.data

            produto = Produto(nome_produto=nome_produto, preco_produto=preco_produto)
            db.session.add(produto)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('adicionar_produto.html', form=formProduto)



@app.route('/registro_estoque', methods=['POST', 'GET'])
def registro_estoque():
    formEstoque = FormEstoque()
    if request.method == 'POST':
        if formEstoque.validate_on_submit():
            id_produto = formEstoque.id_produto.data
            qtd_produto = formEstoque.qtd_produto.data
            status_estoque = formEstoque.status_estoque.data
            id_galpao = formEstoque.id_galpao.data

            estoque = Estoque(id_produto=id_produto, qtd_produto=qtd_produto, status_estoque=status_estoque, id_galpao=id_galpao)
            db.session.add(estoque)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('registro_estoque.html', form=formEstoque)




@app.route('/registro_tarefa', methods=['POST', 'GET'])
def registro_tarefa():
    formTarefa = FormTarefa()
    if request.method == 'POST':
        if formTarefa.validate_on_submit():
            data_tarefa = formTarefa.data_tarefa.data
            nome_tarefa = formTarefa.nome_tarefa.data
            status_tarefa = formTarefa.status_tarefa.data

            tarefa = Tarefa(data_tarefa=data_tarefa, nome_tarefa=nome_tarefa, status_tarefa=status_tarefa)
            db.session.add(tarefa)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('registro_tarefa.html', form=formTarefa)


@app.route('/registro_interacao', methods=['POST', 'GET'])
def registro_interacao():
    formRegistroInteracao = FormRegistroInteracao()
    if request.method == 'POST':
        if formRegistroInteracao.validate_on_submit():
            id_cliente = formRegistroInteracao.id_cliente.data
            id_funcionario = formRegistroInteracao.id_funcionario.data
            data_interacao = formRegistroInteracao.data_interacao.data
            tipo_interacao = formRegistroInteracao.tipo_interacao.data
            descricao_interacao = formRegistroInteracao.descricao_interacao.data
            registro_interacaocol = formRegistroInteracao.registro_interacaocol.data
            etapa_followup = formRegistroInteracao.etapa_followup.data
            status_followup = formRegistroInteracao.status_followup.data
            data_prox_followup = formRegistroInteracao.data_prox_followup.data

            registro_interacao = RegistroInteracao(
                id_cliente=id_cliente,
                id_funcionario=id_funcionario,
                data_interacao=data_interacao,
                tipo_interacao=tipo_interacao,
                descricao_interacao=descricao_interacao,
                registro_interacaocol=registro_interacaocol,
                etapa_followup=etapa_followup,
                status_followup=status_followup,
                data_prox_followup=data_prox_followup
            )
            db.session.add(registro_interacao)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('registro_interacao.html', form=formRegistroInteracao)

#Rotas das listas
@app.route('/lista_funcionarios')
def lista_funcionarios():
    funcionario = Funcionario.query.all()
    return render_template('lista_funcionarios.html', funcionario=funcionario)

@app.route('/lista_clientes')
def lista_clientes():
    cliente = Cliente.query.all()
    return render_template('lista_clientes.html', cliente=cliente)

@app.route('/lista_produtos')
def lista_produtos():
    produtos = Produto.query.all()
    return render_template('lista_produtos.html', produtos=produtos)

@app.route('/lista_estoque')
def lista_estoque():
    estoque_itens = Estoque.query.all()
    return render_template('lista_estoque.html', estoque_itens=estoque_itens)

@app.route('/lista_tarefas')
def lista_tarefas():
    tarefas = Tarefa.query.all()
    return render_template('lista_tarefas.html', tarefas=tarefas)

@app.route('/historico_compra')
def historico_compra():
    historico_compras = HistoricoCompra.query.all()
    return render_template('historico_compra.html', historico_compras=historico_compras)



if __name__ == '__main__':
    app.run(debug=True)