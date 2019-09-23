from py6.ai.hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionArray import SolutionArray # 引入平方根解答類別

# 執行爬山演算法 (從「解答=0.0」開始尋找, 最多十萬代、失敗一千次就跳出。
hillClimbing(SolutionArray([1,1,1]), 100000, 1000)

"""
var hillClimbing = require("./hillClimbing");      // 引入爬山演算法類別
var solutionArray = require("../solution/solutionArray");    // 引入多變數解答類別 (x^2+3y^2+z^2-4x-3y-5z+8)

// 執行爬山演算法 (從「解答(x,y,z)=(1,1,1)」開始尋找, 最多十萬代、失敗一千次就跳出。
hillClimbing(new solutionArray([1,1,1]), 100000, 1000);
"""