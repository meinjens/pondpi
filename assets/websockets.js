let socket = new WebSocket('ws://localhost:5000/ws/echo');

socket.onopen = function(e) {
  socket.send('My name is John');
  console.log('[connect] Connection established.');
};

socket.onmessage = function(event) {
  console.log(event);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    console.log(event);
    console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    // e.g. server process killed or network down
    // event.code is usually 1006 in this case
    console.log('[close] Connection died');
  }
};

socket.onerror = function(error) {
    console.log(`[error] ${error.message}`);
};