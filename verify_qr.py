import os
from PIL import Image
from pyzbar.pyzbar import decode

IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "金属浴PRO二维码_首页.png")

img = Image.open(IMG)
results = decode(img)

if not results:
    print("FAILED: No QR code found in image")
    exit(1)

for r in results:
    data = r.data.decode("utf-8")
    print(f"Decoded: {data}")
    print(f"Type: {r.type}")
    if data == "https://jingjingblackpink.github.io/Metal_Bash_Pro_Manual/":
        print("PASS: QR code matches expected URL")
    else:
        print(f"WARN: QR code does not match expected URL")
        print(f"  Expected: https://jingjingblackpink.github.io/Metal_Bash_Pro_Manual/")
        print(f"  Got:      {data}")
