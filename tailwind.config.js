/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')

module.exports = {
  content: ['./src/**/*.{html,js}', './src/**/forms.py'],
  theme: {
    colors: {
      black: colors.stone,
      ...colors,
    },
    extend: {},
  },
  plugins: [],
}

