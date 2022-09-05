a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
     "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

b = ["K", "C", "P", "S", "V", "M", "H" ,"F", "D", "B", "U", "W",
     "Q", "N", "R", "Y", "T", "J", "O", "I", "X", "E", "L", "A", "Z", "G"]

cypher_type = input("Enter whether to encode or decode:").lower()

if cypher_type == "encode":
     plain_text = input("Enter the text to be encrypted: ").upper()
    
     def encrypt(text):
          cypher_text = ''
          for letter in plain_text:
               if letter in a:
                    plain_text_index = a.index(letter)
                    cypher_text += b[plain_text_index]
          print(f"The encrypted text is {cypher_text}")
     encrypt(text=plain_text)

if cypher_type == "decode":
     plain_text = input("Enter the text to be decrypted: ").upper()
     
     def decrypt(text):
          decypher_text = ''
          for letter in plain_text:
               if letter in b:
                    plain_text_index = b.index(letter)
                    decypher_text += a[plain_text_index]
          print(f"The decrypted text is {decypher_text}")
     decrypt(text = plain_text)
