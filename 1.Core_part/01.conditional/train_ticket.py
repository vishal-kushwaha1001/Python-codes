seat_type = input("Enter your preffered seat type (sleeper / AC / general / luxary) : ").strip().lower()

match seat_type :
    case "sleeper":
        print("only bed")
    case "ac" :
        print("very comfatable seat with ac and no disturbance and average security".upper())
    case "luxary" :
        print("very comfatable seat with ac and no disturbance and high security , personal caben , food available".upper())
    case "general" :
        print("very croweded , onlt sit".upper())
    case _:
        print("invalid seat type".upper())
        