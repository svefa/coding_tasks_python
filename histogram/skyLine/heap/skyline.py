def getSkyline(self, buildings):
    # buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
    # (2 -9 10)  (3 -15 7)  (5 -12 12)                        (15 -10 20) (19, -8, 24)
    # (2 -9 10)  (3 -15 7)  (5 -12 12) (7 0*) (10 0*) (12 0*) (15 -10 20)  (19, -8, 24) (20 0 *) (24 0 *)
    
    res, hp = [[0, 0]], [(0, float("inf"))]
    # hp  [0 0] [0 inf]
    for x, negH, R in events:
        # x=2 -9 R=10 
        #  3 -15 7    (3 >= 10)
        #  5 -12 12  (5 >= 7)
        #  7 0 *     (7 >= 7 7 >= 12)
        #  10 0 *    (10>=12) noth
        #  12 0  *    ( 12 >= 12 12 >= 10 12 >=0)
        while x >= hp[0][1]: 
            heapq.heappop(hp)
            #  [-9, 10] (0,inf) [0,0]
            #  (-12 12) (-9, 10) (0,0)
            #  (-9, 10) (0,inf) (0,0)
            #  (0 inf) (0,0)
        if negH: 
            heapq.heappush(hp, (negH, R))
            # hp : (-15 7) (-12 12) (-9, 10) (0,0)
        if res[-1][1] + hp[0][0]: 
            res += [x, -hp[0][0]],
            # res: [2, 9] [3, 15] [7 12] [12 0]
    return res[1:]