import streamlit as st
import random
import math
from PIL import Image

# Improved Prime Check using Square Root
def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

# Optimized Modular Inverse using Extended Euclidean Algorithm
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y

def mod_inverse(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def rsa_keygen():
    p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)
    while p == q:
        q = generate_prime(1000, 5000)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randint(3, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)
    d = mod_inverse(e, phi_n)
    return (e, n), (d, n), (p, q)

# Encryption and Decryption functions
def encrypt(message, public_key):
    e, n = public_key
    message_encoded = [ord(char) for char in message]
    ciphertext = [pow(char, e, n) for char in message_encoded]
    return ciphertext

def decrypt(ciphertext, private_key):
    d, n = private_key
    message_encoded = [pow(char, d, n) for char in ciphertext]
    message = ''.join(chr(char) for char in message_encoded)
    return message

# Encrypt and Decrypt Files
def encrypt_file(file, public_key):
    e, n = public_key
    content = file.read()
    ciphertext = [pow(byte, e, n) for byte in content]
    return ciphertext

def decrypt_file(ciphertext, private_key):
    d, n = private_key
    content = bytes([pow(byte, d, n) for byte in ciphertext])
    return content

# Streamlit UI
st.set_page_config(page_title="Advanced RSA Encryption", page_icon="🔒")

st.title("Advanced RSA Encryption & Decryption")
st.sidebar.markdown("""
### How RSA Works
1. **Key Generation**:
   - Generate two large prime numbers `p` and `q`.
   - Compute `n = p * q`.
   - Compute the totient function `φ(n) = (p-1) * (q-1)`.
   - Choose an integer `e` such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`.
   - Compute the private key `d` such that `d ≡ e⁻¹ (mod φ(n))`.

2. **Encryption**:
   - Convert the message into an integer `m`.
   - Compute the ciphertext `c = m^e mod n`.

3. **Decryption**:
   - Compute the original message `m = c^d mod n`.
""")

if st.button("Generate Keys"):
    with st.spinner("Generating RSA keys..."):
        public_key, private_key, primes = rsa_keygen()
        p, q = primes
        st.session_state.public_key = public_key
        st.session_state.private_key = private_key
        st.write(f"Public Key: {public_key}")
        st.write(f"Private Key: {private_key}")
        st.write(f"Primes p: {p}, q: {q}")

message = st.text_input("Enter a message to encrypt:")
if st.button("Encrypt Message"):
    if "public_key" in st.session_state:
        public_key = st.session_state.public_key
        with st.spinner("Encrypting message..."):
            ciphertext = encrypt(message, public_key)
            st.session_state.ciphertext = ciphertext
        st.write(f"Encrypted Message: {ciphertext}")
    else:
        st.warning("Please generate keys first.")

if st.button("Decrypt Message"):
    if "private_key" in st.session_state and "ciphertext" in st.session_state:
        private_key = st.session_state.private_key
        ciphertext = st.session_state.ciphertext
        with st.spinner("Decrypting message..."):
            decrypted_message = decrypt(ciphertext, private_key)
        st.write(f"Decrypted Message: {decrypted_message}")
    else:
        st.warning("Please encrypt a message first.")

uploaded_file = st.file_uploader("Choose a file to encrypt")
if st.button("Encrypt File"):
    if uploaded_file is not None and "public_key" in st.session_state:
        public_key = st.session_state.public_key
        file_size = len(uploaded_file.getbuffer())
        st.write(f"File size: {file_size} bytes")
        with st.spinner("Encrypting file..."):
            ciphertext = encrypt_file(uploaded_file, public_key)
            st.session_state.file_ciphertext = ciphertext
        st.success("File encrypted successfully.")
    else:
        st.warning("Please upload a file and generate keys first.")

if st.button("Decrypt File"):
    if "private_key" in st.session_state and "file_ciphertext" in st.session_state:
        private_key = st.session_state.private_key
        ciphertext = st.session_state.file_ciphertext
        with st.spinner("Decrypting file..."):
            decrypted_content = decrypt_file(ciphertext, private_key)
        st.download_button("Download Decrypted File", data=decrypted_content, file_name="decrypted_file")
    else:
        st.warning("Please encrypt a file first.")
