import os
import shutil
import itertools
import pdfplumber

def main(inputs: dict, context):
  pdf_file_path = inputs["pdf_file"]
  images_saved_path = inputs["images_saved"]
  resolution = inputs.get("resolution", 400)
  begin_page_index = inputs.get("begin_page", 1) - 1
  end_page_index = inputs.get("end_page", None)

  clear_folder(images_saved_path)
  image_names: list[str] = []

  with pdfplumber.open(pdf_file_path) as pdf:
    for i, page in itertools.islice(enumerate(pdf.pages), begin_page_index, end_page_index):
      image_name = f"{i + 1}.png"
      image = page.to_image(resolution=resolution)
      image.save(os.path.join(images_saved_path, image_name))
      image_names.append(image_name)

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