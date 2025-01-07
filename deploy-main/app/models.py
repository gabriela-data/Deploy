from app import db

class Funcionario(db.Model):

    __tablename__ = 'funcionario'

    id_funcionario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_funcionario = db.Column(db.String(30))
    cpf_funcionario = db.Column(db.String(15), unique=True)
    email_funcionario = db.Column(db.String(30), unique=True)

    def __init__ (self, nome_funcionario, cpf_funcionario, email_funcionario ):
        self.nome_funcionario = nome_funcionario
        self.cpf_funcionario = cpf_funcionario
        self.email_funcionario = email_funcionario

    def __repr__(self):
        return '<Funcionario %r>' % self.nome_funcionario
    

class Cliente(db.Model):
    __tablename__ = 'cliente'

    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cliente = db.Column(db.String(75))
    cpf_cliente = db.Column(db.String(13), unique=True)
    email_cliente = db.Column(db.String(100), unique=True)
    data_ultima_interacao = db.Column(db.Date)
    status_follow_up = db.Column(db.String(45))
    data_proximo_followup = db.Column(db.Date)
    descricao_ultima_interacao = db.Column(db.String(45))

    def __init__(self, nome_cliente, cpf_cliente, email_cliente, data_ultima_interacao, status_follow_up,
                 data_proximo_followup, descricao_ultima_interacao):
        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente
        self.email_cliente = email_cliente
        self.data_ultima_interacao = data_ultima_interacao
        self.status_follow_up = status_follow_up
        self.data_proximo_followup = data_proximo_followup
        self.descricao_ultima_interacao = descricao_ultima_interacao

    def __repr__(self):
        return '<Cliente %r>' % self.nome_cliente
    
class Produto(db.Model):
    __tablename__ = 'produto'

    id_produto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_produto = db.Column(db.String(255), nullable=False)
    preco_produto = db.Column(db.Float, nullable=False)

    def __init__(self, nome_produto, preco_produto):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto

    def __repr__(self):
         return '<Produto %r>' % self.nome_produto

class Estoque(db.Model):
    __tablename__ = 'estoque'

    id_estoque = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id_produto'))
    qtd_produto = db.Column(db.Integer)
    status_estoque = db.Column(db.String(75))
    id_galpao = db.Column(db.Integer)

    produto = db.relationship('Produto', backref='estoque')

    def __init__(self, id_produto, qtd_produto, status_estoque, id_galpao):
        self.id_produto = id_produto
        self.qtd_produto = qtd_produto
        self.status_estoque = status_estoque
        self.id_galpao = id_galpao

    def __repr__(self):
        return f'<Estoque {self.id_estoque}>'

class Tarefa(db.Model):
    __tablename__ = 'tarefa'

    id_tarefa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_tarefa = db.Column(db.Date)
    nome_tarefa = db.Column(db.String(75))
    status_tarefa = db.Column(db.String(20))

    def __init__(self, data_tarefa, nome_tarefa, status_tarefa):
        self.data_tarefa = data_tarefa
        self.nome_tarefa = nome_tarefa
        self.status_tarefa = status_tarefa

    def __repr__(self):
        return f'<Tarefa {self.id_tarefa}>'

class HistoricoCompra(db.Model):
    __tablename__ = 'historico_compra'

    id_compra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_compra = db.Column(db.Date)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'))
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id_produto'))
    cliente = db.relationship('Cliente', backref='historico_compra')
    produto = db.relationship('Produto', backref='historico_compra')

    def __init__(self, data_compra, id_cliente, id_produto):
        self.data_compra = data_compra
        self.id_cliente = id_cliente
        self.id_produto = id_produto

    def __repr__(self):
        return f'<HistoricoCompra {self.id_compra}>'

class RegistroInteracao(db.Model):
    __tablename__ = 'registro_interacao'

    id_interacao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'))
    id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id_funcionario'))
    data_interacao = db.Column(db.Date)
    tipo_interacao = db.Column(db.String(45))
    descricao_interacao = db.Column(db.String(45))
    registro_interacaocol = db.Column(db.String(45))
    etapa_followup = db.Column(db.String(45))
    status_followup = db.Column(db.String(45))
    data_prox_followup = db.Column(db.Date)

    cliente = db.relationship('Cliente', backref='registro_interacao')
    funcionario = db.relationship('Funcionario', backref='registro_interacao')

    def __init__(self, id_cliente, id_funcionario, data_interacao, tipo_interacao, descricao_interacao,
                 registro_interacaocol, etapa_followup, status_followup, data_prox_followup):
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario
        self.data_interacao = data_interacao
        self.tipo_interacao = tipo_interacao
        self.descricao_interacao = descricao_interacao
        self.registro_interacaocol = registro_interacaocol
        self.etapa_followup = etapa_followup
        self.status_followup = status_followup
        self.data_prox_followup = data_prox_followup

    def __repr__(self):
        return f'<RegistroInteracao {self.id_interacao}>'
