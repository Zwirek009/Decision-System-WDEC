# import Pandas (data manipulation) and Matplotlib (trending)
import pandas as pd
import matplotlib.pyplot as plt

def load_data(result_name):
	data = {}						# data gained from one result file
	combined_data = []				# list of sigle result file data	
	sim_table = {}					# combined data

	temp_result_name = result_name.format(1)			# name of first .xls file
	data = pd.read_excel(temp_result_name, header=None)	# load the file
	combined_data.append(data)							# insert the data to list

	for num in range(2, 6):								# uploading other .xls files
		temp_result_name = result_name.format(num)
		try:
			data = pd.read_excel(temp_result_name, header=None)
			data = data.ix[:, 2]							# get only third column of uploaded data file
			combined_data.append(data)
		except FileNotFoundError:
			print ("File " + temp_result_name + " not found.")

	# concat all uploaded data to one data set
	sim_table = pd.concat(combined_data, axis=1)
	print(sim_table)

	sub_data = {}
	# create separate data sets for different data
	sub_data["runda"] = sim_table.ix[0, 1:]
	sub_data["sprzedaz"] = sim_table.ix[1, 1:]
	sub_data["udzial"] = sim_table.ix[2, 1:]
	sub_data["wynik_firmy"] = sim_table.ix[3, 1:]
	sub_data["gotowka"]= sim_table.ix[4, 1:]
	sub_data["wolumen"] = sim_table.ix[5, 1:]
	sub_data["jakosc"] = sim_table.ix[6, 1:]
	sub_data["cena"] = sim_table.ix[7, 1:]
	sub_data["reklama_tv"] = sim_table.ix[8, 1:]
	sub_data["reklama_int"] = sim_table.ix[9, 1:]
	sub_data["reklama_mag"] = sim_table.ix[10, 1:]

	return sub_data

def main():
	new_result_name = 'wyniki{}.xls'			# .xls name scheme
	old_result_name = 'old_games/wyniki{}.xls'

	# import data from previous simulation
	old_data = load_data(old_result_name)
	new_data = load_data(new_result_name)

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
	plt.plot(old_data["runda"], old_data["sprzedaz"], 'b-')
	plt.plot(new_data["runda"], new_data["sprzedaz"], 'r-')
	plt.legend(['Sprzedane old', 'Sprzedane new'])
	plt.xlabel('Runda')
	plt.ylabel('Sztuki towaru')

	plt.show()

if __name__ == "__main__":
    main()
