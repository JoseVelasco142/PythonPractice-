def sum_in_loop(arg):
        return sum( int(n) for n in arg)

num_list = raw_input().split(' ')
print sum_in_loop(num_list)
