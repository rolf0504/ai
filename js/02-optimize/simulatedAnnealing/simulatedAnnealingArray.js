var simulatedAnnealing = require("./simulatedAnnealing"); // 引入模擬退火法類別
var solutionArray = require("../solution/solutionArray"); // 引入多變數解答類別 (x^2+3y^2+z^2-4x-3y-5z+8)

// 執行模擬退火法 (從「解答(x,y,z)=(1,1,1)」開始尋找, 最多執行 2 萬代。
simulatedAnnealing(new solutionArray([1,1,1]), 20000);