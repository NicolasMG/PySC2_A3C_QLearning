# PySC2_A3C_QLearning
Ce git sert de dépôt pour un projet de 2ème année en école d'ingénieur en Informatique et Réseaux.
les bases de ce projet ont été :
- https://github.com/deepmind/pysc2
- https://github.com/chris-chris/pysc2-examples
- https://github.com/xhujoy/pysc2-agents
- https://github.com/skjb/pysc2-tutorial



## Prérequis :
- Nous utilisons PySC2, un environnement d'apprentissage fournit par DeepMind. Cet environnement permet aux agents d'interagir avec StarCraft 2  en observant les parties et effectuant des actions.
Il s'agit ici de la version 1.1 de PySC2.
```shell
pip install pysc2==1.1
pip install s2clientprotocol==1.1
pip install absl-py
pip install tensorflow-gpu
pip install baselines
```



## Exécution :
- Il est possible de lancer notre agent de plusieurs façons :
	- Pour lancer l'agent par invité commande
		```
		python -m main --option
		```
		d'autres options sont disponibles.

		|Options		|Type de la variable	|Valeur par défaut	|
		|:-------------------:|:---------------------:|:---------------------:|
		| render      		| boolean 		| True			|
		| training      	| boolean	     	| True			|
		| map			| String     		| MoveToBeacon		|
		| agent_race		| String     		| T			|
		| bot_race		| String     		| None			|
		| max_agent_steps	| Integer   		| 1200			|
		| difficulty		| Integer     		| None			|

		Liste des maps disponibles : MoveToBeacon, CollectMineralShards, DefeatRoaches, Simple64
		Liste des races jouables : R (random), T (Terran), Z (Zerg), P (Protos)
		Liste des difficultées : [1-9]
		

	- Pour l'entraîner, le fichier 
		```
		python Rerole.py
		```
		ce qui lancera l'exécution sans interface graphique, cette execution permet, si il y a des dépassements de mémoire, 
		de relancer automatiquement l'agent.

