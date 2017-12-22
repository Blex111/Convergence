from processing import *
boardsize = 9
s = 400
tile = s/boardsize
winsquare = boardsize/2
mx1 = None
my1 = None
movx = None
movy = None
king ="♔"
knight = "♖"
wizard = "♗"
cloud = "☁"
attack = "☆"
selected = 0

moveready = False
winpos = 4
turn="red"
pieceloc=[
        [0,0,0,0,7,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [7,0,0,0,0,0,0,0,7],
        [0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,4],
        [2,1,0,0,0,0,0,4,5],
        [3,2,1,0,7,0,4,5,6]
        ]



def drawboard():
  background(255)
  
  for i in range(boardsize):
    for j in range(boardsize):
      if i%2 == 0:
        
        if j%2 == 0:
          fill(0)
          rect(j*tile,i*tile,tile,tile)
      else:
        if j%2 != 0:
          fill(0)
          rect(j*tile,i*tile,tile,tile)
          
          
      #i = i+ 1;
      
  fill(255,255,0)
  rect(winsquare*tile-tile/2,winsquare*tile-tile/2,tile,tile)
      
      
   
   
def mouseClicked():
  
  global mx1,my1,selected
  
    
    
  selected = None
  mx = mouse.x
  mx -= tile/2
  my = mouse.y
  my -= tile/2
  
  mx1 = int(round(mx/tile))
  my1 = int(round(my/tile))
  
r_k = 0
b_k = 0
    
    
 
   
 
def piecerender():
  global r_k,b_k
  
  r_k = 0
  b_k = 0
  
  for i in range(boardsize):
    for j in range(boardsize):
      
      if pieceloc[i][j] == 3:
        r_k = 1
      
      if pieceloc[i][j] == 6:
        b_k = 1
     
    
      if pieceloc[i][j] > 0:
        if pieceloc[i][j] == 3:
          fill(255,0,0)
          textSize(tile)
          text(king,tile*j,tile*i+tile/1.2)
        if pieceloc[i][j] == 2:
          fill(255,0,0)
          textSize(tile)
          text(wizard,tile*j,tile*i+tile/1.2)
        if pieceloc[i][j] == 1:
          fill(255,0,0)
          textSize(tile)
          text(knight,tile*j,tile*i+tile/1.2)
        if pieceloc[i][j] == 6:
          fill(0,0,255)
          textSize(tile)
          text(king,tile*j,tile*i+tile/1.2)
        if pieceloc[i][j] == 5:
          fill(0,0,255)
          textSize(tile)
          text(wizard,tile*j,tile*i+tile/1.2)
        if pieceloc[i][j] == 4:
          fill(0,0,255)
          textSize(tile)
          text(knight,tile*j,tile*i+tile/1.2)
        if pieceloc[i][j] == 7:
          fill(150,150,150)
          textSize(tile)
          text(cloud,tile*j,tile*i+tile/1.2)
  
def selection():
  global selected
  stroke(255,0,0)
  strokeWeight(20/boardsize)
  noFill()
 
  if mx1 != None and pieceloc[my1][mx1] > 0 and turn == "red":
    rect(mx1*tile,my1*tile,tile,tile)
    if pieceloc[my1][mx1] == 3:
      selected = "rking"
    if pieceloc[my1][mx1] == 2:
      selected = "rwizard"
    if pieceloc[my1][mx1] == 1:
      selected = "rknight"

  elif mx1 != None and pieceloc[my1][mx1] > 0 and turn == "blue" :
    rect(mx1*tile,my1*tile,tile,tile)
    if pieceloc[my1][mx1] == 6:
      selected = "bking"
    if pieceloc[my1][mx1] == 5:
      selected = "bwizard"
    if pieceloc[my1][mx1] == 4:
      selected = "bknight"
      
      
      
  fill(255)
  noStroke()
  strokeWeight(3)
  
#def knightmove():


def inrange(x,y):
  if x > 0 and x < len(pieceloc[0]):
    if y > 0 and y < len(pieceloc):
      return(True)
  return(False)
  
  
def movement():  
  global selected,moveready,turn
  moveready = False
  if selected == "rknight":
    moveready = True;
    
    if pieceloc[my1-1][mx1]==0:
        noFill()
        stroke(255,0,0)       
        ellipse(mx1*tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1] = 1
          pieceloc[my1][mx1] = 0
          turn = "blue"
       
                
    
  
    
    if pieceloc[my1][mx1-1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
          pieceloc[my1][mx1-1] = 1
          pieceloc[my1][mx1] = 0
          turn = "blue"
          
          
    
    if pieceloc[my1+1][mx1] == 0:
        noFill()
        stroke(255,0,0)    
        #bug
        ellipse(mx1*tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
        
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
          pieceloc[my1+1][mx1] = 1
          pieceloc[my1][mx1] = 0
          
          turn = "blue"
          
          
    
    if pieceloc[my1][mx1+1]==0:
        noFill()
        stroke(255,0,0) 
        ellipse(mx1*tile+tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
          pieceloc[my1][mx1+1] = 1
          pieceloc[my1][mx1] = 0
          turn = "blue"
  elif selected == "bknight":
    moveready = True;
    if pieceloc[my1-1][mx1]==0:
        noFill()
        stroke(255,0,0)       
        ellipse(mx1*tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
        
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1] = 4
          pieceloc[my1][mx1] = 0
          turn = "red"
         
                
    
  
        
    if pieceloc[my1][mx1-1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
          pieceloc[my1][mx1-1] = 4
          pieceloc[my1][mx1] = 0
          turn = "red"
          
          
    if inrange(my1+1,mx1):
      if pieceloc[my1+1][mx1] == 0:
        noFill()
        stroke(255,0,0)       
        ellipse(mx1*tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
          pieceloc[my1+1][mx1] = 4
          pieceloc[my1][mx1] = 0
          turn = "red"
          
    if inrange(my1,mx1+1):
      if pieceloc[my1][mx1+1]==0:
        noFill()
        stroke(255,0,0) 
        ellipse(mx1*tile+tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
          pieceloc[my1][mx1+1] = 4
          pieceloc[my1][mx1] = 0
          turn = "red"
      
      
  elif selected == "rwizard":
    moveready= True
    
    if pieceloc[my1-1][mx1-1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1-1] = 2
          pieceloc[my1][mx1] = 0
          turn = "blue"
          
    if inrange(my1+1,mx1-1):   
      if pieceloc[my1+1][mx1-1]==0:
        
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
          pieceloc[my1+1][mx1-1] = 2
          pieceloc[my1][mx1] = 0
          turn = "blue"
          
    if inrange(my1+1,mx1+1):
      if pieceloc[my1+1][mx1+1] == 0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
          pieceloc[my1+1][mx1+1] = 2
          pieceloc[my1][mx1] = 0
          turn = "blue"
          
    if inrange(my1-1,mx1+1):
      if pieceloc[my1-1][mx1+1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1+1] = 2
          pieceloc[my1][mx1] = 0
          turn = "blue"
  elif selected == "bwizard":
    moveready= True
    if inrange(my1-1,mx1-1):
      if pieceloc[my1-1][mx1-1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1-1] = 5
          pieceloc[my1][mx1] = 0
          turn = "red"
          
    if inrange(my1+1,mx1-1):   
      if pieceloc[my1+1][mx1-1]==0:
        
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
          pieceloc[my1+1][mx1-1] = 5
          pieceloc[my1][mx1] = 0
          turn = "red"
          
    if inrange(my1+1,mx1+1):
      if pieceloc[my1+1][mx1+1] == 0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
          pieceloc[my1+1][mx1+1] = 5
          pieceloc[my1][mx1] = 0
          turn = "red"
          
    if inrange(my1-1,mx1+1):
      if pieceloc[my1-1][mx1+1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1+1] = 5
          pieceloc[my1][mx1] = 0
          turn = "red"    
      
  elif selected == "rking":
    moveready = True;
    if pieceloc[my1-1][mx1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1] = 3
          pieceloc[my1][mx1] = 0
          turn = "blue"
    
  
        
    if pieceloc[my1][mx1-1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
          pieceloc[my1][mx1-1] = 3
          pieceloc[my1][mx1] = 0
          turn = "blue"
          
    if inrange(my1+1,mx1):
      if pieceloc[my1+1][mx1] == 0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
          pieceloc[my1+1][mx1] = 3
          pieceloc[my1][mx1] = 0
          turn = "blue"
          
    if inrange(my1,mx1+1):
      if pieceloc[my1][mx1+1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
          pieceloc[my1][mx1+1] = 3
          pieceloc[my1][mx1] = 0
          turn = "blue"
  elif selected == "bking":
    moveready = True;
    if pieceloc[my1-1][mx1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1] = 6
          pieceloc[my1][mx1] = 0
          turn = "red"
    
  
        
    if pieceloc[my1][mx1-1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
          pieceloc[my1][mx1-1] = 6
          pieceloc[my1][mx1] = 0
          turn = "red"
          
    if inrange(my1+1,mx1):
      if pieceloc[my1+1][mx1] == 0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
          pieceloc[my1+1][mx1] = 6
          pieceloc[my1][mx1] = 0
          turn = "red"
          
    if inrange(my1,mx1+1):
      if pieceloc[my1][mx1+1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
          pieceloc[my1][mx1+1] = 6
          pieceloc[my1][mx1] = 0
          turn = "red"

  noStroke()
  
  
  
  
def capture():
    global moveready,selected
    noStroke()
    if selected == "rknight":
      moveready = True
    
      if pieceloc[my1-1][mx1] >=4 and pieceloc[my1-1][mx1] <=6:
        noFill()
        fill(255,0,0)       
        
        text(attack,mx1*tile,my1*tile-tile/8)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1] = 1
          pieceloc[my1][mx1] = 0
          turn = "blue"
       
                
    
  
      if inrange(my1,mx1-1):
        if pieceloc[my1][mx1-1]>=4 and pieceloc[my1][mx1-1] <=6:
          
          noFill()
          fill(255,0,0)
          text(attack,mx1*tile-tile,my1*tile+tile-tile/8)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
            pieceloc[my1][mx1-1] = 1
            pieceloc[my1][mx1] = 0
            turn = "blue"
          
          
      if inrange(my1+1,mx1):
        if pieceloc[my1+1][mx1]>=4 and pieceloc[my1+1][mx1] <=6:
          noFill()
          fill(255,0,0)    
          #bug
          
          text(attack,mx1*tile,my1*tile-tile/8+tile*2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
            pieceloc[my1+1][mx1] = 1
            pieceloc[my1][mx1] = 0
          
            turn = "blue"
          
          
      if inrange(my1,mx1+1):
        if pieceloc[my1][mx1+1]>=4 and pieceloc[my1][mx1+1] <=6:
          noFill()
          fill(255,0,0) 
          text(attack,mx1*tile+tile,my1*tile+tile-tile/8)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
            pieceloc[my1][mx1+1] = 1
            pieceloc[my1][mx1] = 0
            turn = "blue"
            
    elif selected == "bknight":
      moveready = True
      if pieceloc[my1-1][mx1] >=1 and pieceloc[my1-1][mx1] <=3:
        noFill()
        fill(255,0,0)       
        
        text(attack,mx1*tile,my1*tile-tile/8)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1] = 4
          
          pieceloc[my1][mx1] = 0
          
          
          turn = "red"
          moveready = False
          selected = None
        
                
    
  
      if inrange(my1,mx1-1):
        if pieceloc[my1][mx1-1]>=1 and pieceloc[my1][mx1-1] <=3:
          
          noFill()
          fill(255,0,0)
          text(attack,mx1*tile-tile,my1*tile+tile-tile/8)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
            pieceloc[my1][mx1-1] = 4
            pieceloc[my1][mx1] = 0
            turn = "red"
          
          
      if inrange(my1+1,mx1):
        if pieceloc[my1+1][mx1]>=1 and pieceloc[my1+1][mx1] <=3:
          noFill()
          fill(255,0,0)    
          
          
          text(attack,mx1*tile,my1*tile-tile/8+tile*2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
            pieceloc[my1+1][mx1] = 4
            pieceloc[my1][mx1] = 0
          
            turn = "red"
          
          
      if inrange(my1,mx1+1):
        if pieceloc[my1][mx1+1]>=1 and pieceloc[my1][mx1+1] <=3:
          noFill()
          fill(255,0,0) 
          text(attack,mx1*tile+tile,my1*tile+tile-tile/8)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
            pieceloc[my1][mx1+1] = 4
            pieceloc[my1][mx1] = 0
            turn = "red"
      
    elif selected == "rwizard":
      moveready= True
    
      if pieceloc[my1-1][mx1-1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1-1] = 2
          pieceloc[my1][mx1] = 0
          turn = "blue"
          
      if inrange(my1+1,mx1-1):   
       if pieceloc[my1+1][mx1-1]==0:
        
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
          pieceloc[my1+1][mx1-1] = 2
          pieceloc[my1][mx1] = 0
          turn = "blue"
          
      if inrange(my1+1,mx1+1):
        if pieceloc[my1+1][mx1+1] == 0:
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile+tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
            pieceloc[my1+1][mx1+1] = 2
            pieceloc[my1][mx1] = 0
            turn = "blue"
          
      if inrange(my1-1,mx1+1):
        if pieceloc[my1-1][mx1+1]==0:
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile+tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
            pieceloc[my1-1][mx1+1] = 2
            pieceloc[my1][mx1] = 0
            turn = "blue"
    elif selected == "bwizard":
      moveready= True
      if inrange(my1-1,mx1-1):
        if pieceloc[my1-1][mx1-1]==0:
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile-tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
            pieceloc[my1-1][mx1-1] = 5
            pieceloc[my1][mx1] = 0
            turn = "red"
          
      if inrange(my1+1,mx1-1):   
        if pieceloc[my1+1][mx1-1]==0:
        
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile-tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
            pieceloc[my1+1][mx1-1] = 5
            pieceloc[my1][mx1] = 0
            turn = "red"
          
      if inrange(my1+1,mx1+1):
        if pieceloc[my1+1][mx1+1] == 0:
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile+tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
            pieceloc[my1+1][mx1+1] = 5
            pieceloc[my1][mx1] = 0
            turn = "red"
                
      if inrange(my1-1,mx1+1):
        if pieceloc[my1-1][mx1+1]==0:
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile+tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
            pieceloc[my1-1][mx1+1] = 5
            pieceloc[my1][mx1] = 0
            turn = "red"    
      
    elif selected == "rking":
      moveready = True;
      if pieceloc[my1-1][mx1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
          pieceloc[my1-1][mx1] = 3
          pieceloc[my1][mx1] = 0
          turn = "blue"
    
  
        
      if pieceloc[my1][mx1-1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
          pieceloc[my1][mx1-1] = 3
          pieceloc[my1][mx1] = 0
          turn = "blue"
          
      if inrange(my1+1,mx1):
        if pieceloc[my1+1][mx1] == 0:
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
            pieceloc[my1+1][mx1] = 3
            pieceloc[my1][mx1] = 0
            turn = "blue"
          
      if inrange(my1,mx1+1):
        if pieceloc[my1][mx1+1]==0:
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile+tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
            pieceloc[my1][mx1+1] = 3
            pieceloc[my1][mx1] = 0
            turn = "blue"
      elif selected == "bking":
        moveready = True;
        if pieceloc[my1-1][mx1]==0:
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile+tile/4,my1*tile-tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)+1 == my1:
            pieceloc[my1-1][mx1] = 6
            pieceloc[my1][mx1] = 0
            turn = "red"
    
  
        
      if pieceloc[my1][mx1-1]==0:
        noFill()
        stroke(255,0,0)
        ellipse(mx1*tile-tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
        if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)+1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
          pieceloc[my1][mx1-1] = 6
          pieceloc[my1][mx1] = 0
          turn = "red"
          
      if inrange(my1+1,mx1):
        if pieceloc[my1+1][mx1] == 0:
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile+tile/4,my1*tile+tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile) == mx1 and round((mouse.y-tile/2)/tile)-1 == my1:
            pieceloc[my1+1][mx1] = 6
            pieceloc[my1][mx1] = 0
            turn = "red"
          
      if inrange(my1,mx1+1):
        if pieceloc[my1][mx1+1]==0:
          noFill()
          stroke(255,0,0)
          ellipse(mx1*tile+tile+tile/4,my1*tile+tile/4,tile/2,tile/2)
          if moveready == True and mousePressed and round((mouse.x-tile/2)/tile)-1 == mx1 and round((mouse.y-tile/2)/tile) == my1:
            pieceloc[my1][mx1+1] = 6
            pieceloc[my1][mx1] = 0
            turn = "red"
          
      noStroke()
def winsqr():
  global pieceloc
  if pieceloc[winpos][winpos]>0:
    if pieceloc[winpos][winpos] == 3:
      background(255)
      fill(255,255,0)
      textSize(100)
      text("red wins",s/10,s/3)
    if pieceloc[winpos][winpos] == 6:
      background(255)
      fill(255,255,0)
      textSize(100)
      text("blue wins",s/10,s/3)
    if pieceloc[winpos][winpos] == 1 and selected != "rknight":
      if mousePressed:
        pieceloc[round((mouse.y-tile/2)/tile)][round((mouse.x-tile/2)/tile)] = 7
        
        
    if pieceloc[winpos][winpos] == 4:
      pieceloc[my1][mx1] == 7
      print("should work",mx1,my1)


  if b_k == 0:
        background(255)
        fill(255,255,0)
        textSize(100)
        text("red wins",s/10,s/3)
  if r_k == 0:
        background(255)
        fill(255,255,0)
        textSize(100)
        text("blue wins",s/10,s/3)
#def cloudmode():
  
def setup():
  ellipseMode(CORNER)

  size(s,s)

   

def draw():
  global movx,movy,pieceloc
  drawboard()
  selection()
  piecerender()
  movement()
  capture()
  winsqr()
 
  
  
run()