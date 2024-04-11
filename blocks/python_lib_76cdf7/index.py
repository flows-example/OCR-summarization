import os
import shutil
import itertools

from PyPDF2 import PdfReader
from PIL import Image

def main(inputs: dict, context):
  # to see https://gist.github.com/jrsmith3/9947838

  pdf_file_path = inputs["pdf_file"]
  images_saved_path = inputs["images_saved"]
  resolution = inputs.get("resolution", 400)
  begin_page_index = inputs.get("begin_page", 1) - 1
  end_page_index = inputs.get("end_page", None)

  clear_folder(images_saved_path)
  image_names: list[str] = []
  all_tasks_count = float(max(end_page_index - begin_page_index + 1, 1))
  image_index: int = 0

  with open(pdf_file_path, "rb") as file:
    pdf = PdfReader(file)
    for page in itertools.islice(pdf.pages, begin_page_index, end_page_index):

      if len(page.images) <= 0:
        continue

      image_index += 1
      image = page.images[0]
      _, image_ext = os.path.splitext(image.name)
      image_name = f"{image_index}{image_ext}"

      with open(os.path.join(images_saved_path, image_name), "wb") as image_file:
        print(image)
        image_file.write(image.data)

      image_names.append(image_name)
      context.report_progress(float(len(image_names)) / all_tasks_count)

  context.output(images_saved_path, "images_path", False)
  context.output(image_names, "image_names", False)
  context.done()

def clear_folder(folder_path: str):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)