def Count_Ways_torun(a) :
    val = [0] * (a + 2)
    val[0] = 1
    val[1] = 1
    val[2] = 2
     
    for i in range(3, a + 1) :
        val[i] = val[i - 1] + val[i - 2] + val[i - 3]
     
    return val[a]
 
# Driver code
num_of_stairs= int(input("Enter the number of stairs that john has to run:   "))
print('Possible ways Johan can run up the %d stairs is '%(num_of_stairs))
print(Count_Ways_torun(num_of_stairs))
