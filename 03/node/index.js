const fs = require('fs');
const path = require('path');    
const inputPath = path.join(__dirname, 'input');

async function setup(){
    const input = fs.readFileSync(inputPath, 'utf8').split("\n")
    const wires = {"0": [], "1": []}
    input.forEach((line, index) => {
        wires[index] = line.split(",")
    })
    const wirePathA = computePath(wires["0"])
    const wirePathB = computePath(wires["1"])
    const crossOverPoints = getCrossOverPoints(wirePathA, wirePathB)
    console.log(findMinDistance(crossOverPoints));
}
function computePath(path){
    const points = new Set();
    let x = 0;
    let y = 0;    
    path.forEach(movement => {
        let direction = movement.substring(0,1);
        let spaces = parseInt(movement.substring(1, movement.length));   
        for ( let i = 0; i < spaces; i++ ) {
            switch (direction) {
                case 'U': y--; break;
                case 'D': y++; break;
                case 'L': x--; break;
                case 'R': x++; break;
            }   
            if ( !points.has(`${x},${y}`) ) {
                points.add(`${x},${y}`);
            }
        }
    })
    return points
}

function getCrossOverPoints(wirePathA, wirePathB) {
    const crossOverPoints = [];
    wirePathA.forEach( (_, key) => {
        if ( wirePathB.has(key) ) { 
            crossOverPoints.push(key) 
        }
    })
    return crossOverPoints;
}

function findMinDistance(crossOverPoints) {
    let minDistance = findDistanceToStart(crossOverPoints[0].split(","));
    crossOverPoints.forEach(intersection => {
        const currentDistance = findDistanceToStart(intersection.split(","));
        if ( currentDistance < minDistance ) {
            minDistance = currentDistance;
        }
    });
    return minDistance;
}

function findDistanceToStart([x, y]) {
    // @see: https://stackoverflow.com/questions/8224470/calculating-manhattan-distance
    return Math.abs(Number(x)) + Math.abs(Number(y));
}
setup()