**Objetivo**

O site foi feito para registrar as partidas jogadas nas Copas do Mundo. Cadastrando seleções, jogadores, juízes e as partidas (dentro é possível adicionar data, estádio, local de transmissão e os elencos separados).

**1. Seleção**

Local onde todas as seleções que jogaram uma Copa do Mundo são registradas.
A única informação é o nome com limite de 50 caracteres.

**2. Jogador**

Local onde todos os jogadores que jogaram uma Copa do Mundo são registrados.
Uma informação é o nome com limite de 50 caracteres.
A outra é uma chave estrangeira ligando a seleção, porque um jogador só pode jogar por uma seleção, mas uma seleção pode ter vários jogadores.

**3. Juiz**

Local onde todos os juízes que apitaram uma Copa do Mundo são registrados.
A única informação é o nome com limite de 50 caracteres.

**4. Partida**

Local onde se registram as partidas jogadas na Copa do Mundo.
Uma informação é o estádio com limite de 100 caracteres.
Outra é a data com DateField.
Outra é o local de transmissão com limite de 100 caracteres.
Outra é a seleção mandante, que deve ser uma das seleções cadastradas.
Outra é a visitante, que também deve ser uma das seleções cadastradas.
Outra são os jogadores da seleção mandante. (Vários jogadores podem jogar várias partidas.)
Outra são os jogadores da seleção visitante. (Vários jogadores podem jogar várias partidas.)
E, por fim, o nome do juiz. (Vários juízes, incluindo os bandeirinhas, VAR e etc, podem apitar vários jogos.)

**Justificativa Técnica**

No Jogador, utilizei o `on_delete=models.SET_NULL` na seleção, porque mesmo que a seleção seja deletada, os dados dos jogadores são preservados. E por isso o `null=True`, porque pode apagar e ficar vazio e, ao mesmo tempo, o `blank=True`, porque pode simplesmente não adicionar a seleção ao jogador.

python
selecao = models.ForeignKey(Selecao, on_delete=models.SET_NULL, blank=True, null=True)

Assim, o jogador é registrado e não é apagado, podendo posteriormente receber os dados da seleção.

Nos campos `selecao_casa` e `selecao_visitante`, também utilizei o `on_delete=models.SET_NULL`.

python
selecao_casa = models.ForeignKey(Selecao, on_delete=models.SET_NULL, null=True, blank=True)


Se a seleção for removida, além de não apagar o jogador, as partidas cadastradas não serão deletadas e, assim como os jogadores, o campo ficará `null`, preservando o registro da partida.

Isso ajuda a evitar a perda do histórico dos jogos e mantém informações como o estádio, a data, o juiz e os jogadores (visitantes e mandantes), mesmo que as seleções não estejam mais no banco de dados.
