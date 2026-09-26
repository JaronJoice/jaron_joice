import mysql.connector as sql
d=sql.connect(host="localhost",user="root",password="root",database="hotel")
if d.is_connected:
    c=d.cursor()
    c.execute("use hotel ;")
    guest_ids = []
    c.execute("SELECT id FROM guests")
    guest_ids = [row[0] for row in c.fetchall()]


    def thanks():
        print()
        print("THANK YOU FOR USING HOTEL MANAGEMENT SYSTEM !! ")
        print("========================================================================================")
        print("========================================================================================")
        


    def insert():
        try:
            gid=eval(input("Enter the guest number : "))
        except NameError:
            print("ENTER A NUMBER ")
            print()
            gid=eval(input("Enter the guest number : "))
        while gid in guest_ids:
            next_id = max(guest_ids) + 1 if guest_ids else 1
            print()
            print("THIS ID HAS ALREADY BEEN ENTERED")
            print("THE NEXT ID TO BE ENTERED IS :", next_id)
            print()
            try:
                gid = int(input("Enter the guest number : "))
            except ValueError:
                print("ENTER A NUMBER")
                print()
        fn=input("Enter the first name  : ").upper().strip()
        ln=input("Enter the last name   : ").upper().strip()
        ph=input("Enter the phone number : ").upper().strip()
        e=input("Enter the email : ").lower()
        e.strip()
        
        #inputing date
        yr=input("Enter the year  : ")
        mo=input("Enter the month : ")
        while int(mo) not in range(1,13):
            print("ENTER A VALID MONTH")
            print("[ENTER THE VALUE AS NUMBERS]")
            print()
        day=input("Enter the day  : ")
        while int(day) not in range(1,32):
            print("ENTER A VALID DAY")
            print("[ENTER THE VALUE AS NUMBERS]")
            print()
            day=input("Enter the day  : ")
        date=(f"{yr}-{mo}-{day}")

        tday=eval(input("Enter the number of days : "))
        
        s="insert into guests values ({},'{}','{}','{}','{}','{}',{})".format(gid,fn,ln,ph,e,date,tday)
        c.execute(s)
        d.commit()
        guest_ids.append(gid)

        print("SUCCESFULLY ADDED DATAS")
    

    def show():
        print()
        print("1.ID ")
        print("2.NAME ")
        print("3.PHONE NUMBER ")
        print("4.EMAIL ")
        print("5.DATE ")
        print("6.NO OF DAYS STAYED ")
        print("7.ALL")
        print("8.GO BACK ")
        print()
        v=input("ENTER WHAT TO SEARCH BY : ").strip()
        #search using id
        if v.upper()=="ID" or v=="1":
            print()
            x=eval(input("ENTER THE ID YOU WANT TO SEARCH WITH : "))
            s="select * from guests where id={} ; ".format(x)
            c.execute(s)
            data=c.fetchall()
            if len(data)==0:
                print()
                print("NO DATA FOUND")
                print()
            else:
                for i in data :
                    print(i)
                

        #search using name
        if v.lower()=="name" or int(v)==2:
            print()
            print("SEARCH USING :")
            print("1. FIRST NAME")
            print("2. LAST  NAME")
            print()
            o=input("ENTER YOUR CHOICE : ").strip()
            
            while o=="":
                print("ENTER A VALID INPUT")
                print()
                o=input("ENTER YOUR CHOICE : ").strip()
            while o.lower() not in ["first","first name","1","last","last name",'2']:
                print("ENTER A VALID INPUT ")
                print()
                o=input("ENTER YOUR CHOICE : ").strip()
                
            if o.lower()=="first" or o.lower()=="first name" or int(o)==1:
                print()
                x=input("ENTER THE NAME YOU WANT TO SEARCH USING : ").lower()
                x.strip()
                s="select * from guests where first_name='{}' ; ".format(x)

            if o.lower()=="last" or o.lower()=="last name" or int(o)==2:
                print()
                x=input("ENTER THE NAME YOU WANT TO SEARCH USING : ").lower()
                x.strip()
                s="select * from guests where last_name='{}' ; ".format(x)
            
                
            c.execute(s)
            data=c.fetchall()
            if len(data)==0:
                print()
                print("NO DATA FOUND")
                print()
            else:
                for i in data :
                    print(i)
                

        #search using phone number
        if v.lower()=="phone" or v.lower()=="phoneno" or v.lower()=="phone no" or v.lower()=="phone_no" or eval(v)==3:
            print()
            x=input("Enter the phone number you want to search using : ").strip()
            s="select * from guests where phone_no = '{}' ; ".format(x)
            c.execute(s)
            data=c.fetchall()
            if len(data)==0:
                print()
                print("NO DATA FOUND")
                print()
            else:
                for i in data :
                    print(i)
                

        #search using email
        if v.lower()=="email" or eval(v)==4:
            print()
            x=input("Enter the email you want to search using : ").strip()
            while x=="" or not x.endswith(".com"):
                print("ENTER A VALID INPUT")
                print()
                x=input("Enter the email you want to search using : ").strip()
            s="select * from guests where email = '{}' ; ".format(x)
            c.execute(s)
            data=c.fetchall()
            if len(data)==0:
                print()
                print("NO DATA FOUND")
                print()
            else:
                for i in data :
                    print(i)

        #search using date
        try:
            if v.lower()=="entry_date" or v.lower()=="entrydate" or v.lower()=="entry date" or eval(v)==5:
                print()
                yr=input("Enter the year to search using  : ")
                mo=input("Enter the month to search using : ")
                while int(mo) not in range(1,13):
                    print("ENTER A VALID MONTH")
                    print("[ENTER THE VALUE AS NUMBERS]")
                    print()
                    mo=input("Enter the month to search using : ")
                day=input("Enter the day to search using  : ")
                while int(day) not in range(1,32):
                    print("ENTER A VALID DAY")
                    print("[ENTER THE VALUE AS NUMBERS]")
                    print()
                    day=input("Enter the day to search using  : ")
                x=(f"{yr}-{mo}-{day}")
                s="select * from guests where entry_date = '{}' ; ".format(x)
                c.execute(s)
                data=c.fetchall()
                if len(data)==0:
                    print()
                    print("NO DATA FOUND")
                    print()
                else:
                    for i in data :
                        print(i)

        except ValueError:
            print("PLEASE ENTER A VALID DATE")
            print()
            yr=input("Enter the year to search using  : ")
            mo=input("Enter the month to search using : ")
            day=input("Enter the day to search using  : ")
            x=(f"{yr}-{mo}-{day}")
            s="select * from guests where entry_date = '{}' ; ".format(x)
            c.execute(s)
            data=c.fetchall()
            if len(data)==0:
                print()
                print("NO DATA FOUND")
                print()
            else:
                for i in data :
                    print(i)
        except NameError :
            print("PLEASE ENTER DATE USING NUMBERS")
            print()
            yr=input("Enter the year to search using  : ")
            mo=input("Enter the month to search using : ")
            day=input("Enter the day to search using  : ")
            x=(f"{yr}-{mo}-{day}")
            s="select * from guests where entry_date = '{}' ; ".format(x)
            c.execute(s)
            data=c.fetchall()
            if len(data)==0:
                print()
                print("NO DATA FOUND")
                print()
            else:
                for i in data :
                    print(i)
        except:
            print("PLEASE ENTER A VALID DATE")
            print()
            print("[ ENTER THE DATE USING NUMBERS ]")
            print()
            print()
            yr=input("Enter the year to search using  : ")
            mo=input("Enter the month to search using : ")
            day=input("Enter the day to search using  : ")
            x=(f"{yr}-{mo}-{day}")
            s="select * from guests where entry_date = '{}' ; ".format(x)
            c.execute(s)
            data=c.fetchall()
            if len(data)==0:
                print()
                print("NO DATA FOUND")
                print()
            else:
                for i in data :
                    print(i)

        #search using total days
        try :
            if v.lower()=="total_days" or v.lower()=="totaldays" or v.lower()=="total days" or v.lower()=="totalday" or v.lower()=="total day" or v.lower()=="total_day" or eval(v)==6:
                print()
                x=eval(input("Enter the number of days you want to search using : "))
                s="select * from guests where total_days ={} ; ".format(x)
                c.execute(s)
                data=c.fetchall()
                if len(data)==0:
                    print()
                    print("NO DATA FOUND")
                    print()
                else:
                    for i in data :
                        print(i)
        except NameError :
            print("ENTER A NUMBER ")
            print()
            x=eval(input("Enter the number of days you want to search using : "))
            s="select * from guests where total_days ={} ; ".format(x)
            c.execute(s)
            data=c.fetchall()
            if len(data)==0:
                print()
                print("NO DATA FOUND")
                print()
            else:
                for i in data :
                    print(i)

        #search all
        if v.lower()=="all" or eval(v)==7:
            print()
            
            s="select * from guests; "
            c.execute(s)
            data=c.fetchall()
            if len(data)==0:
                print()
                print("NO DATA FOUND")
                print()
            else:
                for i in data :
                    print(i)

        #EXIT
        if v.lower()=="exit" or eval(v)==8:
            ini()

        #if not correct value
        l=['1','2','3','4','5','6','7','8']
        while v not in l:
            print("ENTER A VALID INPUT ")
            show()



    def update():
        from datetime import date

        options = {
            "1": "ID",
            "2": "FIRST NAME",
            "3": "LAST NAME",
            "4": "PHONE NUMBER",
            "5": "EMAIL",
            "6": "DATE",
            "7": "NO. OF DAYS STAYED"
        }

        fields = {
            "1": "id", "id": "id",
            "2": "first_name", "first name": "first_name",
            "3": "last_name", "last name": "last_name",
            "4": "phone_no", "phone": "phone_no", "phone number": "phone_no",
            "5": "email",
            "6": "entry_date", "date": "entry_date",
            "7": "total_days", "total days": "total_days"
        }

        print("\nWHAT DO YOU WANT TO UPDATE?")
        for number, label in options.items():
            print(number + ". " + label)
        print("8. GO BACK")
        print()

        update_choice = input("ENTER WHAT TO UPDATE: ").strip().lower()

        while update_choice=="":
            print("PLEASE ENTER A VALUE")
            print()
            update_choice = input("ENTER WHAT TO UPDATE: ").strip().lower()
            
        if update_choice in {"8", "exit", "back", "go back"}:
            ini()
            return

        update_column = fields.get(update_choice)

        if update_column is None:
            print("ENTER A VALID INPUT")
            return

        if update_column in {"id", "total_days"}:
            try:
                new_value = int(input("ENTER THE NEW VALUE: ").strip())
            except ValueError:
                print("ENTER A NUMBER")
                return

        elif update_column == "entry_date":
            try:
                yr = int(input("Enter the year: "))
                mo = int(input("Enter the month: "))
                day = int(input("Enter the day: "))
                new_value = date(yr, mo, day)
            except ValueError:
                print("PLEASE ENTER A VALID DATE")
                return

        else:
            new_value = input("ENTER THE NEW VALUE: ").strip()

            if update_column in {"first_name", "last_name"}:
                new_value = new_value.upper()
            elif update_column == "email":
                new_value = new_value.lower()

        print("\nSEARCH FOR THE GUEST BY:")
        for number, label in options.items():
            print(number + ". " + label)
        print("8. GO BACK")
        print()

        search_choice = input("ENTER WHAT TO SEARCH BY: ").strip().lower()

        if search_choice in {"8", "exit", "back", "go back"}:
            ini()
            return

        search_column = fields.get(search_choice)

        if search_column is None:
            print("ENTER A VALID INPUT")
            return

        if search_column in {"id", "total_days"}:
            try:
                search_value = int(input("ENTER THE VALUE TO SEARCH WITH: ").strip())
            except ValueError:
                print("ENTER A NUMBER")
                return

        elif search_column == "entry_date":
            try:
                yr = int(input("Enter the year to search with: "))
                mo = int(input("Enter the month to search with: "))
                day = int(input("Enter the day to search with: "))
                search_value = date(yr, mo, day)
            except ValueError:
                print("PLEASE ENTER A VALID DATE")
                return

        else:
            search_value = input("ENTER THE VALUE TO SEARCH WITH: ").strip()

            if search_column in {"first_name", "last_name"}:
                search_value = search_value.upper()
            elif search_column == "email":
                search_value = search_value.lower()

        s = "SELECT * FROM guests WHERE `{}` = %s".format(search_column)
        c.execute(s, (search_value,))
        data = c.fetchall()

        if len(data) == 0:
            print("\nNO DATA FOUND")
            return

        print("\nDATA FOUND:")
        for row in data:
            print(row)

        s = "UPDATE guests SET `{}` = %s WHERE `{}` = %s".format(
            update_column, search_column
        )
        c.execute(s, (new_value, search_value))
        d.commit()

        print("\nSUCCESSFULLY UPDATED DATA")

        display_value = new_value if update_column == search_column else search_value
        s = "SELECT * FROM guests WHERE `{}` = %s".format(search_column)
        c.execute(s, (display_value,))
        data = c.fetchall()

        for row in data:
            print(row)


     
    def delete():
        from datetime import date

        options = {
            "1": "ID",
            "2": "FIRST NAME",
            "3": "LAST NAME",
            "4": "PHONE NUMBER",
            "5": "EMAIL",
            "6": "DATE",
            "7": "NO. OF DAYS STAYED"
        }

        fields = {
            "1": "id", "id": "id",
            "2": "first_name", "first name": "first_name",
            "3": "last_name", "last name": "last_name",
            "4": "phone_no", "phone": "phone_no", "phone number": "phone_no",
            "5": "email",
            "6": "entry_date", "date": "entry_date",
            "7": "total_days", "total days": "total_days"
        }

        print("\nWHAT DO YOU WANT TO DELETE?")
        for number, label in options.items():
            print(number + ". " + label)
        print("8. GO BACK")
        print()

        delete_choice = input("ENTER WHAT TO DELETE: ").strip().lower()

        if delete_choice in {"8", "exit", "back", "go back"}:
            ini()
            return

        delete_column = fields.get(delete_choice)

        if delete_column is None:
            print("ENTER A VALID INPUT")
            return

        if delete_column in {"id", "total_days"}:
            try:
                delete_value = int(input("ENTER THE VALUE OF THIS FIELD: ").strip())
            except ValueError:
                print("ENTER A NUMBER")
                return

        elif delete_column == "entry_date":
            try:
                delete_value = date.fromisoformat(
                    input("ENTER THE DATE (YYYY-MM-DD): ").strip()
                )
            except ValueError:
                print("PLEASE ENTER A VALID DATE AS YYYY-MM-DD")
                return

        else:
            delete_value = input("ENTER THE VALUE OF THIS FIELD: ").strip()

            if delete_column in {"first_name", "last_name"}:
                delete_value = delete_value.upper()
            elif delete_column == "email":
                delete_value = delete_value.lower()

        print("\nSEARCH FOR THE RECORD USING:")
        for number, label in options.items():
            print(number + ". " + label)
        print("8. GO BACK")
        print()

        search_choice = input("ENTER WHAT TO SEARCH BY: ").strip().lower()

        if search_choice in {"8", "exit", "back", "go back"}:
            ini()
            return

        search_column = fields.get(search_choice)

        if search_column is None:
            print("ENTER A VALID INPUT")
            return

        if search_column in {"id", "total_days"}:
            try:
                search_value = int(input("ENTER THE VALUE TO SEARCH WITH: ").strip())
            except ValueError:
                print("ENTER A NUMBER")
                return

        elif search_column == "entry_date":
            try:
                search_value = date.fromisoformat(
                    input("ENTER THE DATE TO SEARCH WITH (YYYY-MM-DD): ").strip()
                )
            except ValueError:
                print("PLEASE ENTER A VALID DATE AS YYYY-MM-DD")
                return

        else:
            search_value = input("ENTER THE VALUE TO SEARCH WITH: ").strip()

            if search_column in {"first_name", "last_name"}:
                search_value = search_value.upper()
            elif search_column == "email":
                search_value = search_value.lower()

        s = "SELECT * FROM guests WHERE `{}` = %s AND `{}` = %s".format(
            delete_column, search_column
        )
        c.execute(s, (delete_value, search_value))
        data = c.fetchall()

        if len(data) == 0:
            print("\nNO DATA FOUND")
            return

        print("\nRECORD FOUND:")
        for row in data:
            print(row)

        if len(data) > 1:
            print("MORE THAN ONE RECORD WAS FOUND. SEARCH USING ID TO DELETE ONE RECORD.")
            return

        confirm = input("ARE YOU SURE YOU WANT TO DELETE THIS RECORD? (YES/NO): ").strip().lower()

        if confirm not in {"yes", "y", "1"}:
            print("DELETE CANCELLED")
            return

        s = "DELETE FROM guests WHERE `{}` = %s AND `{}` = %s".format(
            delete_column, search_column
        )
        c.execute(s, (delete_value, search_value))
        d.commit()
        print("SUCCESSFULLY DELETED DATA")


    def ini():
        ans=True
        while ans:
            print("========================================================================================")
            
            print("========================================================================================")
            print()
            print("HOTEL MANAGEMENT SYSTEM")
            print()
            print("WELCOME TO HOTEL MANAGEMEBNT SYSTEM")
            print()
            print("[ PLEASE ENTER THE NUMBER OF THE CORRESPONDING TASK OR OPERATION ]")
            print()
            print("========================================================================================")
            print()
            print("1. SEARCH DETAILS ")
            print("2. ADD DATA ")
            print("3. UPDATE DATA")
            print("4. DELETE DATA")
            print()
            b=input("SELECT THE TASK YOU WANT TO DO : ").strip()
            while b=="":
                print("PLEASE ENTER A VALUE ")
                print()
                b=input("SELECT THE TASK YOU WANT TO DO : ").strip()
            if b.lower()=="search" or b.lower()=="search details" or b.lower()=="search_details" or int(b)==1:
                show()
            if b.lower()=="add" or b.lower()=="add data" or b.lower()=="add_details" or int(b)==2:
                print()
                try:
                    number=eval(input("ENTER NUMBER OF DATAS TO BE ENTERED : "))
                except NameError:
                    print("ENTER A NUMBER")
                    print()
                    number=eval(input("ENTER NUMBER OF DATAS TO BE ENTERED : "))
                for i in range(number):
                    print()
                    print()
                    insert()
                    print()
            if b.lower()=="update" or b.lower()=="update data" or int(b)==3:
                update()
                
            else:
                print()
                
            if int(b)==4:
                delete()
                
            print()
            print("========================================================================================")
            print("========================================================================================")
            print()
            print("1. YES")
            print("2. NO")
            print()
            s_ans=input("DO YOU WANT TO CONTINUE : ").strip()
            print()
            print("========================================================================================")
            print("========================================================================================")
            print()
            if s_ans.lower()=="yes" or int(s_ans)==1:
                ans=True
            elif s_ans.lower()=="no" or int(s_ans)==2:
                ans=False
                print()
                print("THANK YOU FOR USING HOTEL MANAGEMENT SYSTEM !! ")
                print("========================================================================================")
                print("========================================================================================")
                
    
        
    try:
        ini()
    except ValueError:
        print()
        print("OOPS!!")
        print("AN ERROR HAS OCCURED !!")
        print("PLEASE BE MORE CAREFUL WHILE TYPING")
        print()
        print("========================================================================================")
        print()
        print("1. YES")
        print("2. NO")
        print()
        j=input("DO YOU WANT TO CONTINUE : ").strip()
        if j.lower()=="yes" or j=="1":
            ini()
        if j.lower()=="no" or j=="2":
            print()
            print("THANK YOU FOR USING HOTEL MANAGEMENT SYSTEM !! ")
            print("========================================================================================")
            print("========================================================================================")

    except EOFError:
        print()
        print("1. YES")
        print("2. NO")
        print()
        j=input("DO YOU WANT TO CONTINUE : ").strip()
        if j.lower()=="yes" or int(j)==1:
            ini()
        if j.lower()=="no" or int(j)==2:
            print()
            print("THANK YOU FOR USING HOTEL MANAGEMENT SYSTEM !! ")
            print("========================================================================================")
            print("========================================================================================")


    except:
        print()
        print("OOPS!!")
        print("AN ERROR HAS OCCURED !!")
        print()
        print("========================================================================================")
        print()
        print("START AGAIN ? ")
        print()
        print("1. YES")
        print("2. NO")
        print()
        j=input("DO YOU WANT TO CONTINUE : ").strip()
        if j.lower()=="yes" or int(j)==1:
            ini()
        elif j.lower()=="no" or int(j)==2:
            print()
            print("THANK YOU FOR USING HOTEL MANAGEMENT SYSTEM !! ")
            print("========================================================================================")
            print("========================================================================================")
            











    
