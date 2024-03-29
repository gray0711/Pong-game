import turtle
import winsound

wn=turtle.Screen()
wn.title('pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)
winsound.PlaySound('backsound.wav',winsound.SND_ASYNC)
wn.bgpic('bgpong2.png')

#register the shape
turtle.register_shape('poke.gif')


#start the game
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(200,20)


#score
score_a=0
score_b=0

#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('cyan')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('poke.gif')
ball.penup()
ball.goto(0,0)
ball.dx=0.7
ball.dy=0.7



#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.clear()
pen.write('player A:0 player B:0',align='center',font=('jokerman',20,'normal'))



#function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=50
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=50
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=50
    paddle_b.sety(y)


def paddle_b_down():
    y=paddle_b.ycor()
    y-=50
    paddle_b.sety(y)
    
#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

#main game loop
while True:
    wn.update()
   

    #move the ball
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)

    #border checking
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        winsound.PlaySound('die.wav',winsound.SND_ASYNC)
        pen.write('player A:{} player B:{}'.format(score_a,score_b),align='center',font=('jokerman',20,'normal'))
    

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        winsound.PlaySound('die.wav',winsound.SND_ASYNC)
        pen.write('player A:{} player B:{}'.format(score_a,score_b),align='center',font=('jokerman',20,'normal'))
        
    if paddle_a.ycor()<-245: #border checking :)
        paddle_a.sety(-245)
    if paddle_a.ycor()>245:
        paddle_a.sety(245)
    if paddle_b.ycor()<-245:
        paddle_b.sety(-245)
    if paddle_b.ycor()>245:
        paddle_b.sety(245)

#paddle and collisions
    if (ball.xcor() >340 and ball.xcor()<350) and (ball.ycor() <paddle_b.ycor() +40 and ball.ycor()> paddle_b.ycor() -40):
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.dx*=-1

    
    if (ball.xcor() <-340 and ball.xcor()>-350) and (ball.ycor() <paddle_a.ycor() +40 and ball.ycor()> paddle_a.ycor() -40):
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.dx*=-1

#game over
    if score_a==10:
        pen.clear()
        pen.write('GAME OVER.. A WINS!!',align='center',font=('jokerman,',20,'normal'))
        break
    if score_b==10:
        pen.clear()
        pen.write('GAME OVER.. B WINS!!',align='center',font=('jokerman',20,'normal')) 
        break


        


