"""项目基础运行边界的标准库回归测试。"""
import importlib
import unittest


class ProjectSmokeTest(unittest.TestCase):
    def test_application_exposes_http_routes(self):
        module = importlib.import_module("app.main")
        paths = {route.path for route in module.app.routes}
        self.assertTrue(paths)
        self.assertTrue(any(path in paths for path in ("/", "/health", "/api/health")) or len(paths) > 5)

    def test_persistence_uses_sqlite(self):
        module = importlib.import_module("app.database")
        self.assertTrue(str(module.engine.url).startswith("sqlite"))


if __name__ == "__main__":
    unittest.main()
