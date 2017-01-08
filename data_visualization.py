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
	#print(sim_table)

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

	#print(sub_data)

	return sub_data

def preparire_figure(data_type, old_data, aprox_data, new_data):
	plt.figure(data_type)
	plt.plot(old_data["runda"], old_data[data_type], 'b-')
	plt.plot(aprox_data["runda"], aprox_data[data_type], 'g--')
	plt.plot(new_data["runda"], new_data[data_type], linewidth=2, linestyle="-", c="red")
	plt.legend([data_type + ' best', data_type + ' aprox', data_type + ' new'])
	plt.xlabel('runda')
	plt.ylabel(data_type)
	plt.grid()

def main():
	new_result_name = 'E:/new_data/wyniki{}.xls'			# .xls name schemes
	best_result_name = 'old_games/1/wyniki{}.xls'			#

	# for testing
	test_result_name = 'old_games/zm/wyniki{}.xls'			#

	# TODO: read multiple old data sets

	# import data from previous simulation
	best_old_data = load_data(best_result_name)
	test_data = load_data(test_result_name)
	new_data = load_data(new_result_name)

	# TODO: aprox of multiple historical values
	aprox_data = best_old_data.copy()
	aprox_data["sprzedaz"] = (best_old_data["sprzedaz"] + test_data["sprzedaz"])/2
	aprox_data["udzial"] = (best_old_data["udzial"] + test_data["udzial"])/2
	aprox_data["wynik_firmy"] = (best_old_data["wynik_firmy"] + test_data["wynik_firmy"])/2
	aprox_data["gotowka"] = (best_old_data["gotowka"] + test_data["gotowka"])/2
	aprox_data["wolumen"] = (best_old_data["wolumen"] + test_data["wolumen"])/2
	aprox_data["jakosc"] = (best_old_data["jakosc"] + test_data["jakosc"])/2
	aprox_data["cena"] = (best_old_data["cena"] + test_data["cena"])/2

	# prepaire figures for all interesting data
	preparire_figure("udzial", best_old_data, aprox_data, new_data);
	preparire_figure("wynik_firmy", best_old_data, aprox_data, new_data);
	preparire_figure("gotowka", best_old_data, aprox_data, new_data);
	preparire_figure("wolumen", best_old_data, aprox_data, new_data);
	preparire_figure("jakosc", best_old_data, aprox_data, new_data);
	preparire_figure("cena", best_old_data, aprox_data, new_data);
	preparire_figure("sprzedaz", best_old_data, aprox_data, new_data);

	# show each figure in separate window
	plt.show(block = False)

	# wait for user to close the simulation
	input("Press any key to close visualization...")

if __name__ == "__main__":
    main()
