import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/12

function countBorderingCells(x: number, y: number): number {
    const directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    let differentCells: number = 0;
    for (const [dx, dy] of directions) {
        const nx = x + dx;
        const ny = y + dy;
        if (nx < 0 || nx >= rows || ny < 0 || ny >= cols || grid[nx][ny] !== grid[x][y]) {
            differentCells++;
        }
    }
    return differentCells;
}

function calculateConnectedCells(x: number, y: number): number {
    const directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const seen: Set<string> = new Set();
    const queue: number[][] = [[x, y]];
    let count = 0;
    let perimeter = 0;
    seen.add(`${x},${y}`);
    checked.add(`${x},${y}`);
    while (queue.length > 0) {
        const [x, y] = queue.shift()!;
        count++;
        perimeter += countBorderingCells(x, y);
        for (const [dx, dy] of directions) {
            const nx = x + dx;
            const ny = y + dy;
            if (seen.has(`${nx},${ny}`)) continue;
            seen.add(`${nx},${ny}`);
            if (nx < 0 || nx >= rows || ny < 0 || ny >= cols) continue;
            if (grid[nx][ny] === grid[x][y]) {
                queue.push([nx, ny]);
                checked.add(`${nx},${ny}`);
            }
        }
    }
    return count * perimeter;
}

function solve(): void {
    let score: number = 0;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (checked.has(`${r},${c}`)) continue;
            score += calculateConnectedCells(r, c);
        }
    }
    console.log(score);
}

const lines: string[] = readFileLines(determineInputFile());
const grid: string[][] = lines.map(line => line.split(''));
const rows: number = grid.length;
const cols: number = grid[0].length;
const checked: Set<string> = new Set();
solve();
