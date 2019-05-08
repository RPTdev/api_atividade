from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Maluco', idade=99)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Scrooge')
    # for i in pessoa:
    #    print(i)
    # pessoa = Pessoas.query.filter_by(nome='Scrooge').first()
    # print(pessoa.nome)
    # print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Garmin').first()
    pessoa.nome = 'CucaBeludo'
    pessoa.save()


def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='CucaBeludo').first()
    pessoa.delete()


def inserir_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def listar_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    inserir_usuario('Aderbal', '123')
    inserir_usuario('Bederbal', '123')
    listar_usuarios()
    # insere_pessoas()
    # altera_pessoa()
    # excluir_pessoa()
    # consulta_pessoas()
