from pdf2image import convert_from_path

pdf_file = "c-02.pdf"
poppler_path = r"C:\poppler\bin"  # Caminho até a pasta bin do Poppler

pages = convert_from_path(pdf_file, dpi=300, poppler_path=poppler_path)

for i, page in enumerate(pages, start=1):
    page.save(f"c-02-{i}.jpg", "JPEG")
    print(f"Página {i} salva")


# pip install pdf2image
# pip install pillow
