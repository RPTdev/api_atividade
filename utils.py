from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Scrooge',idade=19)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    #pessoa = Pessoas.query.filter_by(nome='Scrooge')
    #for i in pessoa:
    #    print(i)
    #pessoa = Pessoas.query.filter_by(nome='Scrooge').first()
    #print(pessoa.nome)
    #print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Garmin').first()
    pessoa.nome = 'CucaBeludo'
    pessoa.save()


def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='CucaBeludo').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    excluir_pessoa()
    consulta_pessoas()
