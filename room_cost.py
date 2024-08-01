def whitewashing_area(l,w,h):
    return 2*(h*l)+2*(h*w)+(l*w)        #2*h*(l+w)+(l*w)

def whitewashing_cost(a,r=15):
    return a*r

def flooring_cost(l,w,r):
    return l*w*r

def display_costs(l,w,h):
    print("area: ",whitewashing_area(l,w,h))
    print("Cost: ",whitewashing_cost(whitewashing_area(l,w,h)))
    print("Mosaic floor Cost: ",flooring_cost(l,w,100))
    print("Cement floor Cost: ",flooring_cost(l,w,55))
