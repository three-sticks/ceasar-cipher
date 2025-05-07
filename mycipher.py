import sys

if len(sys.argv) != 2:
    print("Usage: python3 mycipher.py <shift>")
    sys.exit(1)

try:
    shift = int(sys.argv[1]) % 26  
except ValueError:
    print("Shift must be an integer.")
    sys.exit(1)

text = ''
for line in sys.stdin:
    text += line.upper()

filtered_text = ''.join([char for char in text if char.isalpha()])

ciphered_text = ''
for char in filtered_text:
    shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    ciphered_text += shifted_char

for i in range(0, len(ciphered_text), 5):
    block = ciphered_text[i:i+5]
    if i > 0 and i % 50 == 0:
        print()
    print(block, end='')

print() 
