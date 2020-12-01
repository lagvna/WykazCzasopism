import csv
from .Venue import Venue

# VenueSearcher class allows to open the MNiSW journal list file, search for results accordingly and then return
# results as objects which can be easily displayed

class VenueSearcher(object):

	def __init__(self, path):
		self.path = path

	# method for finding journals by title
	# it returns all journals containing the provided title (perhaps as a substring)
	def search_by_title(self, title):
		try:
			data = open(self.path, encoding="utf-8")
			csv_data = csv.reader(data)
			venues = list(csv_data)
		except:
			print("File not found!\n")

		results = []
		for data_line in venues:
			if  title.lower() in data_line[1].lower():
				result = Venue(data_line)
				results.append(result)
				#print(results)

		return results


	# this method loads the entire MNiSW journal list into the class, so they can be handled later
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

	# method for searching for results according to the given parameters
	# it takes the entire list of journals and then drops the ones which don't match with the given filters
	def search_by_params(self, params_dict):
		results = self.load_everything()
		
		if params_dict['-t'] != None:
			results = [x for x in results if str(params_dict['-t']).lower() in str(x.title).lower()]
		if params_dict['-s'] != None:
			results = [x for x in results if str(params_dict['-s']) == str(x.score)]
		if params_dict['-c'] != None:
			results = [x for x in results if str(params_dict['-c']) in str(x.category)]

		return results