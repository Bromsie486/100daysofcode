

class Caesar_Cipher():

    def __init__(self):
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", 
                         "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    

    def ask_for_input(self):
        user_input = {}
        user_input["direction"] = input("Encode or decode? ").lower()
        # while user_input["direction"] != "encode" or user_input["direction"] != "decode":
        #     user_input["direction"] = input("Please write either encode or decode.").lower()

        user_input["text"] = input("Type your message: ")
        user_input["shift"] = int(input("Type your shift number: "))

        return user_input


    def caesar(self, user_input):
        placeholder = ""

        for letter in user_input["text"]:
            if letter.isalpha():
                if user_input["direction"] == "encode":
                    position = self.alphabet.index(letter)
                    new_position = position + user_input["shift"]
                    placeholder += self.alphabet[new_position]
                else:
                    occurence_counter = 0
                    for char in self.alphabet:
                        if char == letter:
                            occurence_counter += 1
                            if occurence_counter == 2:
                                position = self.alphabet.index(char)
                    new_position = position - user_input["shift"]
                    placeholder += self.alphabet[new_position]
            else:
                placeholder += letter
        print(f"Your ciphered text is: {placeholder}")


    def main(self):
        user_input = self.ask_for_input()
        self.caesar(user_input)
        
if __name__ == "__main__":
    caesear_cipher = Caesar_Cipher()
    caesear_cipher.main()