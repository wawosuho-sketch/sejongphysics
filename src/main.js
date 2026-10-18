import { mount } from 'svelte'
import './app.css'
import App from './App.svelte'

import { injectSpeedInsights } from '@vercel/speed-insights';
import { inject as injectAnalytics } from '@vercel/analytics';

injectSpeedInsights();
injectAnalytics();

import { registerSW } from 'virtual:pwa-register'

// onNeedRefresh를 비워 두면 autoUpdate가 멈춥니다. 새 배포는 다음 방문 때 스스로 적용됩니다.
registerSW({
  immediate: true,
  onOfflineReady() {
    console.log('App shell is ready to work offline')
  },
})

const app = mount(App, {
  target: document.getElementById('app'),
})

export default app
