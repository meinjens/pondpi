import nipplejs from 'nipplejs';

jquery(document).ready(function() {
    jquery(".gas").knob();

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
            }
            
        })
        .on('end', function(event, data) {
            console.log('stop engine left');
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
            }
        })
        .on('end', function(event, data) {
            console.log('stop engine right');
        })

});
