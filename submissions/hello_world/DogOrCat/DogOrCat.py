import webbrowser

imgDog = 'https://i.imgur.com/rXHNe2T.jpeg'
imgCat  = 'https://images.unsplash.com/photo-1534567110243-8875d64ca8ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=987&q=80'

while True:
        x = int(input("Enter '1' for Dog. Enter '2' for Cat: "))
        if x == 1:
            webbrowser.open(imgDog)
            break
        elif x == 2:
            webbrowser.open(imgCat)
            break
        else:
            print("\n Error in selection. Select Again.\n")

print("Hehehe")
           
   

