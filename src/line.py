from src.point import Point
from tkinter import Canvas

class Line():
    def __init__(self, pointA : Point, pointB: Point):
        self.pointA = pointA
        self.pointB = pointB

    def draw(self, canvas : Canvas, fill_color : str):
        canvas.create_line(
            self.pointA.x,
            self.pointA.y,
            self.pointB.x,
            self.pointB.y,
            fill=fill_color,
            width=2
        )