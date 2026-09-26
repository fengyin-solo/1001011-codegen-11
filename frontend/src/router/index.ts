import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const SampleReceive = () => import('@/views/sample_receive/index.vue')
const Pretreat = () => import('@/views/pretreat/index.vue')
const Instrument = () => import('@/views/instrument/index.vue')
const InstrumentMgmt = () => import('@/views/instrument_mgmt/index.vue')
const StdSolution = () => import('@/views/std_solution/index.vue')
const DataReview = () => import('@/views/data_review/index.vue')
const Report = () => import('@/views/report/index.vue')
const QcSample = () => import('@/views/qc_sample/index.vue')
const Calibration = () => import('@/views/calibration/index.vue')
const Reagent = () => import('@/views/reagent/index.vue')
const EnvMonitor = () => import('@/views/env_monitor/index.vue')
const SampleStore = () => import('@/views/sample_store/index.vue')
const Dispatch = () => import('@/views/dispatch/index.vue')
const Method = () => import('@/views/method/index.vue')
const BatchLog = () => import('@/views/batch_log/index.vue')
const Consumable = () => import('@/views/consumable/index.vue')
const LimitStandard = () => import('@/views/limit_standard/index.vue')
const Personnel = () => import('@/views/personnel/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/sample_receive', name: 'sample_receive', component: SampleReceive },
    { path: '/pretreat', name: 'pretreat', component: Pretreat },
    { path: '/instrument', name: 'instrument', component: Instrument },
    { path: '/instrument_mgmt', name: 'instrument_mgmt', component: InstrumentMgmt },
    { path: '/std_solution', name: 'std_solution', component: StdSolution },
    { path: '/data_review', name: 'data_review', component: DataReview },
    { path: '/report', name: 'report', component: Report },
    { path: '/qc_sample', name: 'qc_sample', component: QcSample },
    { path: '/calibration', name: 'calibration', component: Calibration },
    { path: '/reagent', name: 'reagent', component: Reagent },
    { path: '/env_monitor', name: 'env_monitor', component: EnvMonitor },
    { path: '/sample_store', name: 'sample_store', component: SampleStore },
    { path: '/dispatch', name: 'dispatch', component: Dispatch },
    { path: '/method', name: 'method', component: Method },
    { path: '/batch_log', name: 'batch_log', component: BatchLog },
    { path: '/consumable', name: 'consumable', component: Consumable },
    { path: '/limit_standard', name: 'limit_standard', component: LimitStandard },
    { path: '/personnel', name: 'personnel', component: Personnel },
  ],
})

export default router
