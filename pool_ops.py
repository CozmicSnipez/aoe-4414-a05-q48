# pool_ops.py
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
# Determines the output shape and operation count of an average pooling layer
#
# Parameters:
#  c_in: input channel count
#  h_in: input height count
#  w_in: input width count
#  h_pool: average pooling kernel height count
#  w_pool: average pooling kernel width count
#  s: stride of average pooling kernel
#  p: amount of padding on each of the four input map sides
#
# Output:
#  Prints the output channel count, output height, output width,
#  and the number of additions, multiplications, and divisions performed.

import sys

# Helper function to find pooling layer output dimensions and operations count
def average_pooling_ops(c_in, h_in, w_in, h_pool, w_pool, s, p):
    # Output dimensions (height and width)
    h_out = (h_in + 2 * p - h_pool) // s + 1
    w_out = (w_in + 2 * p - w_pool) // s + 1
    
    c_out = c_in  # Output channels same as input channels

    # Operations count
    # Additions: each pooling operation involves (h_pool * w_pool - 1) additions
    adds = c_out * h_out * w_out * (h_pool * w_pool - 1)
    
    # Multiplications: no multiplications in average pooling
    muls = 0
    
    # Divisions: one division per pooling operation
    divs = c_out * h_out * w_out

    return c_out, h_out, w_out, adds, muls, divs

# Parse script arguments
if len(sys.argv) == 8:
    c_in = int(sys.argv[1])
    h_in = int(sys.argv[2])
    w_in = int(sys.argv[3])
    h_pool = int(sys.argv[4])
    w_pool = int(sys.argv[5])
    s = int(sys.argv[6])
    p = int(sys.argv[7])
else:
    print('Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p')
    exit()

# Compute output shape and operations count
c_out, h_out, w_out, adds, muls, divs = average_pooling_ops(c_in, h_in, w_in, h_pool, w_pool, s, p)

# Print the results
print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))   # number of additions performed
print(int(muls))   # number of multiplications performed
print(int(divs))   # number of divisions performed
