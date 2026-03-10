# Test

## frac 是什么 / What is frac?

**frac**（fractional part，小数部分函数）是一个数学函数，用于返回一个数的小数部分。

**frac** (fractional part function) is a mathematical function that returns the fractional (decimal) part of a number.

### 定义 / Definition

对于任意实数 `x`：

```
frac(x) = x - floor(x)
```

其中 `floor(x)` 是不大于 `x` 的最大整数（向下取整）。

For any real number `x`:

```
frac(x) = x - floor(x)
```

where `floor(x)` is the largest integer not greater than `x` (floor function).

### 示例 / Examples

| 输入 / Input | 输出 / Output |
|---|---|
| `frac(3.7)` | `0.7` |
| `frac(5.0)` | `0.0` |
| `frac(-1.3)` | `0.7` |
| `frac(0.5)` | `0.5` |

### 实现 / Implementation

```python
import math

def frac(x):
    """返回 x 的小数部分 / Returns the fractional part of x."""
    return x - math.floor(x)
```

### 用途 / Use Cases

- 周期性函数计算（如锯齿波）/ Periodic function computation (e.g., sawtooth waves)
- 着色器编程 / Shader programming
- 数论 / Number theory
- 动画与图形 / Animation and graphics