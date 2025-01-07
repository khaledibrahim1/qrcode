import qrcode

qrcodeImg = qrcode.make('QrCode Maker With Python')

qrcodeImg.save('qrImages/myQrcode.png')