import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
figure, axis = plt.subplots()
axis.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Purples, s=30)

axis.set_title("Cubed Numbers", fontsize=24)
axis.set_xlabel("Value", fontsize=16)
axis.set_ylabel("Cube of Value", fontsize=16)

axis.tick_params(labelsize=14)

plt.show()

