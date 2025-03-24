fruits = ['Apple', 'banana', 'orange']
for f in fruits:
    print (f.upper())
    inputdef input_film (): 
    print("Welcome to our cinema, we have these films available:")
    text_list = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
    for item in text_list:
        print(item)
    films = {"Inception", "The Matrix", "Interstellar", "The Dark Knight"} 

    login = input("Choose a movie: ")

    if login in films:
        print(f"You chose: {login}")
    else:
        print("We don't have this movie.")
    return login

def input_ticket():
    print ("Another options")
    print ("Number of tickets")

    ticket = int(input ("Enter how many tickets you are buying:"))
    print (f"You order - {ticket} ticket (s)")
    if ticket >100: print ("too much")
    return ticket

def seat_types():
    print("Now chose seat type.")
    print ("We have regular and VIP seats")
    print("Regular cost - 7$")
    print("VIP cost - 14$")
    print ("Write '1' if regular or '2' for VIP")

    chair = int(input ("What type? "))
    if chair == 1: 
        seat_type = "Regular seat (s)"
        cost = 7
    elif chair == 2: 
        seat_type = "VIP seat (s)"
        cost = 14
    else:
        seat_type = ("Unknown type")
    return cost, seat_type

def booking_price_calculation (ticket, seat_type, login, cost):
    print(f"Booking {ticket} {seat_type} for {login}")

    print ("That will cost:")
    print(f"{ticket * cost}$ ")

def main():
    login = input_film()
    ticket = input_ticket()
    cost,seat_type = seat_types()
    booking_price_calculation(ticket, seat_type, login, cost)

if __name__== "__main__":
    main()