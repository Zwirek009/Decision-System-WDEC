# Project: Decision Support WDEC - visually-based decision support system for enhancing company income in locally played with other teams market simulation 
# File: data_visualization.py - main Python file 
# Author: Maciej Wiraszka

# import Pandas (data manipulation) and Matplotlib (trending)
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec

# load set of data from multiple .xls files on specified localization and format (argument result_name)
def load_data(result_name):
	data = {}						# data gained from one result file
	combined_data = []				# list of sigle result file data	
	sim_table = {}					# combined data

	temp_result_name = result_name.format(1)			# name of first .xls file
	data = pd.read_excel(temp_result_name, header=None)	# load the file
	combined_data.append(data)							# insert the data to list

	for num in range(2, 9):								# uploading other .xls files
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


	return sub_data

# prepaire single figure visualization (MINIMAL version)
def preparire_figure_minimal(data_type, old_data, aprox_data, new_data):
	plt.figure(data_type + 'MINIMAL')
	plt.plot(old_data["runda"], old_data[data_type], 'b-')
	plt.plot(aprox_data["runda"], aprox_data[data_type], 'g--')
	plt.plot(new_data["runda"], new_data[data_type], linewidth=2, linestyle="-", c="red")
	plt.legend([data_type + ' best', data_type + ' aprox', data_type + ' new'], loc='upper left')
	plt.xlabel('runda')
	plt.ylabel(data_type)
	plt.grid()

# prepaire single figure visualization (MAXIMAL (default) version)
def preparire_figure_maximal(data_type, best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data):
	plt.plot(old_4_data["runda"], old_4_data[data_type], 'k-')
	plt.plot(old_3_data["runda"], old_3_data[data_type], 'm-')
	plt.plot(old_2_data["runda"], old_2_data[data_type], 'y-')
	plt.plot(best_old_data["runda"], best_old_data[data_type], linewidth=2, linestyle="-", c="blue")
	plt.plot(aprox_data["runda"], aprox_data[data_type], 'g--')
	plt.plot(new_data["runda"], new_data[data_type], linewidth=3, linestyle="-", c="red")
	plt.xlabel('runda')
	plt.ylabel(data_type)
	plt.grid()


def main():
	new_result_name = 'E:/new_data/wyniki{}.xls'			# .xls name schemes, .xls data from actual game (new_result_name) stored on external flash 												
	best_result_name = 'old_games/1/wyniki{}.xls'			# (due to simulation working on another computer) 

	# other good data sets
	old_2_result_name = 'old_games/2/wyniki{}.xls'			# historical good game sets .xls name schemas
	old_3_result_name = 'old_games/3/wyniki{}.xls'			#
	old_4_result_name = 'old_games/4/wyniki{}.xls'			#

	# import data from simulations
	best_old_data = load_data(best_result_name)
	new_data = load_data(new_result_name)

	old_2_data = load_data(old_2_result_name)
	old_3_data = load_data(old_3_result_name)
	old_4_data = load_data(old_4_result_name)

	aprox_data = best_old_data.copy()
	num_of_old_data = 4

	# create separate plots approximations
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
#	preparire_figure_minimal("udzial", best_old_data, aprox_data, new_data)
#	preparire_figure_minimal("wynik_firmy", best_old_data, aprox_data, new_data)
#	preparire_figure_minimal("gotowka", best_old_data, aprox_data, new_data)
#	preparire_figure_minimal("wolumen", best_old_data, aprox_data, new_data)
#	preparire_figure_minimal("jakosc", best_old_data, aprox_data, new_data)
#	preparire_figure_minimal("cena", best_old_data, aprox_data, new_data)
#	preparire_figure_minimal("sprzedaz", best_old_data, aprox_data, new_data)
#	preparire_figure_minimal("reklama_tv", best_old_data, aprox_data, new_data)
#	preparire_figure_minimal("reklama_int", best_old_data, aprox_data, new_data)
#	preparire_figure_minimal("reklama_mag", best_old_data, aprox_data, new_data)
	# end MINIMAL

	# prepaire figures for all interesting data (MAXIMAL (default))
	fig = plt.figure('Reklama')	# second figure
	fig.suptitle('Reklama', fontsize=20)
	gs = gridspec.GridSpec(3, 3)
	ax1 = fig.add_subplot(gs[:, 0])
	preparire_figure_maximal("reklama_tv", best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data)
	plt.legend(['fourth', 'third', 'second', 'best', 'aprox', 'new'], loc='upper left')	# show legend to one of plots in the figure
	ax1 = fig.add_subplot(gs[:, 1])
	preparire_figure_maximal("reklama_int", best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data)
	ax1 = fig.add_subplot(gs[:, 2])
	preparire_figure_maximal("reklama_mag", best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data)
	mng = plt.get_current_fig_manager()
	mng.full_screen_toggle()

	fig = plt.figure('Wyniki')	# first figure
	fig.suptitle('Wyniki', fontsize=20)
	gs = gridspec.GridSpec(2, 4)
	ax1 = fig.add_subplot(gs[0, :-2])
	preparire_figure_maximal("wynik_firmy", best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data)
	plt.legend(['fourth', 'third', 'second', 'best', 'aprox', 'new'], loc='upper left')	# show legend to one of plots in the figure
	ax1 = fig.add_subplot(gs[0, 2])
	preparire_figure_maximal("udzial", best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data)
	ax1 = fig.add_subplot(gs[0, 3])
	ax1.yaxis.tick_right()
	preparire_figure_maximal("gotowka", best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data)
	ax1 = fig.add_subplot(gs[1, 0])
	preparire_figure_maximal("wolumen", best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data)
	ax1 = fig.add_subplot(gs[1, 1])
	preparire_figure_maximal("jakosc", best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data)
	ax1 = fig.add_subplot(gs[1, 2])
	preparire_figure_maximal("cena", best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data)
	ax1 = fig.add_subplot(gs[1, 3])
	ax1.yaxis.tick_right()
	preparire_figure_maximal("sprzedaz", best_old_data, old_2_data, old_3_data, old_4_data, aprox_data, new_data)
	mng = plt.get_current_fig_manager()
	mng.full_screen_toggle()
	# end MAXIMAL

	# show each figure in separate window
	plt.show(block = False)

	# wait for user to close the simulation
	input("\nPress Enter key to close visualization...")

if __name__ == "__main__":
    main()
