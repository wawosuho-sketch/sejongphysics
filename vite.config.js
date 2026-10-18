import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import { VitePWA } from 'vite-plugin-pwa'

// https://vite.dev/config/
export default defineConfig({
  base: '/', // <--- 이 부분을 단순하게 수정했습니다.
  plugins: [
    svelte(),
    VitePWA({
      registerType: 'autoUpdate',
      // 등록은 src/main.js 한 곳에서만 합니다. auto 주입과 겹치면 갱신이 두 번 걸립니다.
      injectRegister: null,
      workbox: {
        // 슬라이드 수백 장은 사전 캐시에 넣지 않습니다. 첫 방문이 학교 와이파이에서 수백 MB를 받지 않게 합니다.
        navigateFallbackDenylist: [/^\/resources/, /\.[a-zA-Z0-9]+$/],
        runtimeCaching: [
          {
            urlPattern: ({ request, sameOrigin }) =>
              sameOrigin && request.destination === 'image',
            handler: 'StaleWhileRevalidate',
            options: {
              cacheName: 'textbook-images',
              expiration: {
                maxEntries: 300,
                maxAgeSeconds: 60 * 60 * 24 * 30,
                purgeOnQuotaError: true,
              },
              cacheableResponse: {
                statuses: [0, 200],
              },
            },
          },
          {
            urlPattern: ({ url, sameOrigin }) =>
              sameOrigin &&
              url.pathname.startsWith('/resources/') &&
              url.pathname.toLowerCase().endsWith('.pdf'),
            handler: 'NetworkFirst',
            options: {
              cacheName: 'textbook-pdfs',
              networkTimeoutSeconds: 4,
              expiration: {
                maxEntries: 20,
                maxAgeSeconds: 60 * 60 * 24 * 30,
                purgeOnQuotaError: true,
              },
              cacheableResponse: {
                statuses: [0, 200],
              },
            },
          },
        ],
      },
      manifest: {
        name: '세종고 물리 교과서',
        short_name: '물리 교과서',
        description: '세종고등학교 물리 1 스마트 교과서',
        theme_color: '#0b0f19',
        background_color: '#05070a',
        display: 'standalone',
        icons: [
          {
            src: '/pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: '/pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      }
    })
  ],
})
