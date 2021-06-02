class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0


    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.tittle()


def __str__(self):
    return 'Nome: {} - {} - Likes: {}'.format(self.nome, self.ano, self.likes)

class Filme(Programa):

    def  __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return 'Nome: {} - {} - {} minutos - Likes: {}'.format(self.nome, self.ano, self.duracao, self.likes)





class Serie(Programa):

    def  __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return 'Nome: {} - {} - {} temporadas - Likes: {}'.format(self.nome, self.ano, self.temporadas, self.likes)



class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]


    @property
    def listagem(self):
        return self._programas


    def __len__(self):
        return len(self._programas)




vingadores = Filme('Vingadores Guerra infinita',2018,160)
atlanta = Serie('Atlanta', '2017', '2')
fast_and_furious = Filme('Fast and Furious',2006,140)
hobbit = Filme('O Hobbit',2012,182)
friends = Serie('Friends', '2000', '12')
stranho = Serie('Stranger Things', '2017', '4')


hobbit.dar_like()
hobbit.dar_like()
hobbit.dar_like()
hobbit.dar_like()
hobbit.dar_like()
hobbit.dar_like()
hobbit.dar_like()
hobbit.dar_like()

fast_and_furious.dar_like()
fast_and_furious.dar_like()
fast_and_furious.dar_like()
fast_and_furious.dar_like()
fast_and_furious.dar_like()
fast_and_furious.dar_like()

friends.dar_like()
friends.dar_like()
friends.dar_like()
friends.dar_like()
friends.dar_like()
friends.dar_like()
friends.dar_like()

stranho.dar_like()
stranho.dar_like()
stranho.dar_like()
stranho.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series= [vingadores, atlanta,fast_and_furious,hobbit,friends,stranho]
playlis_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f"Tamano da Playlist = {len(playlis_fim_de_semana)}")

for programa in playlis_fim_de_semana:
    print(programa)
