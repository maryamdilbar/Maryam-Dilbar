ciphertext = input("Password 12345678:")
for key in range(26):
    output = " "
    for char in ciphertext:
        if char .isalpha():
            base = ord('A') if char.isupper() else ord('a')
            output += chr((ord(char) - base - key) % 26 + base)
        else :
            output += char  
print(f"Key {key}: {output}")                    
                        
                        
                        
                        
                        
                        
                        

    