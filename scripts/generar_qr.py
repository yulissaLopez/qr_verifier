import qrcode

url = "https://qrverifier-production.up.railway.app/verificacion/verificar/"

qr = qrcode.make(url)

qr.save("scmt_distintivo.png")

print(f"Codigo qr generado con url {url}")
