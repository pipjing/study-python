import pygal.maps.world

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'North,Central, and South America'
worldmap_chart.add('North countries', {'ca': 34126000 ,'mx':309349000,'us':113423000})
worldmap_chart.add('Central countries', ['bz', 'cr', 'gt', 'hn', 'ni','pa','sv',])
worldmap_chart.add('U countries', ['ar', 'bo', 'br', 'cl', 'co','ec','gf','gy','pe','py','sr','uy','ve'])

worldmap_chart.render_to_file('americas1.svg')