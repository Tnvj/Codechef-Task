import mysql.connector as mycon
cn = mycon.connect(host='127.0.0.1',user='root',password="user",database="company")
cur = cn.cursor()
def showAll():
    
    global cn
    global cur
    
    try:
        query="select * from emp"
        cur.execute(query)
        results = cur.fetchall()
        print("**************************************************")
        print('%5s'%"EMPNO",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY')
        print("**************************************************")
        count=0
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
            count+=1
        print("*************** TOTAL RECORD : ",count,"**********")
    except:
        print("error")
def addEmp():
    global cn,cur
    print("*******************ADD NEW EMPLOYEE**************************")
    eno = int(input("Enter employee number :"))
    en = input("Enter employee name :")
    dp = input("Enter department ")
    sl = int(input("Enter Salary :"))
    query="insert into emp values("+str(eno)+",'"+en+"','"+dp+"',"+str(sl)+")"
    cur.execute(query)
    cn.commit()
    print("\n ## RECORD ADDED SUCCESSFULLY!")
def searchEmp():
    global cn,cur
    print("*******************SEARCH EMPLOYEE FORM **************************")
    en = int(input("Enter Employee number to search :"))
    query="select * from emp where empno="+str(en)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
       
        print("**************************************************")
        print('%5s'%"EMPNO",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY')
        print("**************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
    print("-"*50)
def editEmp():
    global cn,cur
    print("*******************EDIT EMPLOYEE FORM **************************")
    en = int(input("Enter Employee number to edit :"))
    query="select * from emp where empno="+str(en)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
       
        print("**************************************************")
        print('%5s'%"EMPNO",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY')
        print("**************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
    print("-"*50)
    ans = input("Are you sure to update ? (y/n)")
    if ans=="y" or ans=="Y":
        d = input("Enter new department to update (enter old value if not to update) :")
        s = int(input("Enter new salary to update (enter old value if not to update) :"))
        query="update emp set dept='"+d+"',salary="+str(s) + " where empno="+str(en)
        cur.execute(query)
        cn.commit()
        print("\n## RECORD UPDATED  ##")
                
def delEmp():
    global cn,cur
    print("*******************DELETE EMPLOYEE FORM **************************")
    en = int(input("Enter Employee number to delete :"))
    query="select * from emp where empno="+str(en)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
       
        print("**************************************************")
        print('%5s'%"EMPNO",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY')
        print("**************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
    print("-"*50)
    ans = input("Are you sure to delete ? (y/n)")
    if ans=="y" or ans=="Y":
        query="delete from emp where empno="+str(en)
        cur.execute(query)
        cn.commit()
        print("\n## RECORD DELETED  ##")
def clear():
      for i in range(1,50):
          print()
          
def generateSlip():

    global cn,cur
    print("*******************SALARY SLIP **************************")
    en = int(input("Enter Employee number to print salary slip :"))
    query="select * from emp where empno="+str(en)
    cur.execute(query)
    results = cur.fetchone()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
        print("\n")
        #clear()
        print("EMPNO :",results[0]," "*20,"NAME :",results[1])
        print("DEPARTMENT :",results[2])
        print("*"*50)
        s = int(results[3])
        hra = s * 12/100
        da = s * 15/100
        it = s * 0.05
      
        gross = s +hra+da
      
        net = gross - it
        tded=it 
        print("%19s"%"EARNING","%27s"%"DEDUCTION")
        print("-------------------------------------------------")
        print("%20s"%"Basic  :"+str(s),"%22s"%"INC. TAX :"+str(it))
        print("%20s"%"HRA    :"+str(hra))
        print("%20s"%"DA     :"+str(da))
      
        print("-"*50)
        print("     GROSS :",gross," NET SALARY :",net,"  TOTAL DED :",tded)
    print("-"*50)
    print("=== PRESS ANY KEY ===")
    input()
        
while True:
    print("1. SHOW EMPLOYEE LIST ")
    print("2. ADD NEW EMPLOYEE")
    print("3. SEARCH EMPLOYEE ")
    print("4. EDIT EMPLOYEE ")
    print("5. DELETE EMPLOYEE ")
    print("6. GENERATE PAY SLIP ")
    print("0. EXIT")
    ans = int(input("Enter your choice :"))
    if ans==1:
        showAll()
    elif ans==2:
        addEmp()
    elif ans==3:
        searchEmp()
    elif ans==4:
        editEmp()
    elif ans==5:
        delEmp()
    elif ans==6:
        generateSlip()
    elif ans==0:
        print("\nBye!!")
        cn.close()
        break
