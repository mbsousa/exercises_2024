
while True:
    name = input("Name: ")
    age = input("Age: ")
    salary = input("Salary: ")
    gender = input("M or F: ").upper()
    civil_status = input("Please. Enter just the letter:\nS(Single)-M(Married)-W(Widower)-D(Divorced)\n- ").upper()
    try:
        age = int(age)
        salary = float(salary)
        gender = str(gender)
        if len(name) < 3:
            print("Please. Put your name correctly.")
            continue
        elif age < 0 or age > 150:
            print("Please. Put your age correctly.")
            continue
        elif salary < 0:
            print("Please. Put your salary correctly. If you not receiving any money. Answer 0.")
            continue
        elif gender not in ['M','F']:
            print("Please. Answer correctly. M-Male or F-Female.")
            continue
        elif civil_status not in ['S','M','W','D']:
            print("Please. Answer correctly.")
            continue
        else:
            print("Successfully registered.")
            break
    except ValueError:
        print("Something is wrong. Please check your answers.")
        continue


