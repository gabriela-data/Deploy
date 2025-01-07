from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, Length


class FormFuncionario(FlaskForm):
    nome_funcionario = StringField('Nome', validators=[DataRequired()])
    cpf_funcionario = StringField('CPF', validators=[DataRequired()])
    email_funcionario = StringField('E-mail', validators=[DataRequired(), Email()])
    
    #botao_submit_criarconta = SubmitField('Cadastrar Usuario')

class FormCliente(FlaskForm):
    nome_cliente = StringField('Nome do Cliente', validators=[DataRequired()])
    cpf_cliente = StringField('CPF do Cliente', validators=[DataRequired()])
    email_cliente = StringField('Email do Cliente', validators=[DataRequired(), Email()])
    data_ultima_interacao = DateField('Data Última Interação')
    status_follow_up = StringField('Status Follow-Up', validators=[Length(max=45)])
    data_proximo_followup = DateField('Data Próximo Follow-Up')
    descricao_ultima_interacao = StringField('Descrição Última Interação', validators=[Length(max=45)])

class FormProduto(FlaskForm):
    nome_produto = StringField('Nome do Produto', validators=[DataRequired(), Length(max=75)])
    preco_produto = FloatField('Preço do Produto', validators=[DataRequired()])

class FormEstoque(FlaskForm):
    id_produto = IntegerField('ID do Produto', validators=[DataRequired()])
    qtd_produto = IntegerField('Quantidade do Produto', validators=[DataRequired()])
    status_estoque = StringField('Status do Estoque', validators=[Length(max=75)])
    id_galpao = IntegerField('ID do Galpão')

class FormTarefa(FlaskForm):
    data_tarefa = DateField('Data da Tarefa')
    nome_tarefa = StringField('Nome da Tarefa', validators=[DataRequired(), Length(max=75)])
    status_tarefa = StringField('Status da Tarefa', validators=[Length(max=20)])

class FormHistoricoCompra(FlaskForm):
    data_compra = DateField('Data da Compra')
    id_cliente = IntegerField('ID do Cliente', validators=[DataRequired()])
    id_produto = IntegerField('ID do Produto', validators=[DataRequired()])

class FormRegistroInteracao(FlaskForm):
    id_cliente = IntegerField('ID do Cliente', validators=[DataRequired()])
    id_funcionario = IntegerField('ID do Funcionário', validators=[DataRequired()])
    data_interacao = DateField('Data da Interação')
    tipo_interacao = StringField('Tipo de Interação', validators=[Length(max=45)])
    descricao_interacao = StringField('Descrição da Interação', validators=[Length(max=45)])
    registro_interacaocol = StringField('Registro de Interação', validators=[Length(max=45)])
    etapa_followup = StringField('Etapa do Follow-Up', validators=[Length(max=45)])
    status_followup = StringField('Status do Follow-Up', validators=[Length(max=45)])
    data_prox_followup = DateField('Data Próximo Follow-Up')
