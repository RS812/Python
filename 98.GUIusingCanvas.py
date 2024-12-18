from tkinter import *
import math

def draw_ashok_chakra(Canvas, x, y, radius):
    # Draw the outer circle
    Canvas.create_oval(x - radius, y - radius, x + radius, y + radius,width=2)

    # Draw the spokes
    for i in range(24):
        angle = i * (360 / 24)
        x1 = x + radius * 0.8 * math.cos(math.radians(angle))
        y1 = y + radius * 0.8 * math.sin(math.radians(angle))
        x2 = x + radius * math.cos(math.radians(angle))
        y2 = y + radius * math.sin(math.radians(angle))
        Canvas.create_line(x1, y1, x2, y2,width=1)
scr=Tk()
scr.geometry("800x600")
scr.title("ToolKit Interface Demo")
cv=Canvas(scr,bg="Orange",height="100")
cv.pack()
cv1=Canvas(scr,bg="White",height="100")
cv1.pack()
cv2=Canvas(scr,bg="Green",height="100")
cv2.pack()
chakra_x = 400  # Center X position for the chakra
chakra_y = 150  # Center Y position for the chakra
chakra_radius = 30  # Radius of the chakra

draw_ashok_chakra(cv1, chakra_x, chakra_y, chakra_radius)
scr.mainloop()
