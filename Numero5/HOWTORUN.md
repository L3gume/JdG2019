# Instructions pour execution

puisqu'il m'est impossible d'executer le programme dans bash sur windows (les commandes `erl` et `erlc` ne sont pas reconnues), il faudra l'evaluer sur le Erlang shell de cette facon:

*important d'etre dans le meme directory: pwd() et cd(dir) pour confirmer*


```
> c(solution2). // compiler le module
> solution2:main(["key","mot1","mot2",...]). // key = le substring recherche
											 // mots = les mots a filtrer
```
