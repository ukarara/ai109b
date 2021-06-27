def queen(n):                       #n皇后主函數
    q = []                          #紀錄Q位置,一開始沒排所以是空的
    return queeNext(n,q)

def queeNext(n,q):                     #已經排好的q[0..y2-1],繼續排下去
    y2 = qlen = len(q)                 #q的長度qlen =y2=n  
    if qlen == n:                       #所有皇后排好了
        print(q)                        #印出盤面
        return 
    #還沒排滿 繼續排下去
    for x2 in range(n):                 #對本列每一個x去嘗試
        isconflict = False              #設定是否衝突變數    
        for y in range(qlen):           #前面已經排下去的皇后座標為(x,y)
            x = q[y]
            if conflict(x,y,x2,y2):     #檢查新排的皇后是否衝突
                isconflict = True
        if not isconflict:              #如果沒衝突
            q.append(x2)                #把(x2,y2)放進盤面
            queeNext(n,q)               #遞迴尋找下一皇后
            q.pop()                     #把(x2,y2)移出盤面
            
def conflict(x1,y1,x2,y2):          #檢查(x1,y1)(x2,y2)兩個皇后間是否有衝突
    if x1==x2:return True           #判斷X軸重疊
    if y1==y2:return True           #判斷Y軸重疊
    if x1+y1 == x2+y2: return True  #判斷斜線上重疊
    if x1-y1 == x2-y2: return True
    return False

queen(4)                            #四皇后情況
queen(8)                            #八皇后情況