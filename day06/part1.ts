import { readFileSync, stat } from 'fs'
import { join } from 'path'

let filePath = join(__dirname, 'test.txt')
filePath = join(__dirname, "input.txt")
const grid : string[][] = readFileSync(filePath, 'utf-8').split("\n").map(line => line.split(""))

const GRID_HEIGHT = grid.length

class Coord {
    rowNum: number
    colNum: number

    constructor(rowNum: number, colNum: number) {
        this.rowNum = rowNum
        this.colNum = colNum
    }

    getValue() {
        if (this.isValid())
            return grid[this.rowNum][this.colNum]
        else {
            console.log(`Invalid position: ${this.toString()}`)
        }
    }

    add(c: Coord) {
        return new Coord(c.rowNum+this.rowNum, c.colNum+this.colNum)
    }
    
    toString() {
        return `(${this.rowNum}, ${this.colNum})`
    }

    isValid() {
        return this.rowNum >= 0  && this.colNum >= 0 && this.rowNum < GRID_HEIGHT && this.colNum < GRID_HEIGHT
    }
}


let positionsVisited = 1; //include starting position
let currentPosition : Coord = new Coord(0,0)
let pointing = new Coord(-1,0)


for (let i=0;i<GRID_HEIGHT;i++) {
    for (let j=0;j<GRID_HEIGHT;j++) {
        if (grid[i][j] === "^") {
            currentPosition = new Coord(i,j)
        }
    }
}

function nextRotation() {
    if (pointing.rowNum === -1 && pointing.colNum === 0) {
        pointing = new Coord(0, 1)
    } else if (pointing.rowNum === 0 && pointing.colNum === 1) {
        pointing = new Coord(1,0)
    } else if (pointing.rowNum === 1 && pointing.colNum === 0) {
        pointing = new Coord(0, -1)
    } else if (pointing.rowNum === 0 && pointing.colNum === -1) {
        pointing = new Coord(-1, 0);
    }
}

while (currentPosition.isValid()) {
    while (currentPosition.add(pointing).getValue() === "#") {
        nextRotation() // modify pointing globally
    }
    currentPosition = currentPosition.add(pointing)
    if (!currentPosition.isValid()) {
        console.log(`Visited ${positionsVisited} positions`)
        break
    }
    if (currentPosition.getValue() !== "X" && currentPosition.getValue() !== "^") {
        grid[currentPosition.rowNum][currentPosition.colNum] = "X"
        positionsVisited++
    }
    // console.log(grid.map(a => a.join("")).join("\n"))
    // console.log("---------------------\n\n")
}


