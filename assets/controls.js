import nipplejs from 'nipplejs';

let steering_engine_left = null;
let steering_engine_right = null;

jquery(document).ready(function() {
    jquery(".gas").knob();

    steering_engine_left = new WebSocket('ws://localhost:5000/ws/steering/left');
    steering_engine_right = new WebSocket('ws://localhost:5000/ws/steering/right');

    steering_engine_left.onopen = function() {
        console.log('[left] connection to engine');
    }
    steering_engine_left.onclose = function(event) {
        if (event.wasClean) {
            console.log(`[left] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
            console.log(event);
        } else {
            console.log('[left] Connection died');
        }
    }
    steering_engine_right.onopen = function() {
        console.log('[right] connection to engine');
    }
    steering_engine_right.onclose = function(event) {
        if (event.wasClean) {
            console.log(`[right] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
            console.log(event);
        } else {
            console.log('[right] Connection died');
        }
    }

    const steering_left = nipplejs.create({
        zone: document.getElementById('engine_left'),
        mode: 'static',
        position: {left: '50%', top: '50%'},
        fadeTime: 500,
        color: 'blue',
        size: 200,
        lockY: true,
    });

    steering_left
        .on('start', function(event, data) {
            console.log('start engine left');
        })
        .on('move', function(event, data){
            if (data.direction) {
                console.log('move left: ' + data.direction.y + ' ' + data.distance);
                const steering = {
                    'dir': data.direction.y,
                    'dist': data.distance
                };
                steering_engine_left.send(JSON.stringify(steering));
            }
            
        })
        .on('end', function(event, data) {
            const steering = {
                'dir': 'center',
                'dist': 0
            };
            steering_engine_left.send(JSON.stringify(steering));
        })

    const steering_right = nipplejs.create({
        zone: document.getElementById('engine_right'),
        mode: 'static',
        position: {left: '50%', top: '50%'},
        fadeTime: 500,
        color: 'red',
        size: 200,
        lockY: true,
    });

    steering_right
        .on('start', function(event, data) {
            console.log('start engine right');
        })
        .on('move', function(event, data){
            if (data.direction) {
                console.log('move left: ' + data.direction.y + ' ' + data.distance);
                const steering = {
                    'dir': data.direction.y,
                    'dist': data.distance
                };
                steering_engine_right.send(JSON.stringify(steering));
            }
        })
        .on('end', function(event, data) {
            console.log('stop engine right');
            const steering = {
                'dir': 'center',
                'dist': 0
            };
            steering_engine_right.send(JSON.stringify(steering));
        })

});
