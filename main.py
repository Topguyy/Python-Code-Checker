def main() :
 global a #User's input test code
 UserInput = input("Please Enter The Code You want to test!!! \n")
 a = UserInput.split()
 print(a)

#Method to test if the code has a division by 0 or not
def test_ZeroDiv(ZeroDiv='/0'):
 for i in range(0,len(a)):
  if a[i]==ZeroDiv :
   print(a[i-1]+a[i]+' Logical error found,Division by 0 is forbidden!!!')
   #break
 if ZeroDiv not in a :
   print('Test ran Successfully no division by 0 found according to the company coding style!!!')

#Method to test if the functions and conditions have syntax errors or not
def test_Conditions() :
 key=['for','if','def','while','elif','else']
 keywords=['print','return']
 closing=':'
 stack =[]
 for i in range(0,len(a)):
  if a[i] == 'def' :
   stack.append(a[i])
   for j in range (i+1,len(a)) :
    if a[j]==closing :
     stack.append(a[j])
     print(stack)
     print('Test Passed ,Function Syntax is Correct!!!')
     break
    elif a[j] in key and len(stack)!=0:
     print(stack)
     print('Test Failed ,Function Syntax Error!!!')
     break
    elif a[j] in keywords :
     print(stack)
     print('Test Failed ,Function Syntax Error!!!')
     break
    elif j==len(a)-1 :
     print(stack)
     print('Test Failed ,Function Syntax Error!!!')
     break
 for i in range(0,len(a)):
  if a[i] == 'for' :
   stack.append(a[i])
   for j in range (i+1,len(a)) :
    if a[j]==closing :
     stack.append(a[j])
     print(stack)
     print('Test Passed ,For Loop Syntax is Correct!!!')
     break
    elif a[j] in key and len(stack)!=0:
     print(stack)
     print('Test Failed ,For Loop Syntax Error!!!')
     break
    elif a[j] in keywords :
     print(stack)
     print('Test Failed ,For Loop Syntax Error!!!')
     break
    elif j==len(a)-1 :
     print(stack)
     print('Test Failed ,For Loop Syntax Error!!!')
     break
 for i in range(0,len(a)):
  if a[i] == 'while' :
   stack.append(a[i])
   for j in range (i+1,len(a)) :
    if a[j]==closing :
     stack.append(a[j])
     print(stack)
     print('Test Passed ,While Loop Syntax is Correct!!!')
     break
    elif a[j] in key and len(stack)!=0:
     print(stack)
     print('Test Failed ,While Loop Syntax Error!!!')
     break
    elif a[j] in keywords :
     print(stack)
     print('Test Failed ,While Loop Syntax Error!!!')
     break
    elif j==len(a)-1 :
     print(stack)
     print('Test Failed ,While Loop Syntax Error!!!')
     break
 for i in range(0,len(a)):
  if a[i] == 'if' :
   stack.append(a[i])
   for j in range (i+1,len(a)) :
    if a[j]==closing :
     stack.append(a[j])
     print(stack)
     print('Test Passed ,IF Condition Syntax is Correct!!!')
     break
    elif a[j] in key and len(stack)!=0:
     print(stack)
     print('Test Failed ,IF Condition Syntax Error!!!')
     break
    elif a[j] in keywords :
     print(stack)
     print('Test Failed ,IF Condition Syntax Error!!!')
     break
    elif j==len(a)-1 :
     print(stack)
     print('Test Failed ,IF Condition Loop Syntax Error!!!')
     break
 for i in range(0,len(a)):
  if a[i] == 'elif' :
   stack.append(a[i])
   for j in range (i+1,len(a)) :
    if a[j]==closing :
     stack.append(a[j])
     print(stack)
     print('Test Passed ,elif Condition Syntax is Correct!!!')
     break
    elif a[j] in key and len(stack)!=0:
     print(stack)
     print('Test Failed ,elif Condition Syntax Error!!!')
     break
    elif a[j] in keywords :
     print(stack)
     print('Test Failed ,elif Condition Syntax Error!!!')
     break
    elif j==len(a)-1 :
     print(stack)
     print('Test Failed ,elif Condition Loop Syntax Error!!!')
     break
 for i in range(0,len(a)):
  if a[i] == 'else' :
   stack.append(a[i])
   for j in range (i+1,len(a)) :
    if a[j]==closing :
     stack.append(a[j])
     print(stack)
     print('Test Passed ,else Condition Syntax is Correct!!!')
     break
    elif a[j] in key and len(stack)!=0:
     print(stack)
     print('Test Failed ,else Condition Syntax Error!!!')
     break
    elif a[j] in keywords :
     print(stack)
     print('Test Failed ,else Condition Syntax Error!!!')
     break
    elif j==len(a)-1 :
     print(stack)
     print('Test Failed ,else Condition Loop Syntax Error!!!')
     break

