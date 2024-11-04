class Auto:
    def __init__(self,vyrobce, model, objem_motoru, vykon):
        self._vyrobce=vyrobce
        self._model=model
        self._objem_motoru=objem_motoru
        self._vykon=vykon

    def __eq__(self,other):
        if isinstance(other, Auto):
            return self._vyrobce==other._vyrobce and self._model==other._model and self._objem_motoru==other._objem_motoru and  self._vykon== other._vykon
        else:
            return False

a1=Auto("Skoda","Octavia",2.5,130)
a2=Auto("Skoda","Octavia",2.5,130)

if a1==a2:
    print("stejné")
else:
    print("jine")