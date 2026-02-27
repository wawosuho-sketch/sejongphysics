import { mount } from 'svelte'
import './app.css'
import App from './App.svelte'

import { registerSW } from 'virtual:pwa-register'

const updateSW = registerSW({
  onNeedRefresh() {
    // Optionally show a prompt to user to update
  },
  onOfflineReady() {
    console.log('App is ready to work offline')
  },
})

const app = mount(App, {
  target: document.getElementById('app'),
})

export default app
