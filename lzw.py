class LZW():
    def __init__(self, num_bit = 10, separator = ',') -> None:
        self.max_dictionary_size = 2**num_bit
        self._num_bit = num_bit
        self._separator = separator
    
    def __str__(self) -> str:
        return f"LZW_nbit:{self._num_bit}"

    def _start_dictionary(self, text: str) -> None:
        '''
            starts the dictionary with the characters in 'text'
        '''
        self.dictionary = { 
            char : i 
            for i, char in enumerate(set(text))
        }
    
    def _update_dictionary(self, new_string: str) -> None:
        '''
            adds 'new_string' to the dictionary if not full.
        '''
        dictionary_size = len(self.dictionary)

        if dictionary_size <= self.max_dictionary_size:
            self.dictionary[new_string] = dictionary_size


    def compress(self, text: str) -> str:
        def convert_to_str(compressed_data: list):
            result = ""
            for code in compressed_data:
                result = result + str(code) + self._separator
            return result

        self._start_dictionary(text)
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
        
        if string in self.dictionary:       
            compressed_data.append(self.dictionary[string])
        
        return convert_to_str(compressed_data)
        
    def find_key(self, value):
        for key,val in self.dictionary.items():
            if str(val) == str(value):
                return key
        return None


    def decompress(self, compressed_data) -> str:
        compressed_data_list = compressed_data.split(',')
        compressed_data_list = compressed_data_list[:-1]

        output = ""

        for code in compressed_data_list:
            key = self.find_key(code)
            output = output + key

        return output

