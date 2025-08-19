#  Escreva um progrma que leia um valor em metros e o exiba convertido em centimetros e milimetros
metro = float(input('Uma distancia em metor: '))
kilometros = metro / 1000
hectometros = metro / 100
decametros = metro / 10
decimetros = metro * 10
centimetro = metro * 100
milimetro = metro * 1000

print('Você digitou {:.2f} M\nO valor em Kilometros é {} km\nO valor em hectometros é {} hm\nO valor em decametros é {} dam\nO valor em decimetros é {} dm\nO valor em centimetros é {} c\nO valor em milmetros é {} mm'.format(metro, kilometros, hectometros, decametros, decimetros, centimetro, milimetro))