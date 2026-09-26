<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">实验室样品检测流转管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">覆盖样品接收、前处理、仪器分析、数据审核、报告签发及质控管理的实验室全流程检测后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "样品接收", path: "/sample_receive" }, { label: "前处理", path: "/pretreat" }, { label: "仪器分析", path: "/instrument" }, { label: "仪器管理", path: "/instrument_mgmt" }, { label: "标准溶液", path: "/std_solution" }, { label: "数据审核", path: "/data_review" }, { label: "报告签发", path: "/report" }, { label: "质控样品", path: "/qc_sample" }, { label: "校准管理", path: "/calibration" }, { label: "试剂管理", path: "/reagent" }, { label: "环境监控", path: "/env_monitor" }, { label: "样品留存", path: "/sample_store" }, { label: "任务调度", path: "/dispatch" }, { label: "方法管理", path: "/method" }, { label: "批次日志", path: "/batch_log" }, { label: "耗材管理", path: "/consumable" }, { label: "限量标准", path: "/limit_standard" }, { label: "人员管理", path: "/personnel" }]
</script>
