import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
    build: {
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'index.html'),
                about: resolve(__dirname, 'about.html'),
                brands: resolve(__dirname, 'brands.html'),
                'car-audio': resolve(__dirname, 'car-audio.html'),
                'car-starters': resolve(__dirname, 'car-starters.html'),
                contact: resolve(__dirname, 'contact.html'),
                'dream-home': resolve(__dirname, 'dream-home.html'),
                'example-template': resolve(__dirname, 'EXAMPLE-TEMPLATE.html'),
                financing: resolve(__dirname, 'financing.html'),
                'home-audio': resolve(__dirname, 'home-audio.html'),
                'marine-audio': resolve(__dirname, 'marine-audio.html'),
                'privacy-statement': resolve(__dirname, 'privacy-statement.html'),
                'protection-plan': resolve(__dirname, 'protection-plan.html'),
                'return-policy': resolve(__dirname, 'return-policy.html'),
                services: resolve(__dirname, 'services.html'),
                'services-car-audio': resolve(__dirname, 'services-car-audio.html'),
                'services-car-starters': resolve(__dirname, 'services-car-starters.html'),
                'services-marine': resolve(__dirname, 'services-marine.html'),
                'services-office': resolve(__dirname, 'services-office.html'),
                'services-residential': resolve(__dirname, 'services-residential.html'),
                'services-retail': resolve(__dirname, 'services-retail.html'),
                'services-surveillance': resolve(__dirname, 'services-surveillance.html'),
                surveillance: resolve(__dirname, 'surveillance.html'),
                team: resolve(__dirname, 'team.html'),
                'tv-video': resolve(__dirname, 'tv-video.html'),
            },
        },
    },
})
