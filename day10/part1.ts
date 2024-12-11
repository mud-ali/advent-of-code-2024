import { readFileSync } from 'fs'
import { join } from 'path'

let filePath = join(__dirname, 'test.txt')
filePath = join(__dirname, "input.txt")

const grid: string[][] = readFileSync(filePath, 'utf-8').split("\n").map(line => line.split("").map(digit => digit))

const GRID_SIZE = grid.length

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
            //console.log(`Invalid position: ${this.toString()}`)
        }
    }

    add(c: Coord) {
        return new Coord(c.rowNum + this.rowNum, c.colNum + this.colNum)
    }

    toString() {
        return `(${this.rowNum}, ${this.colNum})`
    }

    isValid() {
        return this.rowNum >= 0 && this.colNum >= 0 && this.rowNum < GRID_SIZE && this.colNum < GRID_SIZE
    }

    equals(other: Coord) {
        return this.rowNum === other.rowNum && this.colNum === other.colNum
    }
}

let totalPaths = 0

let foundNines: Coord[] = []

function findAdjacent(c: Coord, num: number) : Coord[] {
    if (num === 9) {
        if (foundNines.find(a => a.equals(c)) === undefined) {
            totalPaths++
            foundNines.push(c)
        }
        return [c]
    }

    for (let i = c.rowNum - 1; i <= c.rowNum + 1; i++) {
        for (let j = c.colNum - 1; j <= c.colNum + 1; j++) {
            
            let newCoord = new Coord(i, j)
            
            if (!(i===c.rowNum || j===c.colNum)) continue
            const value = newCoord.getValue();
            if (value !== undefined && parseInt(value) === num + 1) {
                findAdjacent(newCoord, num + 1)
            }
        }
    }
    return [new Coord(-1,-1)]
}

let totalOfTotals = 0;

for (let i = 0; i < GRID_SIZE; i++) {
    for (let j = 0; j < GRID_SIZE; j++) {
        let c = new Coord(i, j)
        if (c.isValid() && c.getValue() == "0") {
            findAdjacent(c, 0)
            totalOfTotals += totalPaths;
            totalPaths = 0
        }
        foundNines = []
    }
}
console.log(totalOfTotals)
