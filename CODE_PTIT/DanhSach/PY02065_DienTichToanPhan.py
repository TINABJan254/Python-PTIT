if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = []
        Stren = 0  # đếm số khối khác 0 (diện tích mặt trên)
        
        for i in range(n):
            row = list(map(int, input().split()))
            a.append(row)
            Stren += sum(1 for x in row if x != 0)
        
        Sday = 2 * Stren  # diện tích mặt trên và mặt đáy
        
        # diện tích Sxq theo hàng
        Sxq1 = 0
        for i in range(n):
            Sxq1 += a[i][0] + a[i][m-1]  # thêm a[i][1] + a[i][m]
            for j in range(1, m):
                Sxq1 += abs(a[i][j] - a[i][j-1])
        
        # diện tích Sxq theo cột
        Sxq2 = 0
        for j in range(m):
            Sxq2 += a[0][j] + a[n-1][j]  # thêm a[1][j] + a[n][j]
            for i in range(1, n):
                Sxq2 += abs(a[i][j] - a[i-1][j])
        
        print(Sday + Sxq1 + Sxq2)
