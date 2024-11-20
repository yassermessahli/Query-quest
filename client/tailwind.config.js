/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",  // Make sure to scan all .js and .jsx files in src
  ],
  theme: {
    extend: {
      purple: { 500: '#a855f7', 600: '#9333ea', 700: '#7e22ce', },
            fontFamily: {
        consolas: ['Consolas', 'monospace'], 
      },
    },
  },
  plugins: [],
}
