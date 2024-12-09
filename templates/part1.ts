import { readFileSync } from 'fs'
import { join } from 'path'

let filePath = join(__dirname, 'test.txt')
filePath = join(__dirname, "input.txt")

const grid: string[][] = readFileSync(filePath, 'utf-8').split("\n").map(line => line.split(""))

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
            console.log(`Invalid position: ${this.toString()}`)
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

// print the entire grid
console.log(grid.map(g => g.join("")).join("\n"))