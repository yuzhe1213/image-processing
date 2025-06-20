:: 建立訓練樣本 .vec（從 positives.txt）
opencv_createsamples.exe -info positives.txt -num 200 -w 50 -h 50 -vec positives.vec

:: 執行 Haar cascade 訓練
opencv_traincascade.exe -data classifier -vec positives.vec -bg bg.txt -numPos 180 -numNeg 100 -numStages 10 -w 50 -h 50 -featureType HAAR

pause
