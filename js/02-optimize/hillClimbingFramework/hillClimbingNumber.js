var hillClimbing = require("./hillClimbing");        // 引入爬山演算法類別
var solutionNumber = require("../solution/solutionNumber");    // 引入平方根解答類別

// 執行爬山演算法 (從「解答=0.0」開始尋找, 最多十萬代、失敗一千次就跳出。
hillClimbing(new solutionNumber(0.0), 100000, 1000);