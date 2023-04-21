import matplotlib.pyplot as plt
import pyscript

# await pyodide_js.loadPackage('package_name')
fig, ax = plt.subplots()

year_2 = [2016, 2017, 2018, 2019, 2020, 2021]
population_2 = [43, 43, 44, 44, 45, 45]

plt.plot(year_2, population_2)


pyscript.write('lineplot',fig)

print('Python script in pyscript end here ')