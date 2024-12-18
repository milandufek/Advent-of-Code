import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/18

function checkPaths(lastBlock: number): boolean {
    const size = 70;
    const grid = Array.from({ length: size + 1 }, () => Array(size + 1).fill(0));
    for (const [c, r] of blocks.slice(0, lastBlock)) grid[r][c] = 1;

    const queue: number[][] = [[0, 0]];
    const visited: Set<string> = new Set();
    const directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    let nr: number, nc: number;
    while (queue.length > 0) {
        const [r, c] = queue.shift()!;
        for (const [dr, dc] of directions) {
            nr = r + dr;
            nc = c + dc;
            if (nr < 0 || nr > size || nc < 0 || nc > size) {
                continue;
            }
            if (grid[nr][nc] !== 0) {
                continue;
            }
            if (visited.has(`${nr},${nc}`)) {
                continue;
            }
            if (nr === size && nc === size) {
                return true;
            }
            visited.add(`${nr},${nc}`);
            queue.push([nr, nc]);
        }
    }
    return false;
}

function solve(): void {
    let low = 1024;
    let high = lines.length - 1;
    while (low < high) {
        let mid = Math.floor((low + high) / 2);
        if (checkPaths(mid + 1)) {
            low = mid + 1;
            continue;
        }
        high = mid;
    }
    console.log('Last byte:', blocks[low].join(','));
}

const lines: string[] = readFileLines(determineInputFile());
const blocks: number[][] = lines.map(line => line.split(',').map(Number));
solve();
