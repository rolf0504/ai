# OpenCV 影像處理

* https://github.com/justadudewhohacks/opencv4nodejs

先安裝 windows-build-tools

npm install --global windows-build-tools // 失敗

改用以下安裝法就會成功了 https://github.com/felixrieseberg/windows-build-tools/issues/152

npm install --global --production windows-build-tools@4.0.0 // 成功

```
PS D:\ccc\course\ai\js\08-scientific> npm install --global --production windows-build-tools@4.0.0
npm WARN npm npm does not support Node.js v10.16.0
npm WARN npm You should probably upgrade to a newer version of node as we
npm WARN npm can't make any promises that npm will work with this version.
npm WARN npm Supported releases of Node.js are the latest release of 4, 6, 7, 8, 9.
npm WARN npm You can find the latest version at https://nodejs.org/
npm WARN registry Using stale data from https://registry.npmjs.org/ because the host is inaccessible -- are you offline?
npm WARN registry Using stale package data from https://registry.npmjs.org/ due to a request error during revalidation.

> windows-build-tools@4.0.0 postinstall C:\Users\user\AppData\Roaming\npm\node_modules\windows-build-tools
> node ./dist/index.js



Downloading python-2.7.14.amd64.msi
[============================================>] 100.0% of 20.17 MB (1.05 MB/s)
Downloaded python-2.7.14.amd64.msi. Saved to C:\Users\user\.windows-build-tools\python-2.7.14.amd64.msi.
Downloading BuildTools_Full.exe
[>                                            ] 0.0% (0 B/s)
Downloaded BuildTools_Full.exe. Saved to C:\Users\user\.windows-build-tools\BuildTools_Full.exe.

Starting installation...
Launched installers, now waiting for them to finish.
This will likely take some time - please be patient!

Status from the installers:
---------- Visual Studio Build Tools ----------
---------- Visual Studio Build Tools -------------------- Visual Studio Build Tools -------------------- Visual Studio Build Tools ----------Successfully installed Visual Studio Build Tools.------------------- Python --------------------Successfully installed Python 2.7Now configuring the Visual Studio Build Tools and Python...All done!+ windows-build-tools@4.0.0removed 1 package and updated 7 packages in 860.403s
```

然後安裝

npm install --save opencv4nodejs


choco install OpenCV -y -version 4.1.0