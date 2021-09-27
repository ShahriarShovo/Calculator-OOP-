
class Basic_Calculator():

    def __init__(self,first_number,second_number) -> None:
        self.first_number=float(first_number)
        self.second_number=float(second_number)

    def addition(self):
        self.result=self.first_number+self.second_number
        return self.result

    def subtraction(self):
        self.result=self.first_number-self.second_number
        return self.result

    def multiplication(self):
        self.result=self.first_number*self.second_number
        return self.result
    
    def division(self):
        self.result=self.first_number/self.second_number
        return self.result

    
    def display_show(self):
        print("----------------------------")
        print("                         ",float(self.result))


class Matrix_Calculator():

    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.matrix=[]
       
    
    def creat_matrix(self):
        for i in range(self.row):
            temp=[]
            for j in range(self.col):
                ele=int(input("Enter the Elements : "))
                temp.append(ele)
            self.matrix.append(temp)

    def show_matrix_display(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.matrix[i][j],end=' ')
            print()

    def add_matrix(self,other_matrix):
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j]=self.matrix[i][j]+other_matrix.matrix[i][j]

    def sub_matrix(self,other_matrix):
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j]=self.matrix[i][j]-other_matrix.matrix[i][j]

    def mul_matrix(self,other_matrix):
        tempMatrix=[]
        for i in range(self.row):
            temp=[]
            for j in range(self.col):
                self.dot=0
                for k in range(self.col):
                    self.dot=self.dot+self.matrix[i][k]*other_matrix.matrix[k][j]
                temp.append(self.dot)
            tempMatrix.append(temp)
        self.matrix=tempMatrix
        
            

class Binary():

    def __init__(self) -> None:
        self.store_binary=[]
        
        
    def convertToBinary(self,decimal):

        for i in range(decimal):
            self.store_binary.append(decimal%2)
            decimal=decimal//2
            i=i+1
        return self.store_binary

    def convertToDecimal(self,binary):
        self.total=0
        for i in range(binary):
            remainder=binary%10
            self.total=self.total+remainder*pow(2,i)
            binary=binary//10
            i=i+1
        return self.total
        
    def addBinary(self,a,b):
        f=self.convertToDecimal(a)
        s=self.convertToDecimal(b)

        result=f+s
        f_re=self.convertToBinary(result)

    def subBinary(self,a,b):
        f=self.convertToDecimal(a)
        s=self.convertToDecimal(b)

        result=f-s
        f_re=self.convertToBinary(result)

    def mulBinary(self,a,b):
        f=self.convertToDecimal(a)
        s=self.convertToDecimal(b)

        result=f*s
        f_re=self.convertToBinary(result)

 
    def showBinary(self):
        for i in range(len(self.store_binary)-1,-1,-1):
            print(self.store_binary[i],end=' ')

    def showDecimal(self):
        print(self.total)

    


#Display main function------------------------------------

def main_menue():
    print("            1.Basic Calculator")
    print("            2.Matrix Calculator")
    print("            3.Binary Calculator")

def basic_calculator_menue():
    print("            1.Addition")
    print("            2.subtraction")
    print("            3.Multiplication")
    print("            4.Division")
    
    
def matrix_calculator():
    print("            1.Matrix Addition")
    print("            2.Matrix Subtraction")
    print("            3.Matrix Multiplication")


def binary_calculator():
    print("            1.Convert Decimal to Binary ")
    print("            2.Binary to Decimal ")
    print("            3.Binary Addition")
    print("            4.Binary Subtraction")
    print("            5.Binary Multiplication")
    

