import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

path_encode = 'C:/Users/Francis/Desktop/Qrcode'
path_decode = 'C:/Users/Francis/Desktop/Qrcode/qrcode.png'
data = 'Crucificxo Motivate'
'''
# Encoding a QR Code
qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'black', back_color = 'grey')

img.save(path + '/motivateqrcode.png')
'''

# Decoding a QR Code
img = Image.open(path_decode)

result = decode(img)

print(result)