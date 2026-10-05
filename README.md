# 讲解员连续工作保护所在业务服务

这是一个使用 Python、FastAPI 与 SQLite 实现的后端项目。代码包含领域模型、数据访问、接口路由和业务规则，可在单个 Linux 应用容器内完成测试与运行。

## 安装

```bash
python3 -m pip install -r requirements.txt -r requirements-dev.txt
```

## 测试

标准回归：

```bash
python3 -m pytest -q
```

完整业务验证：

```bash
rm -f heritage_scheduling.db && python3 -m app.seed_data && python3 test_unit.py
```

`test_api.py` 与 `test_changes.py` 是服务启动后的人工 HTTP 验证脚本，不属于 pytest 自动发现范围。

## 编译检查

```bash
python3 -m compileall -q .
```

## 接口冒烟

```bash
python3 -c "from app.main import app; print(len(app.routes))"
```

## 启动

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
