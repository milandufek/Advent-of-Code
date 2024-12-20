import { get } from 'http';
import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/6

function getStartPosition(): [number, number] {
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '^') {
                return [r, c];
            }
        }
    }
    return [-1, -1];
}

function isStuck(r: number, c: number): boolean {
    let [dr, dc] = [-1, 0];
    const seen = new Set<string>();

    while (true) {
        const key = `${r},${c},${dr},${dc}`;
        if (seen.has(key)) return true;
        seen.add(key);

        const nr = r + dr;
        const nc = c + dc;

        if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) return false;
        if (grid[nr][nc] === '#') {
            [dr, dc] = [dc, -dr];
        } else {
            r = nr;
            c = nc;
        }
    }
}

function solve(): void {
    let count = 0;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] !== '.') continue;
            grid[r][c] = '#';
            if (isStuck(start[0], start[1])) count++;
            grid[r][c] = '.';
        }
    }
    console.log('Stuck:', count);
}

const grid = readFileLines(determineInputFile()).map(s => s.split(''));
const rows = grid.length;
const cols = grid[0].length;
const start = getStartPosition();
solve();
