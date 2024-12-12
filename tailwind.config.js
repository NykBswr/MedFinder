/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        primary: "#5B247A",
        secondary: "#3A7DAF",
        tertiary: "#1BCEDF",
        white: "#FFFFFF",
        dark: "#1A1A1A",
      },
    },
  },
  plugins: [],
}

