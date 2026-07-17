import os
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

URL = "https://jingjingblackpink.github.io/Metal_Bash_Pro_Manual/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "金属浴PRO二维码_首页.png")

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white",
    module_drawer=RoundedModuleDrawer(),
)
img.save(OUT)
print(f"QR code saved to: {OUT}")
print(f"Content: {URL}")
print(f"Version: {qr.version}")
print(f"Image size: {img.size}")
