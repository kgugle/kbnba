import requests
import sys
import re
from bs4 import BeautifulSoup
import csv
from collections import OrderedDict

def scrape(inp): #help by Sushain Cherivirala
	url = 'http://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fplayers%2F{}%2F{}01.html&div=div_totals'

	if __name__ == '__main__':
		p = inp
		script = requests.get(url.format(p[0], p)).text
		m = re.search(r'(<table class="sortable.*<\/table>)', script)
		table = m.groups()[0]

		s = ""
		dom = BeautifulSoup(table, "lxml")
		for tr in dom.findAll('tr')[1:]:
			if 'stat_total' not in tr.get('class', ''):
				season, team = None, None
				for i, td in enumerate(tr.findAll('td')):
					if i == 0:
						season_unf = td.getText()
						season = season_unf[0:4]
					if i == 2:
						team = td.getText()
						if len(team) > 3: team = '---'
				s+=season +"," + team + ","
		sf = s[:-1]
		return sf


    

def main():
	play = "Stephen Curry,Kevin Durant,LeBron James,Michael Jordan,Kobe Bryant"
	player = play.replace('-', '').replace('\'', '').replace('*','').replace('.','')

	player_list = []
	for p in player.split(","):
		player_list.append(p)

	codeified = []
	for element in player_list:
		c = element.split(" ")

		first_n = c[0]
		last_n = c[-1]
		first_n_cut = first_n[0:2]
		last_n_cut = last_n[0:5]
		word = last_n_cut + first_n_cut
		words = word.lower()
		codeified.append(words)
	codeified2 = [ii for n,ii in enumerate(codeified) if ii not in codeified[:n]]

	lemon = ""
	string_res = ""
	for elem in codeified2:

		string_res = scrape(elem)
		print(elem + "," + string_res)
		lemon += (string_res + "\n")
	print(lemon)

main()

	





