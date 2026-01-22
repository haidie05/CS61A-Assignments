HW_SOURCE_FILE = __file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<10:
        if n==8:
            return 1
        else:
            return 0
    else:
        if n%10==8:
            return num_eights(n//10)+1
        else:
            return num_eights(n//10)


def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777) # 0 + 0
    0
    >>> digit_distance(314) # 2 + 3
    5
    >>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
    32
    >>> digit_distance(3464660003)  # 1 + 2 + 2 + 2 + ... + 3
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<10:
        return 0
    else:
        return digit_distance(n//10)+abs(n%10-n//10%10)


def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['BitAnd', 'BitOr', 'BitXor']) # ban bitwise operators, don't worry about these if you don't know what they are
    True
    """
    "*** YOUR CODE HERE ***"
    def interleaved_unit(k):
        if k>n:
            return 0
        elif k==1:
            return odd_func(1)+even_func(2)+interleaved_unit(k+2)
        elif k==n:
            return odd_func(k)
        else:
            return odd_func(k)+even_func(k+1)+interleaved_unit(k+2)
    return interleaved_unit(1)


def next_smaller_dollar(bill):
    """Returns the next smaller bill in order."""
    if bill == 100:
        return 50
    elif bill == 50:
        return 20
    elif bill == 20:
        return 10
    elif bill == 10:
        return 5
    elif bill == 5:
        return 1

def count_dollars(total):
    """Return the number of ways to make change.

    >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_dollars', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    '''
    if total ==0:
        return 1
    elif total==1:
        return 1
    elif total==5 or total==10 or total==20 or total==50 or total==100:
        print("total=",total)
        return count_dollars(next_smaller_dollar(total))+count_dollars(total-next_smaller_dollar(total))
    elif 1<total and total <5:
        return 1
    elif 5<total and total <10:
        with_5_bill=count_dollars(total-5)
        without_5_bill=1
        return with_5_bill+without_5_bill
    elif 10<total and total <20:
        with_10_bill=count_dollars(total-10)
        without_10_bill=count_dollars(total-5)+count_dollars(10)-1
        return with_10_bill+without_10_bill
    elif 20<total and total <50:
        with_20_bill=count_dollars(total-20)
        without_20_bill=count_dollars(20)-1+count_dollars(total-20)
        return with_20_bill+without_20_bill
    elif 50<total and total <100:
        with_50_bill=count_dollars(total-50)
        without_50_bill=count_dollars(total-50)+count_dollars(50)-1
        return with_50_bill+without_50_bill
    elif 100<total:
        with_100_bill=count_dollars(total-100)
        without_100_bill=count_dollars(total-100)+count_dollars(100)-1
        return with_100_bill+without_100_bill
    '''
    def count_by_bill(total,bill):
        if total==0:
            return 1
        elif total<0:
            return 0
        elif bill==None:
            return 0
        else:
            with_bill=count_by_bill(total-bill,bill)
            without_bill=count_by_bill(total,next_smaller_dollar(bill))
            return with_bill+without_bill
    return count_by_bill(total,100)


def next_larger_dollar(bill):
    """Returns the next larger bill in order."""
    if bill == 1:
        return 5
    elif bill == 5:
        return 10
    elif bill == 10:
        return 20
    elif bill == 20:
        return 50
    elif bill == 50:
        return 100

def count_dollars_upward(total):
    """Return the number of ways to make change using bills.

    >>> count_dollars_upward(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars_upward(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars_upward(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars_upward(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars_upward(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars_upward(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_dollars_upward', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def count_by_bill_upward(total,bill):
        if total==0:
            return 1
        elif total<0:
            return 0
        elif bill==None:
            return 0
        else:
            with_bill=count_by_bill_upward(total-bill,bill)
            without_bill=count_by_bill_upward(total,next_larger_dollar(bill))
            return with_bill+without_bill
    return count_by_bill_upward(total,1)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    medium=6-start-end
    if n==1:
        print_move(start,end)
    else:
        move_stack(n-1,start,medium)
        print_move(start,end)
        move_stack(n-1,medium,end)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    '''
    return lambda x:1 if x==1 else mul(x,make_anonymous_factorial()(x-1))
    '''
    return (lambda f:lambda k:f(f,k))(lambda f,k:k if k==1 else mul(k, f(f,sub(k,1))))
