import random
NUMEROALEATORIO_1=random.randint(1,6)
NUMEROALEATORIO_2=random.randint(1,6)
MENSAJE_LOGRO="Lo lograste"
_suma=NUMEROALEATORIO_1+NUMEROALEATORIO_2
while(_suma!=12):
    print(_suma)
    NUMEROALEATORIO_1=random.randint(1,6)
    NUMEROALEATORIO_2=random.randint(1,6)
    _suma=NUMEROALEATORIO_1+NUMEROALEATORIO_2
print(MENSAJE_LOGRO)