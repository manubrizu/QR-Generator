import qrcode
import image

qr = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=12,
    border=2)
data = "http://165.227.202.250/login/index.php"
qr.add_data(data)
qr.make(fit =True)
img = qr.make_image(fill = 'Black',back_color = 'White')
img.save("image.png")
from IPython.display import display, Image 
display(Image(filename='image.png'))