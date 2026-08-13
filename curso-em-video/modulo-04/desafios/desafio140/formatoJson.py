from json import dumps

class FormatoJson:
    def exportar(self, dados):
        lista = []
        for item in dados:
            lista.append(item.__dict__)
        txt = dumps(lista, ensure_ascii=False, indent=2)
        return txt