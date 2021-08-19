import setup
from docplex.mp.model import Model
from docplex.util.environment import get_environment

n = 10  #worker
m = 20  #number of tasks

EN = [i for i in range(1, n+1)]
EM = [j for j in range(1, m+1)]

Jm = [j for j in range(1, 5)]
J1 = [j for j in range(5, 21)]


N = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


a = [[40, 30, 20, 60, 30, 50, 70, 70, 80, 90, 80, 40, 30, 60, 20, 30, 50, 40, 90, 50],
     [30, 20, 10, 90, 80, 70, 60, 50, 40, 55, 35, 25, 90, 85, 80, 40, 15, 10, 35, 25],
     [90, 80, 70, 60, 50, 40, 30, 40, 50, 20, 45, 65, 95, 60, 80, 45, 35, 80, 65, 90],
     [65, 45, 95, 35, 65, 85, 90, 60, 40, 30, 95, 80, 55, 65, 45, 90, 65, 75, 65, 80],
     [55, 65, 35, 95, 60, 80, 65, 90, 55, 45, 35, 95, 90, 80, 70, 65, 35, 90, 80, 50],
     [60, 50, 40, 90, 80, 75, 80, 90, 80, 85, 90, 65, 75, 85, 65, 85, 95, 95, 90, 80],
     [55, 65, 60, 50, 55, 55, 65, 75, 70, 60, 55, 50, 55, 60, 60, 65, 60, 80, 65, 55],
     [20, 30, 20, 40, 20, 50, 40, 45, 65, 60, 45, 35, 45, 60, 65, 65, 45, 35, 30, 50],
     [50, 40, 45, 80, 90, 65, 65, 35, 90, 65, 85, 95, 90, 50, 55, 65, 95, 85, 90, 55],
     [90, 65, 35, 45, 65, 65, 75, 85, 70, 70, 90, 65, 60, 95, 55, 65, 65, 85, 65, 60]
     ]


F = [50, 40, 35, 45, 20, 10, 15, 30, 20, 20, 25, 15, 10, 25, 20, 15, 10, 25, 30, 20]


twoDim = [(i, j) for i in EN for j in EM]

oneSize = [i for i in EN]
oneSize_j = [j for j in EM]



mdl = Model('IDEAL TASK ASSIGNMENT')

x1 = mdl.binary_var_dict(twoDim, name='x1') #Let Xij be a binary variable indicating whether tester i is assigned to task j
xm = mdl.continuous_var_dict(twoDim, name='xm')
mdl.add_constraints(xm[i, j] >= 0 for i in EN for j in Jm)
mdl.add_constraints(xm[i, j] <= 1 for i in EN for j in Jm)

y = mdl.continuous_var_dict(oneSize, name='y')  #
b = mdl.continuous_var_dict(oneSize, name='b')  #

o = mdl.continuous_var_dict(oneSize, name='O') #Overtime that represents except normal working hours
R = mdl.continuous_var_dict(oneSize, name='R') #Regular time that represents normal working hours
d = mdl.continuous_var(name='d') #Let d be the variable that is equal to the maximum task duration time of a tester.



mdl.maximize(mdl.sum(x1[i, j]*a[i-1][j-1] for i in EN for j in J1)+
             mdl.sum(xm[i, j]*a[i-1][j-1] for i in EN for j in Jm) -
            (mdl.sum(o[i] for i in oneSize))-20*d)

mdl.add_constraints(mdl.sum(x1[i, j] for i in EN) == 1 for j in J1)

mdl.add_constraints(mdl.sum(xm[i, j] for i in EN) == 1 for j in Jm)

mdl.add_constraints(mdl.sum(x1[i, j]*F[j-1]for j in J1)+
                     mdl.sum(xm[i, j] * F[j - 1]for j in Jm) <= y[i] for i in EN)

mdl.add_constraints(o[i] <= 21 for i in oneSize)

mdl.add_constraints(y[i] == o[i]+R[i] for i in oneSize)

mdl.add_constraints(R[i]+N[i-1] <= 45 for i in EN)

mdl.add_constraints(mdl.sum(x1[i, j]*F[j-1]for j in J1)+
                     mdl.sum(xm[i, j] * F[j - 1]for j in Jm) == y[i]-b[i] for i in EN)

mdl.add_constraints(mdl.sum(x1[i, j]*F[j-1]for j in J1)+
                     mdl.sum(xm[i, j] * F[j - 1] for j in Jm)<= d for i in EN)

#ALL DECISION VARIABLES MUST BE GREATER THAN 0.

mdl.add_constraints(b[i] >= 0 for i in oneSize)
mdl.add_constraints(y[i] >= 0 for i in oneSize)
mdl.add_constraints(o[i] >= 0 for i in oneSize)
mdl.add_constraints(R[i] >= 0 for i in oneSize)

#print(mdl.export_to_string())

mdl.solve(log_output=True)
mdl.print_solution()
print(mdl.solve_details)

with get_environment().get_output_stream("solution.json") as fp:
     mdl.solution.export(fp, "json")

