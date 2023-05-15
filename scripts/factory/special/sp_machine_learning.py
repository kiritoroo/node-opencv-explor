import pygame
import numpy as np
import cv2 as cv
from scripts.core.node_detail import NodeDetail
import assets.assets as ats
# from tensorflow import keras

# model_lp = keras.models.load_model(ats.LP_MODEL_PATH)

class SPMachineLearning(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Machine Learning"
    self.color_bg = color_bg
    self.size_panel_config = pygame.Rect(0, 0, 100, 30)
    super().__init__(self.node_name, self.color_bg, image)

  def __apply_effect(self):
    # self.image_apply = cv.transpose(self.image_apply)
    # self.image_apply = cv.resize(self.image_apply, (200, 200))
    # self.image_apply = np.expand_dims(self.image_apply, axis=0)
    # self.image_apply = np.array(self.image_apply)
    # self.image_apply = self.image_apply / 255
    # _boundingbox = model_lp.predict(self.image_apply)
    # _boundingbox = _boundingbox[0]*255

    # rescale_ratio_x = self.image_raw.shape[1] / 200
    # rescale_ratio_y = self.image_raw.shape[0] / 200
    # xmin_rescaled = int(_boundingbox[1] * rescale_ratio_x)
    # ymin_rescaled = int(_boundingbox[0] * rescale_ratio_y)
    # xmax_rescaled = int(_boundingbox[3] * rescale_ratio_x)
    # ymax_rescaled = int(_boundingbox[2] * rescale_ratio_y)
    
    # self.image_apply = cv.rectangle(self.image_raw.copy(),
    #   (xmin_rescaled, ymin_rescaled),
    #   (xmax_rescaled, ymax_rescaled),
    #   (0, 255, 0), thickness=2)
    
    if self.image_apply.ndim < 3:
      self.image_display = cv.cvtColor(self.image_apply.copy(), cv.COLOR_GRAY2RGB)
    else:
      self.image_display = self.image_apply.copy()

  def set_image(self, image_cv: np.matrix) -> None:
    self.image_raw = image_cv.copy()
    self.image_apply = image_cv.copy()
    self.image_display = image_cv.copy()
    self.__apply_effect()
    super().set_image(image_cv)
  
  def set_params(self):
    pass