import pyautogui as pg
import webbrowser as wb
import time as t

points = 0
randomnumberthing = 0

number = pg.prompt("What is your favorite number? ")
if number == "3":
    pg.alert("Three is a lucky number")
    points += 3
    t.sleep(1)
elif number == "4":
    wb.open("https://vignette.wikia.nocookie.net/phobia/images/d/d0/4.jpg/revision/latest?cb=20161127143001")
    points += 4
    t.sleep(3)
elif number == "5":
    wb.open("https://vignette.wikia.nocookie.net/phobia/images/0/03/5.jpg/revision/latest?cb=20170102100251")
    points += 5
    t.sleep(3)
elif number == "6":
    wb.open("https://weeknumber.net/gfx/200x200/6.png")
    points += 6
    t.sleep(3)
elif number == "7":
    wb.open("https://weeknumber.net/gfx/200x200/7.png")
    points += 7
    t.sleep(3)
elif number == "8":
    wb.open ("https://weeknumber.net/gfx/200x200/8.png")
    points += 8
    t.sleep(3)
else:
    pg.alert("Your favorite number is " + number)
    points = number
    randomnumberthing = number
    t.sleep(1)



movie = pg.prompt("What is your favorite movie? ")
if movie == "National Tresure":
    pg.alert("I like the first one better than the second. Cool!")
    points += 3
    t.sleep(2)
elif movie == "Harry Potter":
    wb.open("https://www.irishtimes.com/polopoly_fs/1.3170107.1501253408!/image/image.jpg_gen/derivatives/box_620_330/image.jpg")
    points += 2
    t.sleep(3)
elif movie == "the lego movie":
    wb.open("https://is5-ssl.mzstatic.com/image/thumb/Video4/v4/f1/6f/b1/f16fb1b4-5d39-ea05-2afa-f7cfa13bf782/pr_source.lsr/268x0w.png")
    points -= 6
    t.sleep(3)
elif movie == "Star Wars":
    wb.open("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/1280px-Star_Wars_Logo.svg.png")
    points += 3
    t.sleep(3)
elif movie == "Superman":
    wb.open("https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/SupermanRoss.png/250px-SupermanRoss.png")
    points -= 4
    t.sleep(3)
elif movie == "Batman":
    wb.open("https://upload.wikimedia.org/wikipedia/en/8/87/Batman_DC_Comics.png")
    points -= 3
    t.sleep(3)
else:
    pg.alert("I really like " + movie + " too!")
    points += 2
    t.sleep(1)

book = pg.prompt("What is your favorite book? ")
if book == "James and the giant peach":
    wb.open ("https://images-na.ssl-images-amazon.com/images/I/51I9ZyNs8PL._SY445_.jpg")
    points += 4
    t.sleep(3)
elif book == movie:
    pg.alert("so you like the book, too!")
    points += 6
    t.sleep(1)
elif book == "the lion the whitch and the wardrobe":
    wb.open("https://m.media-amazon.com/images/M/MV5BMTc0NTUwMTU5OV5BMl5BanBnXkFtZTcwNjAwNzQzMw@@._V1_.jpg")
    points += 3
    t.sleep(3)
elif book == "The Hunger Games":
    wb.open("https://images-na.ssl-images-amazon.com/images/I/41LPBRNaVCL._SX355_BO1,204,203,200_.jpg")
    points += 2
    t.sleep(3)
elif book == "How to win friends and Influence people":
    wb.open("https://images-na.ssl-images-amazon.com/images/I/51X7dEUFgoL._SX320_BO1,204,203,200_.jpg")
    points += 4
    t.sleep(3)
elif book == "Magnus Chase":
    wb.open("https://images-na.ssl-images-amazon.com/images/I/A1GFa40NVoL.jpg")
    points -= 3
    t.sleep(3)
else:
    pg.alert (book + " is a good book.")
    points -= 1
    t.sleep(1)

candy = pg.prompt("What is your favorite candy? ")
if candy == "Starburst":
    pg.alert("I like those alot, too.")
    t.sleep(3)
    points += 2
elif candy == "Twizzlers":
    wb.open("https://pics.drugstore.com/prodimg/93030/900.jpg")
    points += 3
    t.sleep(3)
elif candy == "chocolate":
    wb.open("https://target.scene7.com/is/image/Target/GUEST_666737c9-4810-406b-844a-f6626d83b0da?wid=488&hei=488&fmt=pjpeg")
    points -= 3
    t.sleep(3)
elif candy == "marshmallows":
    wb.open("https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iZduHaIniSQ0/v1/800x-1.jpg")
    points -= 4
    t.sleep(3)
elif candy == "Scittles":
    wb.open("https://static1.squarespace.com/static/5402e23ce4b0a7034afad3a2/t/59ef40b2b7411ccab4352aaf/1508851905651/Skittles+candy")
    points += 2
    t.sleep(3)
elif candy == "twix":
    wb.open("https://kiwicornerdairy.com/pub/media/catalog/product/cache/c687aa7517cf01e65c009f6943c2b1e9/t/w/twix-cookie-bar.png")
    points += 3
    t.sleep(3)
else:
    pg.alert("I really like " + candy + " too!")
    points += 1
    t.sleep(1)


day = pg.prompt("What is your favorite day of the week? ")
if day == "Saturday":
    pg.alert("Yes. I love sleeping in on the weekend!")
    points += 4
    t.sleep(3)
