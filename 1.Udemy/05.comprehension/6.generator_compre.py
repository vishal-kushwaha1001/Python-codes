sales_per_day = [200,300,100,400,500,900]

# want sum of all sales which is <= 400

result =sum( sales for sales in sales_per_day if sales <= 400)
print(result)

# find maximum sales which is less than 500

max_sales = max(sales for sales in sales_per_day if sales < 500  )
print(max_sales)