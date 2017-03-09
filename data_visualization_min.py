# import Pandas (data manipulation) and Matplotlib (trending)
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec

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

def preparire_figure_minimal(data_type, old_data, aprox_data, new_data):
	plt.figure(data_type + 'MINIMAL')
	plt.plot(old_data["runda"], old_data[data_type], 'b-')
	plt.plot(aprox_data["runda"], aprox_data[data_type], 'g--')
	plt.plot(new_data["runda"], new_data[data_type], linewidth=2, linestyle="-", c="red")
	plt.legend([data_type + ' best', data_type + ' aprox', data_type + ' new'], loc='upper left')
	plt.xlabel('runda')
	plt.ylabel(data_type)
	plt.grid()

def main():
	new_result_name = 'E:/new_data/wyniki{}.xls'			# .xls name schemes
	best_result_name = 'old_games/1/wyniki{}.xls'			#

	# other good data sets
	old_2_result_name = 'old_games/2/wyniki{}.xls'
	old_3_result_name = 'old_games/3/wyniki{}.xls'
	old_4_result_name = 'old_games/4/wyniki{}.xls'

	# import data from simulations
	best_old_data = load_data(best_result_name)
	new_data = load_data(new_result_name)

	old_2_data = load_data(old_2_result_name)
	old_3_data = load_data(old_3_result_name)
	old_4_data = load_data(old_4_result_name)

	# TODO: aprox of multiple historical values
	aprox_data = best_old_data.copy()
	num_of_old_data = 4

	aprox_data["sprzedaz"] = (best_old_data["sprzedaz"] + old_2_data["sprzedaz"] + old_3_data["sprzedaz"] + old_4_data["sprzedaz"]) / num_of_old_data
	aprox_data["udzial"] = (best_old_data["udzial"] + old_2_data["udzial"] + old_3_data["udzial"] + old_4_data["udzial"]) / num_of_old_data
	aprox_data["wynik_firmy"] = (best_old_data["wynik_firmy"] + old_2_data["wynik_firmy"] + old_3_data["wynik_firmy"] + old_4_data["wynik_firmy"]) / num_of_old_data
	aprox_data["gotowka"] = (best_old_data["gotowka"] + old_2_data["gotowka"] + old_3_data["gotowka"] + old_4_data["gotowka"]) / num_of_old_data
	aprox_data["wolumen"] = (best_old_data["wolumen"] + old_2_data["wolumen"] + old_3_data["wolumen"] + old_4_data["wolumen"]) / num_of_old_data
	aprox_data["jakosc"] = (best_old_data["jakosc"] + old_2_data["jakosc"] + old_3_data["jakosc"] + old_4_data["jakosc"]) / num_of_old_data
	aprox_data["cena"] = (best_old_data["cena"] + old_2_data["cena"] + old_3_data["cena"] + old_4_data["cena"]) / num_of_old_data
	aprox_data["reklama_tv"] = (best_old_data["reklama_tv"] + old_2_data["reklama_tv"] + old_3_data["reklama_tv"] + old_4_data["reklama_tv"]) / num_of_old_data
	aprox_data["reklama_int"] = (best_old_data["reklama_int"] + old_2_data["reklama_int"] + old_3_data["reklama_int"] + old_4_data["reklama_int"]) / num_of_old_data
	aprox_data["reklama_mag"] = (best_old_data["reklama_mag"] + old_2_data["reklama_mag"] + old_3_data["reklama_mag"] + old_4_data["reklama_mag"]) / num_of_old_data

	# prepaire figures for all interesting data (MINIMAL)
	preparire_figure_minimal("udzial", best_old_data, aprox_data, new_data)
	preparire_figure_minimal("wynik_firmy", best_old_data, aprox_data, new_data)
	preparire_figure_minimal("gotowka", best_old_data, aprox_data, new_data)
	preparire_figure_minimal("wolumen", best_old_data, aprox_data, new_data)
	preparire_figure_minimal("jakosc", best_old_data, aprox_data, new_data)
	preparire_figure_minimal("cena", best_old_data, aprox_data, new_data)
	preparire_figure_minimal("sprzedaz", best_old_data, aprox_data, new_data)
	preparire_figure_minimal("reklama_tv", best_old_data, aprox_data, new_data)
	preparire_figure_minimal("reklama_int", best_old_data, aprox_data, new_data)
	preparire_figure_minimal("reklama_mag", best_old_data, aprox_data, new_data)
	# end MINIMAL

	# show each figure in separate window
	plt.show(block = False)

	# wait for user to close the simulation
	input("\nPress Enter key to close visualization...")

if __name__ == "__main__":
    main()
