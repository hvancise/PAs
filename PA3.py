import numpy as np

#Part 1
poly1 = np.poly1d([2,3,0,1])
result1 = np.polyval(poly1, 2)
print(f"The result of the value x=2 on the polynomial\n {poly1} is {result1}")

poly2 = np.poly1d([1, 0, 1])
deriv2 = np.polyder(poly2)
result2 = np.polyval(deriv2, 1)
print(f"The result of the value x=1 on the derivative of the polynomial \n{poly2} is {result2}\n")

#Part 2
def newton(x, poly, counter):
    val1 = np.polyval(poly, x)
    der2 = np.polyder(poly)
    derval2 = np.polyval(der2, x)
    result = round(x - val1 / derval2, 3)
    print(f"x_{counter}: {result}")
    if result == x:
        return "The final value with stabilized thousandths place is: " + str(result)
    counter += 1
    newton(result, poly, counter)

def main():
    num_list = []
    num = 0
    while num != "":
       num = input("Please input the next coefficient of your polynomial. Press enter if you are done inputting numbers." ) 
       if num == "":
           break
       else:
           num_list.append(float(num))
    poly = np.poly1d(num_list)
    val = float(input("\nPlease input the value you would like inputted into the derivative. "))
    newton(val, poly, 0)
    print(f"\nThe roots of the given polynomial are {np.roots(poly)}")
    
main()
       