# --------------------------------------------------> Question 1 (""" Thanos vs Tony Stark """) <--------------------------------------------------


t=int(input())
for i in range(t):
  l=list(map(str,input().split()))
  prog=list(l[1])
  max_dam=int(l[0])
  count=0
  
  def swap(i):
      global count
      swap = 0
      j=i-1
      while swap!=1:
          if prog[j] == 'S':
              swap = 0
              j=j-1
          prog[i],prog[j] = prog[j],prog[i]
          count += 1
          break

      return limit_exceed(prog)

  def limit_exceed(prog):
      global dam
      C_num = 1
      dam = 0
      for i in range(len(prog)):
          if prog[i]=='C':
              C_num=C_num*2
          elif prog[i]=='S':
              dam=dam+C_num
              if dam>max_dam:
                  dam = dam - C_num
                  swap(i)
      return dam
      

  limit_exceed(prog)
  if dam>max_dam:
      print("IMPOSSIBLE")
  else:
    print(count)

#--------------------------------------------------> Question 2 ( Giant Number )<--------------------------------------------------

def multiply(num1, num2):
    result = []
    remain = 0
    for index_num1, digit_num1 in enumerate(num1[::-1]):
        for index_num2, digit_num2 in enumerate(num2[::-1]):
          
            digitProduct = (ord(digit_num1) - ord('0')) * (ord(digit_num2) - ord('0')) + remain
            index_result = index_num1 + index_num2
            if not index_result < len(result):
                result.append(0)

            result[index_result] += digitProduct
            remain = result[index_result] // 10
            result[index_result] %= 10
        if remain:
            result.append(remain)
            remain = 0
    result_str = "".join(map(str,result[::-1])).lstrip("0")
    return result_str if result_str else "0"

num1,num2=map(str,input().split())
print(multiply(num1, num2))



# --------------------------------------------------> Question 3 (""" Remove Duplicates in linked list """) <--------------------------------------------------

class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_beg(self, data):
        if self.head == None:
            return self.head
        
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        
        return self.head

    def remove_dup(self):

        curr=self.head
        swap_node=self.head
        
        while curr:
            if curr.value==swap_node.value:
                curr=curr.next
            else:
                swap_node=swap_node.next
                temp=swap_node.value
                swap_node.value=curr.value
                curr.value=temp
                curr=curr.next
        swap_node.next=None

    def disp_list(self):
        temp = self.head
        while temp != None:
            print(temp.value,end=" ")
            temp = temp.next
        # print("None")

if __name__ == "__main__":
    
    lst_num=list(map(int,input().split()))
    cll = LinkedList()
    cll.head = Node(lst_num[-1])
    # lst = list(map(int, "1 2 3 4 4 4 7 7".split()))
    rev_lst=[]
    for i in range(len(lst_num)-1,-1,-1):
        rev_lst.append(lst_num[i])

    for i in range(len(lst_num)):
        cll.add_at_beg(rev_lst[i])

    cll.remove_dup()
    
    cll.disp_list()



#--------------------------------------------------> Question 4 ( College libarary in trouble )<--------------------------------------------------

A=list(map(int,input().split()))
N=len(A)
# print(A)
B=int(input())

def min_pages(A, N, B): 
    
    if N<B:
      return -1

    init_pages = 0
    max_page = sum(A)
    min_sum_pages = pow(10,5)

    while (init_pages <= max_page):

        mid = (init_pages + max_page)//2
        # mid = (max_page)//2
        curr_min=mid
        if (min_valid(A, N, B, curr_min)): 

            min_sum_pages = min(min_sum_pages, mid) 
            max_page = mid - 1

        else: 
            init_pages = mid + 1

    return min_sum_pages
    

def min_valid(A, N, B, curr_min): 
    total_students = 1
    curr_sum = 0
    for i in range(N): 
      if (A[i] > curr_min): 
        return False
      if (curr_sum + A[i] > curr_min): 
        total_students += 1
        curr_sum = A[i] 
        if (total_students > B): 
          return False
      else: 
        curr_sum += A[i] 
    return True

print(min_pages(A, N, B))



#--------------------------------------------------> Question 5 ( """ World war 3 """ )<--------------------------------------------------


def max_area_histogram(histogram): 
    stack = list() 
  
    max_area = 0
    index = 0
    while index < len(histogram): 
        if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
            stack.append(index) 
            index += 1
        else: 
            top_of_stack = stack.pop() 
            area = (histogram[top_of_stack] * 
                   ((index - stack[-1] - 1)  
                   if stack else index)) 
  
            max_area = max(max_area, area) 
    while stack: 
        top_of_stack = stack.pop() 
        area = (histogram[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
  
        max_area = max(max_area, area) 
    return max_area*600

lst=list(map(int,input().split()))
print(max_area_histogram(lst))

#--------------------------------------------------> Question 6 ( """ All the builts in """ )<--------------------------------------------------

type_input=input()
if type_input=="string":
  st=input()
  for i in range(5):
      oper_inp=input()
      if oper_inp=="all caps":
        s=st
        print(s.upper())
      elif oper_inp=="reverse":
        s=st
        s=s[::-1]
        print(s)
      elif oper_inp=="sort":
        s=st
        sorted_list = sorted(s, key=str.casefold)
        print("".join(sorted_list))
      elif oper_inp=="isdigit":
        s=st
        print(s.isdigit())
      else:
        oper_inp=list(oper_inp)
        s=st
        print(s.find(oper_inp[-1]))
elif type_input=="list":
  lst=list(map(int,input().split(' ')))
  for i in range(5):
    oper_inp=input().split(' ')
    if oper_inp[0]=="append":
      l=lst
      # l.append(10)
      print(l)
    elif oper_inp[0]=="reverse":
      l=lst
      l=l[::-1]
      print(l)
    elif oper_inp[0]=="sort":
      l=lst
      l.sort()
      print(l)
    elif oper_inp[0]=="separate":
      l = lst
      result=[]
      for i in range(len(l)):
        result.append(l[i])
        if i!=len(l)-1:
          result.append(oper_inp[2])
      print(result)
    else:
      # oper_inp=list(oper_inp[1].split(','))
      l = lst
      # print(oper_inp)
      # print(oper_inp[2],oper_inp[1])
      # print(int(oper_inp[2].strip()),int(oper_inp[1].strip()))
      l.insert(int(oper_inp[2]),int(oper_inp[1]))
      print(l)

