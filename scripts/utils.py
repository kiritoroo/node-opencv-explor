import pygame
import pygame.gfxdraw

def draw_rect_bordered(surface, width, height, border_thickness, color, border_color):
  pygame.draw.rect(surface, color, (border_thickness, border_thickness, width, height), 0)
  for i in range(1, border_thickness):
    pygame.draw.rect(surface, border_color, (border_thickness-i, border_thickness-i, width+5, height+5), 1)

def draw_rect_rounded(surface, rect, color, corner_radius):
  if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
    raise ValueError(f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

  pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
  pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
  pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
  pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

  pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
  pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
  pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
  pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

  rect_tmp = pygame.Rect(rect)

  rect_tmp.width -= 2 * corner_radius
  rect_tmp.center = rect.center
  pygame.draw.rect(surface, color, rect_tmp)

  rect_tmp.width = rect.width
  rect_tmp.height -= 2 * corner_radius
  rect_tmp.center = rect.center
  pygame.draw.rect(surface, color, rect_tmp)

def draw_rect_bordered_rounded(surface, rect, color, border_color, corner_radius, border_thickness):
  if corner_radius < 0:
    raise ValueError(f"border radius ({corner_radius}) must be >= 0")

  rect_tmp = pygame.Rect(rect)

  if border_thickness:
    if corner_radius <= 0:
        pygame.draw.rect(surface, border_color, rect_tmp)
    else:
        draw_rect_rounded(surface, rect_tmp, border_color, corner_radius)

    rect_tmp.inflate_ip(-2*border_thickness, -2*border_thickness)
    inner_radius = corner_radius - border_thickness + 1
  else:
    inner_radius = corner_radius

  if inner_radius <= 0:
    pygame.draw.rect(surface, color, rect_tmp)
  else:
    draw_rect_rounded(surface, rect_tmp, color, inner_radius)

def draw_arrow(surface, start_pos: pygame.math.Vector2, end_pos: pygame.math.Vector2, arrow_width: float, arrow_length: float, color: pygame.Color, thickness: int):
  triangle_top = end_pos[0] - arrow_length, end_pos[1]
  triangle_left = end_pos[0] - arrow_width, end_pos[1] - arrow_width
  triangle_right = end_pos[0] - arrow_width, end_pos[1] + arrow_width
  pygame.draw.polygon(surface, color, [triangle_top, triangle_left, triangle_right])
  pygame.draw.line(surface, color, start_pos, triangle_top, thickness)
