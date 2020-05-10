# Goals: Loops, Partially filled lists, Navigating lists by explicit index
seatList = list('')
nameList = list('')
TOTAL_SEATS = 10
numFilledSeats = 0
initialize = 1
# for i in range(1, TOTAL_SEATS + 1):
#     seatList.append("Seat Number " + str(i))

print(seatList)
initialize = 1

while initialize == 1:
    program = int(input('\n\n1: ASSIGN SEAT\n'
                        '2: PRINT SEAT MAP\n'
                        '3: PRINT BOARDING PASS\n'
                        '-1: QUIT\n'))
    if program == 1:
        print("\n\nASSIGN SEAT\n")
        if numFilledSeats < 10:
            name = input("ENTER NAME:").lower()
            if name in nameList:
                print("INVALID NAME. NAME ALREADY ENTERED")
            else:
                nameList.append(name)
                numFilledSeats += 1
                seat = name, numFilledSeats
                seatList.append(list(seat))
                print(seatList)
                print(nameList)
        elif numFilledSeats <= 10:
            print("FLIGHT IS FULL. NEXT FLIGHT LEAVES IN 3 HOURS")

        initialize = 1


    elif program == 2:
        print("\n\nPRINT SEAT MAP\n")
        print("***************************************")
        for i in range(1,TOTAL_SEATS+1):
            print("Seat Number:  #" + str(i) + "\t\t", end="")
            if i <= numFilledSeats:
                print(nameList[i-1])
            elif i != numFilledSeats:
                print("")
        print("***************************************")
        initialize = 1

    elif program == 3:
        print("\n\nPRINT BOARDING PASS\n\n")

        type = int(input("Type '1' to get Boarding Pass by seat number.\nType '2' to get Boarding Pass by name"))
        iT = 0
        if type == 1:
            while iT == 0:
                search = input('ENTER SEAT NUMBER: ')
                if search.isalpha():
                    iT = 1
                else:
                    index = seatList[seat][search]
                    print(index)
        if type == 2:
            while iT:
                search = input('ENTER NAME: ')
                if search.isdigit():
                    iT = 1
                else:
                    print()
        initialize = 1

    elif program == -1:
        initialize = 0
