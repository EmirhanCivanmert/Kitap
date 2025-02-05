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
            files = request.FILES.getlist('file')
            output_dir = os.path.join(settings.MEDIA_ROOT, "converted")
            os.makedirs(output_dir, exist_ok=True)

            success_messages = []
            error_messages = []

            for uploaded_file in files:
                try:
                    input_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
                    output_path = os.path.join(output_dir, f"{os.path.splitext(uploaded_file.name)[0]}.pdf")

                    # Dosyayı geçici olarak kaydet
                    with open(input_path, 'wb') as f:
                        for chunk in uploaded_file.chunks():
                            f.write(chunk)

                    # PDF'e dönüştürme işlemi
                    file_to_pdf(input_path, output_path)
                    
                    success_messages.append(f"{uploaded_file.name} başarıyla dönüştürüldü.")

                except Exception as e:
                    error_messages.append(f"{uploaded_file.name} dönüştürülemedi: {str(e)}")

            return render(request, "pdfconverter/convert.html", {
                'form': form,
                'success_messages': success_messages,
                'error_messages': error_messages
            })
    else:
        form = UploadForm()

    return render(request, "pdfconverter/convert.html", {"form": form})
