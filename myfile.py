import qrcode

def generate_qr(url, filename="qr.png"):
    img = qrcode.make(url)
    img.save(filename)
    print(f"QR code saved as {filename}")