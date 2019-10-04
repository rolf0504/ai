# Tensorflow.js

* 事先訓練好的 model -- https://github.com/tensorflow/tfjs-models

// 注意看 Model 的用法 -- https://js.tensorflow.org/api/0.10.0/#class:Model

試用： https://playground.tensorflow.org/

範例來源： https://github.com/tensorflow/tfjs-examples (重要，愈來愈多了!)

* 手寫辨識 -- https://storage.googleapis.com/tfjs-examples/mnist/dist/index.html
* 物體辨識 -- https://storage.googleapis.com/tfjs-examples/mobilenet/dist/index.html


討論區： https://groups.google.com/a/tensorflow.org/forum/#!forum/tfjs

課程： https://angularfirebase.com/lessons/tensorflow-js-quick-start/#Step-4-Build-a-Machine-Learning-Model

訊息: https://medium.com/@tensorflow

* [记录一下关于 tensorflow.js 的了解](https://www.linpx.com/p/you-want-to-know-that-everything-about-tensorflowjs-is-here.html)

## 參考專案

* https://hpssjellis.github.io/beginner-tensorflowjs-examples-in-javascript/ (超讚!)
  * https://github.com/hpssjellis/beginner-tensorflowjs-examples-in-javascript
  * https://github.com/hpssjellis/beginner-tensorflowjs-examples-in-javascript/tree/master/tf-examples
* https://www.npmjs.com/package/tfjs-yolo-tiny
  * https://pjreddie.com/darknet/yolo/
  * [Deep learning in your browser: A brisk guide](https://towardsdatascience.com/deep-learning-in-your-browser-a-brisk-guide-ca06c2198846)
* https://alantian.net/ganshowcase/
* https://github.com/tensorflow/tfjs-examples/tree/master/mobilenet
  * https://storage.googleapis.com/tfjs-examples/mobilenet/dist/index.html
* https://github.com/iwe7/iwe7-tfjs (@tensorflow/tfjs 初探)

## 文章

* [Machine Learning in Node.js With TensorFlow.js](http://jamesthom.as/blog/2018/08/07/machine-learning-in-node-dot-js-with-tensorflow-dot-js/)
* [Introduction to the TensorFlow.js core API](https://observablehq.com/@nsthorat/introduction-to-deeplearn-js)
* [A Gentle Introduction to TensorFlow.js](https://medium.com/tensorflow/a-gentle-introduction-to-tensorflow-js-dba2e5257702)
* [Getting started with TensorFlow.js — Simple AND Gate Implementation](https://www.linkedin.com/pulse/getting-started-tensorflowjs-simple-gate-sam-alsmadi)
  * https://github.com/lntelliMed/tensorflow-add-js/blob/master/src/App.js
* https://groups.google.com/a/tensorflow.org/forum/#!topic/tfjs/TnIOqbAroWM

I interned in Google last year in Google Cloud, and I want to share my opinion about TypeScript. I think it's a great language when you're working on big projects. Working with multiple libraries becomes much easier - programming and debugging is way faster thanks to the language. You're able to catch bugs before compiling your project. I had my doubts at the beginning, but I found TypeScript to be a great time saver. It does solve many problems that there are in JavaScript. I don't know if there are any performance or architecture benefits specifically for tfjs.

## 影片

* [TensorFlow.js Quick Start](https://www.youtube.com/watch?v=Y_XM3Bu-4yc)
* [Tensorflow.js Explained](https://www.youtube.com/watch?v=Nc8kZABv-KE)
  * Siraj Raval -- https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A

## 範例 1 -- nmist-core

注意： 在 windows 中執行下列 yarn watch 時會失敗

```js
cd mnist-core
yarn
yarn watch
```

因為 package.json 當中的 NODE_ENV=production 會執行失敗。

```js
  "scripts": {
    "watch": "NODE_ENV=development parcel --no-hmr --open index.html ",
    "build": "NODE_ENV=production parcel build index.html  --no-minify --public-url ./"
  },
```

最簡易的解決辦法是使用 cross-env 這個套件

參考： [使用cross-env解决跨平台设置NODE_ENV的问题](https://segmentfault.com/a/1190000005811347)

先安裝 cross-env 之後，把上面的 script 段改成

```
  "scripts": {
    "watch": "cross-env NODE_ENV=development parcel --no-hmr --open index.html ",
    "build": "cross-env NODE_ENV=production parcel build index.html  --no-minify --public-url ./"
  },
```

這樣就可以用 yarn watch 執行了！ 結果如下：

![](img/nmist-core.png)

## deepLearn.js -- 已過期，改為 tensorflow.js 了

* https://deeplearnjs.org/
  * https://github.com/PAIR-code/deeplearnjs

deeplearn.js is an open-source library that brings performant machine learning building blocks to the web, allowing you to train neural networks in a browser or run pre-trained models in inference mode.

## ES6 使用展示範例

* https://github.com/PAIR-code/deeplearnjs/tree/master/starter/es6/


# 官方範例 ccc 測試結果

## abalone-node 失敗

PS D:\ccc\test\tfjs-examples\abalone-node> yarn train
yarn run v1.6.0
(node:10592) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
$ node train.js
internal/modules/cjs/loader.js:805
  return process.dlopen(module, path.toNamespacedPath(filename));
                 ^

Error: A dynamic link library (DLL) initialization routine failed.
\\?\D:\ccc\test\tfjs-examples\abalone-node\node_modules\@tensorflow\tfjs-node\lib\napi-v4\tfjs_binding.node
    at Object.Module._extensions..node (internal/modules/cjs/loader.js:805:18)
    at Module.load (internal/modules/cjs/loader.js:653:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:593:12)
    at Function.Module._load (internal/modules/cjs/loader.js:585:3)
    at Module.require (internal/modules/cjs/loader.js:690:17)
    at require (internal/modules/cjs/helpers.js:25:18)
    at Object.<anonymous> (D:\ccc\test\tfjs-examples\abalone-node\node_modules\@tensorflow\tfjs-node\dist\index.js:44:16)
    at Module._compile (internal/modules/cjs/loader.js:776:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:787:10)
    at Module.load (internal/modules/cjs/loader.js:653:32)
error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
PS D:\ccc\test\tfjs-examples\abalone-node> node -v
v10.16.0

## fashion-mnist-vae 失敗

PS D:\ccc\test\tfjs-examples\fashion-mnist-vae> yarn
yarn install v1.6.0
(node:5592) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(),
or Buffer.from() methods instead.
[1/5] Validating package.json...
[2/5] Resolving packages...
[3/5] Fetching packages...
info fsevents@1.2.7: The platform "win32" is incompatible with this module.
info "fsevents@1.2.7" is an optional dependency and failed compatibility check. Excluding it from installation.
[4/5] Linking dependencies...
warning "@tensorflow/tfjs > @tensorflow/tfjs-data@1.2.2" has unmet peer dependency "seedrandom@~2.4.3".
warning "@tensorflow/tfjs > @tensorflow/tfjs-core > rollup-plugin-visualizer@1.1.1" has unmet peer dependency "rollup@>=0.60.0".
warning "@tensorflow/tfjs-vis > vega-embed > vega-themes@2.3.0" has unmet peer dependency "vega@*".
[5/5] Building fresh packages...
Done in 2182.45s.
PS D:\ccc\test\tfjs-examples\fashion-mnist-vae> yarn train
yarn run v1.6.0
(node:9920) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(),
or Buffer.from() methods instead.
$ node train.js
Training using CPU.
Initialization of backend tensorflow failed
Error: A dynamic link library (DLL) initialization routine failed.
\\?\D:\ccc\test\tfjs-examples\fashion-mnist-vae\node_modules\@tensorflow\tfjs-node\build\Release\tfjs_binding.node
    at Object.Module._extensions..node (internal/modules/cjs/loader.js:805:18)
    at Module.load (internal/modules/cjs/loader.js:653:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:593:12)
    at Function.Module._load (internal/modules/cjs/loader.js:585:3)
    at Module.require (internal/modules/cjs/loader.js:690:17)
    at require (internal/modules/cjs/helpers.js:25:18)
    at bindings (D:\ccc\test\tfjs-examples\fashion-mnist-vae\node_modules\bindings\bindings.js:84:48)
    at Object.factory (D:\ccc\test\tfjs-examples\fashion-mnist-vae\node_modules\@tensorflow\tfjs-node\dist\index.js:48:60)
    at Engine.initializeBackend (D:\ccc\test\tfjs-examples\fashion-mnist-vae\node_modules\@tensorflow\tfjs-core\dist\engine.js:238:48)
    at Engine.<anonymous> (D:\ccc\test\tfjs-examples\fashion-mnist-vae\node_modules\@tensorflow\tfjs-core\dist\engine.js:201:35)
Data File: dataset\train-images-idx3-ubyte does not exist.
      Please see the README for instructions on how to download it
error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
PS D:\ccc\test\tfjs-examples\fashion-mnist-vae>