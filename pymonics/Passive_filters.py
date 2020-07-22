import math as math

class Passive_filters():
    """
    single_tuned_filter:
    Single Tuned filter design. returns [C,L,R]
    """
    def single_tuned_filter(self,h,Qc,Q,f,V):
        wh = 2*math.pi*f*h
        C = Qc/(2*math.pi*f*V*V)
        X = 1/(wh*C)
        L = X/(wh)
        R = X/Q
        return [C,L,R]
    """
    high_pass_filter:
    Highpass filter design. returns [C,L,R]
    """
    def high_pass_filter(self,h,Qc,Q,f,V):
        wh = 2*math.pi*f*h;
        C = Qc/(2*math.pi*f*V*V);
        X = 1/(wh*C);
        L = X/(wh);
        R = X * Q;
        return [C,L,R]