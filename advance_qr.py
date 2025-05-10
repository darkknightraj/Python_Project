import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=13,
    border=2,
)
qr_url = input("Enter the URL: ")
qr.add_data(qr_url)
qr.make(fit=True)
#Even if you provide a small version number (like 1),
# it will automatically increase the version internally if needed,
# so the data fits properly.
img = qr.make_image(fill_color="purple", back_color="cyan")
img.save('github_qr.png')
img.show()  