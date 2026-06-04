#type 1 pyramid pattern(in which number of stars in eachrow = 2*row-1)
n = int(input ("enter the number of lines of your inverted pyramid "))
d=[]
s=" "
q=n//2
m=(2*n)-1
for y in range(0,m):

  d.append("*")

print(*d)
w=0
while w<=n-2:

  print(s*(w+1),*d[(w+1):(m-w-1) ])
  w=w+1

#type 2 pyramid pattern(in which number of stars in each row = row)
n = int(input ("enter the number of lines of your inverted pyramid "))
d=[]
s=" "
m=n
for y in range(0,m):

  d.append("*")

w=0
while w<=n:

  print(s*(w+1),*d[(w):(m)])
  w=w+1




#Short code for Star Pyramids

n = 9
j = 0
for i in range (1,n):
    stars = i + j
    spaces = n -  1 - i
    print(spaces *" " + stars * "*")
    j +=1


print("\n\n\n\n")

l = 0
k = n
for i in range (0 , n ):
    stars = 2*k - 1
    spaces = l
    print(spaces * " " + stars * "*")
    l+=1
    k -=1
