# Caesar Cipher (Encryption & Decryption)

A Python script that encrypts and decrypts text using a Caesar cipher — 
a classic substitution cipher that shifts each letter by a fixed number 
of positions in the alphabet.

## Skills Shown
- String handling and iteration
- Modular arithmetic (`%`)
- ASCII/character conversion using `ord()` and `chr()`
- Function design and code reuse

## How It Works
The script:
- Takes a message and a shift key (an integer) from the user
- Encrypts the message by shifting each letter forward by the shift 
  value, wrapping around the alphabet using modulo 26
- Decrypts the message by reversing the shift
- Leaves spaces, numbers, and punctuation unchanged

## Example
Enter your message: Room 42B
Enter shift key (number): 3
Encrypted: Urrp 42E
Decrypted: Room 42B

## Design Decisions
The core transformation is `(ord(char) - base + shift) % 26 + base`, 
where `base` is 65 for uppercase letters or 97 for lowercase — this 
converts each letter to a 0–25 position, applies the shift, wraps 
around the alphabet with modulo, then converts back to a character.

For decryption, I initially considered simply calling `encrypt()` again 
with a negated shift (`encrypt(text, -shift)`), since decrypting is 
mathematically the inverse of encrypting. I chose instead to write 
`decrypt()` as its own explicit function with the same loop structure, 
subtracting the shift directly. This duplicates a small amount of code, 
but makes the function self-contained and easier to read on its own — 
a deliberate trade-off between conciseness and clarity.

Non-alphabetic characters (spaces, digits, punctuation) are passed 
through unchanged by checking `char.isalpha()` before applying the 
shift, so messages retain their original formatting after encryption 
and decryption.

## Known Limitation
As the project brief notes, the Caesar cipher is not cryptographically 
secure — it has only 25 possible keys, making it trivial to brute-force, 
and it preserves letter-frequency patterns, making it vulnerable to 
frequency analysis. This project demonstrates the underlying logic of 
encryption/decryption rather than a production-grade security solution.