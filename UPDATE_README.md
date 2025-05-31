# 🔗 URL Shortener + QR Code Generator

This is a fork of the original [URL Shortener](https://github.com/ezhil56x/URL-Shortener) project, with an added feature: **QR Code Generation** for shortened URLs.

---

## 📌 Project Overview

This application allows users to convert long URLs into shorter, more shareable links. These short links redirect users to the original URL and help save space and improve link usability on social platforms.

---

## ✨ New Feature: QR Code Generator

### 🔍 Description

A new feature has been added that lets users **generate a QR code** for any given URL. The QR code is saved as an image file (`qr.png`) and can be scanned using any mobile device to open the link instantly.

### ✅ Benefits

- **Improved Accessibility** – Scannable links for phones/tablets  
- **Offline Use** – QR codes can be printed or embedded in physical materials  
- **Easy Sharing** – No need to type or copy-paste links  

---

## 🛠️ Implementation Details

- **New File Added:** `myfile.py`
- **Function:** `generate_qr(url, filename="qr.png")`
- **Library Used:** [`qrcode`](https://pypi.org/project/qrcode/)

### Example Code
```python
import qrcode

def generate_qr(url, filename="qr.png"):
    img = qrcode.make(url)
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    url_to_shorten = input("Enter the URL: ")
    generate_qr(url_to_shorten)
