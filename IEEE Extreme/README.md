# Caesar Cipher Decrypter

This directory contains a simple C program, `caeser.c`, that decrypts a message encrypted with a Caesar cipher.

## `caeser.c`

This program reads a line of text from standard input and decrypts it using a hardcoded Caesar cipher key.

### Key Features:
- **Decrypts Text**: Shifts letters to the left to decrypt them.
- **Hardcoded Key**: Uses a fixed key of `12`.
- **Handles Case**: Works with both uppercase and lowercase English letters.
- **Wraps Alphabet**: Correctly handles letter wrapping (e.g., 'a' wraps to 'o').

### How to Compile

You can compile the program using a C compiler like `gcc`.

```bash
gcc caeser.c -o caeser
```

### How to Run

After compiling, you can run the executable. The program will wait for you to type a message.

```bash
./caeser
```

**Example:**

If you provide the encrypted message:
```
TQXA IADXP
```

The program will output the decrypted message:
```
HELLO WORLD
```
