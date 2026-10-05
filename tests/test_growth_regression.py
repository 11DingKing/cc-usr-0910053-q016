"""讲解员成长与激励体系的核心业务回归。"""

from test_growth_system import (
    test_add_points_and_level_up,
    test_level_badge_config,
    test_monthly_ranking,
    test_point_calculation,
    test_point_records,
    test_recommendation_with_excellent,
    test_review_auto_points,
    test_staff_badges,
    test_staff_fields,
    test_statistics,
)


__all__ = [name for name in globals() if name.startswith("test_")]
