def cal_AP(n):  
    a,d = 1,1
    Sum = 0.0
    for i in range(1,n+1):
        n_term = 1/(a+(i-1)*d) 
        Sum += n_term
    return Sum


number = int(input("Please enter the Nth term: "))
Ans = cal_AP(number)
print(f"Sum is: {Ans}")