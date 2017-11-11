import pygal.maps.world

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'North,Central, and South America'
worldmap_chart.add('North countries', ['ca','mx','us'])
worldmap_chart.add('Central countries', ['bz', 'cr', 'gt', 'hn', 'ni','pa','sv',])
worldmap_chart.add('U countries', ['ar', 'bo', 'br', 'cl', 'co','ec','gf','gy','pe','py','sr','uy','ve'])

worldmap_chart.render_to_file('americas.svg')