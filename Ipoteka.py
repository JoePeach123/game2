import random
from tkinter import *
import time


scrx=700
scry=550


okno=Tk()
okno.title('Ipoteka')
x=okno.winfo_screenwidth()//2-scrx//2
y=okno.winfo_screenheight()//2-scry//2
okno.resizable(False,False)
okno.geometry(f'{scrx}x{scry}+{x}+{y}')
okno.config(bg='black')



class Game():
    def __init__(self):
        self.health=100
        self.food=100
        self.day=1
        self.money=1000
        self.ipoteka=0
        self.ipotekaprice=15000
        self.ipotekatarget=52
        self.onefoodprice=24

    def check(self,ipot=True):
        if ipot:
            if self.day%7==0:
                if self.ipoteka<self.ipotekatarget-1:
                    if self.money>self.ipotekaprice:
                        self.money=self.money-self.ipotekaprice
                        money.config(text=f'Деньги: {game.money} ₽')
                        self.ipoteka=self.ipoteka+1
                        status_screen.config(text=f'Оплата ипотеки {self.ipoteka}/{self.ipotekatarget}',fg='yellow')
                    else:
                        status_screen.config(text='Вы просрочили выплату ипотеки и\n поэтому вас выселили',fg='red')
                        game.gameover()
                else:
                    game.win()


        money.config(text=f'Деньги: {game.money} ₽')
        if self.day==(7*(self.ipoteka+1))-1:
            day.config(text=f'День: {game.day}',fg='yellow')
        else:
            day.config(text=f'День: {game.day}',fg='white')
        if self.health<=0:
            self.health=0
        elif self.health>100:
            self.health=100
        health.config(text=f'Здоровье: {game.health}')
        if self.food<=0:
            self.food=0
        elif self.food>100:
            self.food=100
        food.config(text=f'Еда: {game.food}')



    def work(self):
        if self.health>20:
            hp=True
        else:
            hp=False
        if self.food>10:
            havka=True
        else:
            havka=False
        if hp and havka:
            event_good = random.randint(1, 45)
            event_bad = random.randint(1, 45)
            event_death = random.randint(1, 300)
            salary = random.randint(2000, 4000)
            hurt = random.randint(10, 15)
            starve = random.randint(10, 20)
            self.health = self.health - hurt
            self.food = self.food - starve
            self.day = self.day + 1
            self.money = self.money + salary
            status_screen.config(text=f'Вы заработали на стройке: {salary} ₽\n Потеряно здоровья: {hurt}\n Проголодались на: {starve}',fg='white')
            if event_good==1:
                game.event_good()
            elif event_bad==1:
                game.event_bad()
            elif event_death==1:
                game.event_death()

            self.check()
        elif hp and not(havka):
            status_screen.config(text='У вас мало еды',fg='white')
        elif not(hp):
            status_screen.config(text='У вас мало здоровья',fg='white')


    def chill(self):
        regen = random.randint(20, 30)
        starve = random.randint(10, 20)
        self.health=self.health+regen
        self.food=self.food-starve
        self.day=self.day+1
        status_screen.config(text=f'Вы восстановили {regen} здоровья',fg='white')
        game.check()

    def buy_food(self):
        pricefood=(100-self.food)*self.onefoodprice
        if self.food==100:
            status_screen.config(text='У вас уже есть еда',fg='white')
        else:
            if self.money>=pricefood:
                self.money = self.money - pricefood
                self.food = 100
                status_screen.config(text=f'Вы купили еды на {pricefood} ₽',fg='white')
            else:
                ostatok=self.money//self.onefoodprice
                self.food=self.food+ostatok
                self.money=self.money%self.onefoodprice
            game.check(False)

    def event_good(self):
        premium=random.randint(5000,10000)
        self.money=self.money+premium
        status_screen.config(text=f'Прораб сжалился над вами\n и дал {premium} ₽',fg='lime')

    def event_bad(self):
        dop_hurt=random.randint(5,10)
        self.health=self.health-dop_hurt
        status_screen.config(text=f'На работе случилось чп \n в результате которого \n вы потеряли лишние {dop_hurt} здоровья',fg='yellow')

    def event_death(self):
        self.health=0
        game.gameover()
        status_screen.config(text=f'На стройке вам упал на голову кирпич.\n Каска вас не спасла',fg='red')

    def gameover(self):
        go_work.config(state=DISABLED)
        go_chill.config(state=DISABLED)
        go_tofood.config(state=DISABLED)
        restart_button.place(x=250,y=385)

    def win(self):
        status_screen.config(text=f'Вы полностью погасили ипотеку и \n победили!',fg='lime')
        self.gameover()

    def restart(self):
        restart_button.place_forget()
        go_work.config(state=ACTIVE)
        go_chill.config(state=ACTIVE)
        go_tofood.config(state=ACTIVE)
        self.health = 100
        self.food = 100
        self.day = 1
        self.money = 1000
        self.ipoteka = 0
        status_screen.config(text=f'Вы работаете на стройке строителем.\n Вам нужно каждую неделю\n оплачивать ипотеку на {game.ipotekaprice} рублей\n иначе вас выселят ',fg='white')
        game.check()



game=Game()

frame=Frame(okno,bd=1)

health=Label(
    frame,
    width=16,
    height=3,
    font=('consolas', 15),
    bg='black',
    text=(f'Здоровье: {game.health}'),
    fg='white',
)
health.pack(side=LEFT)

food=Label(
    frame,
    width=16,
    height=3,
    font=('consolas', 15),
    bg='black',
    text=(f'Еда: {game.food}'),
    fg='white',
)
food.pack(side=LEFT)

money=Label(
    frame,
    width=16,
    height=3,
    font=('consolas', 15),
    bg='black',
    text=(f'Деньги: {game.money} ₽'),
    fg='white',
)
money.pack(side=LEFT)

day=Label(
    frame,
    width=16,
    height=3,
    font=('consolas', 15),
    bg='black',
    text=(f'День: {game.day} '),
    fg='white',
)
day.pack(side=LEFT)

frame.pack()

status_screen=Label(
    okno,
    width=60,
    height=12,
    bg='black',
    font=('consolas',20),
    text=(f'Вы работаете на стройке строителем.\n Вам нужно каждую неделю\n оплачивать ипотеку на {game.ipotekaprice} рублей\n иначе вас выселят '),
    fg='white',
    bd=2,
)
status_screen.pack()

frame2=Frame(okno,bd=2)

go_work=Button(
    frame2,
    width=18,
    height=3,
    font=('consolas',18),
    text='Пороботать',
    bd=0,
    bg='black',
    fg='white',
    command=game.work,
)
go_work.pack(side=LEFT)

go_chill=Button(
    frame2,
    width=18,
    height=3,
    font=('consolas',18),
    text='Отдохнуть',
    bd=0,
    bg='black',
    fg='white',
    command=game.chill,
)
go_chill.pack(side=LEFT)

go_tofood=Button(
    frame2,
    width=18,
    height=3,
    font=('consolas',18),
    text='Купить еду',
    bd=0,
    bg='black',
    fg='white',
    command=game.buy_food,
)
go_tofood.pack(side=LEFT)

restart_button=Button(
    okno,
    #width=1,
    #height=1,
    font=('consolas',20),
    text='Начать заново',
    bd=0,
    bg='black',
    fg='white',
    #activebackground='black',
    #activeforeground='white',
    command=game.restart,
)

restart_button.place_forget()



frame2.pack()

okno.mainloop()