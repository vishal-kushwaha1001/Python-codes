# Method Resolution Order

class A :
    label = "A : plain chai"
    
class B(A):
    label = "B : masala chai"
    
    
class C(A):
    label = "C: ginger Tea"
    
class D(C,B):
    # label = "D : cardomom Tea"
    pass
    

s1 = D()

print(s1.label)