elif day == "Monday":
    wb.open("http://fianation.com/wp-content/uploads/2018/08/hello-monday-handwritten-modern-calligraphy-inscription-vector-brush-letters-style-white-background-90761998.jpg")
    points -= 6
    t.sleep(3)
elif day == "Tuesday":
    wb.open("https://bcsbuzz.files.wordpress.com/2018/08/week-days-motivation-quotes-tuesday-vector-handwritten-brush-lettering-your-design-white-background-82229909.jpg?w=800&h=580&crop=1")
    points -= 2
    t.sleep(3)
elif day == "Thursday":
    wb.open ("https://www.thefactsite.com/wp-content/uploads/2017/07/thursday-facts.jpg")
    points += 2
    t.sleep(3)
elif day == "Wednessday":
    wb.open("https://www.thefactsite.com/wp-content/uploads/2017/07/wednesday-facts.jpg")
    points -= 1
    t.sleep(3)
elif "Friday":
    wb.open("https://previews.123rf.com/images/teploleta/teploleta1602/teploleta160200010/52587383-happy-friday-positive-inspiration-quote-on-a-watercolor-blot-background.jpg")
    points += 3
    t.sleep(3)
else:
    pg.alert("I really like " + day + " too!")
    points += 1
    t.sleep(1)




pg.alert("you have " + str(points) + " points.")



'''
rb = input("Are you thinking of a card? ")
if rb == "yes":
    cs = input("are you thinking of a black card? ")
    if cs == "yes":
          number = input("Are you thinking of a Club?")
          if number == "yes!!":
              pg.alert("two of clubs!")
          elif number == "yes!!!":
              print("three of clubs")
          elif number == "yes!!!!":
              print("four of clubs")
          elif number == "yes!!!!!":
              print("five of clubs")
          elif number == "yes!!!!!!":
              print("six of clubs")
          elif number == "yes!!!!!!!":
              print("seven of clubs")
          elif number == "yes!!!!!!!!":
              print("eight of clubs")
          elif number == "yes!!!!!!!!!":
              print("nine of clubs")
          elif number == "yes!!!!!!!!!!":
              print("ten of clubs")
          elif number == "yes":
              print("Jack of clubs")
          elif number == "Yes":
              print("Queen of Clubs")
          elif number == "YES":
              print("King of Clubs")
          elif number == "yes!":
              print("Ace of Clubs")              
    elif cs == "Yes":
        number = input("Are you thinking of a Spade?")
        if number == "yes!!":
            print("two of Spades!")
        elif number == "yes!!!":
            print("three of spades")
        elif number == "yes!!!!":
            print("four of spades")
        elif number == "yes!!!!!":
            print("five of spades")
        elif number == "yes!!!!!!":
            print("six of spades")
        elif number == "yes!!!!!!!":
            wb.open("https://www.youtube.com/watch?v=SpYuvKjlRFE")
        elif number == "yes!!!!!!!!":
            print("eight of spades")
        elif number == "yes!!!!!!!!!":
            print("nine of spades")
        elif number == "yes!!!!!!!!!!":
            print("ten of spades")
        elif number == "yes":
            print("Jack of spades")
        elif number == "Yes":
            print("Queen of spades")
        elif number == "YES":
            print("King of spades")
        elif number == "yes!":
            print("Ace of spades")

elif rb == "Yes":
    hd = input("are you thinking of a red card? ")
    if hd == "yes":
        number = input("are you thinking of a diamond?")
        if number == "yes!!":
            wb.open("https://www.youtube.com/watch?v=8nPir_vzuVM")
        elif number == "yes!!!":
            print("three of diamonds")
        elif number == "yes!!!!":
            print("four of diamonds")
        elif number == "yes!!!!!":
            print("five of diamond")
        elif number == "yes!!!!!!":
            wb.open("https://www.youtube.com/watch?v=APvo6mHXJjY")
        elif number == "yes!!!!!!!":
            print("seven of diamonds")
        elif number == "yes!!!!!!!!":
            print("eight of diamonds")
        elif number == "yes!!!!!!!!!":
            print("nine of diamonds")
        elif number == "yes!!!!!!!!!!":
            print("ten of diamonds")
        elif number == "yes":
            print("Jack of diamonds")
        elif number == "Yes":
            print("Queen of diamonds")
        elif number == "YES":
            print("King of diamonds")
        elif number == "yes!":
            print("Ace of diamonds")
    elif hd == "Yes":
        number = input("are you thinking of a heart?")
        if number == "yes!!":
            print("two of hearts!")
        elif number == "yes!!!":
            print("three of hearts")
        elif number == "yes!!!!":
            print("four of hearts")
        elif number == "yes!!!!!":
            print("five of hearts")
        elif number == "yes!!!!!!":
            print("six of heartss")
        elif number == "yes!!!!!!!":
            wb.open("https://cdn.shopify.com/s/files/1/1850/0919/products/card3.1.1_800x.png?v=1517513308")
        elif number == "yes!!!!!!!!":
            print("eight of heartss")
        elif number == "yes!!!!!!!!!":
            print("nine of hearts")
        elif number == "yes!!!!!!!!!!":
            print("ten of heartss")
        elif number == "yes":
            print("Jack of hearts")
        elif number == "Yes":
            print("Queen of hearts")
        elif number == "YES":
            print("King of hearts")
        elif number == "yes!":
            wb.open("https://www.youtube.com/watch?v=AV7C7gLiIgo")
'''
