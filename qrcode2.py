import qrcode

qr = qrcode.QRCode(border=4,
                   box_size=10,
                   version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('I am aditya')
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color="white")
img.save("adi.png")
