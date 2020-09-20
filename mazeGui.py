import pygame,os,math
from pathFind import  Path
from grid import GridClass

os.environ['SDL_VIDEO_CENTERED'] = '1'


black = (0,0,0)
white = (255,255,255)
red = (255,128,128)
green = (0,255,150)
blue = (0,0,255)
font = "Georgia.ttf"

class guiClass(GridClass):

    def __init__(self,grid):


        self.grid = grid
        self.width = 600
        self.height = 600
        self.bg_color = (0xff,0xff,0xff)
        self.block_size = int(min(self.width,self.height)/max(self.grid.get_col(),self.grid.get_row()))

        self.window = None 

        self.gui_callback()

    
    def get_dir(self,pt1,pt2):

        dx = pt1[0] - pt2[1]
        dy = pt1[1] - pt2[0]

        if dx == 1 and dy == 0:
            return 180
        elif dx == -1 and dy == 0:
            return 0

        if dy == -1 and dx == 0:
            return -90
        elif dy == 1 and dx == 0:
            return 90

        return 0


    def draw_arrow1(self,point1,angle):

        size = self.block_size
        x,y = point1
 
        # Load arrow image
        arrow_png = pygame.image.load("arrow_png.png")
        
        # Scale
        arrow_png = pygame.transform.scale(arrow_png, (int(0.75*size) ,int(0.75*size)))

        #Rotate

        arrow_png = pygame.transform.rotate(arrow_png,angle)

        # Blit and show
        self.window.blit(arrow_png,[size*(x+0),y*size])
        pygame.display.flip()


                
    def create_window(self):

        pygame.init()

        self.window  = pygame.display.set_mode((self.width,self.height))
        self.window.fill(self.bg_color)
        pygame.display.set_caption("Maze Solver 1.0")

        x1 = 0
        rows,cols = self.grid.get_row(),self.grid.get_col()


        # Draw start and end squares
        pygame.draw.rect(self.window,red,(0,0,self.block_size,self.block_size))
        pygame.draw.rect(self.window,red,((rows-1)*self.block_size,(cols-1)*self.block_size,self.block_size,self.block_size))

        #Draw grid
        for col in range(cols):

            x1 = y2 = col*self.block_size
  
            pygame.draw.line(self.window,black,(x1,0),(x1,self.height))
            pygame.draw.line(self.window,black,(0,y2),(self.width,y2))

        pygame.display.flip()
        self.fillMaze()

        lastx,lasty = (rows-1)*self.block_size,(cols-1)*self.block_size


        fontsize = int(self.block_size//4)
        self.render_text("START",font,fontsize,white,(0.5*self.block_size,0.5*self.block_size))
        self.render_text("END",font,fontsize,white,(lastx + 0.5*self.block_size , lasty +0.5*self.block_size ))



    def render_text(self,text,font,fontSize,color,center):
        
        font = pygame.font.Font(font, fontSize)

        text = font.render(text, True, color)

        text_rect = text.get_rect()

        text_rect.center = center

        self.window.blit(text,text_rect)

        pygame.display.update()


      
        

    def fillMaze(self):

        x,y = self.block_size,0
        rows, cols = self.grid.get_row(),self.grid.get_col()

        for i in range(rows):
            x = 0
            for j in range(cols):
                
                if self.grid.islocked(i,j):
            
                    rect = pygame.Rect(x,y,self.block_size-1,self.block_size-1)
                    pygame.draw.rect(self.window,black,rect)

                x += self.block_size
            y += self.block_size

            pygame.display.flip()


            
    
    def gui_callback(self):

        running = True
        maze_solution = None #Path(row,col,test_grid).BFS(start,end)
        
        alg = "BFS"
        while not maze_solution:
            print("Generating a maze with a solution...")
            test_grid.generate_maze()
            maze_solution = eval("Path(row,col,test_grid)."+alg+"(start,end)")  #Path(row,col,test_grid).BFS(start,end)

        self.create_window()
        
             
        for i in range(1,len(maze_solution[:-1])):

            r,c = maze_solution[i][0],maze_solution[i][1]
            
            
            if self.grid.islocked(r,c):
                continue
            else:
                x = c*self.block_size
                y = r*self.block_size

                rect = pygame.Rect(x,y,self.block_size-1,self.block_size-1)
                pygame.draw.rect(self.window,green,rect)

                angle = self.get_dir((c,r),maze_solution[i+1])

                self.draw_arrow1((c,r),angle)
                pygame.display.update(rect)

                pygame.time.delay(50)
 

        # Check for closing event
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Close window
                    running = False
                    pygame.quit()
                    quit()

    

if __name__ == "__main__":


    row ,col = 20,20
    start = (0,0)
    end = (row-1,col-1)
    test_grid = GridClass(row,col)

    


    maze = guiClass(test_grid)      
    