# Test

## frac 是什么？

`frac`（fractional part，小数部分函数）是一个数学函数，用于取一个实数的小数部分。

### 定义

对于任意实数 `x`：

```
frac(x) = x - floor(x)
```

其中 `floor(x)` 是不超过 `x` 的最大整数（即向下取整）。

### 示例

| 输入 `x` | `frac(x)` |
|---------|-----------|
| 3.7     | 0.7       |
| -1.3    | 0.7       |
| 5.0     | 0.0       |
| 0.5     | 0.5       |

### Python 实现

```python
import math

def frac(x):
    """返回 x 的小数部分（fractional part）。"""
    return x - math.floor(x)

# 示例
print(frac(3.7))   # 0.7
print(frac(-1.3))  # 0.7
print(frac(5.0))   # 0.0
print(frac(0.5))   # 0.5
```

### 注意事项

- `frac(x)` 的结果始终满足 `0 ≤ frac(x) < 1`。
- 对于负数，`frac(-1.3) = 0.7`（而非 `-0.3`），因为使用的是向下取整。
- 在 LaTeX 中，`\frac{a}{b}` 表示分数 a/b，与此处的小数部分函数含义不同。