import os
from io import BytesIO
from django.shortcuts import render
from django.conf import settings
from .forms import UploadForm
from docx import Document
from PIL import Image
from reportlab.pdfgen import canvas

def file_to_pdf(input_path, output_path):
    if input_path.endswith(".docx"):
        document = Document(input_path)
        pdf_canvas = canvas.Canvas(output_path)

        for paragraph in document.paragraphs:
            pdf_canvas.drawString(100, 800, paragraph.text)
            pdf_canvas.showPage()

        pdf_canvas.save()

    elif input_path.endswith((".jpg", ".png")):
        image = Image.open(input_path)
        pdf_bytes = BytesIO()
        image.convert("RGB").save(pdf_bytes, format="PDF")
        pdf_bytes.seek(0)

        with open(output_path, "wb") as f:
            f.write(pdf_bytes.read())

def convert_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            input_path = uploaded_file.file.path
            output_dir = os.path.join(settings.MEDIA_ROOT, "converted")
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{os.path.basename(uploaded_file.file.name)}.pdf")

            try:
                file_to_pdf(input_path, output_path)
                success_message = f"Dönüştürme Başarılı:  {output_path}"
            except Exception as e:
                success_message = f"Dönüştürmede Hata Oluştu: {str(e)}"

            return render(request, 'pdfconverter/convert.html', {
                "form" : form,
                "success" : success_message
            })
    else:
        form = UploadForm()

    return render(request, 'pdfconverter/convert.html', {"form" : form})