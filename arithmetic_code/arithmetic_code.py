from functools import reduce

class artithmetic_encoder:
    def __init__(self, alphabet: dict) -> None:
        self.alphabet = alphabet
        self._characters = list(alphabet.keys());
        self.max_probability = reduce(lambda a,b : a+b, alphabet.values())
        self.lx_limit = 0
        self.rx_limit = self.max_probability

    def _calculate_interval(self, input_char: str) -> tuple:
        def _normalize_value():
            pass

        char_lx_limit = self.lx_limit

        for char in self._characters:
            char_probability = self.alphabet[char]

            if char == input_char:
                normalized_lx = _normalize_value(char_lx_limit)
                normalized_rx = _normalize_value(char_lx_limit + char_probability)
                return (normalized_lx, normalized_rx)

            char_lx_limit = char_lx_limit + char_probability

        

    def _process_char(self, char: str):
        '''
                TO_COMPLETE
        low_range, high_range = self._calculate_interval(char) 

        range = self.rx_limit - self.lx_limit
        self.rx_limit = self.lx_limit + (range * high_range)
        '''
        pass 

    def encode(self, text: str) -> int:
        for character in text:



    
