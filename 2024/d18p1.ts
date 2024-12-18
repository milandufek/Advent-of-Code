import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/18

function solve(lines: string[]): number {
    const size = 70;
    const kb = 1024;
    const blocks: number[][] = lines.map(line => line.split(',').map(Number));
    const grid = Array.from({ length: size + 1 }, () => Array(size + 1).fill(0));
    for (const [c, r] of blocks.slice(0, kb)) grid[r][c] = 1;

    const queue: number[][] = [[0, 0, 0]];
    const visited: Set<string> = new Set();
    const directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    let nr: number, nc: number;
    while (queue.length > 0) {
        const [r, c, step] = queue.shift()!;
        for (const [dr, dc] of directions) {
            nr = r + dr;
            nc = c + dc;
            if (nr < 0 || nr > size || nc < 0 || nc > size) {
                continue;
            }
            if (grid[nr][nc] !== 0) {
                continue;
            }
            if (visited.has(`${nr},${nc},${step}`)) {
                continue;
            }
            if (nr === size && nc === size) {
                return step + 1;
            }
            visited.add(`${nr},${nc},${step}`);
            queue.push([nr, nc, step + 1]);
        }
    }
    return -1;
}

const steps: number = solve(readFileLines(determineInputFile()));
console.log('Steps:', steps);
