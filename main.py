import xml.etree.ElementTree as et
import re

TAGS = [
	'entry',
	'ti',
	'au',
	'a',
	'trd',
	'ed',
	'det',
	'pl',
	'pb',
	'y',
	'f',
	'p',
	'bib',
	'ex',
	'tr',
	'res',
	'ae',
]

STEPS = ['entry', 'det', 'res', 'au', 'ae', 'ae_se']

id_pattern = re.compile('^\d{2}\.\d{1,3}((bis)|(ter))?$')
id_in_text_pattern = re.compile('[^>\s]\d{2}\.\d{1,3}[^<\s]')
path_to_dir = '/home/aaron/MiMoText/Fehlersuche/ma_lueschow_programmcode/Python/erstausgaben/tagged/'

year_range = range(52, 101)


def pretty_print(docs):
	for doc in docs:
		print('======')
		print(doc + ":")
		print('======')
		for tag in TAGS:
			for step in STEPS:
				print(str(docs[doc][step][tag]) + " ", end='')
			print("\t" + tag)
		print()


# Searches through the raw files and finds matches fo the id pattern in an attempt to find erroneous entries
def scan_raw_files():
	for year_number in year_range:
		if year_number == 60 or year_number == 70 or year_number == 80 or year_number == 90:
			continue
		print(year_number)
		if year_number == 100:
			file = open(path_to_dir + 'raw/00.txt')
		else:
			file = open(path_to_dir + 'raw/' + str(year_number) + '.txt')

		matches = id_in_text_pattern.findall(file.read())

		print(matches)


# Goes through all _tagged.xml files for each year and counts how often each tag appears
# Allows for a slightly easier analysis of the files
def check_tagged_files():
	# Declare dictionary used to track data
	doc_map = dict()

	# List used to keep track of document ids that do not match the proper pattern
	oopsies = list()

	# List used to keep track of doubled up document ids
	doubled = list()

	for year_number in year_range:
		print("Counting year " + str(year_number))
		if year_number == 60 or year_number == 70 or year_number == 80 or year_number == 90:
			continue
		for step in STEPS:
			# Read the xml file from each step in the process into tree
			if year_number == 100:
				tree = et.parse(path_to_dir + step + '/00_tagged.xml')
			else:
				tree = et.parse(path_to_dir + step + '/' + str(year_number) + '_tagged.xml')

			root = tree.getroot()

			for document in root:
				doc_id = document.find('entry').find('id').text
				matched = bool(id_pattern.search(doc_id))

				# Check if the document id is properly formatted, if not, add to oopsie list
				if not matched:
					if doc_id not in oopsies:
						oopsies.append(doc_id)
				else:
					if doc_id not in doc_map:
						doc_map[doc_id] = dict()
					elif step == 'entry':
						doubled.append(doc_id)
					doc_map[doc_id][step] = dict()
					for tag in TAGS:
						tag_count = len(document.findall('.//' + tag))
						doc_map[doc_id][step][tag] = tag_count

	pretty_print(doc_map)
	print("Incorrectly formatted IDs: " + str(oopsies))
	print("Doubled IDs: " + str(doubled))


def main():
	scan_raw_files()
	check_tagged_files()


if __name__ == '__main__':
	main()
