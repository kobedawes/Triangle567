
def classifyTriangle(a,b,c):
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    if (a + b)<c or (b + c)< a or (c + a)< b:
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b == c == a:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) or ((c ** 2) + (b ** 2)) == (a ** 2):
        return 'Right'
    elif a != b != c != a:
        return 'Scalene'
    else:
        return 'Isosceles'
