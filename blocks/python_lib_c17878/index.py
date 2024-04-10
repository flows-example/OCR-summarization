import os
import pdfplumber

def main(inputs: dict, context):
  ocr_list = inputs["ocr_result"]
  pdf_file_path = inputs["pdf_file"]
  begin_page_index = inputs["begin_page"] - 1

  with pdfplumber.open(pdf_file_path) as pdf:
    for i, page in enumerate(pdf.pages):
    #   if i < begin_page_index:
    #     continue
    #   index = i - begin_page_index

    #   if index >= len(ocr_list):
    #     break

    #   ocr = ocr_list[index]
      page.filter(lambda x: False)

  context.output("result value", "out", True)
