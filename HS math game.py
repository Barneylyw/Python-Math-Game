import time, random, turtle

num1 = 0
num2 = 0
ans = 0
uans = 0
used = 0
start = 0
end = 0
m_health = 0
m_atk = 0
p_atk = 0
p_health = 0
die = True
bonus = 0

def theme1():
	global alice,f,b,b1,b2, c,d,e
	alice = turtle.Screen()
	alice.bgcolor("aqua")
	alice.screensize()
	alice.setup(width = 1.0, height = 1.0)
	alice.window_width()
	
	a = turtle.Turtle()
	a.pensize(5)
	a.speed("fastest")
	a.hideturtle()
	a.pencolor("green")
	a.fillcolor("green")
	a.begin_fill()
	a.up()
	a.goto(-alice.window_width(),-alice.window_height()/4)
	a.down()
	a.fd(alice.window_width()*2)
	a.right(90)
	a.fd(alice.window_height()/4)
	a.right(90)
	a.fd(alice.window_width()*2)
	a.right(90)
	a.fd(alice.window_height()/4)
	a.end_fill()

  #human
	b = turtle.Turtle()
	b.speed("fastest")
	b.hideturtle()
	b.pencolor("black")
	b.up()
	b.goto(-alice.window_width()/4,-(alice.window_height()/5) * -0.5)
	b.down()
	b.fillcolor("white")
	b.begin_fill()
	b.circle((alice.window_height()/10))
	b.end_fill()
	b.right(90)
	b.fd(alice.window_height()/4.5)
	b.right(45)
	b.fd(alice.window_height()/5.8)
	b.right(180)
	b.fd(alice.window_height()/5.8)
	b.right(90)
	b.fd(alice.window_height()/5.8)
	b.right(180)
	b.fd(alice.window_height()/5.8)
	b.right(45)
	b.fd(alice.window_height()/8)
	b.right(65)
	b.fd(alice.window_height()/5.8)
	b.right(180)
	b.fd(alice.window_height()/5.8)
	b.right(185)
	b.fd(alice.window_height()/5.8)
	b.pencolor("brown")
	b.fillcolor("brown")
	b.begin_fill()
	b.right(110)
	b.fd(alice.window_height()/20)
	b.left(90)
	b.fd(alice.window_height()/35)
	b.left(90)
	b.fd(alice.window_height()/20)
	b.right(90)
	b.fd(alice.window_height()/40)
	b.left(90)
	b.fd(alice.window_height()/40)
	b.left(90)
	b.fd(alice.window_height()/12)
	b.left(90)
	b.fd(alice.window_height()/40)
	b.left(90)
	b.fd(alice.window_height()/40)
	b.end_fill()
	b.left(90)
	b.fd(alice.window_height()/40)
	b.pencolor("gold")
	b.fillcolor("gold")
	b.begin_fill()
	b.fd(alice.window_height()/5)
	b.right(45)
	b.fd(alice.window_height()/40)
	b.right(90)
	b.fd(alice.window_height()/40)
	b.right(45)
	b.fd(alice.window_height()/5)
	b.end_fill()
	
	b1 = turtle.Turtle()
	b1.speed("fastest")
	b1.turtlesize(alice.window_width()/800)
	b1.shape("circle")
	b1.pencolor("black")
	b1.fillcolor("black")
	b1.up()
	b1.goto(-alice.window_width()/4.5,(alice.window_height()/4.5))
	b1.down()

	b2 = turtle.Turtle()
	b2.turtlesize(alice.window_width()/800)
	b2.speed("fastest")
	b2.shape("circle")
	b2.pencolor("black")
	b2.fillcolor("black")
	b2.up()
	b2.goto(-alice.window_width()/3.8,(alice.window_height()/4.5))
	b2.down()
	
	#monster
	c = turtle.Turtle()
	c.speed("fastest")
	#c.hideturtle()
	c.pencolor("black")
	c.up()
	c.goto(alice.window_width()/4,(alice.window_height()/5) * 0.5)
	c.down()
	c.circle((alice.window_height()/10))
	c.left(180)
	c.left(90)
	c.fd(alice.window_height()/4.5)
	c.left(45)
	c.fd(alice.window_height()/5.8)
	c.left(180)
	c.fd(alice.window_height()/5.8)
	c.left(90)
	c.fd(alice.window_height()/5.8)
	c.left(180)
	c.fd(alice.window_height()/5.8)
	c.left(45)
	c.fd(alice.window_height()/8)
	c.left(65)
	c.fd(alice.window_height()/5.8)
	c.left(180)
	c.fd(alice.window_height()/5.8)
	c.left(50)
	c.fd(alice.window_height()/5.8)
	c.up()
	c.goto(alice.window_width()/4,(alice.window_height()/4))
	c.right(35)
	c.left(180)
	c.down()
	c.shape("circle")
	c.color("white")
	c.turtlesize((alice.window_height()/65))

	d = turtle.Turtle()
	d.speed("fastest")
	d.shape("turtle")
	#d.hideturtle()
	d.pencolor("black")
	d.up()
	d.goto(alice.window_width()/4*1.15,(alice.window_height()/3)*0.85)
	d.left(45)

	e = turtle.Turtle()
	e.speed("fastest")
	e.shape("turtle")
	#e.hideturtle()
	e.pencolor("black")
	e.up()
	e.goto(alice.window_width()/4*0.85,(alice.window_height()/3)*0.85)
	e.left(135)

	f = turtle.Turtle()
	#f.hideturtle()
	f.up()
	f.speed("fastest")
	f.shape("turtle")
	f.color("blue")
	f.turtlesize((alice.window_height()/65))
	f.right(205)
	f.goto(alice.window_width()/8.5,(alice.window_height()/6)*0.7)
	f.showturtle()

  