#Start from here 
if __name__=="__main__":

    main_menue()

    select_option=int(input("Enter the number 1-3: "))

    if select_option==1:
        basic_calculator_menue()

        select_option=int(input("Which Operation do you want ? : "))

        if select_option==1:
            while True:
                first_number=str(input("Enter the First Number : "))
                Second_number=str(input("Enter the Second Number : "))
                add=Basic_Calculator(first_number,Second_number)
                add.addition()
                add.display_show()
        if select_option==2:
            while True:
                first_number=str(input("Enter the First Number : "))
                Second_number=str(input("Enter the Second Number : "))
                sub=Basic_Calculator(first_number,Second_number)
                sub.subtraction()
                sub.display_show()
        
        if select_option==3:
            while True:
                first_number=str(input("Enter the First Number : "))
                Second_number=str(input("Enter the Second Number : "))
                mul=Basic_Calculator(first_number,Second_number)
                mul.multiplication()
                mul.display_show()
        
        if select_option==4:
            while True:
                first_number=str(input("Enter the First Number : "))
                Second_number=str(input("Enter the Second Number : "))
                div=Basic_Calculator(first_number,Second_number)
                div.division()
                div.display_show()
        

    if select_option==2:
        matrix_calculator()
        select_option=int(input("Which Operation do you want ?1-3 : "))
        if select_option==1:
            while True:
                row=int(input("Enter the Row : "))
                column=int(input("Enter the Column : "))
                firstMatrix=Matrix_Calculator(row,column)
                firstMatrix.creat_matrix()
                firstMatrix.show_matrix_display()
                secondMatrix=Matrix_Calculator(row,column)
                secondMatrix.creat_matrix()
                secondMatrix.show_matrix_display()
                print()
                firstMatrix.add_matrix(secondMatrix)
                print("----------")
                firstMatrix.show_matrix_display()

        if select_option==2:
            while True:
                row=int(input("Enter the Row : "))
                column=int(input("Enter the Column : "))
                firstMatrix=Matrix_Calculator(row,column)
                firstMatrix.creat_matrix()
                firstMatrix.show_matrix_display()
                secondMatrix=Matrix_Calculator(row,column)
                secondMatrix.creat_matrix()
                secondMatrix.show_matrix_display()
                print()
                firstMatrix.sub_matrix(secondMatrix)
                print("----------")
                firstMatrix.show_matrix_display()

        if select_option==3:
            while True:
                first_m_row=int(input("Enter the Row : "))
                first_m_column=int(input("Enter the Column : "))
                second_m_row=int(input("Enter the Row : "))
                second_m_column=int(input("Enter the Column : "))

                while first_m_column!=second_m_row:
                    print("Sorry Matrix Multipcation can be done because of row and coloum is not same")
                    first_m_row=int(input("Enter the Row : "))
                    first_m_column=int(input("Enter the Column : "))
                    second_m_row=int(input("Enter the Row : "))
                    second_m_column=int(input("Enter the Column : "))

            
                firstMatrix=Matrix_Calculator(first_m_row,first_m_column)
                firstMatrix.creat_matrix()
                firstMatrix.show_matrix_display()
                secondMatrix=Matrix_Calculator(second_m_row,second_m_column)
                secondMatrix.creat_matrix()
                secondMatrix.show_matrix_display()
                print()
                firstMatrix.mul_matrix(secondMatrix)
                print("----------")
                firstMatrix.show_matrix_display()


    if select_option==3:
        binary_calculator()
        select_option=int(input("Which Operation do you want ?1-3 : "))
        if select_option==1:

            while True:

                input_decimal=int(input("Enter the Decimal : "))
                convert_decimal_to_Binary=Binary()
                convert_decimal_to_Binary.convertToBinary(input_decimal)
                convert_decimal_to_Binary.showBinary()
                
                
                print()
        if select_option==2:

            while True:
                input_binary=int(input("Enter the Binary : "))
                convert_decimal_to_Binary=Binary()
                convert_decimal_to_Binary.convertToDecimal(input_binary)
                convert_decimal_to_Binary.showDecimal()
        
        if select_option==3:
            while(True):
                first_binary=int(input("Enter the First Binary : "))
                second_binary=int(input("Enter the Second Binary : "))
                binary_add=Binary()
                binary_add.addBinary(first_binary,second_binary)
                binary_add.showBinary()

        if select_option==4:
            while(True):
                first_binary=int(input("Enter the First Binary : "))
                second_binary=int(input("Enter the Second Binary : "))
                print()
                binary_sub=Binary()
                binary_sub.subBinary(first_binary,second_binary)
                binary_sub.showBinary()
        
        if select_option==5:
            while(True):
                first_binary=int(input("Enter the First Binary : "))
                second_binary=int(input("Enter the Second Binary : "))
                print()
                binary_mul=Binary()
                binary_mul.mulBinary(first_binary,second_binary)
                binary_mul.showBinary()

    
    
            




    

