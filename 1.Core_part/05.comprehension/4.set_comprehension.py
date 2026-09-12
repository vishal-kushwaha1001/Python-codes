recipes = {
    "Masala chai" : ["ginger", "cardamom" , "clove"],
    "Elaichi chai" : ["cardamom", "milk" ],
    "Spicy chai" : ["ginger", "black paper" , "clove"]
}

# find the all unique ingredients

unique_ingredients = { u_i for ingredients in recipes.values()
                      for u_i in ingredients}
print(unique_ingredients)