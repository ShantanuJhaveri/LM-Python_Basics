# Goals: Loops, Partially filled lists, Navigating lists by explicit index
# NO DICTIONARIES

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
                seatList.append(str(name + str(numFilledSeats)))
                print(seatList)
                print(nameList)
        elif numFilledSeats <= 10:
            print("FLIGHT IS FULL. NEXT FLIGHT LEAVES IN 3 HOURS")

        initialize = 1


    elif program == 2:
        print("\n\nPRINT SEAT MAP\n")
        print("***************************************")
        for i in range(1, TOTAL_SEATS + 1):
            print("Seat Number:  #" + str(i) + "\t\t", end="")
            if i <= numFilledSeats:
                print(nameList[i - 1])
            elif i != numFilledSeats:
                print("EMPTY")
        print("***************************************")
        initialize = 1

    elif program == 3:
        print("\n\nPRINT BOARDING PASS\n\n")

        type = int(input("Type '1' to get Boarding Pass by seat number.\nType '2' to get Boarding Pass by name"))
        iT = 0
        if type == 1:
            search = input('ENTER SEAT NUMBER: ')
            searchIndex = nameList[int(search) - 1]
            print("======= BOARDING PASS =======\n"
                  "\tSeat Number:" + str(search) +
                  "\n\tPassenger Name: " + str(searchIndex).upper() +
                  "=============================")
        if type == 2:
            search = input('ENTER NAME: ')
            searchIndex = nameList.index(search)
            print("======= BOARDING PASS =======\n"
                  "\tSeat Number:" + str(searchIndex+1) +
                  "\n\tPassenger Name: " + str(search).upper() +
                  "=============================")
        initialize = 1

    elif program == -1:
        initialize = 0
