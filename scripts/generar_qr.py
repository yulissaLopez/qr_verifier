import qrcode

url = "https://example.com/"

qr = qrcode.make(url)

qr.save("scmt_distintivo.png")

print(f"Codigo qr generado con url {url}")
