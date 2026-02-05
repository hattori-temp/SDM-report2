#!/usr/bin/python3

def calc(A, B):
    valid = False
    try:
        a = float(A)
        b = float(B)
        
        if 0 < a < 1000 and 0 < b < 1000:
            valid = True
        else:
            valid = False
            
    except (ValueError, TypeError):
        # 文字列が入力された場合
        valid = False
                
    if valid:
        ans = a * b
        return ans
    else:
        return -1
                
def main():
    while True:
        A = input('input A (or "end" to quit): ')
        if A == 'end':
            break
        B = input('input B (or "end" to quit): ')
        if B == 'end':
            break
            
        print('input A * input B = ', calc(A, B))

if __name__ == '__main__':
    main()
