class Star_Hall:
    hall_list = []
    
    def add_hall(self, obj):
        self.hall_list.append(obj)


class Hall(Star_Hall):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        super().add_hall(self)


    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = [[False for i in range(self.__cols)] for i in range(self.__rows)]


    def book_seats(self, customer_name, phone_number, show_id, seats_for_show):
        if self.__seats.get(show_id) is not None:
            for seat in seats_for_show:
                if (seat[0] > 0 and seat[0] <= self.__rows) and (seat[1] > 0 and seat[1] <= self.__cols):
                    if self.__seats[show_id][seat[0]-1][seat[1]-1] == False:
                        self.__seats[show_id][seat[0]-1][seat[1]-1] = True
                        print(f'Seat with row: {seat[0]}, column: {seat[1]} booked.') 
                    else:
                        print(f'Seat with row: {seat[0]}, colum: {seat[1]} already booked.')
                else:
                    print(f"Seat with row: {seat[0]}, column: {seat[1]} is invalid")
        else:
            print('Invalid id of show')
            return

        

    def view_show_list(self):
        for i in self.__show_list:
            print(f"MOVIE NAME: {i[1]}\tSHOW ID: {i[0]}\tTIME: {i[2]}")

    def view_available_seats(self, show_id):
        if show_id in self.__seats.keys():
            for i in range(len(self.__seats[show_id])):
                for j in range(len(self.__seats[show_id][i])):
                    if self.__seats[show_id][i][j] == False:
                        print(f'{chr(65+i)}{j+1}', end="\t")
                    else:
                        print("XX", end="\t")
                print('\n')
        else:
            print("Invalid show id")


star = Hall(3, 3, 1)

star.entry_show('ae123', 'Black Adam', 'Oct 26 2022 10:00 AM')
star.entry_show('ae50', 'Spiderman', 'Oct 28 2022 8:00 PM')



while True:
    inp = input("1. VIEW ALL SHOWS TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK SEAT\n(Press 'q' to quit)\nEnter option: ")
    print(inp)
    if inp != 'q' and int(inp) in [1, 2, 3]:
        if int(inp) == 1:
            print("\n-------------------------------------------------------\n")
            star.view_show_list()
            print("\n-------------------------------------------------------\n")
        elif int(inp) == 2:
            id_inp = input("ENTER SHOW ID: ")
            print("\n-------------------------------------------------------\n")
            star.view_available_seats(id_inp)
            print("\n-------------------------------------------------------\n")
        elif int(inp) == 3:
            print("\n-------------------------------------------------------\n")
            name_inp = input("ENTER CUSTOMER NAME: ")
            phone_inp = input("ENTER CUSTOMER PHONE NUMBER: ")
            show_id_inp = input("ENTER SHOW ID: ")
            tickets_no = input("ENTER NUMBER OF TICKETS: ")
            tickets = []
            view_tickets = []
            for i in range(int(tickets_no)):
                seat_no = input("ENTER SEAT NO: ")
                view_tickets.append(seat_no)
                seat_row = ord(seat_no[0])-64
                seat_col = int(seat_no[1])
                tickets.append((seat_row, seat_col))
            star.book_seats(name_inp, phone_inp, show_id_inp, tickets)
            print("-------------------------------------------------------\n")
            print(f'CUSTOMER NAME: {name_inp}')
            print(f'PHONE NUMBER: {phone_inp}')
            print(f'SHOW ID: {show_id_inp}')
            print(f'TICKETS: {view_tickets}')
            print("\n-------------------------------------------------------\n")

    else:
        break