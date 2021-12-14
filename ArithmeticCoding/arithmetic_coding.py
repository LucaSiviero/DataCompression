from math import floor

class ArithmeticCoding:
    def __init__(self, alphabet: dict, max_precision=999_999_999) -> None:
        self.alphabet = alphabet
        self._max_precision = max_precision
        self.low = 0
        self.high = max_precision
    
    def __str__(self):
        return "AritCod"

    def _reset(self) -> None:
        '''
            resets interval's low and high to default values.
        '''
        self.low = 0
        self.high = self._max_precision

    def _get_char_range(self, input_char: str) -> tuple:
        '''
            returns 'input_char' corresponding zero-one sub-range.
        '''
        characters = list(self.alphabet.keys())
        char_low = 0

        for char in characters:
            char_probability = self.alphabet[char]

            if char == input_char:
                char_high = char_low + char_probability
                return (char_low, char_high)

            # updating the low for the next char.    
            char_low = char_low + char_probability

    def _restrict_interval(self, char_low: int, char_high: int) -> None:
        '''
            modifies interval's extremes (shrinks the interval)
            according to char's zero-one subrange extremes 'char_low'
            and 'char_high'. 
        '''

        interval_size = self.high - self.low
        self.high = self.low + floor(interval_size * char_high)
        self.low = self.low + floor(interval_size * char_low)

    def _encode_char(self, char: str) -> None:
        '''
            codes a char by shrinking the encoder interval.
        '''
        char_low, char_high = self._get_char_range(char)
        self._restrict_interval(char_low, char_high)
    
    def _decode_char(self, coded_info: int) -> str:
        '''
            decodes a char by verify in which zero-one subranges
            the char occurs.
        '''
        characters = list(self.alphabet.keys())

        for char in characters:
            # char's low and high range extremes (in zero-one range)
            char_low, char_high = self._get_char_range(char)

            # calculating the char's low and high extremes inside
            # the encoder interval ('self.low' and 'self.high').
            interval_size = self.high - self.low
            char_interval_low = self.low + floor(interval_size * char_low)
            char_interval_high = self.low + floor(interval_size * char_high)

            if char_interval_low < coded_info < char_interval_high:
                self._restrict_interval(char_low, char_high)
                return char

    def encode(self, text: str) -> int:
        '''
            resets the encoder and encodes 'text' in a 
            integer value by applying '_encode_char' to each 
            char of 'text'.
            The returned value corresponds to the middle point 
            between the interval extremes ('self.low' and 'self.high')
            at the end of the encoding process.
        '''

        self._reset()

        for char in text: self._encode_char(char)
        encoded = self.low + floor((self.high - self.low)/2)
        return encoded
    
    def decode(self, coded_info: int) -> str:
        '''
            resets the encoder and decodes 'coded_info' into 
            the original text.
        '''

        self._reset()

        decoded_text = ""
        interval_info = self.low + floor((self.high - self.low)/2)

        while coded_info != interval_info:
            decoded_char = self._decode_char(coded_info)
            decoded_text = decoded_text + decoded_char
            interval_info = self.low + floor((self.high - self.low)/2)
        
        return decoded_text