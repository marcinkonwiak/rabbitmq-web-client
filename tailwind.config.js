/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "./src/templates/**/*.html"
  ],
  theme: {
    extend: {
      height: {
        '15-8rem': '15.8rem',
      }
    },
    colors: {
      "dark": {
        300: "#262534",
        400: "#212030",
        500: "#1B1A27",
      },
      "light": {
        300: "#F5F4FF",
        400: "#CFCEDD",
        500: "#8F8EA6",
        600: "#3D3C4B",
      },
      "accent": {
        500: "#5D3AC1"
      }
    }
  },
  plugins: [],
}
