import os
import json
import utils



here = os.path.dirname(os.path.abspath(__file__))
alphabets_path = os.path.join(here, 'alphabets.json')
alphabets_file = open(alphabets_path)
alphabets = utils.order_alphabets(json.load(alphabets_file))





#alphabets["NEW_25"] = new_alph_

for alph in alphabets:
    print(alph, utils.get_entropy(alphabets[alph]))  