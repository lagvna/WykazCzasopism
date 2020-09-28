from VenueSearcher import *

def print_help():
	print("POMOC\n")

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

	

print("Program wspomagający wyszukiwanie informacji w aktualnym wykazie czasopism MNiSW\n")

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
			pass
		elif choice == 1:
			search_venue()
		else:
			pass
