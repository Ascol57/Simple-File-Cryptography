# Simple File Cryptography

> Encrypt and decrypt my files easily

> Crypter et décrypter mes fichiers simplement

---

<p align="center">
  <strong><a href="#-english">English</a></strong>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <strong><a href="#-français">Français</a></strong>
</p>

---

## 🇬🇧 English

### 📖 About / History

I created this project to securely transfer files containing lists of passwords and API keys over networks that are not necessarily secure (email, Discord, etc.). The file, once encrypted, is included in an innocent-looking jpg image.

### 🔧 Installation

General installation :

```bash
git clone https://github.com/Ascol57/Simple-File-Cryptography.git
cd Simple-File-Cryptography
pip install cryptography
````

### 🚀 Usage

Encrypting a file:

```bash
python main.py -g -e file1 img.jpg
```

Without recreating the key.crt file:

```bash
python main.py -e file_in img.jpg
```

Decrypting a file:

```bash
python main.py -d img.jpg file_out
```

### 🙏 Acknowledgements

> ![Ascol57](https://img.shields.io/badge/Made_with_%E2%9D%A4%EF%B8%8F_by-Ascol-red?style=flat&logo=github)

-----

<br>
<br>
<br>
<br>

-----

## 🇫🇷 Français

### 📖 À propos / Histoire

J'ai fait ce projet pour transférer des fichiers contenants des listes de mots de passe, des clés d'API de façon sécurisé sur des réseaux pas forcements surs (mail, discord...). Le fichier, une fois crypté, est inclus dans une image jpg innocente.

### 🔧 Installation

Installation en général :

```bash
git clone https://github.com/Ascol57/Simple-File-Cryptography.git
cd Simple-File-Cryptography
pip install cryptography
```

### 🚀 Utilisation

Crypter un fichier :

```bash
python main.py -g -e file1 img.jpg
```

Sans recréer le key.crt :

```bash
python main.py -e file_in img.jpg
```

Décrypter un fichier :

```bash
python main.py -d img.jpg file_out
```

### 🙏 Remerciements

> ![Ascol57](https://img.shields.io/badge/Fait_avec_%E2%9D%A4%EF%B8%8F_par-Ascol-red?style=flat&logo=github)
