from time import sleep

def forwardMultiplyGate(x, y):
    return x * y

new_x = -2
new_y = 3
output1 = forwardMultiplyGate(new_x, new_y) # - 6
print("\t output1 = ", output1)
h = 0.0001 # or 0.00001
sleep(1)
print("\n")

xph = new_x + h
print("\t xph = ", xph)
output_xph = forwardMultiplyGate(xph, new_y) # -5.9997
print("\t output_xph = ", output_xph)
x_derivative = (output_xph - output1) / h # 3.0
print("\t x_derivative = ", x_derivative)
sleep(1)
print("\n")

# derivative with respect to y
yph = new_y + h # 3.0001
print("\t yph = ", yph)
output_yph = forwardMultiplyGate(new_x, yph) # -6.0002
print("\t output_yph = ", output_yph)
y_derivative = (output_yph - output1) / h # -2.0
print("\t y_derivative = ", y_derivative)
sleep(1)
print("\n")

step_size = 0.01
out = forwardMultiplyGate(new_x, new_y)
new_x = new_x + step_size * x_derivative # -1.97
print("\t x * x_derivative = ", new_x)
new_y = new_y + step_size * y_derivative # +2.98
print("\t y * y_derivative = ", new_y)
new_out = forwardMultiplyGate(new_x, new_y)
print("\t new_output = ", new_out) # -5.87, exciting! > -6.0
sleep(1)
print("\n")

x_again = -2
y_again = 3
new_output = forwardMultiplyGate(x_again, y_again)
x_gradient = y_again
y_gradient = x_again

new_stepsize = 0.015
x_again += new_stepsize * x_gradient
print("\t x_again = ", x_again) # -1.97
y_again += new_stepsize * y_gradient
print("\t y_again = ", y_again) # 2.98
new_output = forwardMultiplyGate(x_again, y_again)
print("\t new_output = ", new_output) # -5.87 > -6.0


