import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# B1: Import thư viện và các phần bổ trợ
# smtplib lib sử dụng để gửi email qua giao thức SMTP (Simple Mail Transfer Protocol).
# MIMEMultipart: tạo email đa phần
# MIMEText: tạo các phần nội dung trong mail dưới nhiều dạng
# MIMEBase: tạo các phần của email như đính kèm

# B2: Tạo function gửi mail với các tham số:
# email ng gửi, email người nhận, password người gửi (là password mã hóa được cấp bởi tài khoản google cho 1 ứng dụng muốn truy cập gmail)
# (Lấy password: Vào Gg Account, vào Security-->Chon 2-Step Vertification-->chọn App passwords)
# nội dung tiêu đề email, nội dung bên trong dưới dạng HTMLm đường dẫn file attached

def send_email(sender_email, sender_password, recipient_email, subject, html_content, attachment_paths):
# Cài đặt nội dung mail gồm người gửi, ng nhận, chủ đề mail
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

# tạo nội dung HTML với list các mục nội dung cần liệt kê, ảnh hiển thị và đường link
    list_content = ""
# vòng lặp sẽ hiển thị các list thành phần trong sale_name
    for sale_name in html_content:
        list_content += f"<li>{sale_name}</li>"

# Thêm nội dung hình ảnh, link, list trong body dưới dạng HTML
    HTML = f"""
    <html>
        <body>
        <h2>Danh sách sản phẩm ở file đính kèm</h2>
        <img src= "https://picsum.photos/200/300.jpg">
        <p>Truy cập website để xem thêm nhiều sản phẩm mới:\n <a href="https://vmgfashion.com/">Website</a></p>
        <ul>
            {list_content}
        </ul>
        <br></br>
        <p>Phạm Hải Thanh.
        <br>0xxxxxx</br></p>
        </body>
    </html>
    """
    message.attach(MIMEText(HTML, 'html'))

# Đính kèm nhiều file có sẵn trong máy tính (file đính kèm ở nhiều định dạng)
# vòng lặp duyệt mở các tệp đính kèm, mã hóa và đính kèm các file attachment vào email
    for attachment_path in attachment_paths:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {attachment_path.split('/')[-1]}")
            # message.attach(part)

    # Tạo hoạt đọng gửi SMTP
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_email, sender_password)

    # Gửi mail, gửi thành công in ra thông báo
    session.sendmail(sender_email, recipient_email, message.as_string())
    session.quit()
    print("Email đã được gửi thành công!")

#B3: Truyền dữ liệu vào tham số

sender_email = "xxx@gmail.com"
sender_password = "xxxxx"
recipient_email = "xxx@gmail.com"
subject = "EMail tự động"
sale_names = ["Sản phẩm 1", "Sản phẩm 2"]
attachment_paths = [r"C:\Users\ASUS\Downloads\woman-working-office.jpg", r"C:\Users\ASUS\Downloads\dhl_express_packing_guide_en.pdf"]


send_email(sender_email, sender_password, recipient_email, subject, sale_names, attachment_paths)