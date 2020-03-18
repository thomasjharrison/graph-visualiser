import PyQt5
import pygame
import math


class codeLoop: #Run the logic loop
    def __init__(self, w, h): #width, height
        global width, height, window, graph
        width, height = w, h, 
        graph = Graph(5, 5)

        self.renderer = Renderer()

        self.clock = pygame.time.Clock()

        while self.update(): #Run loop
            self.renderer.render()

    def update(self): #Update the program
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.VIDEORESIZE:
                global width, height
                width, height = ev.w, ev.h
                window = pygame.display.set_mode((width, height), pygame.RESIZABLE)    
                graph.findParams()      
        return True


class Renderer: #Render the objects in order
    def __init__(self):
        global window
        window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption("graph visualiser")

    def render(self): #Render the screen
        window.fill((0, 0, 0))
        graph.drawAxes()
        pygame.display.update()


class Graph: #Draw the graph axes
    def __init__(self, xs, ys): #x scale, y scale
        self.xs, self.ys = xs, ys
        self.findParams()

    def findOrigin(self): #Finds the origin
        self.x_origin, self.y_origin = width / 2, height / 2

    def findScale(self): #Finds the scale
        self.x_scale, self.y_scale = (width / 2) / self.xs, (height / 2) / self.ys

    def findParams(self): #Central parameter setter
        self.findOrigin()
        self.findScale()
        self.scaleLogic()

    def scaleLogic(self): #Works out the logic for spacing the scale indicators
        if height * 0.01 < width * 0.01:
            self.scaleThickness = height * 0.01
        else:
            self.scaleThickness = width * 0.01

    def drawScale(self): #Draws the scale of the graph
        for pos in range(-self.xs + 1, self.xs):
            if pos != 0:
                pygame.draw.line(window, (40, 40, 40), (round(self.x_origin + (pos * self.x_scale)), round(self.y_origin + self.scaleThickness)), (round(self.x_origin + (pos * self.x_scale)), round(self.y_origin - self.scaleThickness)), 1)
        
        for pos in range(-self.ys + 1, self.ys):
            if pos != 0:
                pygame.draw.line(window, (40, 40, 40), (round(self.x_origin + self.scaleThickness), round(self.y_origin + (pos * self.y_scale))), (round(self.x_origin - self.scaleThickness), round(self.y_origin + (pos * self.y_scale))), 1)
        
    def drawAxes(self): #Draws the graph
        pygame.draw.line(window, (40, 40, 40), (self.x_origin, 0), (self.x_origin, height), 2)
        pygame.draw.line(window, (40, 40, 40), (0, self.y_origin), (width, self.y_origin), 2)
        self.drawScale()

    def drawPoint(self, x, y): #Draw a point on graph
        pygame.draw.circle(window, (255, 255, 255), (round(self.x_origin + (x * self.x_scale)), round(self.y_origin + (-y * self.y_scale))), 0)


if __name__ == "__main__":
    logic = codeLoop(900, 900)