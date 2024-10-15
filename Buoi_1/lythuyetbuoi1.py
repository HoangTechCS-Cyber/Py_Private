import sys

def main():
    import sys
    import threading

    def solve():
        import sys

        import sys

        sys.setrecursionlimit(1 << 25)
        n, q = map(int, sys.stdin.readline().split())
        queries = []
        total_count = [0] * (n + 1)
        for _ in range(q):
            x, y = map(int, sys.stdin.readline().split())
            queries.append( (x, y) )
            total_count[x] +=1
            total_count[y] +=1

        a = [0]*(n+1)
        output = []
        for i in range(q):
            x, y = queries[i]
            current_remaining_x = total_count[x]
            current_remaining_y = total_count[y]

            if a[x] >0 or a[y] >0:
                if a[x] >0 and a[y] >0:
                    if current_remaining_x < current_remaining_y:
                        p = x
                        d = -1
                        op = 'x-'
                    else:
                        p = y
                        d = -1
                        op = 'y-'
                elif a[x] >0:
                    p = x
                    d = -1
                    op = 'x-'
                else:
                    p = y
                    d = -1
                    op = 'y-'
            else:
                if current_remaining_x > current_remaining_y:
                    p = x
                    d = 1
                    op = 'x+'
                else:
                    p = y
                    d =1
                    op = 'y+'

            a[p] += d
            output.append(op)

            # Decrement the remaining counts
            total_count[x] -=1
            total_count[y] -=1

        print('\n'.join(output))


    threading.Thread(target=solve,).start()

if __name__ == "__main__":
    main()
