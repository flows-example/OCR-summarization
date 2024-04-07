import cv2
import tempfile

from base64 import b64encode
from PIL import Image

def main(inputs: dict, context):
  # opencv codes are copied from https://zhuanlan.zhihu.com/p/64543244
  image_path = inputs["image_path"]
  preprocess = inputs["preprocess"]
  image = cv2.imread(image_path)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
  elif preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)

  with tempfile.NamedTemporaryFile(delete=True, suffix=".png") as temp_file:
    cv2.imwrite(temp_file.name, gray)
    bin_content = temp_file.read()

  base64_content = b64encode(bin_content).decode("utf-8")
  context.output(base64_content, "image_bin", True)