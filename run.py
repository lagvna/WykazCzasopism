from VenueSearcher import *
import csv
from matplotlib import pyplot as plt 
import numpy as np 

def print_help():
	print("POMOC\n")
	print("Składnia polecenia filtrowania to:")
	print("-t:nazwa, -s:punktacja, -c:kategoria\n")

def search_venue():
	try:
		title = input("Podaj tytuł czasopisma, którego szukasz: ")
		searcher = VenueSearcher("resources/wykaz.csv")
		results = searcher.search_by_title(title)

		print(f"Znaleziono {len(results)} pozycje: \n")
		for item in results:
			print(item.title)
			print(f"ISSN: {item.issn}")
			print(f"E-ISSN: {item.eissn}")
			print(f"Punktacja: {item.score}")
			print(f"Kategoria: {item.category}")
			print()
	except:
		print("Nie znaleziono podanego czasopisma\n")

	
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
		
		print(f"Znaleziono {len(results)} pozycje: \n")
		filename = input("Podaj nazwę pliku, w którym chciałbyś zapisać wyniki: \n")
		file_to_output = open(filename+'.csv','w',newline='')
		csv_writer = csv.writer(file_to_output,delimiter=',')
		
		for item in results:
			csv_writer.writerow([item.title,item.issn,item.eissn,item.score,item.category])

			print(item.title)
			print(f"ISSN: {item.issn}")
			print(f"E-ISSN: {item.eissn}")
			print(f"Punktacja: {item.score}")
			print(f"Kategoria: {item.category}")
			print()

		file_to_output.close()
	except:
		print("Nieprawidłowe polecenie\n")



def draw_chart():

	# Creating dataset 
	cars = ['AUDI', 'BMW', 'FORD', 
        		'TESLA', 'JAGUAR', 'MERCEDES'] 
	data = [23, 17, 35, 29, 12, 41] 

	fig = plt.figure(figsize =(10, 7)) 
	plt.pie(data, labels = cars) 
  
	plt.savefig("mygraph.png")

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
			draw_chart()
		elif choice == 2:
			filter_venues()
		elif choice == 1:
			search_venue()
		else:
			pass
