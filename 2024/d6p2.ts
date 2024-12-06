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
        seen.add(`${r},${c},${dr},${dc}`);
        if (r + dr < 0 || r + dr >= rows || c + dc < 0 || c + dc >= cols) return false;
        if (grid[r + dr][c + dc] === '#') [dr, dc] = [dc, -dr];
        else {
            r += dr;
            c += dc;
        }
        if (seen.has(`${r},${c},${dr},${dc}`)) return true;
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
