def solution(n):
    def print_up_down():
        print("*" * n)
    def print_mid():
        print("*" + " " * (n-2) + "*")
    print_up_down()
    for i in range(n-2):
        print_mid()
    print_up_down()

solution(3)