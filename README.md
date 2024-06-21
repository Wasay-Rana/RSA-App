# Advanced RSA Encryption App

This project is an interactive RSA encryption and decryption application built using Streamlit. It offers an user-friendly interface to generate RSA keys, encrypt and decrypt messages, and handle file encryption and decryption. The app also provides a detailed explanation of how the RSA algorithm works, making it both a functional tool and an educational resource.

## Features

- **RSA Key Generation**: Generate secure public and private RSA keys.
- **Message Encryption and Decryption**: Encrypt and decrypt messages using the generated RSA keys.
- **File Encryption and Decryption**: Encrypt and decrypt files, with file size display and download functionality for decrypted files.
- **Interactive Visuals**: Real-time feedback during key generation, encryption, and decryption processes.
- **Educational Sidebar**: Step-by-step explanation of the RSA algorithm with a visual representation.

## Screenshot

![UI Image](/images/app_ui.png)

## How RSA Works

### Key Generation
1. **Generate Primes**: Generate two large prime numbers `p` and `q`.
2. **Compute n**: Calculate `n = p * q`.
3. **Totient Function**: Compute `φ(n) = (p-1) * (q-1)`.
4. **Choose e**: Select an integer `e` such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`.
5. **Compute d**: Find the private key `d` such that `d ≡ e⁻¹ (mod φ(n))`.

### Encryption
1. **Convert Message**: Convert the message into an integer `m`.
2. **Compute Ciphertext**: Calculate the ciphertext `c = m^e mod n`.

### Decryption
1. **Decrypt Ciphertext**: Recover the original message `m = c^d mod n`.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Streamlit
- PIL (Python Imaging Library)
- Matplotlib (Optional, if you want to add plots)

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/rsa-encryption-app.git
   cd rsa-encryption-app
   ```

2. **Install the Required Packages**:
   ```sh
   pip install -r requirements.txt
   ```

### Running the App

1. **Run the Streamlit App**:
   ```sh
   streamlit run app.py
   ```

2. **Open in Browser**:
   The app will open in your default web browser. If it doesn't, navigate to `http://localhost:8501` in your browser.

## Usage

1. **Generate Keys**: Click the "Generate Keys" button to create RSA keys.
2. **Encrypt Message**: Enter a message in the input box and click "Encrypt Message" to encrypt it.
3. **Decrypt Message**: Click "Decrypt Message" to decrypt the encrypted message.
4. **Encrypt File**: Upload a file and click "Encrypt File" to encrypt it.
5. **Decrypt File**: Click "Decrypt File" to decrypt the uploaded file and download it.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements. I have made this as a side project to better understand my Information Security Class topic, so your efforts will be greatly appreciated.
