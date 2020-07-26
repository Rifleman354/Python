Vehicle_Demands = ['Leman Russ Tanks', 'Dunewalkers', 'Baneblades']

Dir = 2 # Meaning directory, where putting 0 index means producing 100 Leman Russ Tanks
        # 1 index meaning producing 100 Dunewalkers
        # 2 index meaning pruducing 100 Baneblades

print('Lord General: Mass produce me 100 ' + Vehicle_Demands[Dir] + ', Archmagos Helios!')

if Dir==2: # Conditional statement if index 2 is called
	print('Archmagos Helios: We are short of material for Baneblades, Lord General!')
else:
	print('Archmagos Helios: Understood sir!') # If the demand from Dir is not at "Baneblade"


