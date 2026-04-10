        name_change = False
        while True: 
            c_name = input("Do you want to change the name?: Y or N >").upper
            if c_name == "N":
                break
            elif c_name == "Y":
                up_name = input("Select name").lower()
                records.rename(up_rec, up_name)
                name_change = True
                break
            else:
                print("Please enter 'Y' or'N'")