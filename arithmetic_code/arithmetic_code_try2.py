from functools import reduce

alphabets_ = {
    "a" : 5,
    "b" : 5,
    "c" : 5,
    "d" : 5,
    "e" : 5,
    "f" : 5,
    "g" : 5,
    "h" : 5,
    "i" : 5,
    "l" : 5,
    "m" : 5,
    "n" : 5,
    "o" : 5,
    "p" : 5,
    "q" : 5,
    "r" : 5,
    "s" : 5,
    "t" : 5,
    "u" : 5,
    "v" : 2.5,
    "z" : 2.5,

}

class ArtithmeticEncoder:
    def __init__(self, alphabet: dict) -> None:
        self.alphabet = alphabet
        self._characters = list(alphabet.keys())
        self.max_probability = reduce(lambda a,b : a+b, alphabet.values())
        print("Max probability is: " + str(self.max_probability))
        self.lx_limit = 0
        self.rx_limit = self.max_probability

    def _getIntervals(self, alphabet:dict):     #Funzione che restituisce gli intervalli per i caratteri dell'alfabeto.
        intervals = {}      #Un dizionario nuovo
        palo = self.lx_limit
        for char in alphabet:
            p_char = alphabet[char]   #Probabilità dell'i-esimo char
            tuple_to_add = (palo, (p_char * self.max_probability) + palo)
            intervals[char] = (tuple_to_add)
            palo = tuple_to_add[1] + 1
        return intervals
    
    def encode(self, message:str, alphabet:dict):  #Il metodo prende una stringa da codificare e ritorna un intero che rappresenta la codifica del messaggio.
        encoded_msg = 0
        intervals = self._getIntervals(alphabet)
        high = self.max_probability
        low = 0

        for char in message:
            range = high - low
            high = low + (range * intervals[char][1])       #Qui prendo il secondo elemento della tupla assegnata alla chiave char, quindi il massimo range del carattere
            low = low + (range * intervals[char][0])        #Qui prendo il primo elemento della tupla, cioè il minimo range assegnato al carattere

        encoded_msg = low
        return encoded_msg


def main():
    encoder = ArtithmeticEncoder(alphabets_)
    intervals_ = encoder._getIntervals(alphabets_)
    print("The intervals are: ")
    print(intervals_)
    msg_to_encode = "ciao"
    encoded_msg_ = encoder.encode(msg_to_encode, alphabets_)
    print(encoded_msg_)

if __name__ == "__main__":
    main()