def theme2():
	global alice
	a = turtle.Turtle()
	a.hideturtle()
	a.speed(13)
	a.pencolor("gold")
	a.pensize(4)
	a.up()
	a.goto(-alice.window_width()/9,-(alice.window_height()/3.5) * 0.2)
	a.down()
	a.circle(alice.window_width()/8,180)
	a.right(180)
	
	a.up()
	a.goto(-alice.window_width()/13,-(alice.window_height()/3.5) * 0.2)
	a.down()
	a.circle(alice.window_width()/8,180)
	a.right(180)
	
	a.up()
	a.goto(-alice.window_width()/20,-(alice.window_height()/3.5) * 0.2)
	a.down()
	a.circle(alice.window_width()/8,180)
	a.right(180)
	
	a.up()
	a.goto(alice.window_width()/15,-(alice.window_height()/3.5) * 0.2)
	a.down()
	a.circle(alice.window_width()/8,180)
	a.right(180)
	
	a.up()
	a.goto(alice.window_width()/8,-(alice.window_height()/3.5) * 0.2)
	a.down()
	a.circle(alice.window_width()/8,180)
	
	b = turtle.Turtle()
	b.hideturtle()
	b.pencolor("red")
	b.speed(3)
	b.pensize(5)
	b.up()
	b.goto(alice.window_width()/4,(alice.window_height()/5) * 0.7)
	b.down()
	b.right(140)
	b.fd(alice.window_width()/10)
	
	b.goto(alice.window_width()/4,(alice.window_height()/5) * 0.7)
	b.down()
	b.right(10)
	b.fd(alice.window_width()/10)
	
	b.goto(alice.window_width()/4,(alice.window_height()/5) * 0.7)
	b.down()
	b.right(20)
	b.fd(alice.window_width()/10)
	 
	a.clear()
	b.clear()

def theme3():
	global alice,f
	
	a = turtle.Turtle()
	#a.hideturtle()
	a.pencolor("red")
	a.pensize(5)
	a.hideturtle()
	a.up()
	
	f.speed(5)
	f.up()
	f.goto(-alice.window_width()/4,-(alice.window_height()/5) * -0.5)
	f.right(180)
	
	a.goto(-alice.window_width()/4,-(alice.window_height()/5) * -0.8)
	a.down()
	a.right(10)
	a.fd(alice.window_width()/10)
	
	a.goto(-alice.window_width()/4,-(alice.window_height()/5) * -0.8)
	a.right(10)
	a.fd(alice.window_width()/10)

	f.goto(alice.window_width()/8.5,(alice.window_height()/6)*0.7)
	f.right(180)
	f.down()
	
	a.goto(-alice.window_width()/4,-(alice.window_height()/5) * -0.8)
	a.right(10)
	a.fd(alice.window_width()/10)
	time.sleep(2)
	a.clear()

