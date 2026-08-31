device_status = input("inter device status of your device : ").strip().lower()

if device_status == "active":
    temp = int(input("inter device temperature :"))
    if temp > 35 :
        print("warm : 'High temperature' ")
    else :
        print("Normal temperature")    
else :
    print("device is offline".upper()) 