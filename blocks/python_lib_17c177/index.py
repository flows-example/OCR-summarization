import os
import io
import pytesseract

from PIL import Image
from base64 import b64decode

def main(inputs: dict, context):
  os.environ["TESSDATA_PREFIX"] = inputs["tessdata"]
  images_path = inputs["images_path"]
  image_names = inputs["image_names"]
  lang = inputs["lang"]
  ocr_result: list = []

  for image_name in image_names:
    image_path = os.path.join(images_path, image_name)
    image = Image.open(image_path)
    data = pytesseract.image_to_data(
      image, 
      lang=lang, 
      output_type=pytesseract.Output.DICT,
    )
    text = data["text"]
    left = data["left"]
    top = data["top"]
    width = data["width"]
    height = data["height"]

    ocr_result.append({
      "text": text,
      "left": left,
      "top": top,
      "width": width,
      "height": height,
    })
  context.output(ocr_result, "ocr_result", True)