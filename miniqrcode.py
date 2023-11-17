from qrcode import *
qr=QRCode(
    version=15,
    box_size=10,
    border=5
)
data="https://www.youtube.com/@kdninfotech7244"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="white",back_color="black")
img.save("kdnqr.png")