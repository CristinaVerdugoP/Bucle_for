print("\n--------Basico-----------")
for i in range(0,151):
    print(i);

print("\n------Multiplos de 5------")  
for i in range(5,1005,5):
    print(i)

print("\n-----Contar, a la manera del Dojo------") 
for i in range(0,101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)

print("\n-----Whoa. Es un gran idiota-----")
suma = 0;
for i in range(500001):
    if(i%2!=0):
        suma += i

print("La suma final es:",suma)

print("\n------Cuenta regresiva de a 4-------")
x=2018;
while x>=0:
    print(x)
    x=x-4

print("\n---------Contador flexible-----------")
lowNum=10;
highNum=25;
mult=5;
for i in range(lowNum,highNum):
    if(i % mult == 0):
        print(i)







