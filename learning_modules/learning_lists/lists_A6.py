# Goals: Loops, Partially filled lists, Navigating lists by explicit index
seatList = list('')
TOTAL_SEATS = 10
numFilledSeats = 0
initialize = 1
# for i in range(1, TOTAL_SEATS + 1):
#     seatList.append("Seat Number " + str(i))

print(seatList)
initialize = 1

while initialize == 1:
    program = int(input('1: ASSIGN SEAT\n'
                        '2: PRINT SEAT MAP\n'
                        '3: PRINT BOARDING PASS\n'
                        '-1: QUIT\n'))
    if program == 1:
        print("\n\nASSIGN SEAT\n")
        if numFilledSeats < 10:
            name = input("ENTER NAME:").lower()
            if name in seatList in seat:
                print("INVALID NAME. NAME ALREADY ENTERED")
            else:
                numFilledSeats += 1
                seat = name, numFilledSeats
                seatList.append(list(seat))
        elif numFilledSeats <= 10:
            print("FLIGHT IS FULL. NEXT FLIGHT LEAVES IN 3 HOURS")

        initialize = 1
        print(seat)
        print(seatList)


    elif program == 2:
        print("\n\nPRINT SEAT MAP\n")

        initialize = 1

    elif program == 3:
        print("\n\nPRINT BOARDING PASS\n\n")

        type = int(input("Type '1' to get Boarding Pass by seat number.\nType '2' to get Boarding Pass by name"))
        if type == 1:
            search = input('ENTER SEAT NUMBER: ')

        if type == 2:
            search = input('ENTER NAME: ')

        initialize = 1

    elif program == -1:
        initialize = 0
