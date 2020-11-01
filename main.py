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

id_pattern = re.compile('^\d{2}\.\d{1,3}$')


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


def main():
	path_to_dir = '/home/aaron/MiMoText/Fehlersuche/ma_lueschow_programmcode/Python/erstausgaben/tagged/'
	year_number = '00'

	# Declare dictionary used to track data
	doc_map = dict()

	# List used to keep track of document ids that do not match the proper pattern
	oopsies = list()

	# List used to keep track of doubled up document ids
	doubled = list()

	for step in STEPS:
		# Read the xml file from each step in the process into tree
		tree = et.parse(path_to_dir + step + '/' + year_number + '_tagged.xml')
		root = tree.getroot()

		for document in root:
			doc_id = document.find('entry').find('id').text
			matched = bool(id_pattern.search(doc_id))

			# Check if the document id is properly formatted, if not, add to oopsie list
			if not matched:
				if not doc_id in oopsies:
					oopsies.append(doc_id)
			else:
				if not doc_id in doc_map:
					doc_map[doc_id] = dict()
				elif step == 'entry':
					print("DOUBLED UP " + doc_id)
				inc = 0
				doc_map[doc_id][step] = dict()
				for tag in TAGS:
					tag_count = len(document.findall('.//' + tag))
					doc_map[doc_id][step][tag] = tag_count

	pretty_print(doc_map)
	print()
	print(oopsies)


if __name__ == '__main__':
	main()
