// vue.config.js

module.exports = {
  pluginOptions: {
    ssr: {
      // port: null,
      // host: null,
      // // Specify public file paths to disable resource prefetch hints for
      // shouldNotPrefetch: [],
      // // Specify public file paths to disable resource preload hints for
      // shouldNotPreload: [],
      // // Entry for each target
      // entry: target => `./src/entry-${target}`,
      // // Default title
      defaultTitle: 'SFT SPACE',
      // // Path to favicon
      // favicon: './public/favicon.ico',
      // // Enable Critical CSS
      criticalCSS: true,
      // // Skip some requests from being server-side rendered
      // skipRequests: req => req.originalUrl === '/graphql',

      nodeExternalsWhitelist: [/\.css$/, /vuetify/,/vue-slick/],
      // // Enable node cluster for the production server
      // clustered: false,
      // // Static files Cache-Control maxAge value
      // staticCacheTtl: 1000 * 60 * 60 * 24 * 30,
      // // Directives fallback
      // directives: {
      //   // See 'Directive' chapter
      // },
      // lruCacheOptions: {
      //   // See https://ssr.vuejs.org/guide/caching.html
      // },
      // // apply default middleware like compression, serving static files
      // applyDefaultServer: true,
      // // Function to extend app context object
      // extendContext: (req, res, process) => ({ appMode: process.env.APP_MODE }),
      // // Function to connect custom middlewares
      // extendServer: app => {
      //   const cookieParser = require('cookie-parser')
      //   app.use(cookieParser())
      // },
      // // Copy URL to system clipboard on start
      // copyUrlOnStart: true,
      // // Function to call after rendering has been completed
      // onRender: (res, context) => {
      //   res.setHeader(`Cache-Control', 'public, max-age=${context.maxAge}`)
      // },
      // onError: error => {
      //   // Send to error monitoring service
      // },
      // // Paths
      // distPath: path.resolve(__dirname, './dist'),
      // error500Html: path.resolve(__dirname, './dist/500.html'),
      // templatePath: path.resolve(__dirname, './dist/index.ssr.html'),
      // serviceWorkerPath: path.resolve(__dirname, './dist/service-worker.js'),
    }
  },
  css: {
    sourceMap: process.env.NODE_ENV !== 'production'
  },
  devServer: {
    proxy: {
      '^/api': {
        target: '',
        changeOrigin: true,
        secure: false
      }
    },
  }
}
