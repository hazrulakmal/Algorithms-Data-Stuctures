two-number-Array

#given an array with n elements of which comprimises of two distinct number with equal distribution. 
#create an algorithm that return these two numbers, x and y


function nonrandom(A)
    x = A[1]
    i = 2
    while x == A[i]
        i += 1
    end
    y = A[i]
    return x,y
end

#worst-case analysis. each step requires constant time except for the while loop. worst scenario is when the list is A = [x,..,x,y,...y] the loop is executed omega(n) times

A = [2,2,2,3,2,3,3,3]
nonrandom(A)

function random(A)
    n = length(A)
    x, y= A[1] , A[1]
    while x == y
        j =  rand(1:n, 1)
        y = A[j[1]]
    end
    return x, y
end

random(A)

#expected running time is O(1)