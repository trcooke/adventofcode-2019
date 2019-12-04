const fs = require('fs');
const path = require('path');    
const inputPath = path.join(__dirname, 'input');

async function setup(){
    const input = fs.readFileSync(inputPath, 'utf8').split("\n")
    const wires = {"0": [], "1": []}
    input.forEach((line, index) => {
        wires[index] = line.split(",")
    })
    console.log(wires)
}

setup()