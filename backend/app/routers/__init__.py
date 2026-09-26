"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import sample_receive as router_sample_receive
from app.routers import pretreat as router_pretreat
from app.routers import instrument as router_instrument
from app.routers import instrument_mgmt as router_instrument_mgmt
from app.routers import std_solution as router_std_solution
from app.routers import data_review as router_data_review
from app.routers import report as router_report
from app.routers import qc_sample as router_qc_sample
from app.routers import calibration as router_calibration
from app.routers import reagent as router_reagent
from app.routers import env_monitor as router_env_monitor
from app.routers import sample_store as router_sample_store
from app.routers import dispatch as router_dispatch
from app.routers import method as router_method
from app.routers import batch_log as router_batch_log
from app.routers import consumable as router_consumable
from app.routers import limit_standard as router_limit_standard
from app.routers import personnel as router_personnel

ROUTERS = [router_sample_receive, router_pretreat, router_instrument, router_instrument_mgmt, router_std_solution, router_data_review, router_report, router_qc_sample, router_calibration, router_reagent, router_env_monitor, router_sample_store, router_dispatch, router_method, router_batch_log, router_consumable, router_limit_standard, router_personnel]
