const neostandard = require('neostandard')
const globals = require('globals')

module.exports = [
  { ignores: ['static/**', '.venv/**'] },
  ...neostandard(),
  {
    languageOptions: {
      globals: globals.browser
    }
  }
]
