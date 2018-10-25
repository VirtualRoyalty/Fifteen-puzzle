
# coding: utf-8

# In[3]:


import numpy as np
import sys

x_len=y_len=3

board = np.zeros((x_len,y_len)) 
sample_board=np.zeros((x_len,y_len))
val=[ x for x in range(1,x_len*y_len)]
itr=0
for i in range(len(board)):
    for j in range(len(board)):
        sample_board[i][j]=val[itr]
        itr=itr+1
        if (itr==(x_len*y_len)-1):
            break
val=[ x for x in range(x_len*y_len)]
np.random.shuffle(val)
itr=0
for i in range(len(board)):
    for j in range(len(board)):
        board[i][j]=val[itr]
        itr=itr+1
        if (itr==(x_len*y_len)):
            break
print(sample_board)
print("  ")

board=copy.copy(sample_board)
mov=     ['d','u','r','l']
for x in range(50):
    i=np.random.randint(0,4)
    if(movepossbl(board,mov[i])):
        board=move_to(board,mov[i])
    else:
        continue
        
#print(board)
#board[0][0]=1
#board[0][1]=3
#board[0][2]=6
#board[1][0]=5
#board[1][1]=7
#board[1][2]=2
#board[2][0]=4
#board[2][1]=8
#board[2][2]=0
print(board)

def Astar(sample_board_,board_):#алгоритм А*
    mov=     ['d','u','r','l']
    stop_mov=['u','d','l','r']
    V=copy.copy(board_)
    path=[]
    open_=[[manhet_dist(sample_board_,V),'Path is: ',V]]
    close_=[]
    last_mov=''
    if(solutionPosible_notzero(board_)!=True):
        print("there is no solution")
        return
    while (len(open_)>0): 
        #print(len(open_))
        min_ = -1
        for j in range(len(open_)):
            if open_[min_][0] >= open_[j][0]:
                min_ = j
        last_mov=open_[min_][1]
        V=copy.copy(open_[min_][-1])        
        path.append([inversmov(last_mov),V])
        open_ = open_[:min_] + open_[min_ + 1:]
        if(manhet_dist(sample_board_,V)==0):
            print(path)
            for x in close_: print(x)
            return
        if(isthere(close_,V)==True):
            continue
        listofmovs=movsOF(V,last_mov)
        close_.append(V)
        for v in listofmovs:
            if(isthere(close_,v[-1])==False):
                if(manhet_dist(sample_board_,v[-1])==0):
                    path.append([inversmov(v[0]),v[-1]])
                    print("WE DID IT!in just",len(close_),"moves")
                    for x in path: print(x[0],end='')
                    print('\n')
                    for x in path: print(x[-1])
                    return
                open_.append([manhet_dist(sample_board_,v[-1]),v[0],v[-1]])
                
       
            else:
                continue
        
        
    print('Open_ is empty!!!:(',closed_boards)         
    return False
                        
       

     
    
    
    
Astar(sample_board,board)


# In[2]:




import collections
import copy


def swap(board_,i,j): #меняет два элемента местами
    ix,iy=find_elem(board_,i)
    jx,jy=find_elem(board_,j)
    board_[ix][iy]=j
    board_[jx][jy]=i
    return
    
    
    
def distance(sample_board_,board_): #расстояние от текущей состояния доски до терминальной(число элементов не на своих местах)
    diff=0
    for i in range(len(board_)):
         for j in range(len(board_)):
            if(board_[i][j]!=0):
                if (sample_board_[i][j]!=board_[i][j]):
                    diff=diff+1
    return diff

def manhet_dist(sample_board_,board_): #манхетоновское расстояние
    diff_=0
    for i in range(len(board_)):
         for j in range(len(board_)):
                x0,y0=find_elem(sample_board_,board_[i][j])
                diff_=diff_+(abs(i-x0)+abs(j-y0))
    
    return diff_

def find_elem(board_,elem_):  #ищет данный элемент и возвращает координаты
    for x in range(len(board_)):
        for y in  range(len(board_)):
            if board_[x][y]==elem_:
                elem_x=x
                elem_y=y
                break
    return elem_x,elem_y


    
def solutionPosible_notzero(board_):#проверка по критерию собираемости
    zerx,zery=find_elem(board_,0)
    zerx=zerx+1
    sum=0
    line=board_list(board_)
    for x in range(len(line)):
        if(line[x]!=0):
            for y in range(x+1,len(line)):
                if(line[y]!=0):
                    if line[x]>line[y]:
                        sum=sum+1
            sum=sum+zerx
    
            
    #print(sum)
    if((sum) % 2==0):
        return True
    else:
        return False

def board_list(board_): #интерпретирует доску как список
    string=[]
    for i in range(len(board_)):
        for j in  range(len(board_)):
            string.append(board_[i][j])
    return string

def movepossbl(board_,where): #проверяет возможен ли данный ход
    zery,zerx=find_elem(board_,0)
    if(zerx==len(board_)-1)&(where=='r'):
        return False
    if(zerx==0)&(where=='l'):
        return False
    if(zery==len(board_)-1)&(where=='d'):
        return False
    if(zery==0)&(where=='u'):
        return False
    return True


def isthere(lst,crumb):#проверяет принадлежность вершины(данной доски) к списку
    for x in lst:
        if(manhet_dist(crumb,x)==0):
            return True
        else:
            return False
    
def movsOF(board_,last_mov):#создает массив возвожных ходов
    mov=['d','u','r','l']
    stop_mov=['u','d','l','r']
    moveslst=[]
    for i in [0,1,2,3]:
        if(movepossbl(board_,mov[i])):
            if(mov[i]!=last_mov):
                moveslst.append([stop_mov[i],move_to(board_,mov[i])])
    return moveslst       


  
    
def move_to(l,where):#двигаем ноль вверх или вниз или влево или вправо
    board_=copy.copy(l)
    zerox,zeroy=find_elem(board_,0)
    movex=[1,-1,0,0]
    movey=[0,0,1,-1]
    board_=copy.copy(l)
    if (zerox!=0)&(where == 'u'):
        swap(board_,0,board_[zerox+movex[1],zeroy+movey[1]])
        #print('U')
        return board_
    if (zerox!=len(board_)-1)&(where == 'd'):
        swap(board_,0,board_[zerox+movex[0],zeroy+movey[0]])
       # print('D')
        return board_
    if (zeroy!=0)&(where == 'l'):
        swap(board_,0,board_[zerox+movex[3],zeroy+movey[3]])
      #  print('L')
        return board_
    if (zeroy!=len(board_)-1)&(where == 'r'):
        swap(board_,0,board_[zerox+movex[2],zeroy+movey[2]])
       # print('R')
        return board_
    print('imposible move')
    return []

def inversmov(mov_): #"переворачивает" ход
    if(mov_=='u'):
        return 'd'
    if(mov_=='d'):
        return 'u'
    if(mov_=='l'):
        return 'r'
    if(mov_=='r'):
        return 'l'
    return mov_


