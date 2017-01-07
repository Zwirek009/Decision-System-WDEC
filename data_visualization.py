# import Pandas (data manipulation) and Matplotlib (trending)
import pandas as pd
import matplotlib.pyplot as plt

# import data from previous simulation
data = {}						# data gained from one result file
combined_data = []				# list of sigle result file data	
sim_table = {}					# combined data
base_result_name = 'wyniki{}.xls'	# .xls name scheme

result_name = base_result_name.format(1)			# name of first .xls file
data = pd.read_excel(result_name, header=None)	# load the file
combined_data.append(data)						# insert the data to list

for num in range(2, 6):								# uploading other .xls files
	result_name = base_result_name.format(num)
	try:
		data = pd.read_excel(result_name, header=None)
		data = data.ix[:, 2]							# get only third column of uploaded data file
		combined_data.append(data)
	except FileNotFoundError:
		print ("File " + result_name + " not found.")

# concat all uploaded data to one data set
sim_table = pd.concat(combined_data, axis=1)
print(sim_table)

# create separate data sets for different data
runda = sim_table.ix[0, 1:]
sprzedaz = sim_table.ix[1, 1:]
udzial = sim_table.ix[2, 1:]
wynik_firmy = sim_table.ix[3, 1:]
gotowka = sim_table.ix[4, 1:]
wolumen = sim_table.ix[5, 1:]
jakosc = sim_table.ix[6, 1:]
cena = sim_table.ix[7, 1:]
reklama_tv = sim_table.ix[8, 1:]
reklama_int = sim_table.ix[9, 1:]
reklama_mag = sim_table.ix[10, 1:]

print(sprzedaz)

# example plot
#plt.figure('Sztuki towaru')
#num_bins = 5
# the histogram of the data
#n, bins, patches = plt.hist(sprzedaz, num_bins, facecolor='green')
#plt.plot(runda, wolumen, 'r-')
#plt.legend(['Sprzedane', 'Wyprodukowane'])
#plt.xlabel('Runda')
#plt.ylabel('Liczba sztuk')
#plt.title('Sztuki towaru')

# example plot
plt.figure('Sztuki towaru')
plt.plot(runda, sprzedaz, 'b-')
plt.plot(runda, wolumen, 'r-')
plt.legend(['Sprzedane', 'Wyprodukowane'])
plt.xlabel('Runda')
plt.ylabel('Sztuki towaru')

plt.show()
