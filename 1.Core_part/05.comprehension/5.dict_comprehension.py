tea_prices_INR = {
    "masala chai" : 50,
    "green tea" : 100,
    "lemon tea" : 30,
    "Spicy chai" : 200
}

# convert prices INR into Doller

tea_prices_Dollar = { chai:round(price /95 ,2)for chai , price in tea_prices_INR.items()}
print("tea prices in Doller :", tea_prices_Dollar)