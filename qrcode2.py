import qrcode

qr = qrcode.QRCode(border=4,
                   box_size=10,
                   version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H)
message = input("Enter a message: ")
qr.add_data(message)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color="white")
image_address = input("Enter a file name: ")
img.save(image_address)
