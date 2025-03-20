import sys 
input = sys.stdin.readline

if __name__ == '__main__':
    N = input()             
    first = N
    a = ''
    
    if(N[1] != '\n'):
        a = int(N[0])+int(N[1])
        result = N[1] + str(a%10)
    else:
        a = N[0]
        result = N[0] + str(a)
        
    cnt = 1
    while(int(first)!=int(result)):
        cnt+=1

        a = int(result[0]) + int(result[1])
        if(a >= 10):
            result = result[1] + str(a)[1]
        else:    
            result = result[1] + str(a)[0]
        

    print(cnt)
        
