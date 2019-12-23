#
# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#

# @lc code=start
class ExamRoom:

    def __init__(self, N: int):
        self.seats = []
        self.N = N

    def seat(self) -> int:
        max_distance = 0
        res = 0
        index = 0
        if len(self.seats) == 1:
            if self.seats[0] >= self.N / 2:
                res = 0
                index = 0
            else:
                res = self.N-1
                index = 1
        else:
            if self.seats and self.N-1-self.seats[-1] >= max_distance:
                max_distance = self.N-1-self.seats[-1]
                res = self.N-1
                index = len(self.seats)
            for i in range(len(self.seats)-1, 0, -1):
                l, r = self.seats[i-1], self.seats[i]
                d = (r-l)//2
                if d >= max_distance:
                    max_distance = d
                    res = l + d
                    index = i
            if self.seats and self.seats[0] >= max_distance:
                res = 0
                index = 0        
        self.seats.insert(index, res)
        return res

    def leave(self, p: int) -> None:
        self.seats.remove(p)



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
# @lc code=end

["ExamRoom","seat","seat","seat","leave","leave","seat","seat","seat","seat","seat","seat","seat","seat","seat","leave","leave","seat","seat","leave","seat","leave","seat","leave","seat","leave","seat","leave","leave","seat","seat","leave","leave","seat","seat","leave"]
[[10],[],[],[],[0],[4],[],[],[],[],[],[],[],[],[],[0],[4],[],[],[7],[],[3],[],[3],[],[9],[],[0],[8],[],[],[0],[8],[],[],[2]]
exam = ExamRoom(10)
exam.seat()
exam.seat()
exam.seat()
exam.leave(0)
exam.leave(4)
exam.seat()
exam.seat()
exam.seat()
exam.seat()
exam.seat()
exam.seat()
exam.seat()
exam.seat()
exam.seat()
exam.leave(0)
exam.leave(4)
exam.seat()
exam.seat()
exam.leave(7)
exam.seat()
exam.leave(3)
exam.seat()
exam.leave(3)
exam.seat()
exam.leave(9)
exam.seat()
exam.leave(0)
# exam.leave(8)
# exam.seat()
# exam.seat()
# exam.leave(0)
# exam.leave(8)
# exam.seat()
# exam.seat()
# exam.leave(2)
