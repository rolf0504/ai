const step = 0.01

// 我們想找函數 f 的最低點
function f (p) {
  let [x,y] = p
  return x * x + y * y
}

// 函數 f 對變數 k 的偏微分: df / dk
function df (f, p, k) {
  let p1 = p.slice(0)
  p1[k] += step
  return (f(p1) - f(p)) / step
}

// 函數 f 在點 p 上的梯度
function grad(f, p) {
  let gp = []
  for (let k in p) {
    gp[k] = df(f, p, k)
  }
  return gp
}

let [x,y] = [1,3]
console.log('x=', x, 'y=', y)
console.log('df(f(x,y), 0) = ', df(f, [x, y], 0))
console.log('df(f(x,y), 1) = ', df(f, [x, y], 1))
console.log('grad(f)=', grad(f, [x,y]))
