#this script is used for a homework --oking9
#---------------------------------------------
#there are four functions we need to pay attention to
#first readExcel we use this to get necessary information about the Lp problem
#       FOOD(array for food) read_excel(filename)
#second writeLp with the function to print the Excel information in to a LP file
#       void                 writeLp(FOOD,totalweight C,filename)
#third solveByCplex with the lp file call CPLEX and print the answer
#       void                 solveByCplex(filename)
#
#
#
import sys
import readExcel
import writeLp
import solveByCplex

if __name__ == "__main__":
    if len(sys.argv) != 3:#1.excelfilename 2.the limit C 
        print "error: need 2 parameters"
        sys.exit(-1)
    excelFile = sys.argv[1]
    C = sys.argv[2]
    filename = "oking9.lp"
    FOOD = readExcel.read_excel(excelFile)
    writeLp.writeLp(FOOD,C,filename)
    solveByCplex.Solve(filename)
    
