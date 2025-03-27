# 说明

checkpoint-0-0-0.lst
cluster-0-0.json
这两个是spec06 切片默认文件，前者表示所有切片的位置，后者表示每个子切片占据原本程序的权重（有simpoint 程序生成）
参考h[ttps://github.com/OpenXiangShan/GEM5/README](https://github.com/OpenXiangShan/GEM5/blob/xs-dev/README.md)

把所有切片跑完就是1 coverage，为了运行更快，我们会只跑部分切片，按照切片权重排序，例如选一半切片但切片权重占整体权重80%就是0.8c 

本脚本
gen_coverage.py
gen_lst.py
通过指定不同参数来生成不同权重的切片，用于加速GEM5 程序运行
例如一般可以选择0.8 coverage 的切片（切片数量只占据1.0 coverage 的一半），但可以得到90%准确的性能。
GEM5 CI 默认运行0.8c spec int 的切片，分数会比1.0c 的切片运行结果高0.2 分左右；
XiangShan RTL 也可以用于生成0.3 coverage 的切片


本仓库可以结合https://github.com/shinezyy/gem5_data_proc  一同用于GEM5/Xiangshan 算分


## 使用方法

```
# 输入： cluster-0-0.json, 指定0.8 coverage, -t int 可以指定只生产int
# 输出: 不同coverage的json 文件
python3 gen_coverage.py -j cluster-0-0.json -c 0.8 -o spec06_0.8c_int.json -t int

# 输入: 上一步得到的json, 整体的lst文件
# 输出: 指定覆盖率的lst
python3 gen_lst.py -l checkpoint-0-0-0.lst -j spec06_0.8c_int.json -o spec_0.8c_int.lst
```

GEM5 parallel 脚本就可以使用了
