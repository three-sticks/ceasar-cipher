import sys

# Make sure the user passed a shift value as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 mycipher.py <shift>")
    sys.exit(1)

try:
    shift = int(sys.argv[1]) % 26  # Ensure it's in 0-25 range
except ValueError:
    print("Shift must be an integer.")
    sys.exit(1)

# Read from stdin and convert to uppercase
text = ''
for line in sys.stdin:
    text += line.upper()

# Filter to keep only A-Z letters
filtered_text = ''.join([char for char in text if char.isalpha()])

# Apply Caesar cipher shift
ciphered_text = ''
for char in filtered_text:
    shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    ciphered_text += shifted_char

# Format output: blocks of 5 letters, 10 blocks per line
for i in range(0, len(ciphered_text), 5):
    block = ciphered_text[i:i+5]
    # Start a new line every 10 blocks (50 characters)
    if i > 0 and i % 50 == 0:
        print()
    print(block, end='')

print()  # Final newline at the end