import simplegui
import random

canvas_height = 300
canvas_width = 300

width_A = 20 + random.randrange(0,30,5)
width_B = 20 + random.randrange(0,30,5)
width_C = 20 + random.randrange(0,30,5)

initial_space = 30

space_1 = 30 + random.randrange(0,40,4)
space_2 = 30 + random.randrange(0,40,4)

x_for_A = initial_space
x_for_B = initial_space + width_A + space_1
x_for_C = x_for_B + width_B + space_2
x_for_circle = ( x_for_A + width_A ) // 2
x_for_line = x_for_circle + 2

circle_radius = 8
y_for_circle = canvas_height-100-circle_radius
circle_centre = [x_for_circle,y_for_circle]

var_A = x_for_A
var_B = x_for_B
var_C = x_for_C
var_circle_x = x_for_circle
var_circle_y = y_for_circle 


y_for_block = canvas_height - 100
y_for_line = y_for_block

line_start_click = 'no'
line_finish = 'no'
line_length = y_for_block

start = 'yes'
move = 'no'
distance = 0
fall = 'no'
chance = 0
SCORE = 0

def move_circle():
    global distance
    distance += 1
            
def update():
    global start,width_A,width_B,width_C,space_1,space_2,x_for_A,x_for_B,x_for_C,x_for_circle,x_for_line
    global y_for_circle,circle_centre,var_A,var_B,var_C,var_circle_x,var_circle_y,move,distance,fall,chance
    width_A = width_C
    width_B = 20 + random.randrange(0,30,5)
    width_C = 20 + random.randrange(0,30,5)

    space_1 = 30 + random.randrange(0,40,4)
    space_2 = 30 + random.randrange(0,40,4)

    x_for_A = initial_space
    x_for_B = initial_space + width_A + space_1
    x_for_C = x_for_B + width_B + space_2
    x_for_circle = var_circle_x
    x_for_line = x_for_circle + 2

    y_for_circle = canvas_height-100-circle_radius
    circle_centre = [x_for_circle,y_for_circle]

    var_A = x_for_A
    var_B = x_for_B
    var_C = x_for_C
    var_circle_x = x_for_circle
    var_circle_y = y_for_circle
    
    start = 'yes'
    move = 'no'
    distance = 0
    fall = 'no'
    chance = 0


y_for_block = canvas_height - 100
y_for_line = y_for_block

line_start_click = 'no'
line_finish = 'no'
line_length = y_for_block

start = 'yes'
move = 'no'
distance = 0
fall = 'no'
chance = 0

            
def move_canvas():
    global var_A,var_B,var_C,var_circle_x,move
    if chance == 2:
        move = 'yes'
    if var_C == initial_space:
        move ='no'
        update()
    if move == 'yes':
        var_A -= 1
        var_B -= 1
        var_C -= 1
        var_circle_x -= 1
      

def fall_circle():
    global y_for_circle,fall,start
    if y_for_circle > 300:
        start = 'over'
        time_fall.stop()
    if fall == 'yes':
        y_for_circle += 1
        
def checker(canvas):
    global start,fall,SCORE
    if not (( var_circle_x >= x_for_B - width_B // 2 and var_circle_x <= x_for_B + width_B // 2 ) or (var_circle_x >= x_for_C - width_C // 2 and var_circle_x <= x_for_C + width_C // 2 )):
        fall = 'yes'
        fall_circle()
    if (( var_circle_x >= x_for_B - width_B // 2 and var_circle_x <= x_for_B + width_B // 2 ) or (var_circle_x >= x_for_C - width_C // 2 and var_circle_x <= x_for_C + width_C // 2 )):
        SCORE = SCORE + 1
    
def start_game(canvas):
    global width_A,width_B,width_C,start
    if start == 'yes':
        canvas.draw_polyline([(x_for_A,y_for_block) ,(x_for_A,canvas_height)] ,width_A ,'Red' )
        canvas.draw_polyline([(x_for_B,y_for_block) ,(x_for_B,canvas_height)] ,width_B ,'Red' )
        canvas.draw_polyline([(x_for_C,y_for_block) ,(x_for_C,canvas_height)] ,width_C ,'Red' )
        canvas.draw_circle(circle_centre ,circle_radius ,2 ,'White' ,'White' ) 
        start = 'done'  
        
    
def creation(canvas):
    global distance,var_circle_x,x_for_line,y_for_line,start,line_length,line_finish,line_start_click
    start_game(canvas)
        
    if start == 'done':
        canvas.draw_polyline([(var_A,y_for_block) ,(var_A,canvas_height)] ,width_A ,'Red' )
        canvas.draw_polyline([(var_B,y_for_block) ,(var_B,canvas_height)] ,width_B ,'Red' )
        canvas.draw_polyline([(var_C,y_for_block) ,(var_C,canvas_height)] ,width_C ,'Red' )
        canvas.draw_circle([var_circle_x + distance,y_for_circle] ,circle_radius ,2 ,'White' ,'White' )
        canvas.draw_text('Score : '+str(SCORE),(225,25),15,'White')              
                         
    if start == 'over':
        canvas.draw_text('Game Over', (100,100), 20, 'White', 'serif')
        canvas.draw_text('Score : '+str(SCORE),(150,150),20,'White')  
        line_start_click = 'no'
        line_finish = 'yes'
        
    if line_start_click == 'yes' and line_finish == 'no':
        x_for_line = var_circle_x + 2
        y_for_line = y_for_block
        canvas.draw_line([x_for_line,y_for_line] ,[x_for_line,line_length] ,2 ,'Blue' )
    
    if line_start_click == 'no' and line_finish == 'yes':
        canvas.draw_line([x_for_line,y_for_line] ,[x_for_line+y_for_line-line_length,y_for_line] ,2 ,'Blue' )
        while y_for_line-line_length > distance:
            move_circle()    
        var_circle_x = var_circle_x + distance
        distance = 0
        line_finish = 'no'
        line_length = y_for_block
        checker(canvas)
         
def click(pos):
    global line_start_click,line_finish,chance
    if line_start_click == 'no':
        line_start_click = 'yes'
    elif line_start_click == 'yes':
        line_start_click = 'no'
        chance += 1
        line_finish = 'yes'

def drawline():
    global line_start_click,line_length
    if line_start_click == 'yes':
        line_length = line_length - 2
      
frame = simplegui.create_frame('Game',canvas_width,canvas_height)
frame.set_draw_handler(creation)
frame.set_mouseclick_handler(click)
frame.start()

timer = simplegui.create_timer(25,drawline)
timer.start()

time_fall = simplegui.create_timer(25,fall_circle)
time_fall.start()

timer_for_canvas = simplegui.create_timer(25,move_canvas)
timer_for_canvas.start()
