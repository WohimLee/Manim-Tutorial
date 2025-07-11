# VGroup.arrange

用来对一组子对象（比如 Tex 中的多行）进行排列

>语法
```py
group.arrange(direction=..., aligned_edge=..., buff=...)
```

- `direction`:	子对象排列方向（比如 DOWN, UP, RIGHT, etc）
- `aligned_edge`:	哪个边对齐，例如 LEFT, RIGHT, ORIGIN（中心）
- `buff`:	子对象之间的间隔（默认为 DEFAULT_MOBJECT_TO_MOBJECT_BUFFER = 0.25）
