import numpy as np

Input = np.array([[-1, -1, 1], [-1, 1, 1], [1,-1,1] ,[1,1,1]])
print(Input.shape)

Target_output = np.array([[-1],[-1],[-1],[1]])

random_w=np.array([np.random.rand(1),np.random.rand(1),np.random.rand(1)])
print(random_w.shape)
print(random_w)
random_w=np.reshape(random_w,(1,3))
w=w_new=np.round_(random_w,decimals=1)
Error=E_total=0
w_new=w_old=w
epoch = 0




print("W_mew - ",w_new,w,w_old)
print("Target-",Target_output)
print("Input-",Input)
i=0



for i in range(5):
    E_total = 0
    print("epoch",epoch)
    i=0
    while i < 4:

        print("w_new = ", w_new)
        Target_ = Target_output[i:i + 1, :]
        print("Target - ", Target_, "Value of i = ", i)
        a = Input[i:i + 1, :]
        print("Input - ", i, a)
        print("Shape of the input = ",a.shape)
        a=np.reshape(a,(3,1))
        print("The reshaped value of input = ",a.shape)
        print("Reshaped input = ",a)
        print("w_new = ",w_new)
        print("Shape of w_new = ",w_new.shape)
        net = np.dot(w_new,a)
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
                Delta_w = np.reshape(Delta_w,(1,3))
                print("Delta_w = ", Delta_w)
                w_new = w_old + Delta_w
                print("w_new = ", w_new)
                w_old = w_new
                print("W_old")

            if (Target_ == [[1]] and y == [[-1]]):
                print("For net2>net1 - ")
                Delta_w = +1 * a
                Delta_w = np.reshape(Delta_w, (1, 3))
                print("Delta_w = ", Delta_w)
                w_new = w_old + Delta_w
                print("w_new = ", w_new)
                w_old = w_new
                print("W_old")

        i=i+1

        print("The value of w_new = ", w_new)
    print("Total error", E_total)
    epoch=epoch+1
    if(E_total==[[0]]):
        break;


print("The value of etotal = ",E_total)
