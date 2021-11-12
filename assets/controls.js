/* eslint-disable no-undef */

import nipplejs from 'nipplejs'

let steeringEngineLeft = null
let steeringEngineRight = null

jquery(document).ready(function () {
  jquery('.gas').knob()

  steeringEngineLeft = new WebSocket('ws://localhost:5000/ws/steering/left')
  steeringEngineRight = new WebSocket('ws://localhost:5000/ws/steering/right')

  steeringEngineLeft.onopen = function() {
    console.log('[left] connection to engine')
  }
  steeringEngineLeft.onclose = function (event) {
    if (event.wasClean) {
      console.log(`[left] Connection closed cleanly, code=${event.code} reason=${event.reason}`)
      console.log(event)
    } else {
      console.log('[left] Connection died')
    }
  }
  steeringEngineRight.onopen = function () {
    console.log('[right] connection to engine')
  }
  steeringEngineRight.onclose = function (event) {
    if (event.wasClean) {
      console.log(`[right] Connection closed cleanly, code=${event.code} reason=${event.reason}`)
      console.log(event)
    } else {
      console.log('[right] Connection died')
    }
  }

  const steeringLeft = nipplejs.create({
    zone: document.getElementById('engine_left'),
    mode: 'static',
    position: { left: '50%', top: '50%' },
    fadeTime: 500,
    color: 'blue',
    size: 200,
    lockY: true
  })

  steeringLeft
    .on('start', function (event, data) {
      console.log('start engine left')
    })
    .on('move', function (event, data) {
      if (data.direction) {
        console.log('move left: ' + data.direction.y + ' ' + data.distance)
        const steering = {
          dir: data.direction.y,
          dist: data.distance
        }
        steeringEngineLeft.send(JSON.stringify(steering))
      }
    })
    .on('end', function (event, data) {
      const steering = {
        dir: 'center',
        dist: 0
      }
      steeringEngineLeft.send(JSON.stringify(steering))
    })

  const steeringRight = nipplejs.create({
    zone: document.getElementById('engine_right'),
    mode: 'static',
    position: { left: '50%', top: '50%' },
    fadeTime: 500,
    color: 'red',
    size: 200,
    lockY: true
  })

  steeringRight
    .on('start', function (event, data) {
      console.log('start engine right')
    })
    .on('move', function (event, data) {
      if (data.direction) {
        console.log('move left: ' + data.direction.y + ' ' + data.distance)
        const steering = {
          dir: data.direction.y,
          dist: data.distance
        }
        steeringEngineRight.send(JSON.stringify(steering))
      }
    })
    .on('end', function (event, data) {
      console.log('stop engine right')
      const steering = {
        dir: 'center',
        dist: 0
      }
      steeringEngineRight.send(JSON.stringify(steering))
    })
})
