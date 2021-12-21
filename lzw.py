from alphabets import alphabets_
from first_order_source import FirstOrderSource


class LZW():
    def __init__(self, num_bit = 10) -> None:
        self.max_dictionary_size = 2**num_bit
        self._num_bit = num_bit
    
    def __str__(self) -> str:
        return f"LZW_{self._num_bit}"

    def _start_dictionary(self, start=97, end=109) -> None:
        '''
            starts the dictionary with the characters
            between 'start' and 'end'.

            start = 97 is 'a'
            end = 109 is 'm' (excluded, so is from 'a' to 'l')

            those numbers are Unicode values.
        '''
        self.dictionary = { 
            chr(i) : i 
            for i in range(start, end)
        }
    
    def _update_dictionary(self, new_string: str) -> None:
        '''
            adds 'new_string' to the dictionary if not full.
        '''
        dictionary_size = len(self.dictionary)

        if dictionary_size <= self.max_dictionary_size:
            self.dictionary[new_string] = dictionary_size



    # what about launching Huffman after this?
    def compress(self, text: str) -> str:
        def convert_to_str(compressed_data: list, delimitier = ''):
            result = ""

            for code in compressed_data:
                result = result + str(code) + delimitier

            return result


        self._start_dictionary()
        compressed_data = []
        string = ""

        for symbol in text:                     
            string_plus_symbol = string + symbol

            if string_plus_symbol in self.dictionary: 
                string = string_plus_symbol
            else:
                self._update_dictionary(string_plus_symbol)
                compressed_data.append(self.dictionary[string])
                string = symbol

        return convert_to_str(compressed_data)


    def decompress(self) -> None:
        pass