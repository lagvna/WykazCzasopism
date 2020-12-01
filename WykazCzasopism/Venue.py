# Venue class for creating journal objects described by appropriate attributes:
# - title
# - issn
# - e-issn
# - score
# - category
# Since there are not so many categories in the MNiSW journal list, they were created manually as a dictionary,
# from which objects can extract categories to which they belong

class Venue:
	categories_dict = {
		'8':'archeologia',
		'9':'filozofia',
		'10':'historia',
		'11':'językoznawstwo',
		'12':'literaturoznawstwo',
		'13':'nauki o kulturze i religii',
		'14':'nauki o sztuce',
		'15':'architektura i urbanistyka',
		'16':'automatyka, elektronika i elektrotechnika',
		'17':'informatyka techniczna i telekomunikacja',
		'18':'inżynieria biomedyczna',
		'19':'inżynieria chemiczna',
		'20':'inżynieria lądowa i transport',
		'21':'inżynieria materiałowa',
		'22':'inżynieria mechaniczna',
		'23':'inżynieria środowiska, górnictwo i energetyka',
		'24':'nauki farmaceutyczne',
		'25':'nauki medyczne',
		'26':'nauki o kulturze fizycznej',
		'27':'nauki o zdrowiu',
		'28':'nauki leśne',
		'29':'rolnictwo i ogrodnictwo',
		'30':'technologia żywności i żywienia',
		'31':'weterynaria',
		'32':'zootechnika i rybactwo',
		'33':'ekonomia i finanse',
		'34':'geografia społeczno-ekonomiczna i gospodarka przestrzenna',
		'35':'nauki o bezpieczeństwie',
		'36':'nauki o komunikacji społecznej i mediach',
		'37':'nauki o polityce i administracji',
		'38':'nauki o zarządzaniu i jakości',
		'39':'nauki prawne',
		'40':'nauki socjologiczne',
		'41':'pedagogika',
		'42':'prawo kanoniczne',
		'43':'psychologia',
		'44':'astronomia',
		'45':'informatyka',
		'46':'matematyka',
		'47':'nauki biologiczne',
		'48':'nauki chemiczne',
		'49':'nauki fizyczne',
		'50':'nauki o Ziemi i środowisku',
		'51':'nauki teologiczne'}

	def __init__(self, result):
		self.result = result
		self.title = result[1]
		self.issn = result[2]
		self.eissn = result[3]
		self.score = result[7]
		self.category = self.extract_categories()

	def extract_categories(self):
		categories = []

		for i in range(len(self.result)):
			if self.result[i] == 'x':
				categories.append(self.categories_dict[str(i)])

		return categories