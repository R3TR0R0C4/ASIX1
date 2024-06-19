def parell(num):
    try:
        if num%2==0:
            return True
        else:
            return False
    except:
        return "Entrada no vàlida"

def quadrat(a):
    try:
        return a*a
    except:
        return "Entrada no vàlida"

def cubic(a):
    try:
        return a*a*a
    except:
        return "Entrada no vàlida"
    
def saluda(nom):
    try:
        return "Hello, " + nom
    except:
        return "Entrada no vàlida"