import qrcode as qr
qr_url=input("Enter the URL: ")
img = qr.make(qr_url)
img.save('github_qr.png')
img.show()