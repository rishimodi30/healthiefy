#shivam sada sahayte


from turtle import done


def wj_dfs(cur1,cur2,size1,size2,f):
    if f:
       return

    if target==cur1 | target==cur2:
       print(cur1,cur2)
       flag=True
       return
    visited.append((cur1,cur2))
   
    if (size1,cur2) not in visited:
        wj_dfs(size1,cur2,size1,size2,f)
    
    if (cur1,size2) not in visited:
        wj_dfs(cur1,size2,size1,size2,f)
    
    if (0,cur2) not in visited:
        wj_dfs(0,cur2,size1,size2,f)
    
    if (cur1,0) not in visited:
        wj_dfs(cur1,0,size1,size2,f)                
   
    vac2=min(size2-cur2,cur1)
    if (cur1-vac2,vac2) not in visited:
        wj_dfs(size1-vac2,vac2,size1,size2,f)

    vac1=min(size1-cur1,cur2)
    if (vac1,cur2-vac2) not in visited:
        wj_dfs(vac1,size2-vac1,size1,size2,f)
    
    return

    return


size1= int(input("enter the size of jug 1:"))
size2= int(input("enter the size of jug 2:"))

target=int(input("enter the target value:"))
flagv=False
visited=[(0,0)]

wj_dfs(0,0,size1,size2,flagv)







