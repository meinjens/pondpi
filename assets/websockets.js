const socket = new WebSocket('ws://localhost:5000/ws/status')

socket.onopen = function (e) {
  console.log('[ws] Connection established.')
  socket.send('Start')
}

socket.onmessage = function (event) {
  console.log('[ws] Message received:')
  console.log(event)
}

socket.onclose = function (event) {
  if (event.wasClean) {
    console.log(`[ws] Connection closed cleanly, code=${event.code} reason=${event.reason}`)
    console.log(event)
  } else {
    // e.g. server process killed or network down
    // event.code is usually 1006 in this case
    console.log('[ws] Connection died')
  }
}

socket.onerror = function (error) {
  console.log(`[ws] ${error.message}`)
}
