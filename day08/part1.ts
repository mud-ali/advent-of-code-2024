import { readFileSync, stat } from 'fs'
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

let antennae: { [key: string]: Coord[] } = {}

for (let i = 0; i < GRID_SIZE; i++) {
    for (let j = 0; j < GRID_SIZE; j++) {
        if (grid[i][j] === ".") continue

        if (Object.keys(antennae).includes(grid[i][j])) {
            antennae[grid[i][j]].push(new Coord(i, j))
        } else {
            antennae[grid[i][j]] = [new Coord(i, j)]
        }
    }
}

let count = 0

for (let frequency of Object.keys(antennae)) {
    for (let i = 0; i < GRID_SIZE; i++) {
        for (let j = 0; j < GRID_SIZE; j++) {
            let distances: { dist: number, spot: Coord }[] = []
            let currentSpot: Coord = new Coord(i, j)

            if (currentSpot.getValue() === frequency)
                continue

            for (let antenna of antennae[frequency]) {
                distances.push({
                    dist: manhattanDist(currentSpot, antenna),
                    spot: antenna
                })
            }

            if (distances.length > 1) {
                for (let distance of distances) {
                    for (let distance2 of distances) {
                        if (
                            (distance.dist === 2 * distance2.dist
                            || distance2.dist === 2 * distance.dist) 
                            && areColinear(currentSpot, distance.spot, distance2.spot)
                        ) {
                            if (grid[i][j] !== "#") count++;
                            grid[i][j] = "#"
                            break
                        } else {
                            // if (!distance.spot.equals(distance2.spot))
                            //     console.log(distance2.spot, distance.spot, distance2.dist, distance.dist)
                        }
                    }
                }
            }
        }
    }
}

console.log(grid.map(g => g.join("")).join("\n"))
console.log(count)

function areColinear(c1: Coord, c2: Coord, c3: Coord): boolean {
    const area = c1.rowNum * (c2.colNum - c3.colNum) +
                 c2.rowNum * (c3.colNum - c1.colNum) +
                 c3.rowNum * (c1.colNum - c2.colNum);
    return area === 0;
}

function manhattanDist(c1: Coord, c2: Coord): number {
    return Math.abs(c1.rowNum - c2.rowNum) + Math.abs(c1.colNum - c2.colNum);
}