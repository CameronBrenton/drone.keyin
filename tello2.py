import tello_abridged
t = tello_abridged.Tello()
#t.connect_and_initialize()
#whatever commands you want you can send like this:
#t.send_command("takeoff")
#t.send_command("left 21")
#t.send_command("land")
#Note: Any command from the table below (or in the SDK PDF) will work.

while True:
    x = str(input("Input a command: "))
    if x.lower() == "forward":
        y = int(input("How many centimetres would you like to move forward? (20 - 500cm): "))
        if y > 20 and y < 500:
            t.send_command("Forward {}".format(y))
        else:
            print("Out of range, try again!(20 - 500) ")
            continue
    
    if x.lower() == "back":
        y = int(input("How many centimetres would you like to move back? (20cm - 500cm): "))
        if y > 20 and y < 500:
            t.send_command("Back {}".format(y))
        else:
            print("Out of range, try again!(20 - 500) ")
            continue
        
    
    if x.lower() == "cw":
        y = int(input("How many degrees clockwise would you like to turn: (1 - 360):"))
        if y > 1 and y < 360:
            t.send_command("cw {}".format(y))
        else:
            print("Degree invalid, must be  between 1 - 360")
            continue
            
    
    if x.lower() == "ccw":
        y = int(input("How many degrees counter-clockwise would you like to turn"))
        if y > 1 and y < 360:
            t.send_command("ccw {}".format(y))
        else:
            print("Degree invalid, must be between 1 - 360")
            continue
        
    if x.lower() == "land":
        y = input("Would you like to land the drone? 'Y' or 'N'")
        if y != 'Y':
            break
        else:
            continue