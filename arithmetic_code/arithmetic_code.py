from math import floor

class ArithmeticEncoder:
    def __init__(self, alphabet: dict) -> None:
        self.alphabet = alphabet
        self.low = 0
        self.high = 999_999_999

    def _reset_encoder(self) -> None:
        '''
            resets low and high values to default values.
        '''
        self.low = 0
        self.high = 999_999_999

    def _get_interval(self, input_char: str) -> tuple:
        characters = list(self.alphabet.keys())
        char_interval_low = 0

        for char in characters:
            char_probability = self.alphabet[char]

            if char == input_char:
                char_interval_high = char_interval_low + char_probability
                return (char_interval_low, char_interval_high)

            # updating the low for the next char.    
            char_interval_low = char_interval_low + char_probability

    def _code_char(self, char: str) -> None:
        char_interval_low, char_interval_high = self._get_interval(char)
        interval_range = self.high - self.low

        self.high = self.low + floor(interval_range * char_interval_high)
        self.low = self.low + floor(interval_range * char_interval_low)

    def encode(self, text: str) -> int:
        self._reset_encoder()

        for char in text:
            self._code_char(char)
            print(self.low, self.high)
        return self.low
    
    def decode(self, coded_info: int) -> str:
        pass