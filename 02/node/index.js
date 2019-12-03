const fs = require('fs');
const path = require('path');    
const inputPath = path.join(__dirname, 'input');

function part1(array, startValues = [12, 2]){
    const lookup = {};
    [array[0], ...startValues, ...array.slice(3)].forEach((value, position) => {
        lookup[position] = {
            value,
            isOpcode: [1,2,99].includes(value) && position % 4 === 0,
            operation: getOperation(value)
        }
    })
    for (const [pos, value] of Object.entries(lookup)) {
        if(value.isOpcode){
            const sum = value.operation(lookup[lookup[placesFromPosition(pos,1)].value], lookup[lookup[placesFromPosition(pos,2)].value])
            if(typeof sum === "undefined"){
                break
            }
            lookup[lookup[placesFromPosition(pos,3)].value].value = sum;
        }
    }
    return Object.values(lookup).map(({value})=> value)[0]
}

function part2(){

}

function placesFromPosition(pos, additional){
    return String(Number(pos) + additional)
}

function getOperation(value){
    const lookup = {1: function add(x,y){ return x.value + y.value }, 2: function multiply(x, y){ return x.value * y.value}, 99: function end(){
        return
    }}
    return Object.keys(lookup).includes(String(value)) ? lookup[value] : null;
}

function call(compute = part1){
    return compute(fs.readFileSync(inputPath, 'utf8').split(",").map(v => Number(v)));
}

console.log(call(part1))
console.log(call(part2))