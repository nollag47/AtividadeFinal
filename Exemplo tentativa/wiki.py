from madeira import Madeira
from pedra import picaretadepedra
from ferro import picaretadeferro
from ouro import picaretadeouro
from diamante import picaretadediamante

picareta1 = Madeira("Picareta_de_Madeira",59,"Baixa")
picareta2 = Pedra("Picareta_de_Pedra",131,"Baixa")
picareta3 = Ferro("Picareta_de_Ferro",250,"Moderada")
picareta4 = Ouro("Picareta_de_Ouro",32,"Muito Alta")
picareta5 = Diamante("Picareta_de_Diamante",1561,"Alta")

print("-="*40)
print("Minecraft possui muitos minérios, mas nem todas picaretas conseguem minerá-los")
print("Portanto aqui estão os status das picaretas e quais minérios elas conseguem quebrar")

print(picareta1.getstatus())
print(picareta2.getstatus())
print(picareta3.getstatus())
print(picareta4.getstatus())
print(picareta5.getstatus())

print("Minérios:")
print("Carvão pode ser quebrado por: Picareta_de_Madeira,Picareta_de_Pedra,Picareta_de_Ferro,Picareta_de_Ouro,Picareta_de_Diamante")
print("Lápiz lazuli pode ser quebrado por: Picareta_de_Pedra,Picareta_de_Ferro,Picareta_de_Diamante")
print("Ferro pode ser quebrado por: Picareta_de_Pedra,Picareta_de_Ferro,Picareta_de_Diamante")
print("Redstone pode ser quebrado por: Picareta_de_Ferro,Picareta_de_Diamante")
print("Cobre pode ser quebrado por: Picareta_de_Pedra,Picareta_de_Ferro,Picareta_de_Diamante")
print("Esmeralda pode ser quebrado por: Picareta_de_Ferro,Picareta_de_Diamante")
print("Ouro pode ser quebrado por: Picareta_de_Ferro,Picareta_de_Diamante")
print("Diamante pode ser quebrado por: Picareta_de_Ferro,Picareta_de_Ouro,Picareta_de_Diamante")


