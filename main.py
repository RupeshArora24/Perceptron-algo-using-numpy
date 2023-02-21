import numpy as np

Input = np.array([[-1, -1, 1], [-1, 1, 1], [1,-1,1] ,[1,1,1]])

Target_output = np.array([[-1],[-1],[-1],[1]])

random_w=np.random.rand(3)
print(random_w)
w=np.round_(random_w,decimals=1)
Error=E_total=0
w_new=w_old=w
epoch = 0




print("W - ",w)
print("Target-",Target_output)
print("Input-",Input)
i=0



for i in range(1000):
    print("epoch",epoch)
    i=0
    while i < 4:

        print("w_new = ", w_new)
        Target_ = Target_output[i:i + 1, :]
        print("Target - ", Target_, "Value of i = ", i)

        a = Input[i:i + 1, :]
        print("Input - ", i, a)

        net = np.dot(a, w)
        print("Net - ", i, net)

        y = np.sign(net)
        print("y - ", i, y)

        if (Target_ == y):
            print("successful")
            w_old = w_new
            print("w_new,w_old,w = ", w_new, w_old, w)
        else:
            print("unsuccessful")
            Error = 0.5 * (Target_ - y) ** 2
            print("Error = ", Error)
            E_total = E_total + Error
            print(E_total)

            if (Target_ == [[-1]] and y == [[1]]):
                print("When net2<net1 - ")
                Delta_w = -1 * a
                print("Delta_w = ", Delta_w)
                w_new = w_old + Delta_w
                print("w_new = ", w_new)
                w_old = w_new

            if (Target_ == [[1]] and y == [[-1]]):
                print("For net2>net1 - ")
                Delta_w = +1 * a
                print("Delta_w = ", Delta_w)
                w_new = w_old + Delta_w
                print("w_new = ", w_new)
                w_old = w_new

        i=i+1
        print("The value of w_new = ", w_new)
    epoch=epoch+1
    print(E_total)


print("The value of etotal = ",E_total)
