import cv2 as cv
import numpy as np
import assets.assets as ats

def load_image_cv_default() -> np.matrix:
  image_cv = cv.imread(ats.IMAGE_DEFAULT_PATH)
  image_cv = cv.transpose(image_cv)
  image_cv = cv.cvtColor(image_cv, cv.COLOR_BGR2RGB)
  return image_cv

def load_image_cv(file_path: str) -> np.matrix:
  image_cv = cv.imread(file_path)
  image_cv = cv.transpose(image_cv)
  image_cv = cv.cvtColor(image_cv, cv.COLOR_BGR2RGB)
  return image_cv

scale_ratio: float = 1
image_cv = load_image_cv_default()
