const path = require('path')
const webpack = require('webpack')
const css = require('mini-css-extract-plugin')

module.exports = {
  mode: 'development',
  entry: {
    app: './assets/app.js',
    vendor: './assets/vendor.js'
  },
  output: {
    path: path.resolve(__dirname, 'static/'),
    filename: '[name].js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: ['babel-loader']
      },
      {
        test: /\.scss$/,
        use: [css.loader, 'css-loader', 'sass-loader']
      },
      {
        test: /\.less$/,
        use: [css.loader, 'css-loader', 'less-loader']
      },
      {
        test: /\.css$/,
        use: [css.loader, 'css-loader']
      },
      {
        test: /\.woff($|\?)|\.woff2($|\?)|\.ttf($|\?)|\.eot($|\?)|\.svg($|\?)/,
        use: ['url-loader']
      },
      {
        test: require.resolve('jquery'),
        loader: 'expose-loader',
        options: {
          exposes: ['$', 'jquery', 'jQuery']
        }
      }
    ]
  },
  plugins: [
    new css({
      filename: '[name].css',
      chunkFilename: '[id].css'
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery'
    })
  ]
}
