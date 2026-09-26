"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class SampleReceiveEntry(BaseModel):
    """检测样品明细结构。"""

    field_0: str | None = None  # 样品编号
    field_1: str | None = None  # 样品名称
    field_2: str | None = None  # 样品类别
    field_3: str | None = None  # 委托单位
    field_4: str | None = None  # 送样人
    field_5: str | None = None  # 接收日期
    field_6: str | None = None  # 保存条件
    field_7: str | None = None  # 样品状态

class PretreatEntry(BaseModel):
    """前处理批次明细结构。"""

    field_0: str | None = None  # 批次编号
    field_1: str | None = None  # 样品编号
    field_2: str | None = None  # 处理方法
    field_3: str | None = None  # 处理温度
    field_4: str | None = None  # 处理时长
    field_5: str | None = None  # 试剂用量
    field_6: str | None = None  # 操作人员
    field_7: str | None = None  # 批次状态

class InstrumentEntry(BaseModel):
    """分析任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 仪器编号
    field_2: str | None = None  # 检测项目
    field_3: str | None = None  # 样品编号
    field_4: str | None = None  # 分析方法
    field_5: str | None = None  # 分析人员
    field_6: str | None = None  # 预计时长
    field_7: str | None = None  # 任务状态

class InstrumentMgmtEntry(BaseModel):
    """检测仪器明细结构。"""

    field_0: str | None = None  # 仪器编号
    field_1: str | None = None  # 仪器名称
    field_2: str | None = None  # 仪器型号
    field_3: str | None = None  # 所属实验室
    field_4: str | None = None  # 检定日期
    field_5: str | None = None  # 有效期至
    field_6: str | None = None  # 当前状态
    field_7: str | None = None  # 维护周期

class StdSolutionEntry(BaseModel):
    """标准溶液明细结构。"""

    field_0: str | None = None  # 溶液编号
    field_1: str | None = None  # 溶液名称
    field_2: str | None = None  # 浓度值
    field_3: str | None = None  # 不确定度
    field_4: str | None = None  # 配制日期
    field_5: str | None = None  # 有效期至
    field_6: str | None = None  # 保存条件
    field_7: str | None = None  # 溶液状态

class DataReviewEntry(BaseModel):
    """审核记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 检测项目
    field_2: str | None = None  # 原始数据
    field_3: str | None = None  # 分析结果
    field_4: str | None = None  # 质控结果
    field_5: str | None = None  # 审核人
    field_6: str | None = None  # 审核日期
    field_7: str | None = None  # 审核状态

class ReportEntry(BaseModel):
    """检测报告明细结构。"""

    field_0: str | None = None  # 报告编号
    field_1: str | None = None  # 委托单位
    field_2: str | None = None  # 样品信息
    field_3: str | None = None  # 检测项目
    field_4: str | None = None  # 检测结论
    field_5: str | None = None  # 签发人
    field_6: str | None = None  # 签发日期
    field_7: str | None = None  # 报告状态

class QcSampleEntry(BaseModel):
    """质控样品明细结构。"""

    field_0: str | None = None  # 质控编号
    field_1: str | None = None  # 质控类型
    field_2: str | None = None  # 标准值
    field_3: str | None = None  # 允许偏差
    field_4: str | None = None  # 有效期至
    field_5: str | None = None  # 保存条件
    field_6: str | None = None  # 使用次数
    field_7: str | None = None  # 质控状态

class CalibrationEntry(BaseModel):
    """校准记录明细结构。"""

    field_0: str | None = None  # 校准编号
    field_1: str | None = None  # 仪器编号
    field_2: str | None = None  # 校准项目
    field_3: str | None = None  # 校准结果
    field_4: str | None = None  # 允许误差
    field_5: str | None = None  # 校准人员
    field_6: str | None = None  # 校准日期
    field_7: str | None = None  # 校准状态

class ReagentEntry(BaseModel):
    """化学试剂明细结构。"""

    field_0: str | None = None  # 试剂编号
    field_1: str | None = None  # 试剂名称
    field_2: str | None = None  # 纯度等级
    field_3: str | None = None  # 包装规格
    field_4: str | None = None  # 供应商
    field_5: str | None = None  # 有效期至
    field_6: str | None = None  # 存放位置
    field_7: str | None = None  # 试剂状态

class EnvMonitorEntry(BaseModel):
    """环境记录明细结构。"""

    field_0: str | None = None  # 监测点位
    field_1: str | None = None  # 温度
    field_2: str | None = None  # 湿度
    field_3: str | None = None  # 压差
    field_4: str | None = None  # 尘埃粒子
    field_5: str | None = None  # 监测时间
    field_6: str | None = None  # 记录人员
    field_7: str | None = None  # 监测状态

class SampleStoreEntry(BaseModel):
    """留存样品明细结构。"""

    field_0: str | None = None  # 留存编号
    field_1: str | None = None  # 样品编号
    field_2: str | None = None  # 留存方式
    field_3: str | None = None  # 留存位置
    field_4: str | None = None  # 留存日期
    field_5: str | None = None  # 到期日期
    field_6: str | None = None  # 处置方式
    field_7: str | None = None  # 留存状态

class DispatchEntry(BaseModel):
    """检测任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 样品编号
    field_2: str | None = None  # 检测项目
    field_3: str | None = None  # 检测标准
    field_4: str | None = None  # 要求完成日
    field_5: str | None = None  # 执行科室
    field_6: str | None = None  # 优先级
    field_7: str | None = None  # 任务状态

class MethodEntry(BaseModel):
    """检测方法明细结构。"""

    field_0: str | None = None  # 方法编号
    field_1: str | None = None  # 方法名称
    field_2: str | None = None  # 方法来源
    field_3: str | None = None  # 适用范围
    field_4: str | None = None  # 检出限
    field_5: str | None = None  # 定量限
    field_6: str | None = None  # 版本号
    field_7: str | None = None  # 方法状态

class BatchLogEntry(BaseModel):
    """批次日志明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 批次编号
    field_2: str | None = None  # 操作环节
    field_3: str | None = None  # 操作人员
    field_4: str | None = None  # 操作时间
    field_5: str | None = None  # 异常记录
    field_6: str | None = None  # 处理措施
    field_7: str | None = None  # 日志状态

class ConsumableEntry(BaseModel):
    """实验耗材明细结构。"""

    field_0: str | None = None  # 耗材编号
    field_1: str | None = None  # 耗材名称
    field_2: str | None = None  # 耗材类别
    field_3: str | None = None  # 规格
    field_4: str | None = None  # 供应商
    field_5: str | None = None  # 有效期至
    field_6: str | None = None  # 存放位置
    field_7: str | None = None  # 耗材状态

class LimitStandardEntry(BaseModel):
    """限量标准明细结构。"""

    field_0: str | None = None  # 标准编号
    field_1: str | None = None  # 标准名称
    field_2: str | None = None  # 适用品类
    field_3: str | None = None  # 检测项目
    field_4: str | None = None  # 限量值
    field_5: str | None = None  # 标准来源
    field_6: str | None = None  # 生效日期
    field_7: str | None = None  # 标准状态

class PersonnelEntry(BaseModel):
    """检测人员明细结构。"""

    field_0: str | None = None  # 人员编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 岗位
    field_3: str | None = None  # 资质证书
    field_4: str | None = None  # 授权项目
    field_5: str | None = None  # 所属科室
    field_6: str | None = None  # 在岗状态
    field_7: str | None = None  # 培训记录
