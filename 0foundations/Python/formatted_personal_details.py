letter="<|name|> is this and was born on <|dateofbirth|> in <|placeofbirth|> and now he is living in <|currentplace|>"
name=input("Enter your name: ")
dateofbirth=input("Enter your date of birth: ")
placeofbirth=input("Enter your place of birth: ")   
currentplace=input("Enter your current place: ")
print(letter.replace("<|name|>",name).replace("<|dateofbirth|>",dateofbirth).replace("<|placeofbirth|>",placeofbirth).replace("<|currentplace|>",currentplace))