#Method to test if any Python Reserved Keyword is declared as a variable
def test_ReservedKeywords() :
 rstack=[]
 rKeywords=['print','False','def','if','raise','None','del','import','return','True','elif','in','try','and','else','is','is','while','as','except','lambda','with','assert','finally','non local','yield','break','for','not','class','from','or','continue','global','pass']
 for i in range(0,len(a))  :
  if a[i] == '=' :
   if a[i-1] in rKeywords :
    rstack.append(a[i-1])
    print(rstack)
    print('Error : reserved keyword : "'+str(a[i-1])+'" Can Not be declared as a variable!!!')
  elif i == len(a)-1 and len(rstack)==0 :
   print('Reserved Keyword Test Is Passed Successfully!!!!!!')
  elif i==len(a)-1 and len(rstack)!=0 :
   print('Reserved Keyword Test Failed!!!!!!')

#Method to test if there's unUsed Variables using def_use Method
def test_unUsedVariables() :
 defStack=[] #stack containing all defined variables in the program
 usedStack = [] #stack containing all used variables in the program
 unUsedStack=[] #stack containing all unused variables in the program
 for i in range (0,len(a)) :
  if a[i] == '=' :
   defStack.append(a[i-1])
   for j in range(i+1,len(a)) :
    if a[j] == a[i-1] and a[j] in usedStack :
     break
    if a[j] == a[i-1] or (a[j].find(a[i-1]) ) :
     usedStack.append(a[j])
    # print(usedStack)
     #print('Variable "'+str(a[j])+'" is used')
 #print(defStack)
 for x in range(0,len(defStack)) :
  if defStack[x] not in usedStack :
   unUsedStack.append(defStack[x])
   print(unUsedStack)
   print('Variable "'+str(defStack[x])+'" is declared but not used')
   #print(defStack)
   #print(usedStack)

#Method to test if there's a method which is duplicated
def test_MethodDuplication() :
 key = 'def'
 closing = ':'
 function = ''
 stack = []
 unStack=set(stack)
 for i in range(0, len(a)):
  if a[i] == key:
   for j in range (i,len(a)) :
    function +=a[j]
    #print(function)
    if a[j] == closing:
     stack.append(function)
     unStack.add(function)
     function = ''
     break
 print(stack)
 print(unStack)
 if len(unStack) == len(stack) :
  print('Method Duplication Test Passed Successfully!!!!')
 elif len(unStack) != len(stack):
  print('Error!!!!There is a duplicatted Method,Please try Overloading that Method')

#Method to test out of scope variables
def test_OutVariables() :
 Functionstr=[]
 FunctionVariables=[]
 ooSvariables=[]
 Functionstr3=[]
 for i in range(0, len(a)):
  if a[i] == 'def':
   for j in range(i + 1, len(a)):
    Functionstr.append(a[j])
    if a[j] == 'def':
     Functionstr.pop()
     break
   break
 for x in range(0, len(Functionstr)):
  if Functionstr[x] == '=':
   FunctionVariables.append(str(Functionstr[x - 1]))
   # print(FunctionVariables)
 for x in range(j + 1, len(a)):
  y = x + 1
  if a[x] in FunctionVariables and y != '=':
   ooSvariables.append(a[x])
   print(ooSvariables)
   print('Error Variable " '+a[x]+' " has no reference!!!!')
 #print(Functionstr)
 #print(FunctionVariables)
 #print((ooSvariables))





main()
test_Conditions()
test_ZeroDiv()
test_ReservedKeywords()
test_unUsedVariables()
test_MethodDuplication()
test_OutVariables()
