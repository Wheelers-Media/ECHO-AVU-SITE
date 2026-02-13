/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./**/*.html",
        "./**/*.{js,ts,jsx,tsx}",
        "!./node_modules/**",
    ],
    theme: {
        extend: {
            colors: {
                void: '#000000',
                carbon: '#0A0A0A',
                edge: '#1F1F1F',
                echoRed: '#D60000',
                echoBlue: '#2563EB',
                textMain: '#FFFFFF',
                textBody: '#CCCCCC',
            },
            fontFamily: {
                heading: ['Manrope', 'sans-serif'],
                body: ['Inter', 'sans-serif'],
            }
        },
    },
    plugins: [],
}
