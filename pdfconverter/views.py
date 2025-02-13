import os
from io import BytesIO
from django.shortcuts import render
from django.conf import settings
from .forms import UploadForm
from docx import Document
from PIL import Image
from reportlab.pdfgen import canvas

def file_to_pdf(input_paths, output_path):

    pdf_canvas = canvas.Canvas(output_path)
    
    for input_path in input_paths:
        if input_path.endswith(".docx"):
            document = Document(input_path)

            for paragraph in document.paragraphs:
                pdf_canvas.drawString(100, 800, paragraph.text)
                pdf_canvas.showPage()

        elif input_path.endswith((".jpg", ".png")):
            pdf_canvas.drawImage(input_path, 0, 0)
            pdf_canvas.showPage()

    pdf_canvas.save()


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

                    with open(input_path, 'wb') as f:
                        for chunk in uploaded_file.chunks():
                            f.write(chunk)

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
