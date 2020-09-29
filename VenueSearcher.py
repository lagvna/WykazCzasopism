import csv
from Venue import *

class VenueSearcher:

	def __init__(self, path):
		self.path = path

	def search_by_title(self, title):
		try:
			data = open(self.path, encoding="utf-8")
			csv_data = csv.reader(data)
			venues = list(csv_data)
		except:
			print("Nie znaleziono pliku!\n")

		results = []
		for data_line in venues:
			if  title.lower() in data_line[1].lower():
				result = Venue(data_line)
				results.append(result)
				#print(results)

		return results

	def load_everything(self):
		try:
			data = open(self.path, encoding="utf-8")
			csv_data = csv.reader(data)
			venues = list(csv_data)
		except:
			print("Nie znaleziono pliku!\n")

		results = []
		for data_line in venues:
			result = Venue(data_line)
			results.append(result)
				#print(results)
		return results

	def search_by_params(self, params_dict):
		results = self.load_everything()

		if '-t' in params_dict.keys():
			results = [x for x in results if params_dict['-t'].lower() in x.title.lower()]
		if '-s' in params_dict.keys():
			results = [x for x in results if params_dict['-s'] == x.score]
		if '-c' in params_dict.keys():
			results = [x for x in results if params_dict['-c'] in x.category]

		return results