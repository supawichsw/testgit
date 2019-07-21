meandiff=8
tickdiff=16

Difffactor=(1 if tickdiff<=meandiff else ((meandiff-tickdiff)/meandiff))
print(Difffactor)
Difffactor=Difffactor-1
print(Difffactor)