def theme4():
  global alice, c,d,e,f
  f.hideturtle()
  e.hideturtle()
  d.hideturtle()
  c.hideturtle()
  c.clear()
  
  h = turtle.Turtle()
  h.speed("fastest")
  h.hideturtle()
  h.pencolor("red")
  h.fillcolor("red")
  h.begin_fill()
  h.up()
  h.goto(alice.window_width()/4*0.75,-(alice.window_height()/3))
  h.down()
  h.right(45)
  for i in range (2):
    h.circle(65,90)
    h.circle(13,90)
  h.end_fill()
  h.pencolor("grey")
  h.fillcolor("grey")
  h.begin_fill()
  h.up()
  h.goto(alice.window_width()/3*0.93,-(alice.window_height()/3))
  h.down()
  h.left(135)
  h.fd(100)
  h.circle(47,180)
  h.fd(100)
  h.pencolor("red")
  h.left(90)
  h.fd(94)
  h.end_fill()
  
  g = turtle.Turtle()
  g.hideturtle()
  g.up()
  g.goto(alice.window_width()/4,-(alice.window_height()/5))
  g.down()
  g.write("R.I.P", move=False, align="center", font=("Arial", 15, "normal"))

def theme5():
  global alice, a,b,b1,b2
  b.clear()
  b1.hideturtle()
  b2.hideturtle()
	
  h = turtle.Turtle()
  h.speed("fastest")
  h.hideturtle()
  h.pencolor("red")
  h.fillcolor("red")
  h.begin_fill()
  h.up()
  h.goto(-alice.window_width()/3,-(alice.window_height()/3))
  h.down()
  h.right(45)
  for i in range (2):
    h.circle(65,90)
    h.circle(13,90)
  h.end_fill()
  h.pencolor("grey")
  h.fillcolor("grey")
  h.begin_fill()
  h.up()
  h.goto(-alice.window_width()/4.65,-(alice.window_height()/3))
  h.down()
  h.left(135)
  h.fd(100)
  h.circle(47,180)
  h.fd(100)
  h.left(90)
  h.fd(94)
  h.end_fill()
  
  g = turtle.Turtle()
  g.hideturtle()
  g.up()
  g.goto(-alice.window_width()/3.6,-(alice.window_height()/5))
  g.down()
  g.write("R.I.P", move=False, align="center", font=("Arial", 15, "normal"))

def sg():
	sky = turtle.Turtle()
	sky.speed("fastest")
	sky.pencolor("aqua")
	sky.fillcolor("aqua")
	sky.hideturtle()
	sky.begin_fill()
	sky.goto(-alice.window_width()/9,0)
	sky.left(90)
	sky.fd(alice.window_height()/3)
	sky.left(90)
	sky.fd(alice.window_width()/16)
	sky.left(90)
	sky.fd(alice.window_height()/3.6)
	sky.left(90)
	sky.fd(alice.window_width()/56)
	sky.right(90)
	sky.sety(0)
	sky.setx(0)
	sky.end_fill()

def spatk():
	global f,b,b1,b2
	for i in range(65,1,-5):
		f.turtlesize((alice.window_height()/i))
	time.sleep(0.1)
	f.color("blue")
	time.sleep(0.1)
	f.color("white")
	time.sleep(0.1)
	f.color("blue")
	time.sleep(0.1)
	f.color("white")
	time.sleep(0.1)
	f.color("blue")
	time.sleep(0.1)
	f.color("white")
	time.sleep(0.3)
	f.color("blue")
	theme5()
	time.sleep(0.2)
	f.turtlesize((alice.window_height()/65))
	
def loading(pensize,circlesize,time):
  alice = turtle.Screen()
  alice.bgcolor("black")
  alice.screensize()
  alice.setup(width = 1.0, height = 1.0)

  aa = turtle.Turtle()
  aa.speed(0)
  aa.hideturtle()
  aa.pencolor("black")
  aa.pensize(pensize*2)
  aa.sety(-circlesize)

  bb = turtle.Turtle()
  bb.speed(0)
  bb.hideturtle()
  bb.pencolor("white")
  bb.up()
  bb.sety(circlesize)
  bb.right(180)
  bb.down()
  bb.pensize(pensize)
  
  if time == "True":
    while True:
      num1 = 0
      while num1 < 14:
        if num1 < 14:
          num1 += 1
        aa.up()
        aa.down()
        aa.circle(circlesize,16)
        bb.up()
        bb.down()
        bb.circle(circlesize,16)  
  else:
    for i in range(time):
      num1 = 0
      while num1 < 14:
        if num1 < 14:
          num1 += 1 
        aa.up()
        aa.down()
        aa.circle(circlesize,16)
        bb.up()
        bb.down()
        bb.circle(circlesize,16)  
    bb.clear()
    aa.clear()

