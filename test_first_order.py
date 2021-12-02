from first_order_source import FirstOrderSource
from alphabets import alphabets_


TEXT_LEN = 100
# insert here the directory where files will be written.
FILE_PATH = "/home/fpy/Desktop/" 

const_source = FirstOrderSource(alphabets_["CONST"])
random_source = FirstOrderSource(alphabets_["RANDOM"])

const_source.write_file(TEXT_LEN, FILE_PATH+"const.txt")
random_source.write_file(TEXT_LEN, FILE_PATH+"random.txt")