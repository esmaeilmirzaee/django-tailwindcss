/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')

module.exports = {
  content: ['./src/**/*.{html,js}'],
  theme: {
    colors: {
      black: colors.stone,
      ...colors,
    },
    extend: {},
  },
  plugins: [],
}

