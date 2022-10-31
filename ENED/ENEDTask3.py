from venv import CORE_VENV_DEPS


V = float(input("V(mi/hr)= "))
L = float(input("L(in)= "))
U = float(input("U(lb/in*s)= "))
P = float(input("P(ib/in^3)= "))
Cvn = 0.44704
Cln = 0.0254
Cun = 17.8579673
Cpn = 27679.90471
Vn = V*(Cvn)
Ln = L*(Cln)
Un = U*(Cun)
Pn = P*(Cpn)
Re = (Vn*Ln*Pn)/Un
print(Re)