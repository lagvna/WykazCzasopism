from VenueSearcher import *
import csv

def print_help():
	print("POMOC\n")
	print("Składnia polecenia filtrowania to:")
	print("-t:nazwa, -s:punktacja, -c:kategoria")
	print("Pamiętaj o dwukropkach i przecinkach.\n")

# function allowing to find journals via their titles
# the search is done through a VenueSearcher class, which creates Venue objects denoting journals
# and then returns matches as a list of results to be printed 
def search_venue():
	try:
		title = input("Podaj tytuł czasopisma, którego szukasz: ")

		searcher = VenueSearcher("resources/wykaz.csv")
		results = searcher.search_by_title(title)

		print("Znaleziono {} pozycje: \n".format(len(results)))
		for item in results:
			print(item.title)
			print("ISSN: {}".format(item.issn))
			print("E-ISSN: {}".format(item.eissn))
			print("Punktacja: {}".format(item.score))
			print("Kategoria: {}".format(item.category))
			print()
	except:
		print("Nie znaleziono podanego czasopisma\n")

	
# function for filtering journals according to three parameters:
# - title
# - score
# - category
# it's possible to filter with only a subset of parameters
# the filtering command is parsed into a dictionary and then passed to the VenueSearcher object, which performs the search
# and returns a list of Venue objects denoting journals 
def filter_venues():
	try:
		command = input("Wpisz polecenie filtrowania wyników: \n")
		params = command.split(',')
		params_dict = dict((x.strip(), y.strip()) 
			for x, y in (element.split(':')
				for element in command.split(', ')))
		#print(params_dict)
		searcher = VenueSearcher("resources/wykaz.csv")
		results = searcher.search_by_params(params_dict)
		
		print("Znaleziono {} pozycje: \n".format(len(results)))

		
		for item in results:
			print(item.title)
			print("ISSN: {}".format(item.issn))
			print("E-ISSN: {}".format(item.eissn))
			print("Punktacja: {}".format(item.score))
			print("Kategoria: {}".format(item.category))
			print()
		save_results(results)

	except:
		print("Nieprawidłowe polecenie\n")


# function for saving (if desired) filterd results from filter_venues() function into a csv file
def save_results(results):

	while True:
		try:
			choice = str(input("Czy chcesz zapisać dane do pliku? (t/n): \n"))
			
			if choice.lower() == 't':
				filename = input("Podaj nazwę pliku, w którym chciałbyś zapisać wyniki: \n")
				file_to_output = open(filename+'.csv','w',newline='')
				csv_writer = csv.writer(file_to_output,delimiter=',')

				for item in results:
					csv_writer.writerow([item.title,item.issn,item.eissn,item.score,item.category])

				file_to_output.close()
				break

			if choice.lower() == 'n':
				break
		except:
			print('Nieprawodłowe polecenie\n')

			

######### Main part ###########
# this is just a simple text menu allowing to switch between functions and terminate

print("Program wspomagający wyszukiwanie informacji w aktualnym wykazie czasopism punktowanych MNiSW\n")

while True:
	print("(1) Wyszukaj czasopismo po nazwie")
	print("(2) Wyświetl czasopisma wg filtrów")
	print("(3) Wyświetl pomoc")
	print("(4) Zakończ program\n")

	try:
		choice = int(input("Wybierz opcję (1-4): \n"))
	except ValueError:
		print("Wybór musi być liczbą (1-4)!\n")
	else:
		if choice == 4:
			break
		elif choice == 3:
			print_help()
		elif choice == 2:
			filter_venues()
		elif choice == 1:
			search_venue()
		else:
			pass
