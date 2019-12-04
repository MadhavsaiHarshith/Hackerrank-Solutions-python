def gradingStudents(grades):
    
    for i in range(len(grades)):
        j=grades[i]
        h=(j%5)
        k=(j+5)-h
        if(j>35):
            if(k-j)<3:
                print(k)
            else:
                print(j)
        else:
            
            print(j)