def answer():
    global num1, num2, ans, start, end, m_health, m_atk, p_atk, p_health, uans, used, die, bonus
    if uans == ans:
        print("You are correct")
         
        if used <= 5:
            bouns = (round(random.uniform(1.4,1.9),1))
            p_atk *= bouns
            print("You get a " + str(bouns*100) + "% bouns")
             
        elif 5 < used <= 10:
            bouns = (round(random.uniform(1.3,1.7),1))
            p_atk *= bouns
            print("You get a " + str(bouns*100) + "% bouns")
             
        else:
            bouns = (round(random.uniform(1.2,1.3),1))
            p_atk *= bouns
            print("You get a " + str(bouns*100) + "% bouns")
             
    else:
      print("You are wrong")
       
      print("The correct answer is " + str(ans) +".")
      print("You get a 30% debuff.")
       
      p_atk *= 0.7
		
def tut():
	global num1, num2, ans, start, end, m_health, m_atk, p_atk, p_health, uans, used, die, bonus, alice
	start = time.time()
	uans = input("Your sword asks you :'Whats " + str(num1) + " × " + str(num2) + "?'")
	if uans.isdigit():
		uans = int(uans)
		end = time.time()
		used = end - start
		used = round(used)
		print("You used" , used , "seconds to answer that.")
		answer()
		return used, uans
	else:
		die = False
		input("Your sword: Why you don't answer a number??? what a stupid person[press enter]")
		input("Your sword:I won't help you to beat the monster[press enter]")
		input("Then the sword blow up itself[press enter]")
	
def question():
  global num1, num2, ans, start, end, m_health, m_atk, p_atk, p_health, uans, used, die, bonus
  num1 = random.randint(1,15)
  num2 = random.randint(1,15)
  ans = num1 * num2
	
def player():
	global num1, num2, ans, start, end, m_health, m_atk, p_atk, p_health, uans, used, die,bonus
	p_health = 100
	p_atk = 10
  
def monster():
  global num1, num2, ans, start, end, m_health, m_atk, p_atk, p_health, uans, used, die,bonus
  m_health = 100
  m_atk = random.randint(6,20)

def main():
  global num1, num2, ans, start, end, m_health, m_atk, p_atk, p_health, uans, used, die,bonus,f,b
  loading(3,15,5)
  input("You are a warrior and you are going to kill the monster.[press enter]")
  input("You have an intelligent sword which will ask you question to help you, if you got it wrong and it will decrease you damage.[press enter]")
  theme1()
  player()
  monster()
  question()
  tut()
  if die == False:
    input("Your sword is gone...[press enter]")
    sg()
    input("You attacked the monster with your hands for 0 damage![press enter]")
    input("The monster attacked you with his special skill for 100 damage![press enter]")
    spatk()
    print("You lost")
    theme5()
  else:
    print("You attacked the monster for " + str(p_atk) + " damage!")
    theme2()
     
    m_health -= p_atk
    if m_health < 0:
        m_health = 0
    p_atk = 5
    m_atk = random.randint(6,20)
    print("The monster attacked you for " + str(m_atk) + " damage!")
    theme3()
    
    p_health -= m_atk
    if p_health <= 0:
    	p_health = 0
    print("Ｍonster health:" , m_health)
     
    print("Your health:", p_health)
     
    while True:
        if p_health <=0 or m_health <= 0:
            if p_health <= 0:
                print("You lost")
                theme5()
                break
            elif m_health <= 0:
                print("You won")
                theme4()
                break
        else:
             
            question() 
            tut()
            if die == False:
                input("Your sword is gone...[press enter]")  
                sg()
                input("You attacked the monster with your hands for 0 damage![press enter]")
                
                input("The monster attacked you with his special skill for 100 damage![press enter]")
                spatk()
                print("You lost")
                theme5()
                 
                break
        print("You attacked the monster for " + str(p_atk) + " damage!")
        theme2()
         
        m_health -= p_atk
        if m_health < 0:
        	m_health = 0
        p_atk = 5
        m_atk = random.randint(6,20)
        print("The monster attacked you for " + str(m_atk) + " damage!")
        theme3()
         
        p_health -= m_atk
        if p_health <= 0:
        	p_health = 0
        print("Monster health remain:" , m_health)
         
        print("Your health remain:", p_health)
         
    
main()