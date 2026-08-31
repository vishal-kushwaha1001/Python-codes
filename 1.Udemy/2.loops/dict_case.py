users = [
    {"id": 1 , "total": 100, "coupon" : "P20"},
    {"id": 2 , "total": 150, "coupon" : "F10"},
    {"id": 3 , "total": 80, "coupon" : "P50"}
    
]

discounts = {
    "P20" : (0.2 , 0),
    "F10" : (0.5 , 0),
    "P50" : (0 , 10)
}

for user in users:
    percent , fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(f"{user['id']} paid {user['total'] } and got discount for next visit of rupees {discount}")
    
   
   
# percent, fixed = discounts.get(user["coupon"], (0, 0))
    
#     user["coupon"]
#       ↓
# coupon nikala

# discounts.get(...)
#       ↓
# coupon ki discount information nikali

# percent, fixed = ...
#       ↓
# tuple ko do variables mein unpack kiya

#   Pura program ek flow mein
# users
#   ↓
# for loop
#   ↓
# First user
#   ↓
# coupon = P20
#   ↓
# discounts dictionary mein P20 search
#   ↓
# (0.2, 0)
#   ↓
# percent = 0.2
# fixed = 0
#   ↓
# 100 × 0.2 + 0
#   ↓
# discount = 20
#   ↓
# print result