import ozon3 as ooo

o3 = ooo.Ozon3('71421760dc918d8bc84e43abf45524580875f610')
data = o3.get_city_air('New Delhi')

data = o3.get_multiple_city_air(['Taipei', 'Hong Kong', 'New York'])     # As many locations as you need