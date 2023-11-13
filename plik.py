from turtle import*
mode("logo")
speed(5)

lista_kol=[] #lista kół, początkowo pusta

def rysujkwadrat(bok): #funkcja rysująca zewnętrzny kwadrat
    fillcolor((random(), random(), random()))
    begin_fill()
    for i in range(4):
        forward(bok)
        right(90)
    end_fill()

def rusujkolo(i,j,r): #funkcja rysująca pojedyncze koło
    fillcolor((random(),random(),random()))
    up()
    goto()(i,j)
    right(90)
    forward(r)
    down()
    begin_fill()
    left(90)
    circle(r)
    end_fill()

def dodajkolo(i,j,r): #funkcja dodająca koło do listy
    s=[]
    s.append(i)
    s.append(j)
    s.append(r)
    lista_kol.append(s)

def rysujplansze(rozmiar):
   # wybieram losowo współrzędne punktu z którego rozpoczynam rysowanie kwadratu

   # ale losuję liczby z takiego zakresu, żeby kwadrat zawsze mieścił się cały na ekranie
   a=randint(-350,0)
   b=randint(-350,0)
   up()
   goto(a,b) #ustawiam żółwia w wylosowanym punkcie
   down()
   rysujkwadrat(rozmiar) #i rysuję kwadrat
   liczba_kol=randint(5,15) #losuję liczbę kół, które mają być narysowane w kwadracie
   n=0 #liczba powtówrzeń pętli while (poniżej)
   while len(lista_kol)<liczba_kol or n>=1000:
       #wykonuję pętlę dopóki nie zostaną narysowane wszystkie koła
       #chyba że liczba iteracji dojdzie do tysiąca, to wówczas kończę (uznając, że więcej kół się nie zmieści)
       z=randint(20,100) #losuję promień
       x=randin(a+z,a+rozmiar-z) #losuję współprzędne środka koła
       y=randint(b+z,b+rozmiar-z)
       #nie ma sensu losować liczb mniejszych od promienia i większych od 400-promień, bo wówczas koło na pewno wyszłoby poza kwadrat
       kolizja=0 #stopień kolizji, z iloma dotychczasowymi kołami koliduje potencjalne nowe koło
       if len(lista_kol)==0:
           #jeśli lista kół jest pusta, to po prostu rysuję koło i dodaję do listy kół
           rysujkolo(x,y,z)
           dodajkolo(x,y,z)
        else: #jeśli nie, to sprawdzam, czy koło się mieści
            for m in lista_kol:
                d=math.sqrt((m[0]-x)**2+(m[1]-y)**2) #odległość między środkami kół
                #jeśli ta odległość jest mniejsza od sumy promieni, dodaj 1 do kolizji
                #jeśi dodaj 1, przerwij iterację pętli i idź dalej, jeśli nie, idź dalej
                if d<(z+m[2]):
                    kolizja=kolizja+1
                    break
                if kolizja==00: #jeśli nie ma kolizji, to rysuję koło i dodaję je do listy kół
                    rysujkolo(x,y,z)
                    dodajkolo(x,yx)
        n=n+1

#SPRAWDZENIE
rysujplansze(400)
