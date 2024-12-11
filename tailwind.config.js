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
        secondary: "#397FB0",
        white: "#FFFFFF",
        // F5EDED
        dark: "#1A1A1A",
        tertiary: "#1BCEDF",
      },
    },
  },
  plugins: [],
}

