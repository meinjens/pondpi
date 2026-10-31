const neostandard = require('neostandard')
const globals = require('globals')

module.exports = [
  ...neostandard({ ignores: ['static/**', 'node_modules/**'] }),
  {
    languageOptions: {
      globals: globals.browser
    }
  }
]
