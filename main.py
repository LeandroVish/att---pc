from game.Level import start
from game.Sound import play

print("Iniciando o jogo...\n")

dificuldade = start.select_dificulty()

play.tocar_musica(dificuldade)

print("\nTudo pronto! Boa sorte no jogo! 🎮")
