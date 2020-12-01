from WykazCzasopism.VenueSearcher import VenueSearcher
import logging
from logging import StreamHandler
import csv
import click

root_logger = logging.getLogger()

@click.group()
@click.option('--quiet', default=False, is_flag=True, help='Run in silent mode')
def cli(quiet):
    """
    WykazCzasopism is a command line program which helps operating on the MNiSW
    list of scored journal/conference venues.
    """
    console_handler = StreamHandler()

    if quiet:
        root_logger.setLevel(logging.ERROR)
        console_handler.setLevel(logging.ERROR)

    else:
        root_logger.setLevel(logging.INFO)
        console_handler.setLevel(logging.INFO)
    logger_formatter = logging.Formatter('%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                                         datefmt='%y-%m-%d %H:%M:%S',)
    console_handler.setFormatter(logger_formatter)
    root_logger.addHandler(console_handler)

@cli.command('help', help='Help')
def print_help():
	print("Składnia polecenia filtrowania to:")
	print("-t nazwa, -s punktacja, -c kategoria\n")

# function allowing to find journals via their titles
# search is done through a VenueSearcher class, which creates Venue objects denoting journals
# and then returns matches as a list of results to be printed 
@cli.command('search', help='Search journal')
@click.option('--title', '-t', required=True, help='Journal title')
def search_venue(title):
	searcher = VenueSearcher("resources/wykaz.csv")
	results = searcher.search_by_title(title)

	print("Found {} records: \n".format(len(results)))
	for item in results:
		print(item.title)
		print("ISSN: {}".format(item.issn))
		print("E-ISSN: {}".format(item.eissn))
		print("Score: {}".format(item.score))
		print("Category: {}".format(item.category))
		print()
	
# function for filtering journals according to three parameters:
# - title
# - score
# - category
# it's possible to filter with only a subset of parameters
# the filtering command is parsed into a dictionary and then passed to the VenueSearcher object, 
# which performs the search and returns a list of Venue objects denoting journals 
@cli.command('filter', help='Filter journals with paramteres')
@click.option('--title', '-t', help='Journal title')
@click.option('--category', '-c', help='Journal category')
@click.option('--score', '-s', help='Journal score')
def filter_venues(title, category, score):
	params_dict = {'-t': title, '-c': category, '-s': score}
	searcher = VenueSearcher("resources/wykaz.csv")
	results = searcher.search_by_params(params_dict)
	
	print("Found {} records: \n".format(len(results)))

		
	for item in results:
		print(item.title)
		print("ISSN: {}".format(item.issn))
		print("E-ISSN: {}".format(item.eissn))
		print("Score: {}".format(item.score))
		print("Category: {}".format(item.category))
		print()
	save_results(results)


# function for saving (if desired) filterd results from filter_venues() function into a csv file
def save_results(results):

	while True:
		try:
			choice = str(input("Would you like to save results? (y/n): \n"))
			
			if choice.lower() == 'y':
				filename = input("Enter file name: \n")
				file_to_output = open(filename+'.csv','w',newline='')
				csv_writer = csv.writer(file_to_output,delimiter=',')

				for item in results:
					csv_writer.writerow([item.title,item.issn,item.eissn,item.score,item.category])

				file_to_output.close()
				break

			if choice.lower() == 'n':
				break
		except:
			print('Invalid command\n')

			

#-----------------------------------------------------
if __name__ == '__main__':
    cli()