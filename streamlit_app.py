import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# Streamlit 앱 제목 설정
st.title("QR 코드 생성기")

# URL 입력 받기
url = st.text_input("QR 코드로 만들 URL을 입력하세요", "https://www.example.com")

# QR 코드 생성 버튼
if st.button("QR 코드 생성"):
    if url:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # QR 코드 이미지를 메모리에 저장
        img = qr.make_image(fill="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # 이미지를 웹 페이지에 표시
        st.image(buffer, caption="생성된 QR 코드", use_column_width=True)

        # 다운로드 링크 제공
        btn = st.download_button(
            label="QR 코드 이미지 다운로드",
            data=buffer,
            file_name="qrcode_image.png",
            mime="image/png"
        )
    else:
        st.error("유효한 URL을 입력하세요.")
