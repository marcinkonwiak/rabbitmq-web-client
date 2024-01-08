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
                200: "#292836",
                300: "#262534",
                400: "#212030",
                450: "#1E1D2C",
                500: "#1B1A27",
            },
            "light": {
                300: "#F5F4FF",
                400: "#CFCEDD",
                500: "#8F8EA6",
                600: "#666579",
                700: "#525162",
                800: "#3D3C4B",
            },
            "accent": {
                100: "#B7ADCF",
                500: "#5D3AC1",
            },
            "success2": {
                500: "#BCEBCB",
            },
            "success": {
                300: "#A1CCA5",
                400: "#8FB996",
                500: "#709775",
            },
            "error": {
                300: "#E16E69",
                400: "#DE605A",
                500: "#DB504A",
            },
        }
    },
    plugins: [],
}
