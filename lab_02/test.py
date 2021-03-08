from geometry import find_two_coprime_ints, Epicycloid
import matplotlib.pyplot as plt

print(find_two_coprime_ints(17, 5.10))

epicycloid = Epicycloid(1, 3, 2, 3)
x,y = epicycloid.create_figure()

plt.plot(x,y)
plt.show()


