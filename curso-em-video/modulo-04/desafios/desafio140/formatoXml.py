import xml.etree.ElementTree as ET

class FormatoXml:
    def exportar(self, dados):
        nome = dados[0].__class__.__name__.lower()
        pai = ET.Element("dados")
        for item in dados:
            filho = ET.SubElement(pai, nome)
            for chave, valor in item.__dict__.items():
                neto = ET.SubElement(filho, chave)
                neto.text = str(valor)
        ET.indent(pai, space="\t")
        txt = ET.tostring(pai, encoding="unicode", xml_declaration=True)
        return txt