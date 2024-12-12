import pyqrcode

# 保存するQRコードのファイル名
FILE_PNG_A = 'qrcode_A.png'
FILE_PNG_B = 'qrcode_B.png'

# サーバー上のPDFのURL
pdf_url_A = 'http://localhost:8000/img/test_A.pdf'
pdf_url_B = 'http://localhost:8000/img/test_B.pdf'

# QRコード作成（test_A.pdf）
code_A = pyqrcode.create(pdf_url_A, error='L', version=3, mode='binary')
code_A.png(FILE_PNG_A, scale=5, module_color=[0, 0, 0, 128], background=[255, 255, 255])

# QRコード作成（test_B.pdf）
code_B = pyqrcode.create(pdf_url_B, error='L', version=3, mode='binary')
code_B.png(FILE_PNG_B, scale=5, module_color=[0, 0, 0, 128], background=[255, 255, 255])

print(f"QRコードが生成されました: {FILE_PNG_A}, {FILE_PNG_B}")
