import os
from PIL import Image

def main(inputs: dict, context):
  pdf_paths: list[str] = []
  ocr_result = inputs["ocr_result"]

  for i, ocr in enumerate(ocr_result):
    image_path = ocr["path"]
    base_path, image_name = os.path.split(image_path)
    image_name, _ = os.path.splitext(image_name)
    image = Image.open(image_path)
    image = image.convert("RGB")

    pdf_path = os.path.join(base_path, f"{image_name}.pdf")
    image.save(pdf_path)
    pdf_paths.append(pdf_path)

    context.report_progress(float(i + 1) / float(len(ocr_result)))

  context.output(pdf_paths, "pdf_paths", True)
