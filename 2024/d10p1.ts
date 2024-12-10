import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/10

function getRoutes(r: number, c: number): number {
    let nr: number, nc: number;
    let summits: number = 0;
    const seen: Set<string> = new Set();
    const queue: number[][] = [[r, c]];
    const directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    while (queue.length > 0) {
        const [r, c] = queue.shift()!;
        for (const [dr, dc] of directions) {
            nr = r + dr;
            nc = c + dc;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
                continue;
            }
            if (grid[nr][nc] !== grid[r][c] + 1) {
                continue;
            }
            if (seen.has(`${nr},${nc}`)) {
                continue;
            }
            seen.add(`${nr},${nc}`);
            if (grid[nr][nc] === 9) {
                summits++;
            } else {
                queue.push([nr, nc]);
            }
        }
    }
    return summits;
}

function solve(): void {
    let score: number = 0;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === 0) {
                score += getRoutes(r, c);
            }
        }
    }
    console.log('Score:', score);
}

const lines: string[] = readFileLines(determineInputFile());
const grid: number[][] = lines.map(line => line.split('').map(Number));
const rows: number = grid.length;
const cols: number = grid[0].length;
solve();
