import os
import io
import pytesseract

from PIL import Image
from base64 import b64decode

os.environ["TESSDATA_PREFIX"] = "/oomol-storage/tesseract"

def main(inputs: dict, context):
  # To See https://zhuanlan.zhihu.com/p/142284785
  image_bin = b64decode(inputs["image_bin"])
  image = Image.open(io.BytesIO(image_bin))
  text = pytesseract.image_to_string(image, lang="chi_sim")
  context.output(text, "text", True)