import { Click } from './models/click.js';
import { Move } from './models/move.js';

const socket = new WebSocket('ws://192.168.0.104:2345');
const SEND_INTERVAL = 15;

var move = document.getElementById("touchpad");
let lastClick = null;
let lastMove = null;

move.addEventListener('touchmove', handleTouchMove, false);
move.addEventListener('click', handleClick, false);

function handleTouchMove(event) {
    let _obj = new Move(event.touches[0].clientX, event.touches[0].clientY);

    let intervalTime = Date.now() - lastMove;

    if (socket.readyState === WebSocket.OPEN && intervalTime > SEND_INTERVAL) {
        socket.send(JSON.stringify(_obj));
        lastMove = Date.now()
    }
}

function handleClick(event) {
    let _obj = new Click(event.clientX, event.clientY)

    let intervalTime = Date.now() - lastClick;

    if (socket.readyState === WebSocket.OPEN && intervalTime > SEND_INTERVAL) {
        socket.send(JSON.stringify(_obj));
        lastClick = Date.now();
    }
}
