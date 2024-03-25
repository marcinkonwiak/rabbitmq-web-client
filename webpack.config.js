const path = require('path');

module.exports = {
    entry: './webpack/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'src', 'static', 'dist'),
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
        ],
    },
    mode: 'production',
};
