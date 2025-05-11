#Assignment:Inter Planetary Weights
#Class:Python CIT-115 D80
#Date:3/31/25
#Name:Angie Campos

MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066

sName = input("What is your name:")
iWeight = float(input("What is your weight:"))
sInfo1 = "Weight on Mercury is:"
sInfo2 = "Weight on Venus is:"
sInfo3 = "Weight on our Moon is:"
sInfo4 = "Weight on Mars is:"
sInfo5 = "Weight on Jupiter is:"
sInfo6 = "Weight on Saturn is:"
sInfo7 = "Weight on Uranus is:"
sInfo8 = "Weight on Neptune is:"
sInfo9 = "Weight on Pluto is:"

print(f"{sName} here are your weights on our Solar System's Planets:")


nTotalWeight1 = iWeight * MERCURY
nTotalWeight2 = iWeight * VENUS
nTotalWeight3 = iWeight * MOON
nTotalWeight4 = iWeight * MARS
nTotalWeight5 = iWeight * JUPITER
nTotalWeight6 = iWeight * SATURN
nTotalWeight7 = iWeight * URANUS
nTotalWeight8 = iWeight * NEPTUNE
nTotalWeight9 = iWeight * PLUTO

print(f"{sInfo1:25s} {nTotalWeight1:10,.2f}" )
print(f"{sInfo2:25s} {nTotalWeight2:10,.2f}" )
print(f"{sInfo3:25s} {nTotalWeight3:10,.2f}" )
print(f"{sInfo4:25s} {nTotalWeight4:10,.2f}" )
print(f"{sInfo5:25s} {nTotalWeight5:10,.2f}" )
print(f"{sInfo6:25s} {nTotalWeight6:10,.2f}" )
print(f"{sInfo7:25s} {nTotalWeight7:10,.2f}" )
print(f"{sInfo8:25s} {nTotalWeight8:10,.2f}" )
print(f"{sInfo9:25s} {nTotalWeight9:10,.2f}" )
