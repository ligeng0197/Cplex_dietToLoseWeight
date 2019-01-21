def writeLp (FOOD, C, filename):
    wr=open(filename, 'w')
    #write objective function
    wr.write('MINIMIZE\n')
    wr.write('Objective: ')
    for i in range(0,len(FOOD)):
        if i>0:
            wr.write('+') 
        wr.write(str(FOOD[i].R))
        wr.write('x'+str(i+1))
    #write constraints
    wr.write('\nSubject To:\n')
    #write the Subject_D
    wr.write('C1: ')
    for i in range(0,len(FOOD)):
        if i>0:
            wr.write('+') 
        wr.write(str(FOOD[i].D))
        wr.write('x'+str(i+1))
    wr.write('>=' + str(45) + '\n')
    #write the Subject_S
    wr.write('C2: ')
    for i in range(0,len(FOOD)):
        if i>0:
            wr.write('+') 
        wr.write(str(FOOD[i].S))
        wr.write('x'+str(i+1))
    wr.write('>=' + str(30) + '\n')
    #write the Subject_W
    wr.write('C3: ')
    for i in range(0,len(FOOD)):
        if i>0:
            wr.write('+') 
        wr.write(str(FOOD[i].W))
        wr.write('x'+str(i+1))
    wr.write('>=' + str(1000) + '\n')
    #write the Subject_N
    wr.write('C4: ')
    for i in range(0,len(FOOD)):
        if i>0:
            wr.write('+') 
        wr.write(str(FOOD[i].N))
        wr.write('x'+str(i+1))
    wr.write('>=' + str(2500) + '\n')
    #write the Subject_G
    wr.write('C5: ')
    for i in range(0,len(FOOD)):
        if i>0:
            wr.write('+') 
        wr.write(str(FOOD[i].G))
        wr.write('x'+str(i+1))
    wr.write('>=' + str(1000) + '\n')
    #write the Subject_R
    wr.write('C6: ')
    for i in range(0,len(FOOD)):
        if i>0:
            wr.write('+') 
        wr.write(str(FOOD[i].R))
        wr.write('x'+str(i+1))
    wr.write('>=' + str(C) + '\n')
    
    #write variables
    wr.write('GENERAL\n')
    for i in range(0,len(FOOD)):
        wr.write(' x'+str(i+1)+' ')
        if (i+1)>=20 and ((i+1)%20)==0:
            wr.write('\n') 
    wr.write('\nEND\n')
    wr.close()
