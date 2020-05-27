# With thanks to null-sleep for his prior project - https://github.com/null-sleep/Web-Scraper-for-Bulbapedia/blob/master/python-scraper/Scraper.py

from bs4 import BeautifulSoup as bs
import requests
import sqlalchemy

wiki_home_page = "http://bulbapedia.bulbagarden.net"
pokedex_list_page = wiki_home_page + "/wiki/List_of_Pokémon_by_National_Pokédex_number"
pkmn_stats = [ 	'id', 
				'name', 
				'type', 
				'abilities', 
				'hp', 
				'attack', 
				'defense', 
				'sp_atk', 
				'sp_def', 
				'speed', 
				'BST', 
				'weight', 
				'height', 
				'prev_form', 
				'next_forms']


# Takes every link on the pokedex_list_page, parses them using the LXML parser into a .txt file
# then adds every link text to a list and returns said list
def getPokemonUrls():
	pkmn_link_list = []

	listOfUrls = requests.get(pokedex_list_page)
	soup = bs(listOfUrls.text, "lxml")

	for a in soup.select('table[align="center"] td a[title*="Pok"]'):
		pkmn_link_list.append(a.attrs.get('href'))

	return pkmn_link_list

# for each URL passed into this function, get all the required stats
def getPokemonData(inputUrl):
	pkmn_data = []
	htmldata = requests.get(wiki_home_page + inputUrl)
	soup = bs(htmldata.txt, 'lxml')

	# Pokemon ID
	pkmn_data.append((soup.select( 'th big a[href*="mon_by_National_Pok"] span' ).get_text().replace('#', ''))

	#Pokemon name
	pkmn_data.append(soup.find('h1', class_='firstHeading').text[:-9])

	#Pokemon types
	pkmn_types = []

	for x in soup.select('a[href*="(type)"] span b'):
		pkmn_types.append(('a[href*="(type)"] span b').get_text())

	pkmn_data.append(pkmn_types)

	#Pokemon Abilities

	#Base Stats
	# Not sure how 'td table[cellspacing="0"] tr th' works, but I'm not questioning it
	pkmn_data.append((soup.select( 'td table[cellspacing="0"] tr th' )[ 1 ].get_text()))
	pkmn_data.append((soup.select( 'td table[cellspacing="0"] tr th' )[ 3 ].get_text()))
	pkmn_data.append((soup.select( 'td table[cellspacing="0"] tr th' )[ 5 ].get_text()))
	pkmn_data.append((soup.select( 'td table[cellspacing="0"] tr th' )[ 7 ].get_text()))
	pkmn_data.append((soup.select( 'td table[cellspacing="0"] tr th' )[ 9 ].get_text()))
	pkmn_data.append((soup.select( 'td table[cellspacing="0"] tr th' )[ 11 ].get_text()))
	pkmn_data.append((soup.select( 'td table[cellspacing="0"] tr th' )[ 13 ].get_text()))

	#Weight

	#Height

def allPokemonStats():
	pass

def writeToDB():
	pass

