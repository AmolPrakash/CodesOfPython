def encrypt(plainText, shift): 
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  print ("Your ciphertext is: ", cipherText)
  return cipherText

def decrypt(cipherText, shift): 
  cleanText = ""
  for ch in cipherText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet < ord('a'):
        stayInAlphabet += 26
      finalLetter = chr(stayInAlphabet)
      cleanText += finalLetter
  print ("Your text is: ", cleanText)
  return cipherText

