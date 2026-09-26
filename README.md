# 实验室样品检测流转管理平台

覆盖样品接收、前处理、仪器分析、数据审核、报告签发及质控管理的实验室全流程检测后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 样品接收 | `sample_receive` | 检测样品 | 样品编号、样品名称、样品类别 |
| 前处理 | `pretreat` | 前处理批次 | 批次编号、样品编号、处理方法 |
| 仪器分析 | `instrument` | 分析任务 | 任务编号、仪器编号、检测项目 |
| 仪器管理 | `instrument_mgmt` | 检测仪器 | 仪器编号、仪器名称、仪器型号 |
| 标准溶液 | `std_solution` | 标准溶液 | 溶液编号、溶液名称、浓度值 |
| 数据审核 | `data_review` | 审核记录 | 记录编号、检测项目、原始数据 |
| 报告签发 | `report` | 检测报告 | 报告编号、委托单位、样品信息 |
| 质控样品 | `qc_sample` | 质控样品 | 质控编号、质控类型、标准值 |
| 校准管理 | `calibration` | 校准记录 | 校准编号、仪器编号、校准项目 |
| 试剂管理 | `reagent` | 化学试剂 | 试剂编号、试剂名称、纯度等级 |
| 环境监控 | `env_monitor` | 环境记录 | 监测点位、温度、湿度 |
| 样品留存 | `sample_store` | 留存样品 | 留存编号、样品编号、留存方式 |
| 任务调度 | `dispatch` | 检测任务 | 任务编号、样品编号、检测项目 |
| 方法管理 | `method` | 检测方法 | 方法编号、方法名称、方法来源 |
| 批次日志 | `batch_log` | 批次日志 | 日志编号、批次编号、操作环节 |
| 耗材管理 | `consumable` | 实验耗材 | 耗材编号、耗材名称、耗材类别 |
| 限量标准 | `limit_standard` | 限量标准 | 标准编号、标准名称、适用品类 |
| 人员管理 | `personnel` | 检测人员 | 人员编号、姓名、岗位 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
