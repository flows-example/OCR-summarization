import io
import base64

from PIL import Image
from PyPDF2 import PdfReader, PdfWriter, PageObject

def main(inputs: dict, context):
  # https://pikepdf.readthedocs.io/en/latest/

  pdf_writer = PdfWriter()
  ocr_result = inputs["ocr_result"]
  pdf_paths = inputs["pdf_paths"]

  for i, ocr in enumerate(ocr_result):
    with open(pdf_paths[i], "rb") as image_pdf_file:
      image_pdf = PdfReader(image_pdf_file)
      image_pdf_page = image_pdf.pages[0]
      page = PageObject.create_blank_page(
        width=image_pdf_page.mediabox.width,
        height=image_pdf_page.mediabox.height,
      )
      page.merge_page()
      page.merge_page(image_pdf_page, expand=False)
      pdf_writer.add_page(page)

    context.report_progress(float(i + 1) / float(len(ocr_result)))

  pdf_handle = io.BytesIO()
  pdf_writer.write(pdf_handle)

  pdf_handle.seek(0)
  bin_data = pdf_handle.read()
  str_data = base64.b64encode(bin_data).decode("utf-8")

  context.output(str_data, "bin", True)