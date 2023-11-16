

class Caesar_Cipher():

    def __init__(self):
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", 
                         "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    

    def ask_for_input(self):
        user_input = {}
        user_input["direction"] = input("Encode or decode?").lower()
        # while user_input["direction"] != "encode" or user_input["direction"] != "decode":
        #     user_input["direction"] = input("Please write either encode or decode.").lower()

        user_input["text"] = input("Type your message: ")
        user_input["shift"] = int(input("Type your shift number: "))

        return user_input


    def encode(self, user_input):
        cipher_text = ""
        for letter in user_input["text"]:
            position = self.alphabet.index(letter)
            new_position = position + user_input["shift"]
            cipher_text += self.alphabet[new_position]
        print(f"Your ciphered text is: {cipher_text}")


    def decode(self, user_input):
        plain_text = ""
        for letter in user_input["text"]:
            occurence_counter = 0
            for char in self.alphabet:
                if char == letter:
                    occurence_counter += 1
                    if occurence_counter == 2:
                        position = self.alphabet.index(char)
            new_position = position - user_input["shift"]
            plain_text += self.alphabet[new_position]
        print(f"Your original text is: {plain_text}")
        

    def main(self):
        user_input = self.ask_for_input()
        if user_input["direction"] == "encode":
            self.encode(user_input)
        elif user_input["direction"] == "decode":
            self.decode(user_input)
        
        
if __name__ == "__main__":
    caesear_cipher = Caesar_Cipher()
    caesear_cipher.main()