import matplotlib.pyplot as plt

car = ('Ferari', 'Cadilac', 'Mercedes-benz', 'Bugatti')
max_speed = (300, 330, 380, 400)
colors = ('#32012F', '#524C42', '#E2DFD0', '#F97300')
explode = (0, 0, 0, 0.1)
plt.pie(
    x=max_speed,
    labels=car,
    autopct='%1.1f%%',
    colors=colors,
    wedgeprops= {'width': 0.4}
)

plt.show()