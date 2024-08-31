# Your code below:

toppings=["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
print(toppings)

prices=[2,6,1,3,2,7,2]

num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)

num_pizzas=len(toppings)
print("We sell",num_pizzas,"different kinds of pizza!")

pizza_prices=[[2,"pepperoni"],[2,"pineapple"],[1,"cheese"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]
pizza_prices.sort()
print(pizza_prices)

cheapest_pizza=pizza_prices[0]
print(cheapest_pizza)

priciest_pizza=pizza_prices[-1]
print(priciest_pizza)

pizza_prices.pop()
print(pizza_prices)

pizza_prices.insert(5,[2.5,"peppers"])
print(pizza_prices)

three_cheapest=pizza_prices[:3]
print(three_cheapest)




