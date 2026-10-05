"""自动化回归测试的确定性数据库基线。"""

import pytest

from app.database import Base, engine
from app.seed_data import seed_database


@pytest.fixture(scope="session", autouse=True)
def seeded_database():
    Base.metadata.drop_all(bind=engine)
    seed_database()
    yield
